#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import math
import re

import numpy as np
import pandas as pd

from build_readme_docx import build_docx_from_markdown


REPO_ROOT = Path(__file__).resolve().parent
OUTPUTS_ROOT = REPO_ROOT / "outputs"

MODULE_ORDER = [
    "sheet_FarmGateUA_initial",
    "sheet_FarmGateUA_filled",
    "sheet_ProducerUA",
    "sheet_ConsumerUA",
    "sheet_EU",
    "sheet_ProZorro",
    "sheet_Silpo",
    "sheet_Novus",
    "sheet_CME",
    "model_short_chain_regional",
    "model_ardl",
    "model_ecm",
    "model_nardl",
    "model_vecm",
    "model_discounts",
    "model_intersection_bidirectional",
    "model_forecast_knn",
    "model_secondary_synthetic_consumer",
    "graphs_decomposition",
    "graphs_overlay_ln",
    "graphs_correlations_lags",
    "graphs_brand_region",
]

MODULE_DESCRIPTIONS = {
    "sheet_FarmGateUA_initial": "the initial daily farm-gate workbook for Ukrainian farm-gate prices.",
    "sheet_FarmGateUA_filled": "the gap-filled daily farm-gate workbook used as the alternative reconstruction source.",
    "sheet_ProducerUA": "domestic producer prices used as the first post-farm-gate downstream layer.",
    "sheet_ConsumerUA": "official consumer-price benchmarks used as an external plausibility anchor.",
    "sheet_EU": "EU benchmark prices used as an external international reference.",
    "sheet_ProZorro": "public procurement prices representing the institutional intermediary layer.",
    "sheet_Silpo": "Silpo retail prices and promo-state metadata.",
    "sheet_Novus": "Novus retail prices and brand-level assortment evidence.",
    "sheet_CME": "commodity-market benchmark data used as an external check rather than an endogenous chain stage.",
    "model_short_chain_regional": "the consolidated RW4 chain workbook, which is the main analytical output for forward, reverse, brand, average, and robustness results.",
    "model_ardl": "the pooled ARDL evidence used as a linear distributed-lag benchmark.",
    "model_ecm": "the ECM evidence used for explicit equilibrium-correction interpretation.",
    "model_nardl": "the asymmetric distributed-lag evidence used to detect different responses to positive and negative shocks.",
    "model_vecm": "the system-level VECM evidence used for multistage dynamics and impulse interpretation.",
    "model_discounts": "the retail-promo comparison module that contrasts observed and baseline price transmission.",
    "model_intersection_bidirectional": "the cross-retailer overlap module that tests shared Silpo-Novus evidence where overlap exists.",
    "model_forecast_knn": "the forecasting and synthetic-retail module that projects producer and consumer paths.",
    "model_secondary_synthetic_consumer": "the secondary synthetic-consumer module that would link synthetic retail signals to consumer prices when enough overlap exists.",
    "graphs_decomposition": "the trend-seasonal decomposition graph pack.",
    "graphs_overlay_ln": "the before/after log transformation and cross-source overlay graph pack.",
    "graphs_correlations_lags": "the cross-source correlation and lag graph pack.",
    "graphs_brand_region": "the brand concentration and ProZorro regional heterogeneity graph pack.",
}

SHEET_DESCRIPTIONS = {
    "Run_All_Summary": "execution log with one row per module step, showing whether the step finished and where its artifacts were written.",
    "Artifacts_By_Module": "artifact inventory by module, counting workbook, PDF, Markdown, and PNG outputs.",
    "Sheets_Index": "index of current RW4 workbook sheets discovered during the run-all summarization step.",
    "Tests_Interpretation": "compact interpretation table for stationarity, cointegration-support, and related diagnostics.",
    "Results_Interpretation": "compact interpretation table for coefficient magnitudes, significance shares, and robustness shares.",
    "Module_Block_Interpretation": "one-line module summaries combining diagnostics and result signals.",
    "Consolidated_ModelCoefficients": "the main forward-chain coefficient table across panel definitions, reconstruction variants, farm-gate sources, and model families.",
    "Consolidated_PreTests": "pair-level integration and cointegration pretests used to decide whether level or correction-type models are admissible.",
    "Panel_Index": "catalog of the active product, comparison, and brand panels used in the consolidated RW4 chain.",
    "ReverseFlow_ModelCoefficients": "reverse-flow estimates that test whether downstream retail shocks transmit back through the chain.",
    "RawMilk_To_Product_Transmission": "direct farm-gate to downstream product links used to check whether raw-milk information bypasses intermediate stages.",
    "AveragePrice_Chain_Transmission": "average-price panels that smooth product detail and show chain behavior at a more aggregated level.",
    "Retailer_Brand_Transmission": "brand-level transmission table, mostly for Silpo, that checks whether brand segmentation changes pass-through.",
    "Variant_Robustness": "cross-variant stability table that compares linear and pchip reconstruction choices.",
    "FarmGate_Source_Comparison": "cross-source stability table comparing the initial and gap-filled farm-gate inputs.",
    "Benchmark_Comparison": "best-lag benchmark correlations against ConsumerUA and EU anchors.",
    "Coverage_Validation": "coverage audit that verifies every required RW4 link has estimable rows and shows how many core findings survive.",
    "Reconstruction_Diagnostics": "source-by-region diagnostics for interpolation gaps, spikes, reaggregation gaps, and imputation shares.",
    "Mapping_Audit": "mapping-quality audit from raw labels into product families and admissible units.",
    "Unit_Admissibility": "summary of which source-unit combinations are economically comparable enough to be modeled.",
    "NARDL_Multipliers": "dynamic multiplier paths for asymmetric NARDL models.",
    "VECM_IRF": "impulse-response style outputs from the system models.",
    "Rule_Documentation": "brief description of the admissibility and panel-construction rules used in RW4.",
    "Promo_State_Incidence": "binary promo-incidence model output or an explicit placeholder when the model is not estimable.",
    "Promo_State_Type": "multinomial promo-state model output or an explicit placeholder when the model is not estimable.",
    "Promo_State_Depth": "conditional markdown-depth model output or an explicit placeholder when the model is not estimable.",
    "Asymmetry_Observed_vs_Baseline": "comparison table between observed retail transmission and promo-controlled baseline transmission.",
    "Discount_Strategy_Synthesis": "plain-language summary of the discount-module conclusions.",
    "Silpo_Discounts_Occurrence": "legacy-compatible alias for the promo-incidence output.",
    "Silpo_Discounts_Depth": "legacy-compatible alias for the promo-depth output.",
    "Silpo_Transmission_PromoCtrl": "legacy-compatible alias for the observed-vs-baseline comparison table.",
    "Decomposition_Summary": "summary statistics for trend, seasonal, and residual variance shares.",
    "Decomposition_Index": "index of the decomposition chart set.",
    "Decomposition_All": "long-form data behind the decomposition charts.",
    "BeforeAfterLN_Index": "index of the before/after log-transformation charts.",
    "Overlay_Index": "index of the cross-source overlay charts.",
    "BeforeAfterLN_All": "long-form data behind the before/after log charts.",
    "Overlay_All": "long-form data behind the cross-source overlay charts.",
    "Correlations": "pairwise correlation table across sources, frequencies, and lag choices.",
    "Corr_Matrix": "matrix view of cross-source same-window correlations.",
    "Lag_Best": "best lag per pair and product according to the lag-profile search.",
    "Lag_Profiles": "full lag-profile table behind the lag charts.",
    "Brand_IO_Metrics": "brand concentration and private-label mix table by month and product family.",
    "Brand_Economic_Metrics": "brand premium, promo intensity, volatility, and brand-specific pass-through evidence.",
    "Prozorro_ByRegion": "regional distribution diagnostics for ProZorro prices.",
    "Forecast_Summary": "accuracy summary for the KNN-based producer and consumer forecasts.",
    "Forecast_Predictions": "holdout predictions versus realized values for the forecast module.",
    "Synthetic_Retail_Series": "synthetic-retail panel created from the forecast module.",
    "Synthetic_Influence_Coefficient": "coefficients linking synthetic retail signals to downstream outcomes.",
    "Synthetic_to_Consumer_Link": "consumer-link regressions that test whether synthetic retail contains extra consumer information.",
    "Ultimate_Consumer_Price": "implied consumer price path based on the synthetic-retail exercise.",
    "Bidirectional_Results": "main bidirectional-regression result or an explanatory note when overlap is insufficient.",
    "Bidirectional_Granger": "Granger-type overlap test or an explanatory note when overlap is insufficient.",
    "Intersection_Combination_Summar": "combined-secondary-model summary or an explanatory note when overlap is insufficient.",
    "Intersection_Combination_Detail": "detail table for the combined-secondary model when such a model is estimable.",
    "CrossTable_Correlations": "cross-retailer and cross-source overlap correlations used to diagnose whether bidirectional estimation is even feasible.",
}


