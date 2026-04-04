#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import traceback
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd

import common
from sheet_worker import run_sheet_module
from model_worker import (
    run_ardl,
    run_ecm,
    run_nardl,
    run_vecm,
    run_discounts,
    run_short_chain_regional,
    run_intersection_bidirectional,
    run_forecast_knn_synthetic,
    run_secondary_synthetic_consumer,
)
from graph_worker import (
    run_decomposition_graphs,
    run_overlay_ln_graphs,
    run_corr_lag_graphs,
    run_brand_region_graphs,
)
from total_run_builder import build_total_run


INTERPRETATION_GUIDE = [
    "RW4 models require admissible unit normalization before level/cointegration estimation.",
    "Core findings should be promoted only when signs are stable across linear and pchip reconstructions.",
    "Farm-gate conclusions should also remain directionally stable across the initial and all-missing-filled farm-gate workbooks.",
    "Retail baseline models represent promo-controlled price paths; observed models represent effective transaction-relevant prices.",
    "Reverse-flow coefficients quantify whether downstream retail shocks transmit materially back toward farm-gate prices.",
]


def _run_step(name: str, fn, log_rows: List[Dict[str, str]]) -> None:
    print(f"\n>>> RUNNING: {name}")
    try:
        out = fn()
        print(f"<<< DONE: {name} -> {out}")
        log_rows.append({"step": name, "status": "ok", "output_dir": str(out), "error": ""})
    except Exception as exc:
        print(f"<<< FAILED: {name}: {exc}")
        traceback.print_exc()
        log_rows.append({"step": name, "status": "failed", "output_dir": "", "error": str(exc)})


def _detect_tests(df: pd.DataFrame) -> bool:
    return any(c in df.columns for c in ["adf_p", "kpss_p", "ljungbox_p", "bp_p", "white_p", "jb_p", "stability_flag", "cointegration_p"])


def _detect_model_results(df: pd.DataFrame) -> bool:
    coef_cols = [c for c in df.columns if c.startswith("coef") or c.endswith("_coef") or "effect" in c.lower()]
    p_cols = [c for c in df.columns if c.startswith("p_") or c.endswith("_p") or "pvalue" in c.lower()]
    return bool(coef_cols or p_cols or ("core_finding_flag" in df.columns) or ("ect_coef" in df.columns) or ("robust_across_reconstruction" in df.columns))


def _safe_num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce")


def _interpret_tests(module: str, xlsx: str, sheet: str, df: pd.DataFrame) -> Dict[str, object]:
    adf = _safe_num(df["adf_p"]) if "adf_p" in df.columns else pd.Series(dtype=float)
    kpss = _safe_num(df["kpss_p"]) if "kpss_p" in df.columns else pd.Series(dtype=float)
    coint_p = _safe_num(df["cointegration_p"]) if "cointegration_p" in df.columns else pd.Series(dtype=float)

    n = max(len(df), 1)
    i1_like = ((adf > 0.05) & (kpss < 0.05)).sum() if (not adf.empty and not kpss.empty) else 0
    coint_share = (coint_p < 0.10).sum() if not coint_p.empty else 0
    note = f"I(1)-like share={i1_like/n:.2f}; cointegration-support share={coint_share/n:.2f}; inspect admissibility and reconstruction robustness before promoting findings."
    return {
        "module": module,
        "xlsx_file": xlsx,
        "sheet": sheet,
        "n_rows": int(len(df)),
        "i1_like_share": float(i1_like / n),
        "cointegration_support_share": float(coint_share / n),
        "interpretation": note,
    }


def _interpret_results(module: str, xlsx: str, sheet: str, df: pd.DataFrame) -> Dict[str, object]:
    coef_cols = [c for c in df.columns if c.startswith("coef") or c.endswith("_coef") or "effect" in c.lower()]
    p_cols = [c for c in df.columns if c.startswith("p_") or c.endswith("_p") or "pvalue" in c.lower()]
    coef_values: List[float] = []
    for c in coef_cols:
        coef_values.extend(_safe_num(df[c]).dropna().tolist())
    coef_arr = np.array(coef_values, dtype=float) if coef_values else np.array([], dtype=float)

    p_values: List[float] = []
    for c in p_cols:
        p_values.extend(_safe_num(df[c]).dropna().tolist())
    p_arr = np.array(p_values, dtype=float) if p_values else np.array([], dtype=float)

    robust_share = float(_safe_num(df.get("robust_across_reconstruction", pd.Series(dtype=float))).fillna(0).mean()) if "robust_across_reconstruction" in df.columns else np.nan
    core_share = float(_safe_num(df.get("core_finding_flag", pd.Series(dtype=float))).fillna(0).mean()) if "core_finding_flag" in df.columns else np.nan
    note_parts = []
    if coef_arr.size:
        note_parts.append(f"mean |coef|={float(np.nanmean(np.abs(coef_arr))):.4f}")
    if p_arr.size:
        note_parts.append(f"significance share (p<0.05)={float(np.mean(p_arr < 0.05)):.2f}")
    if pd.notna(robust_share):
        note_parts.append(f"robust-across-reconstruction share={robust_share:.2f}")
    if pd.notna(core_share):
        note_parts.append(f"core-finding share={core_share:.2f}")
    if not note_parts:
        note_parts.append("Result table has no standard coefficient/p-value columns; interpret by table-specific fields.")
    return {
        "module": module,
        "xlsx_file": xlsx,
        "sheet": sheet,
        "n_rows": int(len(df)),
        "robust_across_reconstruction_share": robust_share,
        "core_finding_share": core_share,
        "interpretation": " | ".join(note_parts),
    }


