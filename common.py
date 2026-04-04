#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import tempfile
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mplconfig")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp")
os.environ.setdefault("MPLBACKEND", "Agg")
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

PROJECT_DIR = Path(__file__).resolve().parent
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

import rw2_extended_mapping_pipeline as rw2
import rw4_data

INPUT_XLSX = PROJECT_DIR / "full_uah.xlsx"
OUTPUT_ROOT = Path(__file__).resolve().parent / "outputs"
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

SOURCE_ORDER = [
    "FarmGateUA_initial",
    "FarmGateUA_filled",
    "ProducerUA",
    "ConsumerUA",
    "EU",
    "ProZorro",
    "Silpo",
    "Novus",
    "CME",
]
_RAW_CACHE: Tuple[Path, Dict[str, pd.DataFrame]] | None = None
_CLEANED_CACHE: Dict[str, pd.DataFrame] | None = None
_ALL_DAILY_CACHE: pd.DataFrame | None = None


def _copy_frame_map(frame_map: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    return {k: v.copy() for k, v in frame_map.items()}


def get_output_dir(name: str) -> Path:
    p = OUTPUT_ROOT / name
    p.mkdir(parents=True, exist_ok=True)
    return p


def load_raw() -> Tuple[Path, Dict[str, pd.DataFrame]]:
    global _RAW_CACHE
    if _RAW_CACHE is not None:
        wb_cached, raw_cached = _RAW_CACHE
        return wb_cached, _copy_frame_map(raw_cached)
    wb = rw2.discover_input_workbook(PROJECT_DIR, INPUT_XLSX)
    xls = pd.ExcelFile(wb)
    raw = {
        "ProducerUA": rw2.read_sheet_or_empty(xls, "Producer_UA"),
        "ConsumerUA": rw2.read_sheet_or_empty(xls, "Consumer_UA"),
        "EU": rw2.read_sheet_or_empty(xls, "Europe"),
        "ProZorro": rw2.read_sheet_or_empty(xls, "Prozorro"),
        "Silpo": rw2.read_sheet_or_empty(xls, "Silpo"),
        "Novus": rw2.read_sheet_or_empty(xls, "Novus"),
        "CME": rw2.read_sheet_or_empty(xls, "CME III"),
    }
    raw.update(rw4_data.load_farm_gate_sources())
    _RAW_CACHE = (wb, _copy_frame_map(raw))
    return wb, _copy_frame_map(raw)


def prepare_cleaned(raw: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    global _CLEANED_CACHE
    if _CLEANED_CACHE is not None:
        return _copy_frame_map(_CLEANED_CACHE)
    cleaned = {
        "FarmGateUA_initial": rw4_data.prep_farm_gate(raw["FarmGateUA_initial"], "FarmGateUA_initial"),
        "FarmGateUA_filled": rw4_data.prep_farm_gate(raw["FarmGateUA_filled"], "FarmGateUA_filled"),
        "ProducerUA": rw2.ensure_numeric_price(rw2.prep_producer_consumer(raw["ProducerUA"], "ProducerUA")),
        "ConsumerUA": rw2.ensure_numeric_price(rw2.prep_producer_consumer(raw["ConsumerUA"], "ConsumerUA")),
        "EU": rw2.ensure_numeric_price(rw2.prep_eu(raw["EU"])),
        "ProZorro": rw2.ensure_numeric_price(rw2.prep_prozorro(raw["ProZorro"])),
        "Silpo": rw2.ensure_numeric_price(rw2.prep_retail(raw["Silpo"], "Silpo")),
        "Novus": rw2.ensure_numeric_price(rw2.prep_retail(raw["Novus"], "Novus")),
        "CME": rw2.ensure_numeric_price(rw2.prep_cme(raw["CME"])),
    }
    cleaned = rw4_data.harmonize_cleaned(cleaned)

    # Additional UAH-native derived fields used downstream.
    pz = cleaned["ProZorro"]
    if not pz.empty:
        pz["prozorro_unit_price_uah"] = pd.to_numeric(pz.get("observed_price", pz.get("price")), errors="coerce")
        pz["savings_rate"] = (
            pd.to_numeric(pz.get("expected"), errors="coerce") - pd.to_numeric(pz.get("sum_current"), errors="coerce")
        ) / pd.to_numeric(pz.get("expected"), errors="coerce").replace(0, np.nan)
        cleaned["ProZorro"] = pz

    for retail_source in ["Silpo", "Novus"]:
        retail = cleaned[retail_source]
        if retail.empty:
            continue
        retail["real_price_after_discount"] = pd.to_numeric(retail.get("observed_price"), errors="coerce")
        retail["regular_price_without_discount"] = pd.to_numeric(retail.get("baseline_price"), errors="coerce")
        cleaned[retail_source] = retail
    _CLEANED_CACHE = _copy_frame_map(cleaned)
    return _copy_frame_map(cleaned)


def build_all_daily(cleaned: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    global _ALL_DAILY_CACHE
    if _ALL_DAILY_CACHE is not None:
        return _ALL_DAILY_CACHE.copy()
    parts: List[pd.DataFrame] = []
    for src in SOURCE_ORDER:
        df = cleaned.get(src, pd.DataFrame())
        if df.empty:
            continue
        dv = rw2.daily_variants_for_dataset(df.copy(), source=src)
        if not dv.empty:
            parts.append(dv)
    all_daily = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    if all_daily.empty:
        return all_daily
    all_daily, _ = rw2.winsorize_daily_variants(all_daily, lower_q=0.01, upper_q=0.99)
    _ALL_DAILY_CACHE = all_daily.copy()
    return all_daily


def build_model_inputs(cleaned: Dict[str, pd.DataFrame], all_daily: pd.DataFrame):
    weekly_all = rw2.prepare_weekly_for_tests(all_daily)
    tests = rw2.build_tests_table(weekly_all, min_obs=24)
    level_mask = pd.to_numeric(all_daily.get("admissible_for_level_model", all_daily.get("unit_ok")), errors="coerce").fillna(0).eq(1)
    weekly_level = rw2.prepare_weekly_for_tests(all_daily[level_mask].copy()) if not all_daily.empty else pd.DataFrame()
    model_series = rw2.build_model_series(weekly_level)
    return tests, weekly_level, model_series


def write_tables_xlsx(path: Path, table_map: Dict[str, pd.DataFrame]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False, dir="/tmp") as tf:
        tmp = Path(tf.name)
    with pd.ExcelWriter(tmp, engine="openpyxl") as writer:
        for sheet, df in table_map.items():
            safe = (df if df is not None else pd.DataFrame()).copy()
            safe.to_excel(writer, sheet_name=sheet[:31], index=False)
    shutil.copy2(tmp, path)
    try:
        tmp.unlink(missing_ok=True)
    except Exception:
        pass


def _plot_timeseries(df: pd.DataFrame, date_col: str, value_col: str, group_col: str, title: str, out_path: Path, max_groups: int = 6) -> None:
    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
    d = df.copy()
    d[date_col] = pd.to_datetime(d[date_col], errors="coerce")
    d[value_col] = pd.to_numeric(d[value_col], errors="coerce")
    d = d.dropna(subset=[date_col, value_col])
    top = d[group_col].astype(str).value_counts().head(max_groups).index.tolist()
    for g in top:
        s = d[d[group_col].astype(str) == str(g)].sort_values(date_col)
        if s.empty:
            continue
        series = s.groupby(date_col, as_index=False)[value_col].median()
        ax.plot(series[date_col], series[value_col], linewidth=1.5, label=str(g))
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel(value_col)
    if top:
        ax.legend(frameon=False)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_basic_set(df: pd.DataFrame, out_dir: Path, module_name: str, value_col: str = "price") -> List[Path]:
    paths: List[Path] = []
    if df.empty or value_col not in df.columns or "date" not in df.columns:
        return paths
    product_col = "product" if "product" in df.columns else None
    if product_col:
        p1 = out_dir / f"{module_name}_timeseries_by_product.png"
        _plot_timeseries(df, "date", value_col, product_col, f"{module_name}: Time Series by Product", p1)
        paths.append(p1)

    if "standardized_type" in df.columns:
        p2 = out_dir / f"{module_name}_timeseries_by_standardized_type.png"
        _plot_timeseries(df, "date", value_col, "standardized_type", f"{module_name}: Time Series by Standardized Type", p2)
        paths.append(p2)

    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
    vals = pd.to_numeric(df[value_col], errors="coerce").dropna()
    if len(vals) > 0:
        ax.hist(vals, bins=35, color="#4C78A8", alpha=0.85)
    ax.set_title(f"{module_name}: Distribution of {value_col}")
    ax.set_xlabel(value_col)
    ax.set_ylabel("Count")
    p3 = out_dir / f"{module_name}_distribution.png"
    fig.savefig(p3, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    paths.append(p3)

    return paths


def save_pdf_report(pdf_path: Path, title: str, text_lines: List[str], table_map: Dict[str, pd.DataFrame], image_paths: List[Path]) -> None:
    interpretation_guide = [
        "INTERPRETATION GUIDE",
        "ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.",
        "ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.",
        "Ljung-Box p<0.05 -> autocorrelation; add lag structure.",
        "BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.",
        "JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.",
        "Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.",
        "For retail transmission, compare no-promo vs promo-controlled estimates.",
    ]

    def _table_preview_md(df: pd.DataFrame, max_rows: int = 20, max_cols: int = 10) -> str:
        safe = (df if df is not None else pd.DataFrame()).copy()
        if safe.empty:
            return "_No rows_"
        use_cols = list(safe.columns[:max_cols])
        cut = safe[use_cols].head(max_rows).copy()
        head = "| " + " | ".join([str(c) for c in cut.columns]) + " |"
        sep = "| " + " | ".join(["---"] * len(cut.columns)) + " |"
        rows = []
        for _, row in cut.iterrows():
            vals = [str(row[c]).replace("\n", " ").replace("|", "/") for c in cut.columns]
            rows.append("| " + " | ".join(vals) + " |")
        return "\n".join([head, sep] + rows)

    def write_markdown_report(md_path: Path, title_text: str, notes: List[str], tables: Dict[str, pd.DataFrame], images: List[Path]) -> None:
        md_path.parent.mkdir(parents=True, exist_ok=True)
        lines: List[str] = [f"# {title_text}", ""]
        lines.append("## Interpretation Guide")
        for line in interpretation_guide[1:]:
            lines.append(f"- {line}")
        lines.append("")
        if notes:
            lines.append("## Notes")
            for note in notes:
                lines.append(f"- {note}")
            lines.append("")
        if tables:
            lines.append("## Tables")
            lines.append("")
            for name, df in tables.items():
                lines.append(f"### {name}")
                lines.append("")
                lines.append(_table_preview_md(df, max_rows=25, max_cols=12))
                lines.append("")
        if images:
            lines.append("## Graphs")
            lines.append("")
            for img in images:
                if img.exists():
                    lines.append(f"- {img}")
            lines.append("")
        md_path.write_text("\n".join(lines), encoding="utf-8")

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(pdf_path) as pdf:
        # text page only
        fig, ax = plt.subplots(figsize=(11.69, 8.27), facecolor="white")
        ax.axis("off")
        ax.text(0.02, 0.95, title, fontsize=18, weight="bold", transform=ax.transAxes)
        y = 0.90
        ax.text(0.02, y, interpretation_guide[0], fontsize=11, weight="bold", transform=ax.transAxes)
        y -= 0.035
        for line in interpretation_guide[1:]:
            ax.text(0.02, y, f"- {line}", fontsize=9.2, transform=ax.transAxes)
            y -= 0.030
        y -= 0.015
        ax.text(0.02, y, "RUN NOTES", fontsize=11, weight="bold", transform=ax.transAxes)
        y -= 0.035
        for line in text_lines[:10]:
            ax.text(0.02, y, line, fontsize=10, transform=ax.transAxes)
            y -= 0.033
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)

        # table pages only
        for name, df in table_map.items():
            fig, ax = plt.subplots(figsize=(11.69, 8.27), facecolor="white")
            ax.axis("off")
            ax.text(0.02, 0.95, f"Table: {name}", fontsize=14, weight="bold", transform=ax.transAxes)
            prev = (df if df is not None else pd.DataFrame()).head(40).copy()
            if prev.empty:
                txt = "No rows"
            else:
                txt = prev.astype(str).to_string(index=False, max_colwidth=28)
            ax.text(0.02, 0.90, txt, fontsize=8, family="monospace", va="top", transform=ax.transAxes)
            pdf.savefig(fig, bbox_inches="tight")
            plt.close(fig)

        # graph pages only
        for img in image_paths:
            if not img.exists():
                continue
            arr = plt.imread(str(img))
            fig, ax = plt.subplots(figsize=(11.69, 8.27), facecolor="white")
            ax.imshow(arr)
            ax.axis("off")
            ax.set_title(img.name, fontsize=12)
            pdf.savefig(fig, bbox_inches="tight")
            plt.close(fig)

    md_path = pdf_path.with_suffix(".md")
    write_markdown_report(md_path, title, text_lines, table_map, image_paths)


def print_block(title: str, lines: List[str]) -> None:
    print(f"\n=== {title} ===")
    for ln in lines:
        print(f"- {ln}")