def _find_thesis_root() -> Path:
    for path in [REPO_ROOT, *REPO_ROOT.parents]:
        if path.name == "Master Thesis":
            return path
    return REPO_ROOT.parent


def _safe_num(series: pd.Series | pd.Index | np.ndarray | list[object]) -> pd.Series:
    return pd.to_numeric(pd.Series(series), errors="coerce")


def _is_missing(value: object) -> bool:
    return value is None or (isinstance(value, float) and math.isnan(value))


def _fmt_number(value: object, digits: int = 3) -> str:
    if _is_missing(value):
        return "n/a"
    value = float(value)
    if abs(value) >= 100:
        return f"{value:,.1f}"
    if abs(value) >= 10:
        return f"{value:,.2f}"
    return f"{value:,.{digits}f}"


def _fmt_percent(value: object, digits: int = 1) -> str:
    if _is_missing(value):
        return "n/a"
    return f"{float(value) * 100:.{digits}f}%"


def _bold(text: str) -> str:
    return f"**{text}**"


def _bold_number(value: object, digits: int = 3) -> str:
    return _bold(_fmt_number(value, digits=digits))


def _bold_percent(value: object, digits: int = 1) -> str:
    return _bold(_fmt_percent(value, digits=digits))


def _bold_int(value: object) -> str:
    if _is_missing(value):
        return _bold("n/a")
    return _bold(f"{int(round(float(value))):,}")


def _humanize_token(text: str) -> str:
    pretty = text.replace("_", " ").strip()
    pretty = re.sub(r"\s+", " ", pretty)
    pretty = pretty.replace("rw4", "RW4")
    pretty = pretty.replace("uah", "UAH")
    pretty = pretty.replace("ln", "log")
    return pretty


def _png_stems(path: Path) -> list[str]:
    return sorted(p.stem for p in path.glob("*.png"))


def _png_family_counts(path: Path) -> Counter[str]:
    families: Counter[str] = Counter()
    for png in path.glob("*.png"):
        stem = png.stem
        if stem.startswith("before_after_ln_"):
            families["before_after_ln"] += 1
        elif stem.startswith("overlay_"):
            families["overlay"] += 1
        elif stem.startswith("decomp_observed_trend_"):
            families["decomp_observed_trend"] += 1
        elif stem.startswith("decomp_seasonal_resid_"):
            families["decomp_seasonal_resid"] += 1
        elif stem.startswith("time_series_"):
            families["time_series"] += 1
        elif stem.startswith("lag_profile_"):
            families["lag_profile"] += 1
        elif stem.startswith("nardl_multipliers_"):
            families["nardl_multipliers"] += 1
        elif stem.startswith("ecm_adjustment_"):
            families["ecm_adjustment"] += 1
        else:
            families[stem] += 1
    return families


def _read_excel(path: Path, sheet_name: str) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name=sheet_name)


def _load_context() -> dict[str, object]:
    run_path = OUTPUTS_ROOT / "run_all_summary" / "run_all_rw4_summary.xlsx"
    total_path = OUTPUTS_ROOT / "total_run" / "Total_Run.xlsx"
    primary_path = OUTPUTS_ROOT / "primary_chain_summary" / "primary_chain_consolidated.xlsx"
    discounts_path = OUTPUTS_ROOT / "model_discounts" / "model_discounts_output.xlsx"
    corr_path = OUTPUTS_ROOT / "graphs_correlations_lags" / "graphs_correlations_lags_output.xlsx"
    brand_path = OUTPUTS_ROOT / "graphs_brand_region" / "graphs_brand_region_output.xlsx"
    forecast_path = OUTPUTS_ROOT / "model_forecast_knn" / "model_forecast_knn_output.xlsx"
    decomp_path = OUTPUTS_ROOT / "graphs_decomposition" / "graphs_decomposition_output.xlsx"
    overlay_path = OUTPUTS_ROOT / "graphs_overlay_ln" / "graphs_overlay_ln_output.xlsx"
    intersection_path = OUTPUTS_ROOT / "model_intersection_bidirectional" / "model_intersection_bidirectional_output.xlsx"
    secondary_path = OUTPUTS_ROOT / "secondary_synthetic_consumer" / "secondary_synthetic_consumer_output.xlsx"

    run = {
        "Run_All_Summary": _read_excel(run_path, "Run_All_Summary"),
        "Artifacts_By_Module": _read_excel(run_path, "Artifacts_By_Module"),
        "Sheets_Index": _read_excel(run_path, "Sheets_Index"),
        "Tests_Interpretation": _read_excel(run_path, "Tests_Interpretation"),
        "Results_Interpretation": _read_excel(run_path, "Results_Interpretation"),
        "Module_Block_Interpretation": _read_excel(run_path, "Module_Block_Interpretation"),
    }
    total = {
        "00_Index": _read_excel(total_path, "00_Index"),
        "01_ModuleSummary": _read_excel(total_path, "01_ModuleSummary"),
        "02_CategorySummary": _read_excel(total_path, "02_CategorySummary"),
    }
    primary = {
        "Consolidated_ModelCoefficients": _read_excel(primary_path, "Consolidated_ModelCoefficients"),
        "Consolidated_PreTests": _read_excel(primary_path, "Consolidated_PreTests"),
        "ReverseFlow_ModelCoefficients": _read_excel(primary_path, "ReverseFlow_ModelCoefficients"),
        "RawMilk_To_Product_Transmission": _read_excel(primary_path, "RawMilk_To_Product_Transmission"),
        "AveragePrice_Chain_Transmission": _read_excel(primary_path, "AveragePrice_Chain_Transmission"),
        "Retailer_Brand_Transmission": _read_excel(primary_path, "Retailer_Brand_Transmission"),
        "Variant_Robustness": _read_excel(primary_path, "Variant_Robustness"),
        "FarmGate_Source_Comparison": _read_excel(primary_path, "FarmGate_Source_Comparison"),
        "FarmGate_Direct_Summary": _read_excel(primary_path, "FarmGate_Direct_Summary"),
        "FarmGate_Reverse_Summary": _read_excel(primary_path, "FarmGate_Reverse_Summary"),
        "FarmGate_Variant_Stability": _read_excel(primary_path, "FarmGate_Variant_Stability"),
        "Unified_Retail_Comparison": _read_excel(primary_path, "Unified_Retail_Comparison"),
        "Intersection_Stability": _read_excel(primary_path, "Intersection_Stability"),
        "Benchmark_Comparison": _read_excel(primary_path, "Benchmark_Comparison"),
        "Coverage_Validation": _read_excel(primary_path, "Coverage_Validation"),
        "Reconstruction_Diagnostics": _read_excel(primary_path, "Reconstruction_Diagnostics"),
        "Mapping_Audit": _read_excel(primary_path, "Mapping_Audit"),
        "Unit_Admissibility": _read_excel(primary_path, "Unit_Admissibility"),
        "Retail_Combined_Diagnostics": _read_excel(primary_path, "Retail_Combined_Diagnostics"),
        "Retail_Combined_Methodology": _read_excel(primary_path, "Retail_Combined_Methodology"),
        "NARDL_Multipliers": _read_excel(primary_path, "NARDL_Multipliers"),
        "VECM_IRF": _read_excel(primary_path, "VECM_IRF"),
    }
    discounts = {
        "Promo_State_Incidence": _read_excel(discounts_path, "Promo_State_Incidence"),
        "Promo_State_Type": _read_excel(discounts_path, "Promo_State_Type"),
        "Promo_State_Depth": _read_excel(discounts_path, "Promo_State_Depth"),
        "Asymmetry_Observed_vs_Baseline": _read_excel(discounts_path, "Asymmetry_Observed_vs_Baseline"),
        "Discount_Strategy_Synthesis": _read_excel(discounts_path, "Discount_Strategy_Synthesis"),
    }
    corr = {
        "Corr_Matrix": _read_excel(corr_path, "Corr_Matrix"),
        "Lag_Best": _read_excel(corr_path, "Lag_Best"),
    }
    brand = {
        "Brand_IO_Metrics": _read_excel(brand_path, "Brand_IO_Metrics"),
        "Brand_Economic_Metrics": _read_excel(brand_path, "Brand_Economic_Metrics"),
        "Prozorro_ByRegion": _read_excel(brand_path, "Prozorro_ByRegion"),
    }
    forecast = {
        "Forecast_Summary": _read_excel(forecast_path, "Forecast_Summary"),
        "Synthetic_to_Consumer_Link": _read_excel(forecast_path, "Synthetic_to_Consumer_Link"),
        "Ultimate_Consumer_Price": _read_excel(forecast_path, "Ultimate_Consumer_Price"),
    }
    decomposition = {
        "Decomposition_Summary": _read_excel(decomp_path, "Decomposition_Summary"),
    }
    overlay = {
        "Overlay_Index": _read_excel(overlay_path, "Overlay_Index"),
        "BeforeAfterLN_Index": _read_excel(overlay_path, "BeforeAfterLN_Index"),
    }
    intersection = {
        "Bidirectional_Results": _read_excel(intersection_path, "Bidirectional_Results"),
        "Bidirectional_Granger": _read_excel(intersection_path, "Bidirectional_Granger"),
        "Intersection_Combination_Summar": _read_excel(intersection_path, "Intersection_Combination_Summar"),
        "CrossTable_Correlations": _read_excel(intersection_path, "CrossTable_Correlations"),
    }
    secondary = {
        "Synthetic_Consumer_Link": _read_excel(secondary_path, "Synthetic_Consumer_Link"),
        "Synthetic_Consumer_Predictions": _read_excel(secondary_path, "Synthetic_Consumer_Predictions"),
    }

    return {
        "run": run,
        "total": total,
        "primary": primary,
        "discounts": discounts,
        "corr": corr,
        "brand": brand,
        "forecast": forecast,
        "decomposition": decomposition,
        "overlay": overlay,
        "intersection": intersection,
        "secondary": secondary,
    }


