#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

import pandas as pd

from generate_data_estimation_updated import (
    Block,
    FigureBlock,
    ParagraphBlock,
    TableBlock,
    _b,
    _b_int,
    _b_num,
    _b_pct,
    _coerce_numeric,
    _coverage_row,
    _find_thesis_root,
    _fmt_int,
    _fmt_number,
    _fmt_percent,
    _load_product_book,
    _load_context,
    _mc_row,
    _write_docx_from_template,
)


REPO_ROOT = Path(__file__).resolve().parent
OUTPUTS_ROOT = REPO_ROOT / "outputs"
PRIMARY_PATH = OUTPUTS_ROOT / "primary_chain_summary" / "primary_chain_consolidated.xlsx"
SECOND_STAGE_ROOT = _find_thesis_root() / "analysis second stage"


def _top_literal_examples(literal_summary: pd.DataFrame) -> str:
    grouped = (
        literal_summary.groupby(["product", "product_literal"], as_index=False)["n_item_keys"]
        .sum()
        .sort_values(["n_item_keys"], ascending=[False])
    )
    top = (
        grouped
        .head(5)[["product", "product_literal", "n_item_keys"]]
        .itertuples(index=False)
    )
    parts = []
    for row in top:
        product = str(row.product).replace("_", " ").title()
        literal = str(row.product_literal).replace("_", " ").title()
        parts.append(f"{product} -> {literal} ({_fmt_int(row.n_item_keys)} item keys)")
    return "; ".join(parts)


def _top_brand_examples(brand_support: pd.DataFrame) -> str:
    top = (
        brand_support.sort_values(
            ["product", "retailer", "n_item_keys", "n_dates"],
            ascending=[True, True, False, False],
        )
        .groupby(["product", "retailer"], as_index=False)
        .head(1)
        .head(8)
    )
    parts = []
    for row in top.itertuples(index=False):
        brand = row.brand_norm if pd.notna(row.brand_norm) and str(row.brand_norm).strip() else "unbranded/generic label"
        product = str(row.product).replace("_", " ").title()
        retailer = str(row.retailer)
        day_word = "day" if int(row.n_dates) == 1 else "days"
        parts.append(f"{product} in {retailer}: {brand} ({_fmt_int(row.n_item_keys)} item keys, {_fmt_int(row.n_dates)} {day_word})")
    return "; ".join(parts)


def _select_first(df: pd.DataFrame, mask: pd.Series) -> pd.Series:
    subset = df.loc[mask].copy()
    if subset.empty:
        raise RuntimeError("Expected row was not found while building the fullversion thesis chapter.")
    return subset.iloc[0]


def _load_second_stage_context() -> dict[str, object]:
    data_root = SECOND_STAGE_ROOT / "data"
    outputs_root = SECOND_STAGE_ROOT / "outputs"
    figures_root = SECOND_STAGE_ROOT / "figures"
    docs_root = SECOND_STAGE_ROOT / "documents"

    retail = pd.read_csv(data_root / "retail_items_full_harmonized.csv")
    panel_daily = pd.read_csv(data_root / "second_stage_daily_panel.csv", parse_dates=["date"])
    match_audit = pd.read_csv(data_root / "retail_match_audit.csv")
    literal_summary = pd.read_csv(data_root / "retail_literal_summary.csv")
    brand_support = pd.read_csv(data_root / "retail_brand_support.csv")
    level_scores = pd.read_csv(data_root / "retail_level_scores.csv")
    level_selection = pd.read_csv(data_root / "retail_level_selection.csv")
    panel_coverage = pd.read_csv(data_root / "second_stage_panel_coverage.csv")
    lp_summary = pd.read_csv(outputs_root / "local_projection_summary.csv")
    lp_coeff = pd.read_csv(outputs_root / "local_projection_coefficients.csv")
    spread = pd.read_csv(outputs_root / "margin_market_power_models.csv")
    discount = pd.read_csv(outputs_root / "discount_strategy_models.csv")
    robust = pd.read_csv(outputs_root / "robust_findings.csv")

    return {
        "data_root": data_root,
        "outputs_root": outputs_root,
        "figures_root": figures_root,
        "docs_root": docs_root,
        "retail": retail,
        "panel_daily": panel_daily,
        "match_audit": match_audit,
        "literal_summary": literal_summary,
        "brand_support": brand_support,
        "level_scores": level_scores,
        "level_selection": level_selection,
        "panel_coverage": panel_coverage,
        "lp_summary": lp_summary,
        "lp_coeff": lp_coeff,
        "spread": spread,
        "discount": discount,
        "robust": robust,
    }


