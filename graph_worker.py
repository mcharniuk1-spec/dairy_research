#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import common
import rw2_extended_mapping_pipeline as rw2


def run_decomposition_graphs(max_series: int = 12) -> Path:
    _, raw = common.load_raw()
    cleaned = common.prepare_cleaned(raw)
    all_daily = common.build_all_daily(cleaned)
    decomp_all, decomp_summary, decomp_tables, decomp_index = rw2.build_decomposition_tables(all_daily)

    out_dir = common.get_output_dir("graphs_decomposition")
    images: List[Path] = []

    for i, (sname, df) in enumerate(decomp_tables.items()):
        if i >= max_series:
            break
        d = df.copy()
        d["date"] = pd.to_datetime(d["date"], errors="coerce")
        d = d.dropna(subset=["date"]).sort_values("date")
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        ax.plot(d["date"], d["log_observed"], label="Observed (log)", linewidth=1.5)
        ax.plot(d["date"], d["trend"], label="Trend", linewidth=1.8)
        ax.set_title(f"Decomposition Observed vs Trend: {sname}")
        ax.legend(frameon=False)
        p = out_dir / f"decomp_observed_trend_{i+1:02d}.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p)

        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        ax.plot(d["date"], d["seasonal"], label="Seasonal", linewidth=1.5)
        ax.plot(d["date"], d["resid"], label="Residual", linewidth=1.3)
        ax.set_title(f"Decomposition Seasonal/Residual: {sname}")
        ax.legend(frameon=False)
        p2 = out_dir / f"decomp_seasonal_resid_{i+1:02d}.png"
        fig.savefig(p2, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p2)

    xlsx = out_dir / "graphs_decomposition_output.xlsx"
    common.write_tables_xlsx(xlsx, {"Decomposition_Summary": decomp_summary, "Decomposition_Index": decomp_index, "Decomposition_All": decomp_all})
    pdf = out_dir / "graphs_decomposition_report.pdf"
    common.save_pdf_report(pdf, "Decomposition Graphs", [f"series_plotted={min(len(decomp_tables), max_series)}", "Interpretation option: trend vs seasonal strength from Decomposition_Summary."], {"Decomposition_Summary": decomp_summary}, images)
    common.print_block("GRAPHS DECOMPOSITION", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"images: {len(images)}"])
    return out_dir


def run_overlay_ln_graphs(max_products: int = 12) -> Path:
    _, raw = common.load_raw()
    cleaned = common.prepare_cleaned(raw)
    all_daily = common.build_all_daily(cleaned)

    ba_all, ba_tables, ba_idx = rw2.build_before_after_ln_tables(all_daily)
    ov_all, ov_tables, ov_idx = rw2.build_overlay_tables(all_daily)

    out_dir = common.get_output_dir("graphs_overlay_ln")
    images: List[Path] = []

    # before/after ln plots
    for i, (_, d) in enumerate(list(ba_tables.items())[:max_products]):
        dd = d.copy()
        dd["date"] = pd.to_datetime(dd["date"], errors="coerce")
        dd = dd.dropna(subset=["date"]).sort_values("date")
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        ax.plot(dd["date"], dd["price"], label="Before ln", linewidth=1.5)
        ax.plot(dd["date"], dd["log_price"], label="After ln", linewidth=1.5)
        ax.plot(dd["date"], dd["trend_before_ln"], label="Trend before", linewidth=1.4, linestyle="--")
        ax.plot(dd["date"], dd["trend_after_ln"], label="Trend after", linewidth=1.4, linestyle="--")
        ax.set_title("Before vs After ln (with trends)")
        ax.legend(frameon=False)
        p = out_dir / f"before_after_ln_{i+1:02d}.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p)

    # overlays by product
    for i, (_, d) in enumerate(list(ov_tables.items())[:max_products]):
        dd = d.copy()
        dd["date"] = pd.to_datetime(dd["date"], errors="coerce")
        dd = dd.dropna(subset=["date"]).sort_values("date")
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        for c in ["ProducerUA", "ConsumerUA", "ProZorro", "Silpo", "Novus", "EU", "CME"]:
            if c in dd.columns:
                yy = pd.to_numeric(dd[c], errors="coerce")
                if yy.notna().sum() > 3:
                    ax.plot(dd["date"], yy, linewidth=1.4, label=c)
        ax.set_title("Overlay / Intersection Dynamics")
        ax.legend(frameon=False, ncol=2)
        p = out_dir / f"overlay_{i+1:02d}.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p)

    xlsx = out_dir / "graphs_overlay_ln_output.xlsx"
    common.write_tables_xlsx(xlsx, {"BeforeAfterLN_Index": ba_idx, "Overlay_Index": ov_idx, "BeforeAfterLN_All": ba_all, "Overlay_All": ov_all})
    pdf = out_dir / "graphs_overlay_ln_report.pdf"
    common.save_pdf_report(pdf, "Overlay and Before/After ln Graphs", [f"before_after_series={len(ba_tables)}", f"overlay_products={len(ov_tables)}", "Interpretation option: compare trend shifts and cross-layer alignment windows."], {"BeforeAfterLN_Index": ba_idx, "Overlay_Index": ov_idx}, images)
    common.print_block("GRAPHS OVERLAY/LN", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"images: {len(images)}"])
    return out_dir