def _interp_lookup(run_ctx: dict[str, pd.DataFrame]) -> dict[tuple[str, str, str], str]:
    lookup: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    for sheet_name in ["Tests_Interpretation", "Results_Interpretation"]:
        df = run_ctx[sheet_name]
        for _, row in df.iterrows():
            key = (str(row["module"]), str(row["xlsx_file"]), str(row["sheet"]))
            text = str(row["interpretation"]).strip()
            if text and text not in lookup[key]:
                lookup[key].append(text)
    return {k: " ".join(v) for k, v in lookup.items()}


def _sheet_description(sheet: str) -> str:
    if sheet in SHEET_DESCRIPTIONS:
        return SHEET_DESCRIPTIONS[sheet]
    lower = sheet.lower()
    if lower.endswith("_index") or lower == "panel_index":
        return "index sheet that points to generated panels, tables, or chart families."
    if "summary" in lower:
        return "summary sheet that condenses the module's main outputs."
    if lower.endswith("_all"):
        return "long-form stacked data underpinning the charts or summaries in this module."
    if "tests" in lower:
        return "diagnostic output focused on integration, residual, or admissibility testing."
    if "corr" in lower or "lag" in lower:
        return "correlation and lag diagnostic output."
    return "supporting output sheet that should be interpreted in conjunction with its module context."


def _source_name_from_module(module: str) -> str:
    return module.replace("sheet_", "")


def _top_source_rows(df: pd.DataFrame, count: int = 3) -> str:
    if df.empty:
        return "n/a"
    rows = []
    for _, row in df.head(count).iterrows():
        label = " / ".join(str(row[c]) for c in df.columns[:3])
        rows.append(label)
    return "; ".join(rows)


def _module_row(df: pd.DataFrame, module: str) -> pd.Series | None:
    subset = df[df["module"] == module]
    if subset.empty:
        return None
    return subset.iloc[0]


def _append_module_inventory(lines: list[str], ctx: dict[str, object]) -> None:
    artifacts = ctx["run"]["Artifacts_By_Module"]  # type: ignore[index]
    blocks = ctx["run"]["Module_Block_Interpretation"]  # type: ignore[index]
    lines.append("## Current RW4 Module Inventory")
    lines.append("")
    for module in MODULE_ORDER:
        arow = _module_row(artifacts, module)
        brow = _module_row(blocks, module)
        if arow is None:
            continue
        lines.append(f"### {module}")
        lines.append("")
        lines.append(
            f"{module} contains {MODULE_DESCRIPTIONS.get(module, 'a current RW4 output module')} "
            f"It currently writes {_bold_int(arow['xlsx_count'])} workbook(s), {_bold_int(arow['pdf_count'])} PDF(s), "
            f"{_bold_int(arow['md_count'])} Markdown file(s), and {_bold_int(arow['png_count'])} PNG figure(s)."
        )
        if brow is not None:
            lines.append(f"The run-all summary reads this block as: {brow['interpretation']}.")
        out_dir = Path(str(arow["output_dir"]))
        stems = _png_stems(out_dir)
        if stems:
            pretty = ", ".join(_humanize_token(stem) for stem in stems[:6])
            tail = "" if len(stems) <= 6 else f", plus {_bold_int(len(stems) - 6)} more figure file(s)"
            lines.append(f"The directly named figure files in this module begin with {pretty}{tail}.")
        lines.append("")


def _append_source_interpretation(lines: list[str], ctx: dict[str, object]) -> None:
    tests = ctx["run"]["Tests_Interpretation"]  # type: ignore[index]
    results = ctx["run"]["Results_Interpretation"]  # type: ignore[index]
    artifacts = ctx["run"]["Artifacts_By_Module"]  # type: ignore[index]
    lines.append("## Data And Preprocessing Interpretation")
    lines.append("")
    lines.append(
        "The source modules are not causal findings by themselves. They tell us whether each raw series behaves like a trending level series, "
        "whether simple level regressions are admissible, and whether the accompanying graphs suggest outliers, gaps, or region-specific irregularities."
    )
    lines.append("")

    source_modules = [m for m in MODULE_ORDER if m.startswith("sheet_")]
    for module in source_modules:
        trow = _module_row(tests, module)
        rrow = _module_row(results, module)
        arow = _module_row(artifacts, module)
        if trow is None or arow is None:
            continue
        out_dir = Path(str(arow["output_dir"]))
        graph_names = ", ".join(_humanize_token(stem) for stem in _png_stems(out_dir))
        source_name = _source_name_from_module(module)
        lines.append(f"### {source_name}")
        lines.append("")
        sentence = (
            f"{source_name} records an I(1)-like share of {_bold_percent(trow['i1_like_share'])} across its diagnostic rows. "
            f"This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without "
            "cointegration logic would be risky. "
        )
        if not _is_missing(trow.get("cointegration_support_share")):
            sentence += (
                f"Its cointegration-support share is {_bold_percent(trow['cointegration_support_share'])}, which matters only as a screening signal, "
                "not as final evidence of pass-through. "
            )
        if rrow is not None and not _is_missing(rrow.get("interpretation")):
            sentence += f"The compact run summary for this source is: {rrow['interpretation']}. "
        sentence += (
            f"The module currently emits {_bold_int(arow['png_count'])} graph(s), namely {graph_names}. "
            "The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, "
            "and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts."
        )
        lines.append(sentence)
        lines.append("")

    primary = ctx["primary"]  # type: ignore[assignment]
    recon = primary["Reconstruction_Diagnostics"]
    mapping = primary["Mapping_Audit"]
    unit = primary["Unit_Admissibility"]
    recon_summary = (
        recon.groupby("source", as_index=False)
        .agg(
            mean_abs_variant_gap=("mean_abs_variant_gap", "mean"),
            max_abs_variant_gap=("max_abs_variant_gap", "max"),
            monthly_reaggregation_gap=("monthly_reaggregation_gap", "mean"),
            linear_spike_count=("linear_spike_count", "mean"),
            pchip_spike_count=("pchip_spike_count", "mean"),
        )
        .sort_values("source")
    )
    matched_share = (mapping["mapping_quality_flag"].astype(str) == "matched").mean()
    multi_match_share = (mapping["mapping_quality_flag"].astype(str) == "multi_match").mean()
    unmatched_share = (mapping["mapping_quality_flag"].astype(str) == "unmatched").mean()
    economic_share = _safe_num(mapping["economically_comparable_flag"]).fillna(0).mean()
    lexical_share = _safe_num(mapping["lexical_anomaly_flag"]).fillna(0).mean()

    lines.append("### Reconstruction, Mapping, And Unit Admissibility")
    lines.append("")
    lines.append(
        f"The mapping audit covers {_bold_int(len(mapping))} mapped label groups. Exact matches account for {_bold_percent(matched_share)}, "
        f"multi-match cases account for {_bold_percent(multi_match_share)}, and explicit unmatched rows account for {_bold_percent(unmatched_share)}. "
        f"Economic comparability remains high at {_bold_percent(economic_share)}, while lexical anomalies are nearly absent at {_bold_percent(lexical_share)}. "
        "This means the weak points are not broad text noise; they are mostly concentrated in sources whose unit normalization is intrinsically imperfect."
    )
    lines.append("")

    top_recon_lines = []
    for _, row in recon_summary.iterrows():
        top_recon_lines.append(
            f"{row['source']} has mean absolute variant gap {_bold_number(row['mean_abs_variant_gap'])}, "
            f"worst-case variant gap {_bold_number(row['max_abs_variant_gap'])}, and mean monthly reaggregation gap {_bold_number(row['monthly_reaggregation_gap'])}"
        )
    lines.append(
        "Reconstruction diagnostics show that "
        + "; ".join(top_recon_lines)
        + ". In practice, this says producer reconstructions are smooth but still non-identical, while the farm-gate regional rebuild remains sensitive enough that robustness filtering is necessary."
    )
    lines.append("")

    admissible = unit[["source", "admissible_share", "admissibility_reason"]].copy()
    admissible["admissibility_reason"] = admissible["admissibility_reason"].astype(str)
    unit_bits = []
    for _, row in admissible.iterrows():
        unit_bits.append(
            f"{row['source']} retains admissible-share {_bold_percent(row['admissible_share'])} under reason '{row['admissibility_reason']}'"
        )
    lines.append(
        "The unit-admissibility table confirms that most active sources remain model-usable after normalization. "
        + "; ".join(unit_bits)
        + ". The important exceptions are EU missing-price rows, ProZorro rows without normalized unit price, and a thin Novus liter-based fragment that should not be forced into mass-style product comparisons."
    )
    lines.append("")