def _build_blocks() -> list[Block]:
    ctx = _load_context()
    ss = _load_second_stage_context()

    primary = ctx["primary"]
    discounts = ctx["discounts"]
    corr = ctx["corr"]
    brand_ctx = ctx["brand"]
    forecast = ctx["forecast"]

    coef = _coerce_numeric(primary["Consolidated_ModelCoefficients"])
    pretests = _coerce_numeric(primary["Consolidated_PreTests"])
    reverse = _coerce_numeric(primary["ReverseFlow_ModelCoefficients"])
    raw = _coerce_numeric(primary["RawMilk_To_Product_Transmission"])
    coverage = _coerce_numeric(primary["Coverage_Validation"])
    mapping = _coerce_numeric(primary["Mapping_Audit"])
    retail_combined_diag = _coerce_numeric(primary["Retail_Combined_Diagnostics"])
    farmgate_direct = _coerce_numeric(primary["FarmGate_Direct_Summary"])
    farmgate_reverse = _coerce_numeric(primary["FarmGate_Reverse_Summary"])
    benchmark = _coerce_numeric(primary["Benchmark_Comparison"])

    panel_index = _coerce_numeric(pd.read_excel(PRIMARY_PATH, sheet_name="Panel_Index"))
    lag_best = _coerce_numeric(corr["Lag_Best"])
    brand_io = _coerce_numeric(brand_ctx["Brand_IO_Metrics"])
    region = _coerce_numeric(brand_ctx["Prozorro_ByRegion"])
    forecast_summary = _coerce_numeric(forecast["Forecast_Summary"])
    synthetic_link = _coerce_numeric(forecast["Synthetic_to_Consumer_Link"])
    asymmetry = _coerce_numeric(discounts["Asymmetry_Observed_vs_Baseline"])

    retail = ss["retail"]
    panel_daily = ss["panel_daily"]
    match_audit = ss["match_audit"]
    literal_summary = ss["literal_summary"]
    brand_support = ss["brand_support"]
    level_selection = ss["level_selection"]
    lp_summary = ss["lp_summary"]
    lp_coeff = ss["lp_coeff"]
    spread = ss["spread"]
    discount = ss["discount"]
    robust = ss["robust"]

    butter = _load_product_book("butter", "silpo_novus")
    milk = _load_product_book("milk", "silpo")
    hard_cheese = _load_product_book("hard_cheese", "silpo_novus")
    sour_cream = _load_product_book("sour_cream", "silpo_novus")
    cream = _load_product_book("cream", "silpo")

    coverage_fp = _coverage_row(coverage, "FarmGateUA", "ProducerUA")
    coverage_pp = _coverage_row(coverage, "ProducerUA", "ProZorro")
    coverage_pr = _coverage_row(coverage, "ProZorro", "Retail")
    coverage_fr = _coverage_row(coverage, "FarmGateUA", "Retail")
    coverage_fz = _coverage_row(coverage, "FarmGateUA", "ProZorro")
    coverage_rz = _coverage_row(coverage, "Retail", "ProZorro")
    coverage_brand = _select_first(coverage, coverage["check_type"].astype(str) == "brand_panels")

    family_counts = coef["model_family"].astype(str).value_counts().to_dict()
    core_by_family = (
        coef.groupby("model_family", as_index=False)["core_finding_flag"]
        .sum()
        .set_index("model_family")["core_finding_flag"]
        .to_dict()
    )
    family_summary = (
        coef.assign(
            sr_coef_num=pd.to_numeric(coef["sr_coef"], errors="coerce"),
            lr_coef_num=pd.to_numeric(coef["lr_coef"], errors="coerce"),
            ect_coef_num=pd.to_numeric(coef["ect_coef"], errors="coerce"),
            n_obs_num=pd.to_numeric(coef["n_obs"], errors="coerce"),
            core_flag_num=pd.to_numeric(coef["core_finding_flag"], errors="coerce").fillna(0),
            ok_flag_num=(coef["model_status"].astype(str) == "ok").astype(int),
        )
        .groupby("model_family", as_index=False)
        .agg(
            rows=("model_family", "size"),
            core=("core_flag_num", "sum"),
            ok_share=("ok_flag_num", "mean"),
            median_n=("n_obs_num", "median"),
            sr_abs_med=("sr_coef_num", lambda s: pd.to_numeric(s, errors="coerce").abs().median()),
            lr_abs_med=("lr_coef_num", lambda s: pd.to_numeric(s, errors="coerce").abs().median()),
            ect_med=("ect_coef_num", "median"),
        )
        .set_index("model_family")
    )
    no_fit = coef[coef["model_family"].astype(str) == "NO_FIT"].copy()
    no_fit_i2 = int((no_fit["unreliable_reason"].astype(str) == "i2_series_blocked").sum())
    no_fit_overlap = int((no_fit["unreliable_reason"].astype(str) == "insufficient_overlap").sum())

    raw_stage_summary = (
        raw.groupby("stage_to", as_index=False)["core_finding_flag"]
        .agg(["count", "sum", "mean"])
        .reset_index()
        .sort_values("mean", ascending=False)
    )

    anchor_diag = retail_combined_diag[retail_combined_diag["panel_name"].astype(str) == "Retail_combined"].copy()
    core_diag = retail_combined_diag[retail_combined_diag["panel_name"].astype(str) == "Retail_combined_core"].copy()

    lp_screen = lp_coeff[(pd.to_numeric(lp_coeff["pvalue"], errors="coerce") < 0.10) & (pd.to_numeric(lp_coeff["n_obs"], errors="coerce") >= 30)]
    lp_h714 = lp_summary[lp_summary["horizon_days"].isin([7, 14])].copy()
    downstream_lp = lp_h714[
        lp_h714["link"].astype(str).str.startswith("ProZorro ->")
        & lp_h714["price_variant"].astype(str).str.contains("retail|silpo|novus", case=False, regex=True)
    ].copy()

    prozorro_silpo_best = _select_first(
        downstream_lp.sort_values(["core_share", "horizon_days"], ascending=[False, True]),
        downstream_lp["link"].astype(str).eq("ProZorro -> Silpo"),
    )
    prozorro_novus_best = _select_first(
        downstream_lp.sort_values(["core_share", "horizon_days"], ascending=[False, True]),
        downstream_lp["link"].astype(str).eq("ProZorro -> Novus"),
    )
    prozorro_matched_best = _select_first(
        downstream_lp.sort_values(["core_share", "horizon_days"], ascending=[False, True]),
        downstream_lp["link"].astype(str).eq("ProZorro -> Retail matched"),
    )
    prozorro_retail_best = _select_first(
        downstream_lp.sort_values(["core_share", "horizon_days"], ascending=[False, True]),
        downstream_lp["link"].astype(str).eq("ProZorro -> Retail"),
    )
    lp_best_overall = lp_summary.sort_values(
        ["core_share", "sig_share", "mean_abs_coef", "median_n_obs"],
        ascending=[False, False, False, False],
    ).iloc[0]

    fg_proc_pairwise = _select_first(
        farmgate_direct.sort_values(
            ["core_finding_share", "robust_across_reconstruction_share", "robust_linear_vs_pchip_share", "median_n_obs"],
            ascending=[False, False, False, False],
        ),
        (farmgate_direct["stage_from"].astype(str) == "FarmGateUA")
        & (farmgate_direct["stage_to"].astype(str) == "ProZorro")
        & (farmgate_direct["intersection_rule"].astype(str) == "pairwise_overlap")
        & (farmgate_direct["model_family"].astype(str) == "NARDL"),
    )
    fg_retail_anchor = _select_first(
        farmgate_direct.sort_values(
            ["core_finding_share", "median_n_obs"],
            ascending=[False, False],
        ),
        (farmgate_direct["stage_from"].astype(str) == "FarmGateUA")
        & (farmgate_direct["stage_to"].astype(str) == "Retail")
        & (farmgate_direct["retailer_panel"].astype(str) == "Retail_combined")
        & (farmgate_direct["intersection_rule"].astype(str) == "pairwise_overlap")
        & (farmgate_direct["model_family"].astype(str) == "NARDL")
        & (farmgate_direct["price_variant"].astype(str) == "baseline"),
    )
    fg_retail_core = _select_first(
        farmgate_direct.sort_values(
            ["core_finding_share", "median_n_obs"],
            ascending=[False, False],
        ),
        (farmgate_direct["stage_from"].astype(str) == "FarmGateUA")
        & (farmgate_direct["stage_to"].astype(str) == "Retail")
        & (farmgate_direct["retailer_panel"].astype(str) == "Retail_combined_core")
        & (farmgate_direct["intersection_rule"].astype(str) == "pairwise_overlap")
        & (farmgate_direct["model_family"].astype(str) == "NARDL")
        & (farmgate_direct["price_variant"].astype(str) == "observed"),
    )
    fg_reverse_anchor = _select_first(
        farmgate_reverse.sort_values(["core_finding_share", "median_n_obs"], ascending=[False, False]),
        (farmgate_reverse["stage_from"].astype(str) == "Retail")
        & (farmgate_reverse["stage_to"].astype(str) == "FarmGateUA")
        & (farmgate_reverse["retailer_panel"].astype(str) == "Retail_combined")
        & (farmgate_reverse["intersection_rule"].astype(str) == "pairwise_overlap")
        & (farmgate_reverse["model_family"].astype(str) == "NARDL")
        & (farmgate_reverse["price_variant"].astype(str) == "baseline"),
    )
    fg_reverse_core = _select_first(
        farmgate_reverse.sort_values(["core_finding_share", "median_n_obs"], ascending=[False, False]),
        (farmgate_reverse["stage_from"].astype(str) == "Retail")
        & (farmgate_reverse["stage_to"].astype(str) == "FarmGateUA")
        & (farmgate_reverse["retailer_panel"].astype(str) == "Retail_combined_core")
        & (farmgate_reverse["intersection_rule"].astype(str) == "pairwise_overlap")
        & (farmgate_reverse["model_family"].astype(str) == "NARDL")
        & (farmgate_reverse["price_variant"].astype(str) == "baseline"),
    )

    reverse_retail_to_producer = _select_first(
        reverse.sort_values(["core_finding_flag", "unreliable_flag", "ect_pvalue"], ascending=[False, True, True]),
        (reverse["stage_from"].astype(str) == "Retail")
        & (reverse["stage_to"].astype(str) == "ProducerUA")
        & (reverse["model_family"].astype(str) == "NARDL"),
    )

    butter_prod = _mc_row(butter, "producer_to_prozorro", "NARDL")
    cream_prod = _mc_row(cream, "producer_to_prozorro", "NARDL")
    hard_prod = _mc_row(hard_cheese, "producer_to_prozorro", "NARDL")
    butter_ardl = _mc_row(butter, "prozorro_to_retail", "ARDL")
    butter_ecm = _mc_row(butter, "prozorro_to_retail", "ECM")
    butter_nardl = _mc_row(butter, "prozorro_to_retail", "NARDL")
    milk_ecm = _mc_row(milk, "prozorro_to_retail", "ECM")
    milk_nardl = _mc_row(milk, "prozorro_to_retail", "NARDL")
    hard_ardl = _mc_row(hard_cheese, "prozorro_to_retail", "ARDL")
    hard_nardl = _mc_row(hard_cheese, "prozorro_to_retail", "NARDL")
    sour_nardl = _mc_row(sour_cream, "prozorro_to_retail", "NARDL")

    butter_lag = butter["LagProfile"]
    milk_lag = milk["LagProfile"]
    hard_lag = hard_cheese["LagProfile"]
    butter_lag_prod = butter_lag[butter_lag["pair"].astype(str) == "producer_to_prozorro"].sort_values("corr", ascending=False).iloc[0]
    butter_lag_retail = butter_lag[butter_lag["pair"].astype(str) == "prozorro_to_retail"].sort_values("corr", ascending=False).iloc[0]
    milk_lag_retail = milk_lag[milk_lag["pair"].astype(str) == "prozorro_to_retail"].sort_values("corr", ascending=False).iloc[0]
    hard_lag_prod = hard_lag[hard_lag["pair"].astype(str) == "producer_to_prozorro"].sort_values("corr", ascending=False).iloc[0]
    hard_lag_retail = hard_lag[hard_lag["pair"].astype(str) == "prozorro_to_retail"].sort_values("corr", ascending=False).iloc[0]

    delta_sr_mean = pd.to_numeric(asymmetry["delta_sr_coef"], errors="coerce").abs().mean()
    delta_lr_mean = pd.to_numeric(asymmetry["delta_lr_coef"], errors="coerce").abs().mean()
    delta_ect_mean = pd.to_numeric(asymmetry["delta_ect_coef"], errors="coerce").abs().mean()
    pseudo_share = pd.to_numeric(asymmetry["pseudo_asymmetry_likely"], errors="coerce").fillna(0).mean()
    ols_shock_summary = family_summary.loc["OLS_HAC_SHOCK"]
    ols_retail_summary = family_summary.loc["OLS_HAC_RETAIL_CTRL"]
    ardl_summary = family_summary.loc["ARDL"]
    ecm_summary = family_summary.loc["ECM"]
    nardl_summary = family_summary.loc["NARDL"]
    vecm_summary = family_summary.loc["VECM"]

    spread_persistent = int(pd.to_numeric(spread["persistent_margin_flag"], errors="coerce").fillna(0).sum())
    spread_asymmetric = int(pd.to_numeric(spread["asymmetric_margin_flag"], errors="coerce").fillna(0).sum())
    spread_best = spread.sort_values(
        ["persistent_margin_flag", "asymmetric_margin_flag", "r2", "n_obs"],
        ascending=[False, False, False, False],
    ).iloc[0]
    discount_signals = int(pd.to_numeric(discount["discount_strategy_signal"], errors="coerce").fillna(0).sum())
    discount_best = discount.sort_values(["discount_strategy_signal", "r2", "n_obs"], ascending=[False, False, False]).iloc[0]

    producer_rmse = forecast_summary.loc[forecast_summary["target"].astype(str) == "ProducerUA", "rmse_dlog"]
    consumer_rmse = forecast_summary.loc[forecast_summary["target"].astype(str) == "ConsumerUA", "rmse_dlog"]
    forecast_r2 = pd.to_numeric(forecast_summary["r2_train"], errors="coerce")
    synth_best = synthetic_link.sort_values("p_synth_to_consumer", ascending=True).iloc[0]

    benchmark["abs_corr"] = pd.to_numeric(benchmark["corr_at_best_lag"], errors="coerce").abs()
    benchmark_best = (
        benchmark.groupby(["benchmark_source", "stage"], as_index=False)["abs_corr"]
        .mean()
        .sort_values("abs_corr", ascending=False)
        .head(3)
    )
    lag_best_sorted = lag_best.sort_values("corr", ascending=False)
    lag_top_1 = lag_best_sorted.iloc[0]
    lag_top_2 = lag_best_sorted.iloc[1]
    lag_top_3 = lag_best_sorted.iloc[2]

    top_hhi = brand_io.sort_values("hhi_brand", ascending=False).head(3)
    top_region = region.sort_values("cv", ascending=False).head(3)

    match_counts = Counter(match_audit["match_status"].astype(str))
    selected_count = level_selection["candidate_label"].value_counts().to_dict()

    product_compare_rows: list[dict[str, object]] = []
    for prod, g in panel_daily.groupby("product"):
        mask = g[["silpo_observed", "novus_observed", "retail_observed"]].notna().any(axis=1)
        gg = g.loc[mask].copy().sort_values("date")
        if gg.empty:
            continue
        row: dict[str, object] = {
            "product": prod,
            "product_label": gg["product_label"].dropna().iloc[0] if gg["product_label"].notna().any() else prod,
            "date_min": gg["date"].min(),
            "date_max": gg["date"].max(),
            "n_days": len(gg),
            "silpo_keys": pd.to_numeric(gg.get("silpo_n_item_keys"), errors="coerce").median(),
            "novus_keys": pd.to_numeric(gg.get("novus_n_item_keys"), errors="coerce").median(),
            "retail_keys": pd.to_numeric(gg.get("retail_n_item_keys"), errors="coerce").median(),
            "silpo_brands": pd.to_numeric(gg.get("silpo_n_brands"), errors="coerce").median(),
            "novus_brands": pd.to_numeric(gg.get("novus_n_brands"), errors="coerce").median(),
            "retail_brands": pd.to_numeric(gg.get("retail_n_brands"), errors="coerce").median(),
            "silpo_discount": pd.to_numeric(gg.get("silpo_discount_share"), errors="coerce").mean(),
            "novus_discount": pd.to_numeric(gg.get("novus_discount_share"), errors="coerce").mean(),
        }
        row["silpo_novus_gap_mean"] = pd.to_numeric((gg.get("silpo_observed") - gg.get("novus_observed")).abs(), errors="coerce").mean()
        row["silpo_novus_gap_max"] = pd.to_numeric((gg.get("silpo_observed") - gg.get("novus_observed")).abs(), errors="coerce").max()
        for col in [
            "silpo_observed",
            "novus_observed",
            "retail_observed",
            "producer_linear_model",
            "prozorro_model",
            "consumer_linear_model",
        ]:
            s = gg[["date", col]].dropna()
            if s.empty:
                row[f"{col}_first"] = None
                row[f"{col}_last"] = None
                row[f"{col}_pct"] = None
            else:
                first = float(s.iloc[0][col])
                last = float(s.iloc[-1][col])
                row[f"{col}_first"] = first
                row[f"{col}_last"] = last
                row[f"{col}_pct"] = (last / first - 1.0) * 100 if first != 0 else None
        product_compare_rows.append(row)
    product_compare = pd.DataFrame(product_compare_rows)
    product_compare_lookup = product_compare.set_index("product")

    def change_text(value: object) -> str:
        num = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
        if pd.isna(num):
            return "n/a"
        sign = "+" if num > 0 else ""
        return f"{sign}{_fmt_number(num, digits=1)}%"

    milk_compare = product_compare_lookup.loc["milk"]
    butter_compare = product_compare_lookup.loc["butter"]
    hard_compare = product_compare_lookup.loc["hard_cheese"]
    sour_compare = product_compare_lookup.loc["sour_cream"]
    condensed_compare = product_compare_lookup.loc["condensed_milk"]
    cottage_compare = product_compare_lookup.loc["cottage_cheese"]
    cream_compare = product_compare_lookup.loc["cream"]
    yogurt_compare = product_compare_lookup.loc["yogurt_dessert"]
    powder_compare = product_compare_lookup.loc["milk_powder"]

    synthesis_table_headers = [
        "Model or screen",
        "Estimated output",
        "Main numeric result",
        "Timing or correlation signal",
        "Upstream reading",
        "Downstream and chain reading",
    ]
    synthesis_table_rows = [
        [
            "Lagged correlation scan",
            f"{_fmt_int(len(lag_best))} pair-product lag scans",
            f"Top corr {_fmt_number(lag_top_1['corr'])} for {lag_top_1['pair_left']} -> {lag_top_1['pair_right']} ({lag_top_1['product']}); next {_fmt_number(lag_top_2['corr'])}.",
            f"Producer-to-procurement peaks at {_fmt_int(butter_lag_prod['lag'])}-{_fmt_int(hard_lag_prod['lag'])} days; procurement-to-retail at {_fmt_int(hard_lag_retail['lag'])}-{_fmt_int(milk_lag_retail['lag'])} days.",
            "Supports delayed repricing rather than same-day pass-through.",
            "Motivates product-specific distributed-lag and retail-endpoint specifications.",
        ],
        [
            "ARDL",
            f"{_fmt_int(ardl_summary['rows'])} equations; median n {_fmt_int(ardl_summary['median_n'])}; ok share {_fmt_percent(ardl_summary['ok_share'])}.",
            f"Butter retail SR {_fmt_number(butter_ardl['sr_coef'])}, LR {_fmt_number(butter_ardl['lr_coef'])}; hard cheese retail SR {_fmt_number(hard_ardl['sr_coef'])}, LR {_fmt_number(hard_ardl['lr_coef'])}.",
            "Benchmark distributed-lag structure when a long-run relation remains plausible.",
            "Shows gradual producer-to-procurement incorporation without forcing asymmetry.",
            "Useful sign and magnitude benchmark, but long-run retail coefficients are not read literally.",
        ],
        [
            "ECM",
            f"{_fmt_int(ecm_summary['rows'])} equations; {_fmt_int(ecm_summary['core'])} core findings; median n {_fmt_int(ecm_summary['median_n'])}.",
            f"ECTs: butter retail {_fmt_number(butter_ecm['ect_coef'])}, milk retail {_fmt_number(milk_ecm['ect_coef'])}, cream upstream {_fmt_number(cream_prod['ect_coef'])}.",
            "Negative ECTs show how fast disequilibrium is removed after shocks.",
            "Strongest evidence that procurement re-anchors toward producer conditions.",
            "Milk is the fastest downstream correction case; butter also corrects under managed shelf pricing.",
        ],
        [
            "NARDL",
            f"{_fmt_int(nardl_summary['rows'])} equations; {_fmt_int(nardl_summary['core'])} core findings; median n {_fmt_int(nardl_summary['median_n'])}.",
            f"ECTs: butter {_fmt_number(butter_nardl['ect_coef'])}, milk {_fmt_number(milk_nardl['ect_coef'])}, sour cream {_fmt_number(sour_nardl['ect_coef'])}; hard-cheese LR {_fmt_number(hard_nardl['lr_coef'])}.",
            "Separates positive and negative shock processing and retains the core asymmetry evidence.",
            "Butter, cream, and hard cheese show clear procurement correction under nonlinear adjustment.",
            "Hard cheese remains the clearest asymmetric downstream category; retailer management matters most here.",
        ],
        [
            "VECM",
            f"{_fmt_int(vecm_summary['rows'])} system equations; {_fmt_int(vecm_summary['core'])} retained core findings; median n {_fmt_int(vecm_summary['median_n'])}.",
            f"Median system adjustment term {_fmt_number(vecm_summary['ect_med'])}.",
            "Multivariate consistency check only; short overlapping samples limit retained evidence.",
            "Confirms that system-wide modelling is possible, but not the main identification base in this sample.",
            "Used as robustness rather than as the headline estimator for retail transmission.",
        ],
        [
            "OLS-HAC shock",
            f"{_fmt_int(ols_shock_summary['rows'])} reduced-form equations; median n {_fmt_int(ols_shock_summary['median_n'])}.",
            f"Median absolute short-run coefficient {_fmt_number(ols_shock_summary['sr_abs_med'])}.",
            "Shock-dummy stress test without long-run equilibrium structure.",
            "Captures event sensitivity around the chain without imposing cointegration.",
            "Helpful for robustness, but not read as structural pass-through.",
        ],
        [
            "OLS-HAC retail controls",
            f"{_fmt_int(ols_retail_summary['rows'])} reduced-form promo-control equations; median n {_fmt_int(ols_retail_summary['median_n'])}.",
            f"Median absolute short-run coefficient {_fmt_number(ols_retail_summary['sr_abs_med'])}; observed-vs-baseline delta SR {_fmt_number(delta_sr_mean)}; pseudo-asymmetry {_fmt_percent(pseudo_share)}.",
            "Tests whether promotions and baseline construction reshape measured pass-through.",
            "Not an upstream anchor; it is a downstream measurement check.",
            "Shows that discount-aware retail preparation changes the observed coefficient surface materially.",
        ],
        [
            "Local projections",
            f"{_fmt_int(len(lp_coeff) / 2)} horizon equations; {_fmt_int(len(lp_screen))} screened responses.",
            f"Best downstream screen: {prozorro_silpo_best['link']} with core share {_fmt_percent(prozorro_silpo_best['core_share'])} at horizon {_fmt_int(prozorro_silpo_best['horizon_days'])}; overall best {lp_best_overall['link']} at horizon {_fmt_int(lp_best_overall['horizon_days'])}.",
            "Non-parametric horizon responses preserve timing without imposing one lag polynomial.",
            "Shows where producer and farm-gate shocks appear earliest in the chain.",
            "Confirms that Silpo often carries the cleanest short-horizon procurement-to-retail response.",
        ],
        [
            "Vertical spread models",
            f"{_fmt_int(len(spread))} usable equations; {_fmt_int(spread_persistent)} persistent-margin flags; {_fmt_int(spread_asymmetric)} asymmetric-margin flags.",
            f"Best spread case {spread_best['product_label']} ({spread_best['spread']}) with R2 {_fmt_number(spread_best['r2'])} and discount-share coef {_fmt_number(spread_best['discount_share_coef'])}.",
            "Spread persistence and asymmetry proxy selective margin adjustment across stages.",
            "Shows where procurement and farm-gate gaps remain persistent after upstream shocks.",
            "Supports a category-management reading of downstream market power rather than one static markup wedge.",
        ],
        [
            "Discount models",
            f"{_fmt_int(len(discount))} direct discount equations; {_fmt_int(discount_signals)} strategy signals.",
            f"Butter lag discount {_fmt_number(discount.loc[discount['product'].astype(str)=='butter', 'lag_discount_coef'].iloc[0])}; milk lag discount {_fmt_number(discount.loc[discount['product'].astype(str)=='milk', 'lag_discount_coef'].iloc[0])}; best R2 {_fmt_number(discount_best['r2'])}.",
            "Discount state is more persistent than spread state in staple categories.",
            "Producer and procurement shocks enter discount behavior selectively, not uniformly.",
            "Discounts act as tactical smoothing instruments, especially in milk and butter.",
        ],
    ]

    blocks: list[Block] = []
    current_chapter: int | None = None
    figure_counters: dict[int, int] = {5: 0, 6: 0}
    table_counters: dict[int, int] = {5: 0, 6: 0}

    def para(text: str, style: str | None = None, page_break_before: bool = False) -> None:
        nonlocal current_chapter
        chapter_match = re.match(r"Chapter\s+([56])\.", str(text).strip())
        if style == "Heading1" and chapter_match:
            current_chapter = int(chapter_match.group(1))
        blocks.append(ParagraphBlock(text=text, style=style, page_break_before=page_break_before))

    def fig(path: str | Path, caption: str, source: str, caption_style: str = "Subtitle", width_in: float = 5.9) -> None:
        numbered_caption = caption
        if current_chapter in figure_counters and not re.match(r"^\s*Figure\s+\d+\.\d+", caption):
            figure_counters[current_chapter] += 1
            numbered_caption = f"Figure {current_chapter}.{figure_counters[current_chapter]}. {caption}"
        blocks.append(FigureBlock(path=Path(path), caption=numbered_caption, source=source, caption_style=caption_style, width_in=width_in))

    def table(headers: list[str], rows: list[list[str]], caption: str, source: str, caption_style: str = "NoSpacing") -> None:
        numbered_caption = caption
        if current_chapter in table_counters and not re.match(r"^\s*Table\s+\d+\.\d+", caption):
            table_counters[current_chapter] += 1
            numbered_caption = f"Table {current_chapter}.{table_counters[current_chapter]}. {caption}"
        blocks.append(TableBlock(caption=numbered_caption, headers=headers, rows=rows, source=source, caption_style=caption_style))

    para("Chapter 5. Data", "Heading1")
    para(
        "This chapter presents the integrated empirical architecture of the thesis and explains how the different raw sources are transformed into one economically coherent research design. "
        "The four-stage chain remains the same throughout the study, but the downstream block is now prepared more deeply at item level, so the empirical narrative no longer depends only on broad category pooling. "
        "The purpose of the revision is not to replace the original analytical logic, but to tighten it where the identification problem is hardest: retailer product naming, brand reconciliation, discount-aware pricing, and the choice of the most credible stage-4 retail endpoint."
    )
    para(
        "The chapter therefore combines two tasks. First, it documents the institutional meaning of each price layer: raw-milk farm-gate conditions, processed-dairy producer prices, public procurement prices, and retailer-facing shelf prices do not represent the same market mechanism and should not be interpreted as if they did. "
        "Second, it shows how the deeper retail reconstruction improves comparability without breaking the broader vertical-transmission story developed in the thesis."
    )

    para("5.1 Data sources and datasets", "Heading2")
    para(
        "All sources are expressed in a common hryvnia-based analytical environment and then transformed into modelling panels that correspond to distinct stages of price formation rather than to arbitrary storage tables. "
        "The research design keeps the chain visible: FarmGateUA provides the raw-milk benchmark, ProducerUA captures processor-level domestic prices for processed dairy categories, ProZorro captures procurement prices under tender and contract rules, and the retail block represents the consumer-facing shelf environment reconstructed from Silpo and Novus. "
        "External EU and CME benchmarks, together with ConsumerUA, remain important supporting layers because they help distinguish domestic chain behaviour from broader dairy-cycle movement."
    )

    para("5.1.1 FarmGateUA (raw-milk farm-gate benchmark and reconstructed daily layer).", "Heading3")
    para(
        "The farm-gate layer retains its special role in the thesis. It is the only stage that starts from an official raw-milk benchmark rather than from processed-dairy or retail observations. "
        "Because the original benchmark is low-frequency, the study keeps both the initial and the gap-filled daily reconstructions, each in linear and shape-preserving form, so later inference can be checked against reconstruction sensitivity instead of hiding the issue inside one synthetic series."
    )
    fig(
        OUTPUTS_ROOT / "sheet_farmgateua_filled" / "sheet_farmgateua_filled_region_trends.png",
        "Farm-gate raw-milk benchmark and reconstructed regional trends",
        "Source: author's calculations based on the integrated FarmGateUA reconstruction.",
        caption_style="Quote",
    )
    para(
        f"The technical quality of this layer is high even though its economic interpretation must remain cautious. The required-link audit keeps {_b_int(coverage_fp['rows_total'])} FarmGateUA -> ProducerUA rows, {_b_int(coverage_fz['rows_total'])} FarmGateUA -> ProZorro rows, and {_b_int(coverage_fr['rows_total'])} FarmGateUA -> Retail rows. "
        f"At the same time, only {_b_int(coverage_fp['core_finding_rows'])} of the FarmGateUA -> ProducerUA rows survive into the core-finding set, which is just {_b_pct(coverage_fp['core_finding_rows'] / coverage_fp['rows_total'])}. "
        "This confirms the central identification point: the farm-gate benchmark is useful as an upstream anchor and robustness dimension, but it is too aggregated to behave like a literal product-by-product pass-through series."
    )

    para("5.1.2 ProducerUA (processor-level domestic producer prices).", "Heading3")
    para(
        "ProducerUA remains the cleanest domestic anchor for the processed part of the chain. The series represent processor-level domestic prices for standardized dairy categories and therefore stand between raw milk and procurement rather than duplicating the farm-gate benchmark. "
        "This layer is also the most naturally suited to error-correction reasoning because it is product-specific, persistent, and less distorted by retailer assortment management than the downstream stage."
    )
    fig(
        OUTPUTS_ROOT / "sheet_producerua" / "sheet_producerua_timeseries_by_standardized_type.png",
        "Ukrainian producer prices by products",
        "Source: author's calculations based on the ProducerUA layer.",
        caption_style="Quote",
    )
    para(
        f"In the benchmark-comparison table, the strongest average coherence appears in the producer layer, with the best benchmark pairings reaching mean absolute best-lag correlations of {_b_num(benchmark_best.iloc[0]['abs_corr'])}, {_b_num(benchmark_best.iloc[1]['abs_corr'])}, and {_b_num(benchmark_best.iloc[2]['abs_corr'])}. "
        "Economically, this matters because the producer block is the first stage at which raw-milk conditions have already been translated into differentiated dairy products but have not yet been fully filtered by procurement rules or retail category management."
    )

    para("5.1.3 ProZorro.", "Heading3")
    para(
        "The procurement layer is institutionally different from both the producer and retail stages. Contract prices in ProZorro move through tender timing, specification mix, fat content, packaging, and delivery terms rather than through continuous spot repricing. "
        "That is exactly why procurement must be modeled as its own layer: it is the first place where upstream cost pressure is translated into standardized transaction prices, yet it remains slower and more rule-bound than the retail shelf."
    )
    fig(
        OUTPUTS_ROOT / "sheet_prozorro" / "sheet_prozorro_timeseries_by_standardized_type.png",
        "Ukrainian procurement prices by products",
        "Source: author's calculations based on the ProZorro layer.",
        caption_style="Quote",
    )
    para(
        f"The required-link validation retains {_b_int(coverage_pp['rows_total'])} ProducerUA -> ProZorro rows and {_b_int(coverage_pp['core_finding_rows'])} core findings. "
        "That concentration of admissible and interpretable evidence is one of the main reasons why procurement is treated later as the key institutional transmission buffer rather than as a passive middle observation."
    )

    para("5.1.4 Retail (Silpo and Novus).", "Heading3")
    para(
        "The most substantial data improvement in the integrated design concerns the retail block. Instead of relying only on broad category pooling, the downstream layer is rebuilt from item-level Silpo and Novus observations with cleaned product titles, cleaned brands, canonical item names, literal dairy-product typing, and explicit discount-aware prices. "
        "The effective shelf price already includes the markdown faced by the buyer, but the discount amount, discount type, discount dummy, and markdown depth are retained as separate variables. This allows the thesis to study both the transacted price and the promotional mechanism behind it."
    )
    para(
        f"After dairy-only reconciliation, the retail input contains {_b_int(len(retail))} product-day observations, {_b_int(retail['brand_norm'].nunique())} normalized brand identifiers, and {_b_int(retail['product_literal'].nunique())} literal dairy-product types. "
        f"The literal mix is selective rather than generic: {_b(_top_literal_examples(literal_summary))}. "
        "This matters because the chain is more economically coherent when hard cheese, butter, milk, sour cream, condensed milk, and yogurt are not collapsed into one undifferentiated downstream average."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "07_retail_literal_mix.png",
        "Retail literal-product mix after dairy-only reconciliation",
        "Source: author's calculations based on the harmonized Silpo-Novus item catalog.",
        caption_style="Quote",
    )
    para(
        f"The harmonized item-key audit identifies {_b_int(match_counts['matched_both_shops'])} cross-shop matches, {_b_int(match_counts['silpo_only'])} Silpo-only keys, and {_b_int(match_counts['novus_only'])} Novus-only keys. "
        f"Within the matched group, {_b_int(((match_audit['match_status'].astype(str) == 'matched_both_shops') & (match_audit['strict_alignment_flag'] == 1)).sum())} items also align on the stricter pack-and-fat diagnostic key. "
        "This shows that the naming problem is not cosmetic. A large part of the downstream identification problem comes from real assortment asymmetry across retailers, not only from spelling or formatting noise."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "06_cross_shop_match_status.png",
        "Cross-shop retail item harmonisation status",
        "Source: author's calculations based on the cross-shop item-key audit.",
        caption_style="Quote",
    )
    para(
        f"The brand-support table reinforces that interpretation: {_b(_top_brand_examples(brand_support))}. "
        "The downstream stage is therefore not a flat retail average. It is a layered environment where category design, brand structure, and promotion routines coexist with price transmission."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "08_dominant_brand_support.png",
        "Dominant retailer-brand support by dairy product",
        "Source: author's calculations based on retailer-brand support in the harmonized retail panel.",
        caption_style="Quote",
    )

    para("5.1.5 External benchmarks (EU and CME).", "Heading3")
    para(
        "EU dairy price monitoring and CME Class III milk futures remain supporting benchmark layers rather than structural stages of the domestic chain. Their role is to help distinguish chain-specific movements from broader regional or global dairy cycles and to support the high-frequency reconstruction of the farm-gate benchmark."
    )
    fig(
        OUTPUTS_ROOT / "sheet_cme" / "sheet_cme_distribution.png",
        "U.S. CME Class III milk prices distribution",
        "Source: author's calculations based on the CME benchmark layer.",
        caption_style="Quote",
    )
    fig(
        OUTPUTS_ROOT / "sheet_eu" / "sheet_eu_timeseries_by_standardized_type.png",
        "EU dairy products prices by products",
        "Source: author's calculations based on the EU benchmark layer.",
        caption_style="Quote",
    )
    para(
        "These series are not interpreted as domestic transmission stages, but they remain valuable for judging whether a given Ukrainian episode is likely to reflect wider dairy-cycle movement or a more local institutional pricing response."
    )

    para("5.1.6 ConsumerUA (domestic consumer layer).", "Heading3")
    para(
        "ConsumerUA remains a supporting downstream environment rather than a replacement for retailer data. It is useful where retailer coverage is thin, where a consumer-facing anchor helps extend the downstream horizon, and where the plausibility of the broader market timing needs to be checked against official consumer-price movement."
    )
    fig(
        OUTPUTS_ROOT / "sheet_consumerua" / "sheet_consumerua_timeseries_by_standardized_type.png",
        "Ukrainian consumer prices by products",
        "Source: author's calculations based on the ConsumerUA layer.",
        caption_style="Quote",
    )
    para(
        f"In the integrated retail diagnostics, consumer support is non-zero only for {_b_int(pd.to_numeric(anchor_diag['coverage_consumer'], errors='coerce').fillna(0).gt(0).sum())} product groups, and the median consumer weight in the anchored downstream panel remains {_b_num(pd.to_numeric(anchor_diag['weight_consumer'], errors='coerce').median())}. "
        "This means the consumer layer helps continuity and plausibility, but it does not erase retailer information."
    )

    para("5.2 Data construction and transformation", "Heading2")
    para(
        "The data-construction pipeline is deliberately conservative. It passes each source through product harmonization, unit harmonization, and frequency alignment before the prices are allowed to enter the econometric analysis. "
        "The objective is not to maximize raw sample length at any cost, but to retain windows in which the compared prices are economically similar enough for dynamic interpretation."
    )
    para(
        f"The product-mapping audit covers {_b_int(len(mapping))} mapped label groups. Exact matches account for {_b_pct((mapping['mapping_quality_flag'].astype(str) == 'matched').mean())}, multi-match cases account for {_b_pct((mapping['mapping_quality_flag'].astype(str) == 'multi_match').mean())}, and unmatched rows account for {_b_pct((mapping['mapping_quality_flag'].astype(str) == 'unmatched').mean())}. "
        f"At the same time, the economically comparable share remains {_b_pct(pd.to_numeric(mapping['economically_comparable_flag'], errors='coerce').fillna(0).mean())}. "
        "The implication is that the major problem is not general labeling chaos, but the smaller set of economically awkward cases in which pack size, product definition, or institutional wording does not line up cleanly across stages."
    )
    para(
        "Retail preparation now adds a fourth gate that did not exist at the same depth before: item-level cross-shop reconciliation. The harmonized item key combines the thesis product group, cleaned brand, and canonicalized product name stripped of redundant fat and pack tokens. "
        "This greatly improves the downstream stage because Novus and Silpo often carry the same economic item under different wording, while other items are truly unique to only one chain and should not be forced into a false common sample."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "01_panel_coverage.png",
        "Integrated panel coverage by product and source",
        "Source: author's calculations based on the combined daily panel.",
        caption_style="Quote",
    )
    para(
        "Frequency alignment follows the same economic logic as in the methodology chapter. Retail observations are daily, procurement observations remain irregular but are converted into comparable daily sequences within overlap windows, and the farm-gate benchmark is reconstructed to higher frequency in multiple admissible variants. "
        "Those variants are not treated as hidden technical steps; they are retained explicitly so later inference can be judged against interpolation and reconstruction robustness."
    )
    para(
        "The revised downstream block also no longer assumes that one retail series is universally optimal for every product. Instead, the study tests several candidate stage-4 endpoints: the merged full-list retail panel, the stricter matched cross-shop panel, Silpo-only and Novus-only panels, and a retail-plus-ConsumerUA variant. "
        "These candidates are compared product by product using a composite score that reflects coverage, procurement alignment, consumer alignment, item support, and discount variation."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "09_retail_level_scores.png",
        "Candidate downstream retail scores by product",
        "Source: author's calculations based on the retail-level comparison table.",
        caption_style="Quote",
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "10_optimal_retail_level.png",
        "Chosen downstream retail level by product",
        "Source: author's calculations based on the selected downstream hierarchy.",
        caption_style="Quote",
    )
    para(
        f"The selected hierarchy chooses the merged full retail list for {_b_int(selected_count.get('Retail merged full list', 0))} of the {_b_int(len(level_selection))} thesis product groups, the Retail plus ConsumerUA endpoint for {_b_int(selected_count.get('Retail plus ConsumerUA', 0))} group, and the matched cross-shop panel for {_b_int(selected_count.get('Retail matched cross-shop', 0))} group. "
        "Hard cheese is the clearest case where the downstream extension benefits from the consumer-linked endpoint, while milk powder is the clearest case where the stricter matched panel is preferable to a broad pooled average."
    )

    para("5.3 Diagnostic tests and interpretation", "Heading2")
    para(
        "Before estimation, every candidate link is screened through stationarity and admissibility diagnostics. The pretest block combines ADF and KPSS evidence, overlap rules, residual diagnostics, and explicit no-fit classification. "
        "This matters substantively: the models are not treated as automatic coefficient generators, but as conditional tools whose interpretation depends on whether the underlying data support a long-run relation, a correction mechanism, or only a reduced-form short-run response."
    )
    para(
        f"The integrated pretests confirm that the environment is heterogeneous rather than uniformly I(1). The dependent series is classified as I(0) in {_b_int((pretests['integration_y'].astype(str) == 'I(0)').sum())} cases, I(1) in {_b_int((pretests['integration_y'].astype(str) == 'I(1)').sum())}, I(2) in {_b_int((pretests['integration_y'].astype(str) == 'I(2)').sum())}, and ambiguous in {_b_int((pretests['integration_y'].astype(str) == 'ambiguous').sum())}. "
        f"Cointegration support appears in {_b_pct((pd.to_numeric(pretests['cointegration_p'], errors='coerce') < 0.10).mean())}. "
        "This is substantial enough to motivate error-correction models, but not enough to justify forcing every link into the same dynamic form."
    )
    para(
        f"The consolidated coefficient table contains {_b_int(len(coef))} rows. Of these, {_b_pct((coef['model_status'].astype(str) == 'ok').mean())} finish with status 'ok', {_b_pct(pd.to_numeric(coef['unreliable_flag'], errors='coerce').fillna(0).mean())} remain unreliable, and only {_b_pct(pd.to_numeric(coef['core_finding_flag'], errors='coerce').fillna(0).mean())} survive into the core-finding layer. "
        f"There are {_b_int(len(no_fit))} explicit no-fit rows, dominated by {_b_int(no_fit_i2)} I(2)-blocked cases and {_b_int(no_fit_overlap)} insufficient-overlap cases. "
        "This is analytically important because it shows that the code excludes weak or non-comparable estimates instead of hiding them."
    )
    fig(
        OUTPUTS_ROOT / "graphs_overlay_ln" / "before_after_ln_01.png",
        "Before/after log transformation (illustrative)",
        "Source: author's calculations based on the log-transformation diagnostics.",
        caption_style="Quote",
    )
    fig(
        OUTPUTS_ROOT / "graphs_correlations_lags" / "lag_best_bar.png",
        "Best-lag correlation scan across stages",
        "Source: author's calculations based on the lag-profile diagnostics.",
        caption_style="Quote",
    )
    para(
        f"The lag structure also remains central for interpretation. The strongest best-lag examples in the descriptive scan include {lag_top_1['pair_left']} -> {lag_top_1['pair_right']} for {lag_top_1['product']} at lag {_b_int(lag_top_1['lag_days'])} with correlation {_b_num(lag_top_1['corr'])}, {lag_top_2['pair_left']} -> {lag_top_2['pair_right']} for {lag_top_2['product']} at lag {_b_int(lag_top_2['lag_days'])} with correlation {_b_num(lag_top_2['corr'])}, and {lag_top_3['pair_left']} -> {lag_top_3['pair_right']} for {lag_top_3['product']} at lag {_b_int(lag_top_3['lag_days'])} with correlation {_b_num(lag_top_3['corr'])}. "
        "This pattern confirms that delayed adjustment, rather than same-day co-movement, is the economically relevant object in the dairy chain."
    )

    para("5.4 Market-structure and regional heterogeneity diagnostics", "Heading2")
    para(
        "The empirical design does not rely on time-series structure alone. It also incorporates market-structure diagnostics because bargaining power, assortment design, and regional contract conditions shape how price shocks are filtered across the chain. "
        "This is especially important downstream, where promotions and category management can alter the observed timing of transmission even when the long-run relation is preserved."
    )
    fig(
        OUTPUTS_ROOT / "graphs_brand_region" / "brand_hhi.png",
        "Retail brand concentration over time",
        "Source: author's calculations based on the retail brand-structure diagnostics.",
        caption_style="Quote",
    )
    para(
        f"The concentration block shows that retailer power is not evenly distributed across products. The highest HHI episodes in the current sample appear in {top_hhi.iloc[0]['source']} {top_hhi.iloc[0]['standardized_type']} at {_b_num(top_hhi.iloc[0]['hhi_brand'])}, {top_hhi.iloc[1]['source']} {top_hhi.iloc[1]['standardized_type']} at {_b_num(top_hhi.iloc[1]['hhi_brand'])}, and {top_hhi.iloc[2]['source']} {top_hhi.iloc[2]['standardized_type']} at {_b_num(top_hhi.iloc[2]['hhi_brand'])}. "
        "These values must still be read together with SKU support, but they confirm that concentration is a real feature of parts of the retail environment rather than an abstract theoretical concern."
    )
    fig(
        OUTPUTS_ROOT / "graphs_brand_region" / "prozorro_region_median.png",
        "Regional procurement-price dispersion by product type",
        "Source: author's calculations based on the ProZorro regional diagnostics.",
        caption_style="Quote",
    )
    para(
        f"Regional procurement dispersion is equally important. The highest coefficients of variation appear in {top_region.iloc[0]['region']} {top_region.iloc[0]['standardized_type']} at {_b_num(top_region.iloc[0]['cv'])}, {top_region.iloc[1]['region']} {top_region.iloc[1]['standardized_type']} at {_b_num(top_region.iloc[1]['cv'])}, and {top_region.iloc[2]['region']} {top_region.iloc[2]['standardized_type']} at {_b_num(top_region.iloc[2]['cv'])}. "
        "That dispersion helps explain why procurement is best interpreted as an institutional transmission buffer rather than as one homogeneous national middle layer."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "12_discount_environment.png",
        "Retail discount environment by product and retailer",
        "Source: author's calculations based on the harmonized Silpo-Novus retail panel.",
        caption_style="Quote",
    )
    para(
        "The integrated discount environment shows the same point from a different angle. Promotions are not random statistical noise attached to a true price that lies somewhere behind the shelf. They are part of how the shelf path itself is managed, especially in high-frequency retailer data."
    )

    para("5.5 Product-level retail price movements in the consumer basket", "Heading2")
    para(
        "The product-level retail evidence deserves separate discussion before the estimation chapter because it is the point at which the thesis comes closest to the way households actually experience dairy inflation. "
        "As the introduction stresses, dairy products are purchased frequently, are immediately visible in the day-to-day consumer basket, and become salient not because one category alone dominates household spending, but because several staple categories move in front of consumers repeatedly. "
        "That intuition is exactly why the item-level Silpo-Novus reconstruction matters: it allows the chapter to compare visible shelf movements product by product against the corresponding producer, procurement, and consumer layers rather than treating retail as one abstract average."
    )
    para(
        f"The retail window covers mostly the period from {_b(str(pd.Timestamp(product_compare['date_min'].min()).date()))} to {_b(str(pd.Timestamp(product_compare['date_max'].max()).date()))}. "
        f"Within that interval, the densest daily category support appears in yogurt/dessert with median {_b_int(yogurt_compare['retail_keys'])} retail item keys and {_b_int(yogurt_compare['retail_brands'])} brands, milk/fermented milk with {_b_int(milk_compare['retail_keys'])} item keys and {_b_int(milk_compare['retail_brands'])} brands, butter with {_b_int(butter_compare['retail_keys'])} item keys and {_b_int(butter_compare['retail_brands'])} brands, sour cream with {_b_int(sour_compare['retail_keys'])} item keys and {_b_int(sour_compare['retail_brands'])} brands, and hard cheese with {_b_int(hard_compare['retail_keys'])} item keys and {_b_int(hard_compare['retail_brands'])} brands. "
        "This ranking matches the economic logic of the consumer basket quite closely: the everyday categories that households notice most are also the categories for which the downstream panel is most densely observed."
    )
    fig(
        OUTPUTS_ROOT / "sheet_novus" / "sheet_novus_timeseries_by_standardized_type.png",
        "Novus retail-level prices by product",
        "Source: author's calculations based on the Novus retail panel.",
        caption_style="Quote",
    )
    fig(
        OUTPUTS_ROOT / "sheet_silpo" / "sheet_silpo_timeseries_by_standardized_type.png",
        "Silpo retail-level prices by product",
        "Source: author's calculations based on the Silpo retail panel.",
        caption_style="Quote",
    )
    para(
        f"The preparation results already show why retailer-level construction cannot be separated from later model interpretation. In several categories Silpo carries the dense part of the item universe, while Novus contributes a much thinner but still informative reference line. Milk is built on a median {_b_int(milk_compare['silpo_keys'])} Silpo item keys and {_b_int(milk_compare['silpo_brands'])} brands, but only {_b_int(milk_compare['novus_keys'])} Novus key and {_b_int(milk_compare['novus_brands'])} brand; butter shows {_b_int(butter_compare['silpo_keys'])} Silpo keys against {_b_int(butter_compare['novus_keys'])} Novus key; sour cream shows {_b_int(sour_compare['silpo_keys'])} against {_b_int(sour_compare['novus_keys'])}; and even hard cheese, which is one of the richer comparison categories, has only {_b_int(hard_compare['novus_keys'])} median Novus keys against {_b_int(hard_compare['silpo_keys'])} in Silpo. "
        "This means that cross-shop comparison is economically useful, but it should not be read as if both chains contribute the same product depth in every category."
    )
    para(
        f"Milk and butter are the clearest examples of visible basket categories that move more smoothly on the shelf than upstream prices would suggest. Over the observed retail window of {_b_int(milk_compare['n_days'])} days for milk, Silpo milk changes by {_b(change_text(milk_compare['silpo_observed_pct']))}, while Novus milk changes by {_b(change_text(milk_compare['novus_observed_pct']))}; over the same interval the producer series falls by {_b(change_text(milk_compare['producer_linear_model_pct']))}, ProZorro rises by {_b(change_text(milk_compare['prozorro_model_pct']))}, and the consumer layer rises by {_b(change_text(milk_compare['consumer_linear_model_pct']))}. "
        f"The mean absolute Silpo-Novus gap in milk is only {_b_num(milk_compare['silpo_novus_gap_mean'])} UAH, which is small compared with the same-category gap in hard cheese. "
        f"In butter, over {_b_int(butter_compare['n_days'])} days, Silpo changes by {_b(change_text(butter_compare['silpo_observed_pct']))} and Novus by {_b(change_text(butter_compare['novus_observed_pct']))}, while the producer layer falls by {_b(change_text(butter_compare['producer_linear_model_pct']))} and procurement still rises slightly by {_b(change_text(butter_compare['prozorro_model_pct']))}. "
        f"These are also heavily promoted Silpo categories, with mean discount shares of {_b_pct(milk_compare['silpo_discount'])} for milk and {_b_pct(butter_compare['silpo_discount'])} for butter, while the average absolute cross-chain gap remains {_b_num(butter_compare['silpo_novus_gap_mean'])} UAH in butter. "
        "Economically, this is a strong sign of downstream smoothing: the products that matter most in the daily basket do not mirror upstream shocks one-for-one, even when those upstream shocks are substantial."
    )
    para(
        f"Sour cream sits close to the same everyday-basket logic. Silpo sour cream changes by {_b(change_text(sour_compare['silpo_observed_pct']))}, while Novus changes by {_b(change_text(sour_compare['novus_observed_pct']))}. "
        f"At the same time, the producer layer falls by {_b(change_text(sour_compare['producer_linear_model_pct']))}, procurement falls by {_b(change_text(sour_compare['prozorro_model_pct']))}, and the consumer layer still rises by {_b(change_text(sour_compare['consumer_linear_model_pct']))}. "
        f"With median support of {_b_int(sour_compare['retail_keys'])} retail item keys, {_b_int(sour_compare['retail_brands'])} brands, an average Silpo discount share of {_b_pct(sour_compare['silpo_discount'])}, and a mean Silpo-Novus gap of only {_b_num(sour_compare['silpo_novus_gap_mean'])} UAH, sour cream behaves like a typical visible shelf category: it stays inside a comparatively narrow retail corridor even when other parts of the chain move more sharply."
    )
    para(
        f"Hard cheese is the clearest contrast. Over the same window, Silpo hard-cheese prices rise by {_b(change_text(hard_compare['silpo_observed_pct']))}, while Novus falls by {_b(change_text(hard_compare['novus_observed_pct']))}. "
        f"The producer series falls by {_b(change_text(hard_compare['producer_linear_model_pct']))}, procurement rises by {_b(change_text(hard_compare['prozorro_model_pct']))}, and the consumer layer rises by {_b(change_text(hard_compare['consumer_linear_model_pct']))}. "
        f"The category still has a substantial Silpo discount share of {_b_pct(hard_compare['silpo_discount'])}, but its average cross-chain gap reaches {_b_num(hard_compare['silpo_novus_gap_mean'])} UAH and the maximum observed gap reaches {_b_num(hard_compare['silpo_novus_gap_max'])} UAH. "
        "This is not the pattern of a homogeneous downstream category. It is the pattern of a strategically managed category in which retailer assortment, brand mix, imported and premium lines, and product differentiation matter enough to produce materially different shelf paths across chains."
    )
    para(
        f"The thinner and more differentiated categories reinforce the same point in a more selective way. Condensed milk is observed over {_b_int(condensed_compare['n_days'])} days and shows Silpo at {_b(change_text(condensed_compare['silpo_observed_pct']))} against Novus at {_b(change_text(condensed_compare['novus_observed_pct']))}, while procurement rises by {_b(change_text(condensed_compare['prozorro_model_pct']))}; cottage cheese shows Silpo at {_b(change_text(cottage_compare['silpo_observed_pct']))} against Novus at {_b(change_text(cottage_compare['novus_observed_pct']))}, while procurement rises by {_b(change_text(cottage_compare['prozorro_model_pct']))}; and cream shows Silpo at {_b(change_text(cream_compare['silpo_observed_pct']))} against Novus at {_b(change_text(cream_compare['novus_observed_pct']))}, while procurement falls by {_b(change_text(cream_compare['prozorro_model_pct']))}. "
        f"These are all categories where Novus support remains very thin, usually {_b_int(condensed_compare['novus_keys'])} key in condensed milk, {_b_int(cottage_compare['novus_keys'])} key in cottage cheese, and {_b_int(cream_compare['novus_keys'])} key in cream, so the Novus path should be treated as a focused chain signal rather than a broad market average. "
        f"Yogurt/dessert remains one of the densest shelf categories, with {_b_int(yogurt_compare['retail_keys'])} median item keys and {_b_int(yogurt_compare['retail_brands'])} brands, yet even there Silpo changes by only {_b(change_text(yogurt_compare['silpo_observed_pct']))} while Novus changes by {_b(change_text(yogurt_compare['novus_observed_pct']))}. "
        f"Milk powder is the thinnest category, with only {_b_int(powder_compare['retail_keys'])} median retail item keys and {_b_int(powder_compare['novus_keys'])} median Novus keys, which is why its very large Silpo increase of {_b(change_text(powder_compare['silpo_observed_pct']))} and mean discount share of {_b_pct(powder_compare['silpo_discount'])} should be read more cautiously than the staple-basket categories."
    )
    para(
        "From the viewpoint of data preparation, these comparisons justify the later modelling hierarchy. A strict matched cross-shop retail panel is valuable when the same economic item truly exists in both chains, but it is not always the best analytical endpoint when one retailer contributes only one or two matched observations inside a category with otherwise rich shelf turnover. "
        "For staple categories, the broader merged retail panel preserves the visible consumer basket better; for categories with thinner and more specialized retail support, the matched or consumer-linked variants can be more credible. "
        "This is why product-level preparation is not a separate descriptive appendix to the thesis, but the mechanism through which the stage-4 price object becomes economically interpretable."
    )
    para(
        "Read together, these product-level comparisons tighten the thesis story before the formal estimation begins. The visible basket categories, especially milk, butter, and sour cream, show dense retail support and comparatively bounded shelf movement relative to larger upstream shifts, which is consistent with markdown smoothing and retail timing control. "
        "The more differentiated categories, especially hard cheese, cream, and some condensed-milk and cottage-cheese lines, show wider retailer divergence and therefore provide a more natural setting for asymmetric adjustment and category-management effects. "
        "This is exactly the distinction that the estimation chapter must then take seriously: not all dairy products transmit shocks in the same way, and the product level is not detail around the model but part of the model's economic meaning."
    )

    para("5.6 What data remain after preparation - datasets in models", "Heading2")
    para(
        f"After filtering and standardization, the integrated modelling universe contains {_b_int(len(panel_index))} panel definitions: {_b_int((panel_index['panel_level'].astype(str) == 'pairwise_product').sum())} pairwise-product panels, {_b_int((panel_index['panel_level'].astype(str) == 'product').sum())} product panels, {_b_int((panel_index['panel_level'].astype(str) == 'brand').sum())} brand panels, {_b_int((panel_index['panel_level'].astype(str) == 'average').sum())} average panels, and {_b_int((panel_index['panel_level'].astype(str) == 'comparison').sum())} comparison panels. "
        "This is a large empirical universe, but it remains economically uneven because overlap and admissibility differ sharply by link and by product."
    )
    para(
        f"The required-link coverage makes that unevenness visible. FarmGateUA -> ProducerUA contributes {_b_int(coverage_fp['rows_total'])} rows with {_b_int(coverage_fp['core_finding_rows'])} core findings; ProducerUA -> ProZorro contributes {_b_int(coverage_pp['rows_total'])} rows with {_b_int(coverage_pp['core_finding_rows'])} core findings; ProZorro -> Retail contributes {_b_int(coverage_pr['rows_total'])} rows with {_b_int(coverage_pr['core_finding_rows'])} core findings; Retail -> ProZorro contributes {_b_int(coverage_rz['rows_total'])} rows with {_b_int(coverage_rz['core_finding_rows'])} core findings; and the brand block adds {_b_int(coverage_brand['rows_total'])} brand panels with {_b_int(coverage_brand['core_finding_rows'])} core findings. "
        "The integrated retail reconstruction improves the stage-4 interpretation substantially, but it does not remove the basic fact that some products and some links remain much better identified than others."
    )
    para(
        f"The direct farm-gate block is especially important to interpret correctly. Its core-finding share is {_b_pct(raw_stage_summary.loc[raw_stage_summary['stage_to'].astype(str) == 'ProducerUA', 'mean'].iloc[0])} for ProducerUA, {_b_pct(raw_stage_summary.loc[raw_stage_summary['stage_to'].astype(str) == 'ProZorro', 'mean'].iloc[0])} for ProZorro, and {_b_pct(raw_stage_summary.loc[raw_stage_summary['stage_to'].astype(str) == 'Retail', 'mean'].iloc[0])} for Retail. "
        "This corrected ranking matters because it shows that the strongest direct extreme-points evidence is farm-gate to procurement, not farm-gate to processor. The raw-milk benchmark is therefore informative, but it works best where the downstream stage is still relatively standardized."
    )

    para("Chapter 6. Estimation results", "Heading1", page_break_before=True)
    para(
        "The estimation chapter asks where along the dairy chain price adjustment is fast, where it is buffered, and where it is reshaped by downstream commercial conduct. "
        "The core structural evidence still comes from the chain ProducerUA -> ProZorro -> Retail because this remains the clearest sequence through which an upstream cost signal can be traced into procurement and then to the shelf. "
        "The deeper retail reconstruction does not replace that logic. It strengthens it by making the stage-4 measurement more transparent and by checking whether the main economic interpretation survives under alternative retailer-grounded downstream definitions."
    )

    para("6.1 Model strategy and what the families contribute", "Heading2")
    para(
        "The model families are deliberately complementary rather than redundant. ARDL remains the distributed-lag benchmark when a stable long-run relation is plausible. ECM turns that relation into an explicit speed-of-adjustment object. NARDL tests whether positive and negative shocks are processed differently. VECM remains a multivariate robustness layer. "
        "To deepen the downstream interpretation, the study also adds local projections, vertical spread equations, and focused discount regressions built on the item-level retail reconstruction. These additional models are not substitutes for the structural stack; they are retailer-sensitive robustness layers that clarify timing, endpoint choice, and the role of promotions."
    )
    para(
        f"Across the integrated coefficient table, the study estimates {_b_int(len(coef))} coefficients: {_b_int(family_counts.get('NARDL', 0))} NARDL rows, {_b_int(family_counts.get('ARDL', 0))} ARDL rows, {_b_int(family_counts.get('ECM', 0))} ECM rows, {_b_int(family_counts.get('VECM', 0))} VECM rows, and the remainder in OLS-HAC stress-test families or explicit no-fit cases. "
        f"Crucially, {_b_int(int(core_by_family.get('NARDL', 0) + core_by_family.get('ECM', 0)))} out of {_b_int(int(pd.to_numeric(coef['core_finding_flag'], errors='coerce').fillna(0).sum()))} core findings sit in the NARDL or ECM families. "
        "That is why the thesis treats equilibrium correction and asymmetry, rather than one-period coefficients, as the main evidential objects."
    )
    fig(
        OUTPUTS_ROOT / "model_ardl" / "ardl_short_run.png",
        "Short-run ARDL coefficient dispersion across active links",
        "Source: author's calculations based on the integrated ARDL summary output.",
        caption_style="Quote",
    )
    fig(
        OUTPUTS_ROOT / "model_ecm" / "ecm_ect.png",
        "Long-run adjustment signals across links",
        "Source: author's calculations based on the integrated ECM summary output.",
        caption_style="Quote",
    )
    fig(
        OUTPUTS_ROOT / "model_nardl" / "nardl_long_run.png",
        "Asymmetric long-run transmission evidence",
        "Source: author's calculations based on the integrated NARDL summary output.",
        caption_style="Quote",
    )
    para(
        f"The additional retailer-sensitive block estimates {_b_int(lp_coeff[['product', 'link', 'price_variant', 'horizon_days', 'reconstruction_variant', 'farm_gate_source']].drop_duplicates().shape[0])} local-projection equations and retains {_b_int(len(lp_screen))} screened horizon responses. "
        f"The vertical spread block adds {_b_int(len(spread))} usable equations, while the focused discount block adds {_b_int(len(discount))} direct discount equations. "
        "These models are deliberately simpler than the structural ARDL-ECM-NARDL system, but they are informative because they stress-test the same economic story with a data build that is much more explicit about item-level retail construction."
    )

    para("6.2 Producers to procurement (processors) transmission", "Heading2")
    para(
        "The upstream link remains the clearest part of the chain. Procurement does not behave like a frictionless conduit, but it repeatedly re-anchors to producer conditions. This is the stage at which cost pressure is translated into standardized transaction prices, yet contracting and specification rules still smooth part of the short-run noise."
    )
    para(
        f"In the required-link audit, ProducerUA -> ProZorro contributes {_b_int(coverage_pp['rows_total'])} rows and {_b_int(coverage_pp['core_finding_rows'])} core findings. "
        f"The product-level NARDL block shows especially clear correction for butter with ECT {_b_num(butter_prod['ect_coef'])}, cream with ECT {_b_num(cream_prod['ect_coef'])}, and hard cheese with ECT {_b_num(hard_prod['ect_coef'])}, all with very small p-values. "
        "This is exactly the kind of repeated equilibrium re-anchoring one would expect when procurement is institutionally slower than the producer layer but cannot remain detached from it for long."
    )
    para(
        f"The timing evidence supports the same interpretation. In the pooled butter panel, the strongest producer-to-procurement lag appears at {_b_int(butter_lag_prod['lag'])} days; in hard cheese it appears at {_b_int(hard_lag_prod['lag'])} days. "
        f"In the horizon-based robustness block, ProducerUA -> ProZorro reaches a screened 7-day core share of {_b_pct(_select_first(lp_summary, (lp_summary['link'].astype(str) == 'ProducerUA -> ProZorro') & (lp_summary['price_variant'].astype(str) == 'procurement_price') & (lp_summary['horizon_days'] == 7))['core_share'])}. "
        "So the evidence is not only statistically present; it is also consistent with delayed but real institutional repricing."
    )
    para(
        "What matters economically is not a literal one-to-one long-run markup coefficient. The more important result is that procurement repeatedly corrects disequilibrium with the producer stage, which is precisely what gives the middle of the chain its buffering role. "
        "Procurement absorbs, delays, and regularizes shocks; it does not sever the link."
    )

    para("6.3 Procurement to retail transmission and retailer heterogeneity", "Heading2")
    para(
        "The downstream link is harder to interpret because retail price is not only a function of upstream cost. It is also a function of assortment design, markdown policy, category management, and the retailer's ability to choose when a procurement shock becomes visible on the shelf. "
        "That is why retailer heterogeneity matters more downstream than upstream."
    )
    para(
        f"Butter remains the clearest example of managed but real downstream linkage. In the pooled retail panel, ARDL gives a short-run coefficient of {_b_num(butter_ardl['sr_coef'])} and a long-run coefficient of {_b_num(butter_ardl['lr_coef'])}. "
        f"ECM then sharpens the interpretation with ECT {_b_num(butter_ecm['ect_coef'])} at p-value {_b_num(butter_ecm['ect_pvalue'])}, while NARDL also yields a strong correction term of {_b_num(butter_nardl['ect_coef'])}. "
        "The stable conclusion is not a literal long-run markup; it is that the pooled butter category re-anchors after procurement shocks, but does so through a managed shelf path rather than through one-step repricing."
    )
    fig(
        OUTPUTS_ROOT / "butter" / "silpo_novus" / "time_series_observed.png",
        "Butter, pooled retail, observed category series",
        "Source: author's calculations based on the integrated butter retail-procurement panel.",
        caption_style="Quote",
    )
    fig(
        OUTPUTS_ROOT / "butter" / "silpo_novus" / "ecm_adjustment_observed.png",
        "Butter, pooled retail, ECM adjustment",
        "Source: author's calculations based on the integrated butter ECM output.",
        caption_style="Quote",
    )
    para(
        f"Milk in Silpo remains the clearest fast-adjustment case. ECM gives a short-run coefficient of {_b_num(milk_ecm['sr_coef'])}, a long-run coefficient of {_b_num(milk_ecm['lr_coef'])}, and ECT {_b_num(milk_ecm['ect_coef'])}. "
        f"NARDL produces the same qualitative result, with ECT {_b_num(milk_nardl['ect_coef'])}. "
        f"The lag profile places the strongest procurement-to-retail relation at {_b_int(milk_lag_retail['lag'])} days with correlation {_b_num(milk_lag_retail['corr'])}. "
        "This is economically consistent with a high-turnover product category in which disequilibrium is removed relatively quickly."
    )
    fig(
        OUTPUTS_ROOT / "milk" / "silpo" / "time_series_observed.png",
        "Milk, Silpo, observed category series",
        "Source: author's calculations based on the integrated milk Silpo panel.",
        caption_style="Quote",
    )
    fig(
        OUTPUTS_ROOT / "milk" / "silpo" / "ecm_adjustment_observed.png",
        "Milk, Silpo, ECM adjustment",
        "Source: author's calculations based on the integrated milk ECM output.",
        caption_style="Quote",
    )
    para(
        f"Hard cheese is different again. The pooled ARDL coefficient is short-run {_b_num(hard_ardl['sr_coef'])} and long-run {_b_num(hard_ardl['lr_coef'])}, while the pooled NARDL gives short-run {_b_num(hard_nardl['sr_coef'])}, long-run {_b_num(hard_nardl['lr_coef'])}, and ECT {_b_num(hard_nardl['ect_coef'])}. "
        f"The category also shows one of the strongest delayed patterns, with the procurement-to-retail lag peak at {_b_int(hard_lag_retail['lag'])} days and the producer-to-procurement peak at {_b_int(hard_lag_prod['lag'])}. "
        "This is the strongest downstream case for strategic category management and asymmetric treatment of cost pressure."
    )
    fig(
        OUTPUTS_ROOT / "hard_cheese" / "silpo_novus" / "nardl_multipliers_observed.png",
        "Hard cheese, pooled retail, NARDL multipliers",
        "Source: author's calculations based on the integrated hard-cheese NARDL output.",
        caption_style="Quote",
    )
    para(
        f"Sour cream sits between the milk and hard-cheese cases. Its pooled NARDL gives short-run {_b_num(sour_nardl['sr_coef'])}, long-run {_b_num(sour_nardl['lr_coef'])}, and ECT {_b_num(sour_nardl['ect_coef'])}. "
        "The category clearly corrects, but it remains more strategically managed than plain drinking milk."
    )
    para(
        "The deeper retail reconstruction clarifies this heterogeneity further because it allows the stage-4 endpoint to vary by product instead of being imposed mechanically. "
        f"In the horizon-based downstream comparison, the strongest procurement-to-retail evidence appears for Silpo, where the best screened ProZorro -> Silpo specification reaches a 7-day core share of {_b_pct(prozorro_silpo_best['core_share'])}. "
        f"Novus follows with {_b_pct(prozorro_novus_best['core_share'])}, the matched cross-shop panel with {_b_pct(prozorro_matched_best['core_share'])}, and the broad retail pool with {_b_pct(prozorro_retail_best['core_share'])}. "
        "This ranking is economically useful because it shows that more coverage is not always more informative: the broader pooled panel is longer, but the retailer-specific endpoint can carry a cleaner timing signal."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "11_candidate_downstream_core_share.png",
        "Procurement-to-retail evidence across downstream endpoint candidates",
        "Source: author's calculations based on 7- and 14-day local-projection screening across candidate retail endpoints.",
        caption_style="Quote",
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "02_lp_pass_through_horizons.png",
        "Local-projection pass-through by horizon",
        "Source: author's calculations based on the integrated local-projection summary.",
        caption_style="Quote",
    )
    para(
        "The local-projection evidence should still be interpreted carefully. It is intentionally less structural than ECM or NARDL. Its value lies in showing whether the timing of the response survives when the lag structure is not imposed parametrically. "
        "In that role, it supports the same conclusion as the structural models: transmission is delayed, product-specific, and sensitive to how the downstream stage is measured."
    )

    para("6.4 Discounts, retail design, and market-power signals", "Heading2")
    para(
        "Discounts are not treated here as an afterthought. The retail item-level reconstruction makes them explicit in two ways at once: the effective price already contains the markdown, but the discount state remains visible through the baseline price, discount amount, discount type, discount dummy, and markdown depth. "
        "That design matters because retailers can absorb part of the short-run pressure by changing the promotional regime while leaving the broader shelf path comparatively smooth."
    )
    para(
        f"The structural discount comparison confirms that observed and baseline retail paths are not equivalent. Across {_b_int(len(asymmetry))} observations in the observed-versus-baseline table, the mean absolute difference equals {_b_num(delta_sr_mean)} in short-run coefficients, {_b_num(delta_lr_mean)} in long-run coefficients, and {_b_num(delta_ect_mean)} in adjustment terms. "
        f"Pseudo-asymmetry is flagged in {_b_pct(pseudo_share)} of rows. "
        "This is much more consistent with tactical price smoothing than with a clean one-price retail regime."
    )
    fig(
        OUTPUTS_ROOT / "model_discounts" / "discount_delta_short_run.png",
        "Observed-versus-baseline discount effect in short-run transmission",
        "Source: author's calculations based on the integrated discount-comparison output.",
        caption_style="Quote",
    )
    para(
        f"The retailer-sensitive robustness block sharpens the same point from a different direction. The vertical spread module estimates {_b_int(len(spread))} usable equations, of which {_b_int(int(pd.to_numeric(spread['persistent_margin_flag'], errors='coerce').fillna(0).sum()))} indicate persistent spreads and {_b_int(int(pd.to_numeric(spread['asymmetric_margin_flag'], errors='coerce').fillna(0).sum()))} indicate asymmetric adjustment. "
        "These spread results are not direct legal proof of market power, but they are highly consistent with timing control, selective margin adjustment, and category management."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "04_vertical_spread_proxy.png",
        "Vertical spread and margin-adjustment proxy across chain segments",
        "Source: author's calculations based on the integrated spread-model summary.",
        caption_style="Quote",
    )
    para(
        f"The focused discount model is intentionally narrower and therefore more cautious. It yields {_b_int(len(discount))} usable equations and {_b_int(int(pd.to_numeric(discount['discount_strategy_signal'], errors='coerce').fillna(0).sum()))} explicit discount-strategy signals, notably in butter and milk. "
        "This does not weaken the economic role of promotions. It clarifies it. Promotions appear to matter most as part of the downstream data-generating process itself rather than as a stand-alone structural driver that dominates every category."
    )
    fig(
        SECOND_STAGE_ROOT / "figures" / "05_discount_incidence.png",
        "Retail discount incidence by product",
        "Source: author's calculations based on the integrated discount-model outputs.",
        caption_style="Quote",
    )
    para(
        "Taken together, the main and retailer-sensitive discount blocks lead to the same interpretation. Discounts help retailers control the timing and visibility of transmission. They do not eliminate the upstream link, but they do alter how quickly and how visibly that link reaches the shelf."
    )

    para("6.4.1 Farm-gate transmission and whole-chain interpretation", "Heading3")
    para(
        "The direct farm-gate question remains the most difficult part of the thesis because it compresses several institutional transformations into one relationship. The issue is not whether the farm-gate benchmark exists in the data. It does. The issue is how much of that benchmark can be recovered once one national raw-milk series is asked to explain processed-dairy categories, procurement prices, and retailer-controlled shelf prices."
    )
    para(
        f"The corrected direct-summary shares make the ranking clear. FarmGateUA -> ProducerUA contributes {_b_int(coverage_fp['core_finding_rows'])} core findings out of {_b_int(coverage_fp['rows_total'])}, or {_b_pct(coverage_fp['core_finding_rows'] / coverage_fp['rows_total'])}. "
        f"FarmGateUA -> ProZorro contributes {_b_int(coverage_fz['core_finding_rows'])} core findings out of {_b_int(coverage_fz['rows_total'])}, or {_b_pct(coverage_fz['core_finding_rows'] / coverage_fz['rows_total'])}. "
        f"FarmGateUA -> Retail contributes {_b_int(coverage_fr['core_finding_rows'])} core findings out of {_b_int(coverage_fr['rows_total'])}, or {_b_pct(coverage_fr['core_finding_rows'] / coverage_fr['rows_total'])}. "
        "The strongest direct block is therefore farm-gate to procurement, not farm-gate to processor."
    )
    fig(
        OUTPUTS_ROOT / "primary_chain_summary" / "farmgate_direct_heatmap.png",
        "Direct farm-gate evidence by downstream stage and downstream panel",
        "Source: author's calculations based on the integrated primary-chain farm-gate summary.",
        caption_style="Quote",
    )
    para(
        f"In the pairwise NARDL comparison, the strongest FarmGateUA -> ProZorro route reaches a core-finding share of {_b_pct(fg_proc_pairwise['core_finding_share'])}, with reconstruction robustness of {_b_pct(fg_proc_pairwise['robust_across_reconstruction_share'])} and interpolation robustness of {_b_pct(fg_proc_pairwise['robust_linear_vs_pchip_share'])}. "
        f"For the anchored broad retail panel, the comparable FarmGateUA -> Retail share is {_b_pct(fg_retail_anchor['core_finding_share'])} with median overlap {_b_int(fg_retail_anchor['median_n_obs'])}; for the stricter retailer-core panel it is {_b_pct(fg_retail_core['core_finding_share'])} with median overlap {_b_int(fg_retail_core['median_n_obs'])}. "
        "This is the central trade-off of the full-chain design: the broader downstream endpoint lengthens the horizon, while the retailer-core endpoint is shorter but economically cleaner."
    )
    fig(
        OUTPUTS_ROOT / "primary_chain_summary" / "unified_retail_comparison.png",
        "Comparison of broad and retailer-core downstream panels in the full chain",
        "Source: author's calculations based on the integrated downstream-panel comparison output.",
        caption_style="Quote",
    )
    para(
        f"The reverse-flow evidence is equally important for interpretation. In the pairwise NARDL block, the broad downstream panel reaches {_b_pct(fg_reverse_anchor['core_finding_share'])} core support in Retail -> FarmGateUA, while the retailer-core panel reaches {_b_pct(fg_reverse_core['core_finding_share'])}. "
        f"The broader reverse-flow table also retains {_b_int(coverage_rz['core_finding_rows'])} core findings out of {_b_int(coverage_rz['rows_total'])} for Retail -> ProZorro, or {_b_pct(coverage_rz['core_finding_rows'] / coverage_rz['rows_total'])}. "
        f"In the pooled Retail -> ProducerUA comparison panel, the strongest NARDL specification yields short-run {_b_num(reverse_retail_to_producer['sr_coef'])}, long-run {_b_num(reverse_retail_to_producer['lr_coef'])}, and ECT {_b_num(reverse_retail_to_producer['ect_coef'])}. "
        "This does not prove simple reverse causality in every period. It shows something more interesting: downstream pricing decisions contain information that travels back through the chain."
    )
    fig(
        OUTPUTS_ROOT / "model_intersection_bidirectional" / "bidirectional_coef.png",
        "Bidirectional coefficient evidence across upstream and downstream intersection panels",
        "Source: author's calculations based on the integrated bidirectional model summary.",
        caption_style="Quote",
    )
    para(
        "The whole-chain interpretation is therefore more precise than a simple forward pass-through statement. Forward transmission remains the dominant structural story. Procurement still re-anchors to producer conditions, and retail still responds to procurement shocks. But the integrated evidence also shows that the downstream stage is informative in its own right. Retailers are not only receivers of shocks; they are coordinators of how those shocks are timed, displayed, and partially fed back into the broader price environment."
    )

    para("6.4.2 Comparative synthesis of model results", "Heading3")
    para(
        "To keep the empirical story economically coherent, the final step before the conclusion is to place all estimation blocks into one comparative matrix. "
        "The purpose of the table is not to mechanically rank estimators, but to show what each model family contributes, which numeric results carry the interpretation, and how the same chain story changes when the price object, lag structure, or downstream measurement rule changes."
    )
    table(
        headers=synthesis_table_headers,
        rows=synthesis_table_rows,
        caption="Integrated comparative summary of the estimated model blocks",
        source="Source: author's calculations based on the integrated primary-chain outputs, local-projection outputs, spread models, and discount models.",
    )

    para("6.5 Conclusion and economic implications", "Heading2")
    para(
        "The integrated empirical conclusion is that the Ukrainian dairy market is vertically coordinated, but that coordination is neither frictionless nor uniform. The study does not support one universal pass-through coefficient. Instead, it reveals a layered chain in which different institutional stages bear different parts of the adjustment burden and in which the downstream stage has its own strategic logic rather than behaving like a passive residual of upstream cost."
    )
    para(
        "The most persuasive structural evidence remains equilibrium correction. Procurement repeatedly re-anchors to producer prices; retail categories repeatedly re-anchor to procurement conditions; and the strongest product-level results appear where the category is economically coherent enough for disequilibrium to be observed and then removed. Milk is the clearest high-frequency downstream correction case, butter is the clearest managed-but-linked case, and hard cheese is the clearest strategic category-management case."
    )
    para(
        "The deeper retail reconstruction strengthens that conclusion rather than overturning it. Once Novus and Silpo are harmonized at item level, discounts are kept inside the effective price but modeled separately, and the downstream endpoint is allowed to vary by product, the main story survives. The shelf does not behave like a pure cost-plus series. It behaves like a managed adjustment layer in which timing, brand structure, discount policy, and assortment design reshape how upstream shocks become visible to consumers."
    )
    para(
        "This integrated result is economically valuable at several levels. For processors and procurement managers, it shows that disequilibrium tends to be corrected, but not at the same speed across products. For retailers, it quantifies how category management and promotions can soften or delay the shelf response without fully severing the upstream link. For competition and policy analysis, it suggests that downstream market power is best understood not as one static markup wedge, but as control over the timing, visibility, and selectivity of transmission."
    )
    para(
        "The difficult coefficients are also informative when read correctly. Large negative long-run values, selective asymmetry, and weak direct farm-gate coefficients concentrate where economic granularity is coarse, where overlap is thin, or where retailer assortment is structurally uneven across chains. The correct response is therefore not to smooth those results away, but to acknowledge where the chain is well identified and where it remains sensitive to data design."
    )
    para(
        "On that standard, the present version is materially stronger than before. The retail stage is better grounded in item-level evidence, the farm-gate interpretation is more accurately delimited, the core structural models and the retailer-sensitive robustness layers now tell the same economic story, and the thesis can state its main claim more confidently: vertical price transmission in the Ukrainian dairy chain is real, procurement acts as an institutional transmission buffer, and downstream market power appears primarily through category management, discount smoothing, and selective asymmetry rather than through one mechanical pass-through coefficient."
    )

    return blocks