def run_corr_lag_graphs() -> Path:
    _, raw = common.load_raw()
    cleaned = common.prepare_cleaned(raw)
    all_daily = common.build_all_daily(cleaned)

    corr = rw2.compute_correlations(all_daily)
    corr_mat = rw2.build_corr_matrix(corr)
    lag_all = rw2.build_lag_matrix_all(all_daily)
    lag_best, lag_profiles = rw2.build_lag_outputs(lag_all)

    out_dir = common.get_output_dir("graphs_correlations_lags")
    images: List[Path] = []

    if not corr_mat.empty and "source" in corr_mat.columns:
        m = corr_mat.set_index("source")
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        sns.heatmap(m, cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
        ax.set_title("Correlation Matrix by Source")
        p = out_dir / "corr_matrix_sources.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p)

    if not lag_best.empty:
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        top = lag_best.dropna(subset=["corr"]).copy().sort_values("corr", key=lambda s: s.abs(), ascending=False).head(20)
        labels = top["product"].astype(str) + "|" + top["pair_left"].astype(str) + "->" + top["pair_right"].astype(str)
        ax.barh(labels, pd.to_numeric(top["lag_days"], errors="coerce"))
        ax.set_title("Best Lag (days) by Product/Pair")
        ax.set_xlabel("Lag days")
        p = out_dir / "lag_best_bar.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p)

    xlsx = out_dir / "graphs_correlations_lags_output.xlsx"
    common.write_tables_xlsx(xlsx, {"Correlations": corr, "Corr_Matrix": corr_mat, "Lag_Best": lag_best, "Lag_Profiles": lag_profiles})
    pdf = out_dir / "graphs_correlations_lags_report.pdf"
    common.save_pdf_report(pdf, "Correlations and Lags Graphs", [f"corr_rows={len(corr)}", f"lag_profiles_rows={len(lag_profiles)}", "Interpretation option: inspect strongest co-movements and dominant lag distances."], {"Corr_Matrix": corr_mat, "Lag_Best": lag_best}, images)
    common.print_block("GRAPHS CORR/LAG", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"images: {len(images)}"])
    return out_dir


def run_brand_region_graphs() -> Path:
    _, raw = common.load_raw()
    cleaned = common.prepare_cleaned(raw)
    all_daily = common.build_all_daily(cleaned)

    brand_io = rw2.build_brand_io_metrics(cleaned["Silpo"], cleaned["Novus"])
    brand_econ = rw2.build_brand_economic_metrics(cleaned["Silpo"], cleaned["Novus"], all_daily)
    by_region = rw2.group_stats(cleaned["ProZorro"], "price", ["region", "product", "standardized_type"]) if not cleaned["ProZorro"].empty else pd.DataFrame()

    out_dir = common.get_output_dir("graphs_brand_region")
    images: List[Path] = []

    if not brand_io.empty:
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        d = brand_io.copy()
        d["hhi_brand"] = pd.to_numeric(d["hhi_brand"], errors="coerce")
        top = d.sort_values("hhi_brand", ascending=False).head(20)
        labels = top["source"].astype(str) + "|" + top["standardized_type"].astype(str) + "|" + top["month"].astype(str)
        ax.barh(labels, top["hhi_brand"])
        ax.set_title("Brand Concentration (HHI)")
        p = out_dir / "brand_hhi.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p)

    if not brand_econ.empty and "promo_intensity" in brand_econ.columns:
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        d = brand_econ.copy().dropna(subset=["promo_intensity"])
        top = d.sort_values("promo_intensity", ascending=False).head(20)
        key_col = "product" if "product" in top.columns else "standardized_type"
        labels = top["source"].astype(str) + "|" + top[key_col].astype(str) + "|" + top["brand"].astype(str)
        ax.barh(labels, pd.to_numeric(top["promo_intensity"], errors="coerce"))
        ax.set_title("Promo Intensity by Brand")
        p = out_dir / "brand_promo_intensity.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p)

    if not by_region.empty:
        fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
        d = by_region.copy()
        d["median"] = pd.to_numeric(d["median"], errors="coerce")
        top = d.sort_values("median", ascending=False).head(25)
        labels = top["region"].astype(str) + "|" + top["product"].astype(str)
        ax.barh(labels, top["median"])
        ax.set_title("ProZorro Median Unit Price by Region/Product")
        p = out_dir / "prozorro_region_median.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        images.append(p)

    xlsx = out_dir / "graphs_brand_region_output.xlsx"
    common.write_tables_xlsx(xlsx, {"Brand_IO_Metrics": brand_io, "Brand_Economic_Metrics": brand_econ, "Prozorro_ByRegion": by_region})
    pdf = out_dir / "graphs_brand_region_report.pdf"
    common.save_pdf_report(pdf, "Brand and Region Graphs", [f"brand_io_rows={len(brand_io)}", f"brand_econ_rows={len(brand_econ)}", f"region_rows={len(by_region)}", "Interpretation option: IO concentration, promo intensity, and regional dispersion."], {"Brand_IO_Metrics": brand_io, "Prozorro_ByRegion": by_region}, images)
    common.print_block("GRAPHS BRAND/REGION", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"images: {len(images)}"])
    return out_dir


if __name__ == "__main__":
    run_decomposition_graphs()
    run_overlay_ln_graphs()
    run_corr_lag_graphs()
    run_brand_region_graphs()