def _append_primary_chain_interpretation(lines: list[str], ctx: dict[str, object]) -> None:
    primary = ctx["primary"]  # type: ignore[assignment]
    coef = primary["Consolidated_ModelCoefficients"].copy()
    rev = primary["ReverseFlow_ModelCoefficients"].copy()
    raw = primary["RawMilk_To_Product_Transmission"].copy()
    avg = primary["AveragePrice_Chain_Transmission"].copy()
    brand = primary["Retailer_Brand_Transmission"].copy()
    coverage = primary["Coverage_Validation"].copy()
    pretests = primary["Consolidated_PreTests"].copy()
    robustness = primary["Variant_Robustness"].copy()
    farmgate_compare = primary["FarmGate_Source_Comparison"].copy()
    benchmark = primary["Benchmark_Comparison"].copy()

    for frame in [coef, rev, raw, avg, brand]:
        for col in ["sr_coef", "lr_coef", "ect_coef", "robust_across_reconstruction", "core_finding_flag", "unreliable_flag"]:
            if col in frame.columns:
                frame[col] = pd.to_numeric(frame[col], errors="coerce")

    pretests["cointegration_p"] = pd.to_numeric(pretests["cointegration_p"], errors="coerce")
    robustness["robust_linear_vs_pchip"] = pd.to_numeric(robustness["robust_linear_vs_pchip"], errors="coerce")
    robustness["interpolation_sensitive"] = pd.to_numeric(robustness["interpolation_sensitive"], errors="coerce")
    farmgate_compare["robust_across_reconstruction"] = pd.to_numeric(farmgate_compare["robust_across_reconstruction"], errors="coerce")
    benchmark["corr_at_best_lag"] = pd.to_numeric(benchmark["corr_at_best_lag"], errors="coerce")

    ok_share = (coef["model_status"].astype(str) == "ok").mean()
    unreliable_share = coef["unreliable_flag"].fillna(0).mean()
    core_share = coef["core_finding_flag"].fillna(0).mean()
    coint_share = (pretests["cointegration_p"] < 0.10).mean()
    integration_counts = pretests["integration_y"].value_counts(dropna=False).to_dict()
    no_fit_counts = coef.loc[coef["model_family"].astype(str) == "NO_FIT", "unreliable_reason"].fillna("NA").value_counts().to_dict()
    robust_linear = robustness["robust_linear_vs_pchip"].fillna(0).mean()
    interp_sensitive = robustness["interpolation_sensitive"].fillna(0).mean()
    robust_farmgate = farmgate_compare["robust_across_reconstruction"].fillna(0).mean()
    benchmark_summary = (
        benchmark.assign(abs_corr=benchmark["corr_at_best_lag"].abs())
        .groupby(["benchmark_source", "stage"], as_index=False)["abs_corr"]
        .mean()
        .sort_values(["benchmark_source", "abs_corr"], ascending=[True, False])
    )

    lines.append("## RW4 Chain Interpretation")
    lines.append("")
    lines.append(
        f"The consolidated forward-chain table contains {_bold_int(len(coef))} rows across {_bold_int(coef['model_family'].nunique())} model families. "
        f"Models finish with status 'ok' in {_bold_percent(ok_share)}, while {_bold_percent(unreliable_share)} of rows are still flagged unreliable and only {_bold_percent(core_share)} survive into the core-finding layer. "
        f"The pretests show cointegration-support share {_bold_percent(coint_share)} and an integration mix of I(0) {_bold_int(integration_counts.get('I(0)', 0))}, "
        f"I(1) {_bold_int(integration_counts.get('I(1)', 0))}, I(2) {_bold_int(integration_counts.get('I(2)', 0))}, and ambiguous {_bold_int(integration_counts.get('ambiguous', 0))}. "
        "So the mathematically safe reading is that the data are heterogeneous enough to require admissibility screening, not a one-model-fits-all shortcut."
    )
    lines.append("")
    lines.append(
        f"Recorded NO_FIT rows total {_bold_int(len(coef.loc[coef['model_family'].astype(str) == 'NO_FIT']))}. "
        f"The two dominant reasons are i2_series_blocked at {_bold_int(no_fit_counts.get('i2_series_blocked', 0))} rows and insufficient_overlap at {_bold_int(no_fit_counts.get('insufficient_overlap', 0))} rows. "
        "These rows are analytically useful because they tell us where the pipeline refused to fabricate coefficients on mathematically weak samples."
    )
    lines.append("")
    lines.append(
        f"Cross-variant robustness remains limited. Linear-versus-pchip robustness averages {_bold_percent(robust_linear)}, "
        f"interpolation sensitivity is flagged in {_bold_percent(interp_sensitive)}, and farm-gate-source robustness averages only {_bold_percent(robust_farmgate)}. "
        "That means coefficients should only be promoted when they survive both reconstruction and source comparisons."
    )
    lines.append("")

    lines.append("### Coverage Validation")
    lines.append("")
    for _, row in coverage.iterrows():
        if str(row["check_type"]) == "brand_panels":
            lines.append(
                f"The brand-panel coverage audit records {_bold_int(row['rows_total'])} panel definitions, {_bold_int(row['preferred_family_rows'])} preferred-family rows, "
                f"and {_bold_int(row['core_finding_rows'])} core findings."
            )
            continue
        lines.append(
            f"{row['chain_direction'].title()} {row['stage_from']} -> {row['stage_to']} has {_bold_int(row['rows_total'])} total rows, "
            f"{_bold_int(row['preferred_family_rows'])} preferred-family rows, and {_bold_int(row['core_finding_rows'])} core findings."
        )
    lines.append("")

    forward_pairs = (
        coef.groupby(["stage_from", "stage_to"], as_index=False)["core_finding_flag"]
        .agg(["count", "sum", "mean"])
        .reset_index()
        .sort_values("mean", ascending=False)
    )
    reverse_pairs = (
        rev.groupby(["stage_from", "stage_to"], as_index=False)["core_finding_flag"]
        .agg(["count", "sum", "mean"])
        .reset_index()
        .sort_values("mean", ascending=False)
    )
    raw_pairs = raw.groupby("stage_to", as_index=False)["core_finding_flag"].agg(["count", "sum", "mean"]).reset_index().sort_values("mean", ascending=False)
    avg_pairs = avg.groupby(["stage_from", "stage_to"], as_index=False)["core_finding_flag"].agg(["count", "sum", "mean"]).reset_index().sort_values("mean", ascending=False)

    lines.append("### Forward And Reverse Transmission")
    lines.append("")
    if not forward_pairs.empty:
        top_forward = forward_pairs.iloc[0]
        weakest_forward = forward_pairs.iloc[-1]
        lines.append(
            f"The strongest forward evidence appears in {top_forward['stage_from']} -> {top_forward['stage_to']}, where core findings reach {_bold_percent(top_forward['mean'])} across {_bold_int(top_forward['count'])} rows. "
            f"The weakest required forward link is {weakest_forward['stage_from']} -> {weakest_forward['stage_to']}, where core findings stay at {_bold_percent(weakest_forward['mean'])}. "
            "In this run that pattern means downstream transmission is easier to confirm than the earliest farm-gate step."
        )
    if not reverse_pairs.empty:
        top_reverse = reverse_pairs.iloc[0]
        lines.append(
            f"Reverse-flow evidence is non-trivial. {top_reverse['stage_from']} -> {top_reverse['stage_to']} reaches core-finding share {_bold_percent(top_reverse['mean'])}, "
            "which is stronger than several forward upstream links. This does not prove literal reverse causality by itself, but it does show that downstream pricing carries information back into the rest of the chain."
        )
    lines.append("")
    lines.append(
        f"One thesis-level warning is that FarmGateUA -> ProducerUA has coverage but no core findings: {_bold_int(int(coverage.loc[(coverage['stage_from'] == 'FarmGateUA') & (coverage['stage_to'] == 'ProducerUA'), 'core_finding_rows'].fillna(0).sum()))} core findings out of {_bold_int(int(coverage.loc[(coverage['stage_from'] == 'FarmGateUA') & (coverage['stage_to'] == 'ProducerUA'), 'rows_total'].fillna(0).sum()))} total rows. "
        "So the current national farm-gate series remains too blunt to explain producer prices cleanly, even though midstream and retail layers do transmit to one another."
    )
    lines.append("")

    lines.append("### Raw-Milk, Average, Brand, And Benchmark Layers")
    lines.append("")
    if not raw_pairs.empty:
        raw_best = raw_pairs.iloc[0]
        lines.append(
            f"The direct raw-milk-to-product layer is weak. Its best stage-to target is {raw_best['stage_to']} with core-finding share only {_bold_percent(raw_best['mean'])}, "
            "so the direct bypass interpretation should be treated as mostly unsupported on the present sample."
        )
    if not avg_pairs.empty:
        avg_best = avg_pairs.iloc[0]
        lines.append(
            f"The average-price layer is more stable than many product-specific links. Its strongest pair is {avg_best['stage_from']} -> {avg_best['stage_to']} with core-finding share {_bold_percent(avg_best['mean'])}, "
            "which suggests aggregation removes some product-level noise and exposes a smoother retail-procurement signal."
        )
    brand_missing_share = brand["brand"].isna().mean()
    brand_core_share = brand["core_finding_flag"].fillna(0).mean()
    brand_by_retailer = brand.groupby("retailer_panel", as_index=False)["core_finding_flag"].agg(["count", "sum", "mean"]).reset_index()
    lines.append(
        f"Brand-level transmission remains much thinner than product-level transmission. The brand table has {_bold_int(len(brand))} rows, but brand labels are missing in {_bold_percent(brand_missing_share)} of them and the overall core-finding share is only {_bold_percent(brand_core_share)}. "
        "Most surviving brand evidence comes from Silpo rather than Novus, which means any cross-retailer brand conclusions should still be framed as asymmetric in data support."
    )
    if not brand_by_retailer.empty:
        brand_parts = []
        for _, row in brand_by_retailer.iterrows():
            brand_parts.append(
                f"{row['retailer_panel']} contributes {_bold_int(row['count'])} rows with core-finding share {_bold_percent(row['mean'])}"
            )
        lines.append("By retailer, " + "; ".join(brand_parts) + ".")
    bench_parts = []
    for _, row in benchmark_summary.head(6).iterrows():
        bench_parts.append(
            f"{row['benchmark_source']} versus {row['stage']} has mean absolute best-lag correlation {_bold_number(row['abs_corr'])}"
        )
    lines.append(
        "Benchmark-comparison tables show how the RW4 layers line up with external anchors. "
        + "; ".join(bench_parts)
        + ". The strongest benchmark coherence is at the producer layer, especially against ConsumerUA for milk and sour-cream style products."
    )
    lines.append("")

    multipliers = primary["NARDL_Multipliers"]
    irf = primary["VECM_IRF"]
    if not multipliers.empty:
        pos_mean = _safe_num(multipliers["mult_pos"]).mean()
        neg_mean = _safe_num(multipliers["mult_neg"]).mean()
        lines.append(
            f"NARDL dynamic multipliers remain directionally informative even when single coefficients are unstable. Across saved multiplier rows, average positive-path multiplier is {_bold_number(pos_mean)} and average negative-path multiplier is {_bold_number(neg_mean)}. "
            "A large gap between those paths is the practical signal of asymmetry."
        )
        lines.append("")
    if not irf.empty:
        irf_cols = [c for c in irf.columns if c.startswith("irf_")]
        irf_max = pd.concat([_safe_num(irf[c]).abs() for c in irf_cols], axis=0).max()
        lines.append(
            f"The saved VECM impulse-style outputs span {_bold_int(len(irf))} rows, and the largest absolute response among explicit IRF columns is {_bold_number(irf_max)}. "
            "Because the system-level VECM block has low overall significance support, these IRFs should be read as structural diagnostics rather than headline elasticities."
        )
        lines.append("")


