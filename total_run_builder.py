#!/usr/bin/env python3
from __future__ import annotations

import os
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

import common


INTERPRETATION_GUIDE = [
    "ADF p>0.05 and KPSS p<0.05 suggests I(1)-like behavior; use differences/cointegration frameworks.",
    "ADF p<0.05 and KPSS p>0.05 suggests stationarity; level models are more admissible.",
    "Ljung-Box p<0.05 indicates autocorrelation; include lag terms.",
    "BP/White p<0.05 indicates heteroskedasticity; use robust/HAC standard errors.",
    "JB p<0.05 indicates non-normality; rely on robust inference.",
    "Stability flag=1 indicates drift/break risk; use rolling or split-sample checks.",
    "For retail, compare no-promo and promo-controlled transmission.",
]


def _safe_num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce")


def _detect_tests(df: pd.DataFrame) -> bool:
    return any(c in df.columns for c in ["adf_p", "kpss_p", "ljungbox_p", "bp_p", "white_p", "jb_p", "stability_flag"])


def _detect_forecast(df: pd.DataFrame) -> bool:
    cols = set(df.columns)
    return bool({"pred_dlog", "actual_dlog", "synthetic_retail_price", "Forecast_Summary"} & cols) or any(
        "forecast" in str(c).lower() or "synthetic" in str(c).lower() for c in cols
    )


def _detect_model_results(df: pd.DataFrame) -> bool:
    coef_cols = [c for c in df.columns if c.startswith("coef") or c.endswith("_coef") or "effect" in c.lower()]
    p_cols = [c for c in df.columns if c.startswith("p_") or c.endswith("_p") or "pvalue" in c.lower()]
    return bool(coef_cols or p_cols or ("cointegration_rank" in df.columns) or ("ect_coef" in df.columns))


def _detect_descriptive(df: pd.DataFrame) -> bool:
    desc_cols = {"count", "missing", "mean", "median", "std", "min", "max", "q05", "q95", "cv"}
    return len(desc_cols.intersection(set(df.columns))) >= 5


def _detect_corr_lag(df: pd.DataFrame) -> bool:
    cols = set(df.columns)
    return bool({"pearson", "spearman", "lag_days", "corr"}.intersection(cols))


def _detect_decomposition(df: pd.DataFrame) -> bool:
    cols = set(df.columns)
    return bool({"trend", "seasonal", "resid", "log_observed"}.intersection(cols))


def classify_table(df: pd.DataFrame, sheet: str) -> Tuple[str, str]:
    if _detect_tests(df):
        adf = _safe_num(df["adf_p"]) if "adf_p" in df.columns else pd.Series(dtype=float)
        kpss = _safe_num(df["kpss_p"]) if "kpss_p" in df.columns else pd.Series(dtype=float)
        n = max(len(df), 1)
        i1_like = ((adf > 0.05) & (kpss < 0.05)).sum() if (not adf.empty and not kpss.empty) else 0
        stationary = ((adf < 0.05) & (kpss > 0.05)).sum() if (not adf.empty and not kpss.empty) else 0
        text = (
            f"Diagnostics summary: I(1)-like share={i1_like/n:.2f}, stationary share={stationary/n:.2f}. "
            "Use lag structure + robust/HAC + stability checks when needed."
        )
        return "tests", text

    if _detect_forecast(df):
        return "forecast", "Forecast/synthetic table. Focus on prediction errors, stability across products, and synthetic-retail linkage."

    if _detect_model_results(df):
        coef_cols = [c for c in df.columns if c.startswith("coef") or c.endswith("_coef") or "effect" in c.lower()]
        coef_vals: List[float] = []
        for c in coef_cols:
            coef_vals.extend(_safe_num(df[c]).dropna().tolist())
        if coef_vals:
            mean_abs = float(np.nanmean(np.abs(np.array(coef_vals, dtype=float))))
            text = f"Model results table. Mean |coef|={mean_abs:.4f}; interpret sign and magnitude jointly with diagnostics."
        else:
            text = "Model results table. Interpret coefficients, p-values, and model admissibility columns."
        return "model_results", text

    if _detect_descriptive(df):
        return "descriptive", "Descriptive statistics table. Use dispersion and tails (q05/q95, std, cv) to assess instability by product/source."

    if _detect_corr_lag(df):
        return "correlation_lag", "Correlation/lag table. Use lag structure to guide directionality and dynamic model specifications."

    if _detect_decomposition(df):
        return "decomposition", "Decomposition table. Compare trend/seasonal/residual components for structural interpretation."

    if str(sheet).lower() in {"raw", "clean"}:
        return "raw_clean", "Raw/clean processing table. Use this for data lineage and transformation traceability."

    return "other", "General output table. Interpret with module context and linked diagnostic/model outputs."