def _blocks_to_markdown(blocks: list[Block]) -> str:
    lines: list[str] = []
    for block in blocks:
        if isinstance(block, ParagraphBlock):
            if block.style == "Heading1":
                lines.append(f"# {block.text}")
            elif block.style == "Heading2":
                lines.append(f"## {block.text}")
            elif block.style == "Heading3":
                lines.append(f"### {block.text}")
            else:
                lines.append(block.text)
            lines.append("")
        elif isinstance(block, TableBlock):
            lines.append(block.caption)
            lines.append("")
            header_line = "| " + " | ".join(block.headers) + " |"
            sep_line = "| " + " | ".join(["---"] * len(block.headers)) + " |"
            lines.append(header_line)
            lines.append(sep_line)
            for row in block.rows:
                escaped = [str(cell).replace("|", "\\|") for cell in row]
                lines.append("| " + " | ".join(escaped) + " |")
            lines.append("")
            lines.append(block.source)
            lines.append("")
        else:
            lines.append(block.caption)
            lines.append(f"![{block.caption}]({block.path})")
            lines.append(block.source)
            lines.append("")
    return "\n".join(lines).strip() + "\n"


def _blocks_to_html(blocks: list[Block]) -> str:
    html_lines = ["<html><body>"]
    for block in blocks:
        if isinstance(block, ParagraphBlock):
            if block.style == "Heading1":
                html_lines.append(f"<h1>{block.text}</h1>")
            elif block.style == "Heading2":
                html_lines.append(f"<h2>{block.text}</h2>")
            elif block.style == "Heading3":
                html_lines.append(f"<h3>{block.text}</h3>")
            else:
                html_lines.append(f"<p>{block.text}</p>")
        elif isinstance(block, TableBlock):
            html_lines.append(f"<p>{block.caption}</p>")
            html_lines.append('<table border="1" cellspacing="0" cellpadding="6" style="border-collapse: collapse; width: 100%;">')
            html_lines.append("<thead><tr>" + "".join(f"<th>{header}</th>" for header in block.headers) + "</tr></thead>")
            html_lines.append("<tbody>")
            for row in block.rows:
                html_lines.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
            html_lines.append("</tbody></table>")
            html_lines.append(f"<p>{block.source}</p>")
        else:
            html_lines.append(f"<p>{block.caption}</p>")
            html_lines.append(f'<p><img src="{block.path}" alt="{block.caption}" style="max-width: 100%;"/></p>')
            html_lines.append(f"<p>{block.source}</p>")
    html_lines.append("</body></html>")
    return "\n".join(html_lines)