def _append_model_module_interpretation(lines: list[str], ctx: dict[str, object]) -> None:
    results = ctx["run"]["Results_Interpretation"]  # type: ignore[index]
    tests = ctx["run"]["Tests_Interpretation"]  # type: ignore[index]
    discounts = ctx["discounts"]  # type: ignore[assignment]
    forecast = ctx["forecast"]  # type: ignore[assignment]
    intersection = ctx["intersection"]  # type: ignore[assignment]
    secondary = ctx["secondary"]  # type: ignore[assignment]

    lines.append("## Model-Specific Interpretation")
    lines.append("")

    for module in ["model_ardl", "model_ecm", "model_nardl", "model_vecm"]:
        rrow = _module_row(results, module)
        trow = _module_row(tests, module)
        if rrow is None:
            continue
        lines.append(f"### {module}")
        lines.append("")
        base = f"{module} currently summarizes {_bold_int(rrow['n_rows'])} rows. {rrow['interpretation']}."
        if trow is not None:
            base += f" The diagnostic screen for this block reads {trow['interpretation']}."
        if module == "model_ecm":
            base += " ECM is the most interpretable correction-style block here, but the sample is tiny and should be treated as confirmatory only where it agrees with the consolidated chain."
        if module == "model_nardl":
            base += " NARDL remains the richest block for asymmetric pass-through, but it also contains many of the largest unstable coefficients, so core-filtering matters."
        if module == "model_vecm":
            base += " The VECM system is structurally informative, yet its significance density is low, so system coefficients should not outrank simpler robust links."
        lines.append(base)
        lines.append("")

    lines.append("### model_discounts")
    lines.append("")
    incidence = discounts["Promo_State_Incidence"]
    promo_type = discounts["Promo_State_Type"]
    promo_depth = discounts["Promo_State_Depth"]
    synthesis = discounts["Discount_Strategy_Synthesis"]
    lines.append(
        f"The discount module is analytically useful, but the explicit promo-state equations are not estimable on the present sample. "
        f"Incidence, type, and depth each contain {_bold_int(len(incidence))}, {_bold_int(len(promo_type))}, and {_bold_int(len(promo_depth))} placeholder row(s) rather than fitted coefficient tables. "
        "That is an honest mathematical outcome: the data do not provide enough stable within-panel variation or convergence support for those nonlinear equations right now."
    )
    lines.append("")
    synthesis_bits = []
    for _, row in synthesis.iterrows():
        synthesis_bits.append(f"{row.iloc[0]} = {_bold(str(row.iloc[1]))}")
    lines.append(
        "The plain-language synthesis table currently says "
        + "; ".join(synthesis_bits)
        + ". The correct interpretation is that promotions matter for reading transmission, but the exact promo-state probability mechanism still needs a different data structure."
    )
    lines.append("")

    lines.append("### model_forecast_knn")
    lines.append("")
    forecast_summary = forecast["Forecast_Summary"].copy()
    forecast_summary["rmse_dlog"] = pd.to_numeric(forecast_summary["rmse_dlog"], errors="coerce")
    forecast_summary["r2_train"] = pd.to_numeric(forecast_summary["r2_train"], errors="coerce")
    producer_mask = forecast_summary["target"].astype(str) == "ProducerUA"
    consumer_mask = forecast_summary["target"].astype(str) == "ConsumerUA"
    synth_consumer = forecast["Synthetic_to_Consumer_Link"].copy()
    synth_consumer["p_synth_to_consumer"] = pd.to_numeric(synth_consumer["p_synth_to_consumer"], errors="coerce")
    synth_consumer["coef_synth_to_consumer"] = pd.to_numeric(synth_consumer["coef_synth_to_consumer"], errors="coerce")
    sig_links = synth_consumer[synth_consumer["p_synth_to_consumer"] < 0.05]
    lines.append(
        f"The forecast block is one of the cleaner empirical components. Producer holdout RMSE ranges from {_bold_number(forecast_summary.loc[producer_mask, 'rmse_dlog'].min())} to {_bold_number(forecast_summary.loc[producer_mask, 'rmse_dlog'].max())}, "
        f"consumer holdout RMSE ranges from {_bold_number(forecast_summary.loc[consumer_mask, 'rmse_dlog'].min())} to {_bold_number(forecast_summary.loc[consumer_mask, 'rmse_dlog'].max())}, "
        f"and training R-squared stays in the {_bold_percent(forecast_summary['r2_train'].min())} to {_bold_percent(forecast_summary['r2_train'].max())} range. "
        "So forecasting is working as a smoothing and plausibility tool even where causal transmission remains ambiguous."
    )
    lines.append("")
    if sig_links.empty:
        lines.append(
            "Synthetic retail does not add statistically significant consumer information beyond the baseline consumer link on the present sample."
        )
    else:
        parts = []
        for _, row in sig_links.iterrows():
            parts.append(
                f"{row['product']} has synthetic-to-consumer coefficient {_bold_number(row['coef_synth_to_consumer'])} at p-value {_bold_number(row['p_synth_to_consumer'])}"
            )
        lines.append(
            "Within the synthetic-to-consumer link table, the significant results are "
            + "; ".join(parts)
            + ". This makes sour cream the clearest case where the synthetic retail proxy is carrying independent information."
        )
    lines.append("")

    lines.append("### model_intersection_bidirectional And model_secondary_synthetic_consumer")
    lines.append("")
    lines.append(
        f"The intersection module currently resolves to explicit insufficiency notes rather than regressions: '{intersection['Bidirectional_Results'].iloc[0, 0]}', "
        f"'{intersection['Bidirectional_Granger'].iloc[0, 0]}', and '{intersection['Intersection_Combination_Summar'].iloc[0, 0]}'. "
        "This does not prove the absence of cross-retailer interaction; it proves that the shared Silpo-Novus sample is not long or dense enough to estimate that interaction credibly."
    )
    lines.append("")
    lines.append(
        f"The secondary synthetic-consumer module is still empty, with {_bold_int(len(secondary['Synthetic_Consumer_Link']))} rows in Synthetic_Consumer_Link and "
        f"{_bold_int(len(secondary['Synthetic_Consumer_Predictions']))} rows in Synthetic_Consumer_Predictions. "
        "That should be read as unfinished data support rather than as a negative substantive result."
    )
    lines.append("")