def _safe_sheet_name(base: str, used: set[str]) -> str:
    name = base[:31]
    if name not in used:
        used.add(name)
        return name
    for i in range(1, 10000):
        suffix = f"_{i}"
        cut = base[: 31 - len(suffix)] + suffix
        if cut not in used:
            used.add(cut)
            return cut
    raise RuntimeError("Unable to generate unique sheet name.")


def _write_total_xlsx(total_xlsx: Path, table_records: List[Dict[str, object]]) -> pd.DataFrame:
    index_rows: List[Dict[str, object]] = []
    used_names: set[str] = set()
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False, dir="/tmp") as tf:
        tmp = Path(tf.name)
    with pd.ExcelWriter(tmp, engine="openpyxl") as writer:
        for idx, rec in enumerate(table_records, start=1):
            xlsx_path = Path(str(rec["xlsx_path"]))
            sheet = str(rec["sheet"])
            try:
                df = pd.read_excel(xlsx_path, sheet_name=sheet)
            except Exception:
                continue
            short = f"T{idx:04d}"
            sname = _safe_sheet_name(short, used_names)
            df.to_excel(writer, sheet_name=sname, index=False)
            index_rows.append(
                {
                    "table_id": sname,
                    "module": rec["module"],
                    "xlsx_file": xlsx_path.name,
                    "original_sheet": sheet,
                    "category": rec["category"],
                    "rows": len(df),
                    "cols": len(df.columns),
                    "interpretation": rec["interpretation"],
                }
            )

        index_df = pd.DataFrame(index_rows)
        if not index_df.empty:
            index_df.to_excel(writer, sheet_name="00_Index", index=False)
            mod = (
                index_df.groupby("module", as_index=False)
                .agg(
                    tables=("table_id", "count"),
                    rows_total=("rows", "sum"),
                    cols_avg=("cols", "mean"),
                )
                .sort_values("module")
            )
            mod.to_excel(writer, sheet_name="01_ModuleSummary", index=False)
            cat = (
                index_df.groupby("category", as_index=False)
                .agg(tables=("table_id", "count"), rows_total=("rows", "sum"))
                .sort_values("category")
            )
            cat.to_excel(writer, sheet_name="02_CategorySummary", index=False)
    shutil.copy2(tmp, total_xlsx)
    tmp.unlink(missing_ok=True)
    return pd.DataFrame(index_rows)


def _table_to_md(df: pd.DataFrame, max_rows: int | None = None, max_cols: int | None = None) -> str:
    d = df.copy()
    if max_cols is not None:
        d = d.iloc[:, :max_cols]
    if max_rows is not None:
        d = d.head(max_rows)
    if d.empty:
        return "_No rows_"
    head = "| " + " | ".join([str(c) for c in d.columns]) + " |"
    sep = "| " + " | ".join(["---"] * len(d.columns)) + " |"
    rows = []
    for _, row in d.iterrows():
        vals = [str(row[c]).replace("\n", " ").replace("|", "/") for c in d.columns]
        rows.append("| " + " | ".join(vals) + " |")
    return "\n".join([head, sep] + rows)