def _write_combined_md(
    md_path: Path,
    logs_df: pd.DataFrame,
    artifacts_df: pd.DataFrame,
    sheets_df: pd.DataFrame,
    tests_df: pd.DataFrame,
    results_df: pd.DataFrame,
    module_blocks_df: pd.DataFrame,
) -> None:
    lines: List[str] = []
    lines.append("# RW4 Full Modular Run Summary")
    lines.append("")
    lines.append("## Interpretation Guide")
    for row in INTERPRETATION_GUIDE:
        lines.append(f"- {row}")
    lines.append("")
    lines.append("## Run Status")
    lines.append(f"- steps: {len(logs_df)}")
    lines.append(f"- failed: {int((logs_df['status'] == 'failed').sum()) if not logs_df.empty else 0}")
    lines.append(f"- artifact modules: {len(artifacts_df)}")
    lines.append("")
    lines.append("## Module Blocks")
    lines.append("")
    for _, row in module_blocks_df.iterrows():
        lines.append(f"### {row['module']}")
        lines.append("")
        lines.append(f"- {row['interpretation']}")
        lines.append(f"- xlsx files: {row['xlsx_files']}")
        lines.append(f"- pdf files: {row['pdf_files']}")
        lines.append(f"- md files: {row['md_files']}")
        lines.append(f"- png count: {int(row['png_count'])}")
        lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")


def _build_combined_summary(logs: List[Dict[str, str]], outputs_root: Path) -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame], List[str]]:
    logs_df = pd.DataFrame(logs)
    artifact_rows: List[Dict[str, object]] = []
    sheet_rows: List[Dict[str, object]] = []
    tests_rows: List[Dict[str, object]] = []
    result_rows: List[Dict[str, object]] = []
    module_block_rows: List[Dict[str, object]] = []

    for _, log in logs_df.iterrows():
        module = str(log.get("step", ""))
        status = str(log.get("status", ""))
        out_dir_txt = str(log.get("output_dir", ""))
        if status != "ok" or not out_dir_txt:
            continue
        out_dir = Path(out_dir_txt)
        if not out_dir.exists():
            continue
        xlsx_paths = sorted(out_dir.rglob("*.xlsx"))
        pdf_paths = sorted(out_dir.rglob("*.pdf"))
        md_paths = sorted(out_dir.rglob("*.md"))
        png_count = len(list(out_dir.rglob("*.png")))
        xlsx_files = [str(p.relative_to(out_dir)) for p in xlsx_paths]
        pdf_files = [str(p.relative_to(out_dir)) for p in pdf_paths]
        md_files = [str(p.relative_to(out_dir)) for p in md_paths]
        artifact_rows.append(
            {
                "module": module,
                "output_dir": str(out_dir),
                "xlsx_count": len(xlsx_files),
                "pdf_count": len(pdf_files),
                "md_count": len(md_files),
                "png_count": png_count,
                "xlsx_files": "; ".join(xlsx_files),
                "pdf_files": "; ".join(pdf_files),
                "md_files": "; ".join(md_files),
            }
        )

        module_test_notes: List[str] = []
        module_result_notes: List[str] = []
        for xf in xlsx_paths:
            try:
                xl = pd.ExcelFile(xf)
            except Exception:
                continue
            for sheet in xl.sheet_names:
                try:
                    df = xl.parse(sheet)
                except Exception:
                    continue
                sheet_rows.append(
                    {
                        "module": module,
                        "xlsx_file": str(xf.relative_to(out_dir)),
                        "sheet": sheet,
                        "rows": int(len(df)),
                        "cols": int(len(df.columns)),
                        "has_tests_pattern": int(_detect_tests(df)),
                        "has_model_results_pattern": int(_detect_model_results(df)),
                    }
                )
                if _detect_tests(df):
                    tr = _interpret_tests(module, str(xf.relative_to(out_dir)), sheet, df)
                    tests_rows.append(tr)
                    module_test_notes.append(str(tr["interpretation"]))
                if _detect_model_results(df):
                    rr = _interpret_results(module, str(xf.relative_to(out_dir)), sheet, df)
                    result_rows.append(rr)
                    module_result_notes.append(str(rr["interpretation"]))

        interp = " | ".join((module_test_notes[:1] + module_result_notes[:1])).strip() if (module_test_notes or module_result_notes) else "No explicit test/model tables detected; inspect module-specific outputs."
        module_block_rows.append(
            {
                "module": module,
                "output_dir": str(out_dir),
                "xlsx_files": "; ".join(xlsx_files),
                "pdf_files": "; ".join(pdf_files),
                "md_files": "; ".join(md_files),
                "png_count": png_count,
                "interpretation": interp,
            }
        )

    artifacts_df = pd.DataFrame(artifact_rows).sort_values("module") if artifact_rows else pd.DataFrame()
    sheets_df = pd.DataFrame(sheet_rows).sort_values(["module", "xlsx_file", "sheet"]) if sheet_rows else pd.DataFrame()
    tests_df = pd.DataFrame(tests_rows).sort_values(["module", "xlsx_file", "sheet"]) if tests_rows else pd.DataFrame()
    results_df = pd.DataFrame(result_rows).sort_values(["module", "xlsx_file", "sheet"]) if result_rows else pd.DataFrame()
    module_blocks_df = pd.DataFrame(module_block_rows).sort_values("module") if module_block_rows else pd.DataFrame()

    table_map = {
        "Run_All_Summary": logs_df,
        "Artifacts_By_Module": artifacts_df,
        "Sheets_Index": sheets_df,
        "Tests_Interpretation": tests_df,
        "Results_Interpretation": results_df,
        "Module_Block_Interpretation": module_blocks_df,
    }
    text_lines = [
        f"steps={len(logs_df)}",
        f"failed={(logs_df['status'] == 'failed').sum() if not logs_df.empty else 0}",
        f"modules_with_outputs={len(artifacts_df)}",
        f"indexed_sheets={len(sheets_df)}",
        "RW4 run-all now includes both farm-gate reconstruction sheets and consolidated robustness outputs.",
    ]
    return logs_df, table_map, text_lines