def _append_graph_interpretation(lines: list[str], ctx: dict[str, object]) -> None:
    artifacts = ctx["run"]["Artifacts_By_Module"]  # type: ignore[index]
    corr = ctx["corr"]  # type: ignore[assignment]
    brand = ctx["brand"]  # type: ignore[assignment]
    forecast = ctx["forecast"]  # type: ignore[assignment]
    decomposition = ctx["decomposition"]  # type: ignore[assignment]
    overlay = ctx["overlay"]  # type: ignore[assignment]

    lines.append("## Graph Interpretation")
    lines.append("")
    lines.append(
        "This section explains what the graph families are telling us without reproducing the figures themselves. "
        "The main rule is that graphs are strongest as pattern checks and plausibility screens; they are not substitutes for the robustness-filtered coefficient tables."
    )
    lines.append("")

    source_graph_modules = [m for m in MODULE_ORDER if m.startswith("sheet_")]
    lines.append("### Source-Sheet Graphs")
    lines.append("")
    for module in source_graph_modules:
        arow = _module_row(artifacts, module)
        if arow is None:
            continue
        out_dir = Path(str(arow["output_dir"]))
        graphs = _png_stems(out_dir)
        lines.append(
            f"{_source_name_from_module(module)} contributes {_bold_int(len(graphs))} source graphs: "
            + ", ".join(_humanize_token(stem) for stem in graphs)
            + ". The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, "
            "and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through."
        )
        lines.append("")

    lines.append("### Decomposition Graphs")
    lines.append("")
    decomp_dir = Path(str(_module_row(artifacts, "graphs_decomposition")["output_dir"]))  # type: ignore[index]
    decomp_families = _png_family_counts(decomp_dir)
    decomp_summary = decomposition["Decomposition_Summary"].copy()
    decomp_summary["seasonal_strength"] = pd.to_numeric(decomp_summary["seasonal_strength"], errors="coerce")
    top_seasonal = decomp_summary.sort_values("seasonal_strength", ascending=False).head(5)
    seasonal_parts = []
    for _, row in top_seasonal.iterrows():
        seasonal_parts.append(
            f"{row['source']} {row['product']} with seasonal strength {_bold_number(row['seasonal_strength'])}"
        )
    lines.append(
        f"The decomposition pack contains {_bold_int(decomp_families.get('decomp_observed_trend', 0))} observed-versus-trend figures and "
        f"{_bold_int(decomp_families.get('decomp_seasonal_resid', 0))} seasonal-versus-residual figures. "
        "These plots show that upstream series are largely trend-driven, while some retail families carry visibly stronger seasonal structure. "
        "The strongest seasonal signatures in the summary table are "
        + "; ".join(seasonal_parts)
        + ". That means seasonality is mostly a retail-category issue rather than a farm-gate issue."
    )
    lines.append("")

    lines.append("### Overlay And Log-Transformation Graphs")
    lines.append("")
    overlay_dir = Path(str(_module_row(artifacts, "graphs_overlay_ln")["output_dir"]))  # type: ignore[index]
    overlay_families = _png_family_counts(overlay_dir)
    lines.append(
        f"The overlay pack contains {_bold_int(overlay_families.get('before_after_ln', 0))} before/after-log figures and {_bold_int(overlay_families.get('overlay', 0))} cross-source overlay figures. "
        "The log figures answer whether scale compression makes dynamics more comparable across products; the overlay figures answer whether different sources co-move in their common windows. "
        f"The overlay index spans {_bold_int(len(overlay['Overlay_Index']))} product windows, while the before/after index spans {_bold_int(len(overlay['BeforeAfterLN_Index']))} source-product combinations."
    )
    lines.append("")

    lines.append("### Correlation And Lag Graphs")
    lines.append("")
    lag_best = corr["Lag_Best"].copy()
    lag_best["corr"] = pd.to_numeric(lag_best["corr"], errors="coerce")
    top_pos = lag_best.sort_values("corr", ascending=False).head(5)
    top_neg = lag_best.sort_values("corr", ascending=True).head(5)
    pos_parts = []
    neg_parts = []
    for _, row in top_pos.iterrows():
        pos_parts.append(
            f"{row['pair_left']} -> {row['pair_right']} for {row['product']} at lag {_bold_int(row['lag_days'])} with correlation {_bold_number(row['corr'])}"
        )
    for _, row in top_neg.iterrows():
        neg_parts.append(
            f"{row['pair_left']} -> {row['pair_right']} for {row['product']} at lag {_bold_int(row['lag_days'])} with correlation {_bold_number(row['corr'])}"
        )
    lines.append(
        "The correlation-and-lag graphs are the quickest visual check on timing. The strongest positive best-lag relationships are "
        + "; ".join(pos_parts)
        + ". The strongest negative best-lag relationships are "
        + "; ".join(neg_parts)
        + ". Large negative lag peaks are not automatically errors, but they are the first place to look for mismatch, opposite seasonal timing, or unit-composition drift."
    )
    lines.append("")

    lines.append("### Brand And Regional Graphs")
    lines.append("")
    brand_io = brand["Brand_IO_Metrics"].copy()
    region = brand["Prozorro_ByRegion"].copy()
    brand_io["hhi_brand"] = pd.to_numeric(brand_io["hhi_brand"], errors="coerce")
    region["cv"] = pd.to_numeric(region["cv"], errors="coerce")
    top_hhi = brand_io.sort_values("hhi_brand", ascending=False).head(5)
    top_cv = region.sort_values("cv", ascending=False).head(5)
    hhi_parts = []
    cv_parts = []
    for _, row in top_hhi.iterrows():
        hhi_parts.append(
            f"{row['source']} {row['standardized_type']} in {str(row['month'])[:10]} with HHI {_bold_number(row['hhi_brand'])} on {_bold_int(row['sku_count'])} SKU(s)"
        )
    for _, row in top_cv.iterrows():
        cv_parts.append(
            f"{row['region']} {row['product']} with CV {_bold_number(row['cv'])}"
        )
    lines.append(
        "The brand-region pack contains three direct figure files: brand HHI, brand promo intensity, and ProZorro regional median. "
        "Those graphs should be interpreted together with the tables: concentration spikes are meaningful only when SKU counts are not trivially small, and regional volatility is meaningful only when it persists beyond one-off outliers. "
        "The highest concentration cases are "
        + "; ".join(hhi_parts)
        + ". The most volatile regional ProZorro pockets are "
        + "; ".join(cv_parts)
        + "."
    )
    lines.append("")

    lines.append("### Model-Family Figures")
    lines.append("")
    model_graph_descriptions = [
        ("model_ardl", "ardl_short_run.png", "shows the pooled short-run ARDL effects and should be read against the low overall ARDL significance density."),
        ("model_ecm", "ecm_ect.png", "shows the equilibrium-correction coefficients, where more negative values mean faster error correction."),
        ("model_nardl", "nardl_short_run.png", "shows short-run asymmetry and should be paired with the multiplier tables."),
        ("model_nardl", "nardl_long_run.png", "shows long-run asymmetry and is useful only when the corresponding models remain admissible."),
        ("model_vecm", "vecm_alpha.png", "shows system adjustment coefficients and is more diagnostic than headline-causal in this run."),
        ("model_short_chain_regional", "chain_retail_from_producer.png", "summarizes the shorter producer-to-retail regional relationship."),
        ("model_discounts", "discount_delta_short_run.png", "shows how observed-vs-baseline short-run retail transmission differs."),
        ("model_discounts", "discount_delta_producer.png", "shows how producer-linked discount effects differ between observed and baseline pricing."),
        ("model_discounts", "discount_delta_eu.png", "shows how EU-linked discount effects differ between observed and baseline pricing."),
        ("model_forecast_knn", "forecast_producer_consumer.png", "visualizes holdout forecasting quality for producer and consumer series."),
        ("model_forecast_knn", "consumer_link_coef.png", "visualizes the consumer-link coefficients from the synthetic-retail module."),
        ("model_forecast_knn", "synthetic_retail_top_entity.png", "shows the dominant entities inside the synthetic-retail construction."),
        ("model_intersection_bidirectional", "bidirectional_coef.png", "would show cross-retailer bidirectional coefficients, but on this run it is mainly a placeholder context plot because overlap is thin."),
        ("model_intersection_bidirectional", "intersection_combo_coef.png", "would show combination-model coefficients, but again the current overlap is too weak for strong inference."),
    ]
    for module, filename, text in model_graph_descriptions:
        lines.append(f"{filename}: {text}")
    lines.append("")

    lines.append("### Legacy Product-Retailer Graph Packs")
    lines.append("")
    legacy_books = [p for p in OUTPUTS_ROOT.glob("*/*/primary_chain_output*.xlsx") if "primary_chain_summary" not in str(p)]
    legacy_products = sorted({p.parts[-3] for p in legacy_books})
    legacy_retailers = sorted({p.parts[-2] for p in legacy_books})
    legacy_counter: Counter[str] = Counter()
    for png in OUTPUTS_ROOT.glob("*/*/*.png"):
        if png.parts[-3] in legacy_products:
            stem = png.stem
            if stem.startswith("time_series_"):
                legacy_counter["time_series"] += 1
            elif stem.startswith("lag_profile_"):
                legacy_counter["lag_profile"] += 1
            elif stem.startswith("nardl_multipliers_"):
                legacy_counter["nardl_multipliers"] += 1
            elif stem.startswith("ecm_adjustment_"):
                legacy_counter["ecm_adjustment"] += 1
    lines.append(
        f"The output tree still contains {_bold_int(len(legacy_books))} legacy product-retailer workbooks spanning products {', '.join(legacy_products)} and retailer panels {', '.join(legacy_retailers)}. "
        f"Their graph inventory includes {_bold_int(legacy_counter.get('time_series', 0))} time-series figures, {_bold_int(legacy_counter.get('lag_profile', 0))} lag-profile figures, "
        f"{_bold_int(legacy_counter.get('nardl_multipliers', 0))} NARDL-multiplier figures, and {_bold_int(legacy_counter.get('ecm_adjustment', 0))} ECM-adjustment figures. "
        "These packs are still useful as panel-level diagnostics, but they are not the authoritative RW4 chain summary anymore because they follow the older product-retailer reporting structure."
    )
    lines.append("")


