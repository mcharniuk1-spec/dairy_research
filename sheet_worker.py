#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Dict

import pandas as pd

import common
import rw2_extended_mapping_pipeline as rw2

SHEET_CONFIG: Dict[str, Dict[str, str]] = {
    "ProducerUA": {"raw_sheet": "Producer_UA", "value_col": "price"},
    "ConsumerUA": {"raw_sheet": "Consumer_UA", "value_col": "price"},
    "EU": {"raw_sheet": "Europe", "value_col": "price"},
    "ProZorro": {"raw_sheet": "Prozorro", "value_col": "price"},
    "Silpo": {"raw_sheet": "Silpo", "value_col": "price_current"},
    "Novus": {"raw_sheet": "Novus", "value_col": "price_current"},
    "CME": {"raw_sheet": "CME III", "value_col": "price"},
}


def run_sheet_module(source: str) -> Path:
    if source not in SHEET_CONFIG:
        raise ValueError(f"Unknown source {source}. Allowed: {list(SHEET_CONFIG)}")

    wb_path, raw = common.load_raw()
    cleaned_all = common.prepare_cleaned(raw)
    clean = cleaned_all[source].copy()
    if clean.empty:
        raise ValueError(f"No cleaned data for {source}")

    daily = rw2.daily_variants_for_dataset(clean, source=source)
    desc = rw2.build_descriptive_stats(daily, source) if not daily.empty else pd.DataFrame()
    series = rw2.long_price_series(daily) if not daily.empty else pd.DataFrame()

    tests = pd.DataFrame()
    if not daily.empty:
        weekly = rw2.prepare_weekly_for_tests(daily)
        tests = rw2.build_tests_table(weekly, min_obs=24)

    module_dir = common.get_output_dir(f"sheet_{source.lower()}")

    # Graph set
    plot_col = SHEET_CONFIG[source]["value_col"]
    value_col = plot_col if plot_col in clean.columns else "price"
    images = common.plot_basic_set(clean, module_dir, f"sheet_{source.lower()}", value_col=value_col)

    # Additional source-specific charts
    if source == "ProZorro" and "region" in clean.columns:
        p = module_dir / "sheet_prozorro_region_trends.png"
        common._plot_timeseries(clean, "date", "price", "region", "ProZorro: Region Unit Price Trends", p, max_groups=8)
        images.append(p)
    if source in {"Silpo", "Novus"} and "brand" in clean.columns:
        p = module_dir / f"sheet_{source.lower()}_brand_trends.png"
        common._plot_timeseries(clean, "date", value_col, "brand", f"{source}: Brand Price Trends", p, max_groups=8)
        images.append(p)

    xlsx = module_dir / f"sheet_{source.lower()}_output.xlsx"
    common.write_tables_xlsx(
        xlsx,
        {
            "raw": raw[source],
            "clean": clean,
            "daily_variants": daily,
            "series_long": series,
            "descriptive_stats": desc,
            "tests": tests,
        },
    )

    text = [
        f"Input workbook: {wb_path.name}",
        f"Source sheet: {SHEET_CONFIG[source]['raw_sheet']}",
        f"Rows (clean): {len(clean)}",
        f"Date range: {pd.to_datetime(clean['date'], errors='coerce').min().date()} .. {pd.to_datetime(clean['date'], errors='coerce').max().date()}",
        f"Products: {clean['product'].nunique() if 'product' in clean.columns else 0}",
        f"Stats rows: {len(desc)}",
        f"Tests rows: {len(tests)}",
        "Interpretation option: use tests table -> recommended_action/recommended_model_family per product.",
    ]

    pdf = module_dir / f"sheet_{source.lower()}_report.pdf"
    common.save_pdf_report(
        pdf,
        title=f"RW3 Separate Sheet Module - {source}",
        text_lines=text,
        table_map={
            "clean": clean,
            "descriptive_stats": desc,
            "tests": tests,
        },
        image_paths=images,
    )

    common.print_block(
        f"SHEET MODULE {source}",
        [
            f"xlsx: {xlsx}",
            f"pdf: {pdf}",
            f"graphs: {len(images)}",
            f"clean rows: {len(clean)}",
            f"tests rows: {len(tests)}",
        ],
    )
    return module_dir


if __name__ == "__main__":
    # default quick run
    run_sheet_module("ProducerUA")