def main() -> None:
    logs: List[Dict[str, str]] = []
    sheet_sources = ["FarmGateUA_initial", "FarmGateUA_filled", "ProducerUA", "ConsumerUA", "EU", "ProZorro", "Silpo", "Novus", "CME"]
    for src in sheet_sources:
        _run_step(f"sheet_{src}", lambda s=src: run_sheet_module(s), logs)

    _run_step("model_short_chain_regional", run_short_chain_regional, logs)
    _run_step("model_ardl", run_ardl, logs)
    _run_step("model_ecm", run_ecm, logs)
    _run_step("model_nardl", run_nardl, logs)
    _run_step("model_vecm", run_vecm, logs)
    _run_step("model_discounts", run_discounts, logs)
    _run_step("model_intersection_bidirectional", run_intersection_bidirectional, logs)
    _run_step("model_forecast_knn", run_forecast_knn_synthetic, logs)
    _run_step("model_secondary_synthetic_consumer", run_secondary_synthetic_consumer, logs)

    _run_step("graphs_decomposition", run_decomposition_graphs, logs)
    _run_step("graphs_overlay_ln", run_overlay_ln_graphs, logs)
    _run_step("graphs_correlations_lags", run_corr_lag_graphs, logs)
    _run_step("graphs_brand_region", run_brand_region_graphs, logs)

    run_dir = common.get_output_dir("run_all_summary")
    logs_df, table_map, text_lines = _build_combined_summary(logs, Path(common.OUTPUT_ROOT))
    xlsx = run_dir / "run_all_rw4_summary.xlsx"
    common.write_tables_xlsx(xlsx, table_map)
    pdf = run_dir / "run_all_rw4_summary.pdf"
    common.save_pdf_report(pdf, "RW4 Full Modular Run Summary (Combined)", text_lines, table_map, [])
    md = run_dir / "run_all_rw4_summary.md"
    _write_combined_md(
        md_path=md,
        logs_df=logs_df,
        artifacts_df=table_map["Artifacts_By_Module"],
        sheets_df=table_map["Sheets_Index"],
        tests_df=table_map["Tests_Interpretation"],
        results_df=table_map["Results_Interpretation"],
        module_blocks_df=table_map["Module_Block_Interpretation"],
    )

    total_run_dir: Path | None = None
    try:
        total_run_dir = build_total_run()
    except Exception as exc:
        print(f"\nWARNING: Total Run build failed: {exc}")

    print("\nRW4 modular pipeline finished.")
    print(f"Outputs root: {Path(__file__).resolve().parent / 'outputs'}")
    print(f"Run-all summary xlsx: {xlsx}")
    print(f"Run-all summary pdf: {pdf}")
    print(f"Run-all summary md: {md}")
    if total_run_dir is not None:
        print(f"Total Run output dir: {total_run_dir}")


if __name__ == "__main__":
    main()