def _append_workbook_map(lines: list[str], ctx: dict[str, object]) -> None:
    run = ctx["run"]  # type: ignore[assignment]
    sheets = run["Sheets_Index"]
    artifacts = run["Artifacts_By_Module"]
    interp = _interp_lookup(run)

    lines.append("## Detailed Workbook Map")
    lines.append("")
    lines.append(
        "The lines below explain every current run-all workbook sheet without reproducing the output itself. "
        "Row and column counts are included so it is easy to tell whether a sheet is substantive, sparse, or just an index."
    )
    lines.append("")

    module_positions = {module: idx for idx, module in enumerate(MODULE_ORDER)}
    sheets = sheets.assign(_module_order=sheets["module"].map(lambda x: module_positions.get(str(x), 10_000)))
    sheets = sheets.sort_values(["_module_order", "module", "xlsx_file", "sheet"]).drop(columns="_module_order")

    for module, module_df in sheets.groupby("module", sort=False):
        arow = _module_row(artifacts, str(module))
        lines.append(f"### {module}")
        lines.append("")
        if arow is not None:
            lines.append(
                f"This module writes workbook(s) {arow['xlsx_files']} and the main output directory currently contains {_bold_int(arow['png_count'])} PNG figure(s)."
            )
        lines.append(MODULE_DESCRIPTIONS.get(str(module), "This is a current RW4 output module."))
        lines.append("")
        for xlsx_file, book_df in module_df.groupby("xlsx_file", sort=False):
            lines.append(f"Workbook {xlsx_file}:")
            for _, row in book_df.iterrows():
                key = (str(row["module"]), str(row["xlsx_file"]), str(row["sheet"]))
                note = interp.get(key, "")
                desc = _sheet_description(str(row["sheet"]))
                extra = f" Current compact interpretation: {note}" if note else ""
                lines.append(
                    f"Sheet {row['sheet']} has {_bold_int(row['rows'])} rows and {_bold_int(row['cols'])} columns. It is {desc}{extra}"
                )
            lines.append("")