def _render_table_pages_portrait(pdf: PdfPages, df: pd.DataFrame, table_title: str, category: str) -> None:
    # Keep portrait orientation and split by columns/rows to avoid over-wide pages.
    max_cols = 6
    row_chunk = 32
    full_rows = category in {"tests", "model_results", "forecast", "descriptive", "correlation_lag", "decomposition"}
    max_rows_cap = None if full_rows else 250
    hard_cap = 2000

    d = df.copy()
    truncated = False
    if len(d) > hard_cap:
        d = d.head(hard_cap)
        truncated = True
    if max_rows_cap is not None and len(d) > max_rows_cap:
        d = d.head(max_rows_cap)
        truncated = True

    cols = list(d.columns)
    if not cols:
        cols = ["_empty"]
        d = pd.DataFrame({"_empty": []})

    for c0 in range(0, len(cols), max_cols):
        csel = cols[c0 : c0 + max_cols]
        sub = d[csel].copy()
        for r0 in range(0, max(len(sub), 1), row_chunk):
            chunk = sub.iloc[r0 : r0 + row_chunk].copy()
            fig, ax = plt.subplots(figsize=(8.27, 11.69), facecolor="white")
            ax.axis("off")
            ax.text(0.02, 0.97, table_title, fontsize=11, weight="bold", transform=ax.transAxes)
            ax.text(0.02, 0.94, f"columns {c0+1}-{min(c0+max_cols, len(cols))}, rows {r0+1}-{r0+len(chunk)}", fontsize=9, transform=ax.transAxes)
            if truncated:
                ax.text(0.02, 0.92, "Preview truncated for PDF readability; full table is in Total_Run.xlsx", fontsize=8, color="#AA0000", transform=ax.transAxes)
                ypos = 0.89
            else:
                ypos = 0.91
            if chunk.empty:
                txt = "No rows"
            else:
                txt = chunk.astype(str).to_string(index=False, max_colwidth=28)
            ax.text(0.02, ypos, txt, fontsize=7.8, family="monospace", va="top", transform=ax.transAxes)
            pdf.savefig(fig, bbox_inches="tight")
            plt.close(fig)


def _write_total_pdf(total_pdf: Path, table_records: List[Dict[str, object]], index_df: pd.DataFrame, images: List[Path]) -> None:
    with PdfPages(total_pdf) as pdf:
        fig, ax = plt.subplots(figsize=(8.27, 11.69), facecolor="white")
        ax.axis("off")
        ax.text(0.03, 0.97, "Total Run - Combined Results", fontsize=16, weight="bold", transform=ax.transAxes)
        ax.text(0.03, 0.93, "Interpretation guide", fontsize=11, weight="bold", transform=ax.transAxes)
        y = 0.90
        for line in INTERPRETATION_GUIDE:
            ax.text(0.03, y, f"- {line}", fontsize=8.8, transform=ax.transAxes)
            y -= 0.030
        y -= 0.01
        ax.text(0.03, y, f"Tables included: {len(index_df)}", fontsize=9.2, transform=ax.transAxes)
        y -= 0.03
        ax.text(0.03, y, f"Graphs included: {len(images)}", fontsize=9.2, transform=ax.transAxes)
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)

        for rec in table_records:
            xlsx_path = Path(str(rec["xlsx_path"]))
            sheet = str(rec["sheet"])
            category = str(rec["category"])
            interp = str(rec["interpretation"])
            try:
                df = pd.read_excel(xlsx_path, sheet_name=sheet)
            except Exception:
                continue

            intro = plt.figure(figsize=(8.27, 11.69), facecolor="white")
            ax = intro.add_subplot(111)
            ax.axis("off")
            ax.text(0.02, 0.97, f"Module: {rec['module']}", fontsize=12, weight="bold", transform=ax.transAxes)
            ax.text(0.02, 0.94, f"File: {xlsx_path.name}", fontsize=9.5, transform=ax.transAxes)
            ax.text(0.02, 0.92, f"Sheet: {sheet}", fontsize=9.5, transform=ax.transAxes)
            ax.text(0.02, 0.90, f"Category: {category}", fontsize=9.5, transform=ax.transAxes)
            ax.text(0.02, 0.87, "Interpretation:", fontsize=10, weight="bold", transform=ax.transAxes)
            ax.text(0.02, 0.84, interp, fontsize=9, wrap=True, transform=ax.transAxes)
            ax.text(0.02, 0.80, f"Rows: {len(df)} | Cols: {len(df.columns)}", fontsize=9, transform=ax.transAxes)
            pdf.savefig(intro, bbox_inches="tight")
            plt.close(intro)

            _render_table_pages_portrait(
                pdf=pdf,
                df=df,
                table_title=f"{rec['module']} | {xlsx_path.name} | {sheet}",
                category=category,
            )

        for img in images:
            if not img.exists():
                continue
            arr = plt.imread(str(img))
            fig, ax = plt.subplots(figsize=(8.27, 11.69), facecolor="white")
            ax.axis("off")
            ax.set_title(img.name, fontsize=10)
            ax.imshow(arr)
            pdf.savefig(fig, bbox_inches="tight")
            plt.close(fig)