def generate_fullversion(
    main_output: Path | None = None,
    full_output: Path | None = None,
    md_output: Path | None = None,
    html_output: Path | None = None,
) -> tuple[Path, Path, Path, Path]:
    thesis_root = _find_thesis_root()
    template_path = thesis_root / "Charniuk_Maksym_MScThesis_Draft_correctedformat.docx"
    if not template_path.exists():
        raise FileNotFoundError(f"Template DOCX not found: {template_path}")

    blocks = _build_blocks()

    main_output = main_output or (thesis_root / "data_estiamtion_updated_conclusion.docx")
    full_output = full_output or (thesis_root / "data_estiamtion_updated_conclusion_fullversion.docx")
    md_output = md_output or (thesis_root / "data_estiamtion_updated_conclusion_fullversion.md")
    html_output = html_output or (thesis_root / "data_estiamtion_updated_conclusion_fullversion.html")

    _write_docx_from_template(template_path, main_output, blocks)
    _write_docx_from_template(template_path, full_output, blocks)
    md_output.write_text(_blocks_to_markdown(blocks), encoding="utf-8")
    html_output.write_text(_blocks_to_html(blocks), encoding="utf-8")
    return main_output, full_output, md_output, html_output


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the integrated fullversion of Chapters 5 and 6.")
    parser.add_argument("--main-output", type=Path, help="Optional explicit path for data_estiamtion_updated_conclusion.docx.")
    parser.add_argument("--full-output", type=Path, help="Optional explicit path for the _fullversion DOCX.")
    parser.add_argument("--md-output", type=Path, help="Optional explicit path for the Markdown companion.")
    parser.add_argument("--html-output", type=Path, help="Optional explicit path for the HTML companion.")
    args = parser.parse_args()

    main_output, full_output, md_output, html_output = generate_fullversion(
        main_output=args.main_output,
        full_output=args.full_output,
        md_output=args.md_output,
        html_output=args.html_output,
    )
    print(f"Updated thesis chapter DOCX generated: {main_output}")
    print(f"Fullversion DOCX generated: {full_output}")
    print(f"Markdown companion generated: {md_output}")
    print(f"HTML companion generated: {html_output}")


if __name__ == "__main__":
    main()