def _append_caveats_and_plan(lines: list[str], ctx: dict[str, object]) -> None:
    primary = ctx["primary"]  # type: ignore[assignment]
    discounts = ctx["discounts"]  # type: ignore[assignment]
    coef = primary["Consolidated_ModelCoefficients"].copy()
    brand = primary["Retailer_Brand_Transmission"].copy()
    coverage = primary["Coverage_Validation"].copy()
    region = ctx["brand"]["Prozorro_ByRegion"].copy()  # type: ignore[index]
    coef["sr_coef"] = pd.to_numeric(coef["sr_coef"], errors="coerce")
    coef["lr_coef"] = pd.to_numeric(coef["lr_coef"], errors="coerce")
    coef["ect_coef"] = pd.to_numeric(coef["ect_coef"], errors="coerce")
    coef["max_abs_coef"] = coef[["sr_coef", "lr_coef", "ect_coef"]].abs().max(axis=1)
    region["cv"] = pd.to_numeric(region["cv"], errors="coerce")

    extreme = coef.loc[(coef["model_status"].astype(str) == "ok") & (coef["unreliable_flag"].fillna(0) == 0)].sort_values("max_abs_coef", ascending=False).head(5)
    extreme_parts = []
    for _, row in extreme.iterrows():
        extreme_parts.append(
            f"{row['panel_name']} on {row['link']} reaches maximum absolute coefficient {_bold_number(row['max_abs_coef'])}"
        )
    top_region_cv = region.sort_values("cv", ascending=False).head(3)
    region_parts = []
    for _, row in top_region_cv.iterrows():
        region_parts.append(f"{row['region']} {row['product']} with CV {_bold_number(row['cv'])}")

    farm_to_prod = coverage.loc[(coverage["stage_from"] == "FarmGateUA") & (coverage["stage_to"] == "ProducerUA")]
    farm_to_prod_core = int(farm_to_prod["core_finding_rows"].fillna(0).sum())
    farm_to_prod_rows = int(farm_to_prod["rows_total"].fillna(0).sum())
    missing_brand_share = brand["brand"].isna().mean()

    lines.append("## Mismatches, Non-Logical Results, And How To Fix Them")
    lines.append("")
    lines.append(
        f"1. Promo-state incidence, type, and depth are not mathematically estimable on the current sample. Each sheet is a placeholder row rather than a fitted model. "
        f"To fix this, widen the overlap window, aggregate promo states to weekly frequency, reduce the state space, or use regularized classification models after checking class balance."
    )
    lines.append(
        f"2. Brand rows miss explicit brand labels in {_bold_percent(missing_brand_share)} of the brand-transmission table. The missing-label pattern is concentrated in empty-brand Silpo cream panels. "
        "To fix this, drop empty normalized brands before panel construction, require a minimum non-empty brand share, and re-run the brand panel builder only on supported brand names."
    )
    lines.append(
        f"3. FarmGateUA -> ProducerUA has {_bold_int(farm_to_prod_core)} core findings out of {_bold_int(farm_to_prod_rows)} covered rows. "
        "That is a substantive mismatch between economic intuition and the present proxy quality. To reduce it, replace or supplement the national farm-gate average with product-resolved procurement or raw-milk contract data."
    )
    lines.append(
        f"4. Some statistically fitted coefficients are economically implausible in magnitude even when the row is not mechanically marked unreliable. Examples include "
        + "; ".join(extreme_parts)
        + ". To get rid of this, impose minimum overlap and variance thresholds, winsorize or robustify extreme panels, and add coefficient-plausibility filters before promoting results."
    )
    lines.append(
        f"5. Reconstruction robustness is still limited, so mathematically significant results can disappear when interpolation or farm-gate source changes. "
        "The fix is to report only doubly-robust findings, tighten interpolation anchors, and surface robustness flags directly in the thesis narrative rather than only in appendices."
    )
    lines.append(
        f"6. Regional ProZorro outliers remain strong in places such as "
        + "; ".join(region_parts)
        + ". These can create non-logical pass-through estimates if left untouched. The fix is to audit regional outliers, trim extreme procurement spikes, or run robust regional medians before aggregation."
    )
    lines.append(
        "7. Cross-retailer overlap is too thin for the bidirectional intersection module, and the secondary synthetic-consumer module is still empty. "
        "The fix is straightforward but data-heavy: extend the shared Silpo-Novus time window, standardize retailer calendar alignment, and only then re-run those modules."
    )
    lines.append(
        "8. Legacy three-stage product-retailer packs are still present inside the output tree and therefore remain visible in Total Run. "
        "If the thesis appendix should be RW4-only, move these legacy folders into an archive subtree or exclude them in the Total Run builder."
    )
    lines.append("")

    lines.append("## Further Changes")
    lines.append("")
    lines.append(
        "1. Clean brand normalization and rerun brand panels so the brand table no longer carries empty-brand rows."
    )
    lines.append(
        "2. Rebuild promo-state estimation on a pooled or weekly panel so promo incidence, type, and depth become genuinely estimable rather than placeholders."
    )
    lines.append(
        "3. Tighten admissibility filters with coefficient-plausibility screens and minimum support thresholds before calling anything a core finding."
    )
    lines.append(
        "4. Add a farm-gate data upgrade step, ideally using product-linked procurement or raw-milk contractual information, because the first chain link is the current bottleneck."
    )
    lines.append(
        "5. Separate authoritative RW4 outputs from legacy diagnostic packs in Total Run so the final thesis bundle is easier to defend and easier to read."
    )
    lines.append(
        "6. Re-run the final thesis narrative only on links that survive both interpolation robustness and farm-gate-source robustness, with brand and regional caveats attached explicitly."
    )
    lines.append("")


def build_report_markdown() -> str:
    ctx = _load_context()
    thesis_root = _find_thesis_root()
    run = ctx["run"]  # type: ignore[assignment]
    total = ctx["total"]  # type: ignore[assignment]

    run_status = run["Run_All_Summary"]
    artifacts = run["Artifacts_By_Module"]
    sheets = run["Sheets_Index"]
    total_index = total["00_Index"]
    total_modules = total["01_ModuleSummary"]
    category_summary = total["02_CategorySummary"]

    total_graphs = len(list(OUTPUTS_ROOT.rglob("*.png")))
    failed_steps = int((run_status["status"].astype(str) == "failed").sum())
    steps_ok = int((run_status["status"].astype(str) == "ok").sum())
    tables_total = len(total_index)
    current_module_count = len(artifacts)
    current_sheet_count = len(sheets)

    lines: list[str] = []
    lines.append("# RW4 Interpretation Report")
    lines.append("")
    lines.append(
        "This document explains the current RW4 output set without reproducing the raw tables or graphs. "
        "All values below are interpretive guideposts for the thesis write-up, not replacements for the original workbooks."
    )
    lines.append("")
    lines.append("## Executive View")
    lines.append("")
    lines.append(
        f"The current run completes {_bold_int(steps_ok)} of {_bold_int(len(run_status))} module steps with {_bold_int(failed_steps)} recorded failures. "
        f"Across the full output tree, Total Run bundles {_bold_int(tables_total)} tables and {_bold_int(total_graphs)} graphs, while the active RW4 run-all summary indexes "
        f"{_bold_int(current_sheet_count)} current sheets across {_bold_int(current_module_count)} modules. "
        f"The active input stack is the farm-gate initial workbook, the farm-gate gap-filled workbook, and the full UAH source workbook located under {thesis_root / 'Main materials/Model/Charniuk_Dairy_Research'}."
    )
    lines.append("")
    lines.append(
        f"The category mix inside Total Run is dominated by {_bold_int(int(category_summary.loc[category_summary['category'] == 'other', 'tables'].fillna(0).sum()))} general supporting tables, "
        f"{_bold_int(int(category_summary.loc[category_summary['category'] == 'tests', 'tables'].fillna(0).sum()))} diagnostic tables, "
        f"{_bold_int(int(category_summary.loc[category_summary['category'] == 'model_results', 'tables'].fillna(0).sum()))} coefficient tables, and "
        f"{_bold_int(int(category_summary.loc[category_summary['category'] == 'forecast', 'tables'].fillna(0).sum()))} forecast tables. "
        "So the pipeline is already richer than a single regression appendix; it is a layered evidence system with diagnostics, coefficients, forecasts, and graph packs."
    )
    lines.append("")

    _append_module_inventory(lines, ctx)
    _append_source_interpretation(lines, ctx)
    _append_primary_chain_interpretation(lines, ctx)
    _append_model_module_interpretation(lines, ctx)
    _append_graph_interpretation(lines, ctx)
    _append_workbook_map(lines, ctx)
    _append_caveats_and_plan(lines, ctx)

    return "\n".join(lines).strip() + "\n"


def generate_report(md_path: Path | None = None, docx_path: Path | None = None) -> tuple[Path, Path]:
    thesis_root = _find_thesis_root()
    md_path = md_path or (thesis_root / "RW4_Interpretation_Report.md")
    docx_path = docx_path or (thesis_root / "RW4_Interpretation_Report.docx")

    report_md = build_report_markdown()
    md_path.write_text(report_md, encoding="utf-8")
    build_docx_from_markdown(md_path, docx_path)
    return md_path, docx_path


def main() -> None:
    md_path, docx_path = generate_report()
    print(f"RW4 interpretation markdown generated: {md_path}")
    print(f"RW4 interpretation docx generated: {docx_path}")


if __name__ == "__main__":
    main()