def _write_total_md(total_md: Path, table_records: List[Dict[str, object]], index_df: pd.DataFrame, images: List[Path]) -> None:
    lines: List[str] = []
    lines.append("# Total Run - Combined Results")
    lines.append("")
    lines.append("## Interpretation Guide")
    for row in INTERPRETATION_GUIDE:
        lines.append(f"- {row}")
    lines.append("")
    lines.append(f"- Tables included: {len(index_df)}")
    lines.append(f"- Graphs included: {len(images)}")
    lines.append("")
    lines.append("## Index")
    lines.append("")
    lines.append(_table_to_md(index_df, max_rows=None, max_cols=8) if not index_df.empty else "_No index rows_")
    lines.append("")

    for rec in table_records:
        xlsx_path = Path(str(rec["xlsx_path"]))
        sheet = str(rec["sheet"])
        category = str(rec["category"])
        interp = str(rec["interpretation"])
        try:
            df = pd.read_excel(xlsx_path, sheet_name=sheet)
        except Exception:
            continue
        lines.append(f"## {rec['module']} :: {xlsx_path.name} :: {sheet}")
        lines.append("")
        lines.append(f"- Category: {category}")
        lines.append(f"- Interpretation: {interp}")
        lines.append(f"- Rows: {len(df)}")
        lines.append(f"- Cols: {len(df.columns)}")
        lines.append("")
        md_hard_cap = 200
        dmd = df.copy()
        md_truncated = False
        if len(dmd) > md_hard_cap:
            dmd = dmd.head(md_hard_cap)
            md_truncated = True
        if category in {"tests", "model_results", "forecast", "descriptive", "correlation_lag", "decomposition"}:
            md_table = _table_to_md(dmd, max_rows=None, max_cols=12)
        else:
            md_table = _table_to_md(dmd, max_rows=300, max_cols=12)
            if len(df) > 300:
                lines.append("_Table truncated in markdown for readability; full table in Total_Run.xlsx._")
                lines.append("")
        if md_truncated:
            lines.append("_Large table truncated in markdown; full table in Total_Run.xlsx._")
            lines.append("")
        lines.append(md_table)
        lines.append("")

    lines.append("## Graphs")
    lines.append("")
    for img in images:
        lines.append(f"- {img}")
    lines.append("")
    total_md.write_text("\n".join(lines), encoding="utf-8")


def build_total_run(outputs_root: Path | None = None) -> Path:
    out_root = outputs_root if outputs_root is not None else common.OUTPUT_ROOT
    total_dir = common.get_output_dir("total_run")
    total_xlsx = total_dir / "Total_Run.xlsx"
    total_pdf = total_dir / "Total_Run.pdf"
    total_md = total_dir / "Total_Run.md"

    table_records: List[Dict[str, object]] = []
    images: List[Path] = []
    seen_images: set[str] = set()
    xlsx_paths = sorted(
        [
            p
            for p in out_root.rglob("*.xlsx")
            if p.is_file() and "total_run" not in p.parts
        ]
    )
    for img in sorted([p for p in out_root.rglob("*.png") if p.is_file() and "total_run" not in p.parts]):
        key = str(img.resolve())
        if key not in seen_images:
            seen_images.add(key)
            images.append(img)
    for xlsx in xlsx_paths:
        rel_parent = str(xlsx.parent.relative_to(out_root))
        module = rel_parent if rel_parent else "root"
        try:
            xl = pd.ExcelFile(xlsx)
        except Exception:
            continue
        for sheet in xl.sheet_names:
            try:
                dsmall = xl.parse(sheet_name=sheet, nrows=200)
            except Exception:
                continue
            category, interp = classify_table(dsmall, sheet)
            table_records.append(
                {
                    "module": module,
                    "xlsx_path": str(xlsx),
                    "sheet": sheet,
                    "category": category,
                    "interpretation": interp,
                }
            )

    index_df = _write_total_xlsx(total_xlsx, table_records)
    _write_total_pdf(total_pdf, table_records, index_df, images)
    _write_total_md(total_md, table_records, index_df, images)

    print("\n=== TOTAL RUN ===")
    print(f"- xlsx: {total_xlsx}")
    print(f"- pdf: {total_pdf}")
    print(f"- md: {total_md}")
    print(f"- tables_included: {len(index_df)}")
    print(f"- graphs_included: {len(images)}")
    return total_dir


if __name__ == "__main__":
    build_total_run()
