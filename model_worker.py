#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

import os
import warnings
import numpy as np
import pandas as pd
os.environ.setdefault("MPLCONFIGDIR", "/tmp/mplconfig")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp")
os.environ.setdefault("MPLBACKEND", "Agg")
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests

import common
import rw2_extended_mapping_pipeline as rw2
import vpt_primary_chain as vpt


def _coef_bar(df: pd.DataFrame, x_col: str, y_col: str, title: str, out_path: Path, top_n: int = 20) -> Path:
    d = df.copy()
    if x_col not in d.columns or y_col not in d.columns or d.empty:
        return out_path
    d[y_col] = pd.to_numeric(d[y_col], errors="coerce")
    d = d.dropna(subset=[x_col, y_col]).head(top_n)
    if d.empty:
        return out_path
    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
    ax.bar(d[x_col].astype(str), d[y_col])
    ax.set_title(title)
    ax.set_ylabel(y_col)
    ax.tick_params(axis="x", rotation=35)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out_path


def _line_plot(df: pd.DataFrame, x_col: str, y_cols: List[str], title: str, out_path: Path) -> Path:
    if df.empty or x_col not in df.columns:
        return out_path
    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
    d = df.copy()
    d[x_col] = pd.to_datetime(d[x_col], errors="coerce")
    d = d.dropna(subset=[x_col]).sort_values(x_col)
    if d.empty:
        plt.close(fig)
        return out_path
    for c in y_cols:
        if c not in d.columns:
            continue
        y = pd.to_numeric(d[c], errors="coerce")
        if y.notna().sum() < 3:
            continue
        ax.plot(d[x_col], y, label=c, linewidth=1.4)
    ax.set_title(title)
    ax.set_xlabel("date")
    ax.legend(frameon=False)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out_path


def _prep():
    _, raw = common.load_raw()
    cleaned = common.prepare_cleaned(raw)
    all_daily = common.build_all_daily(cleaned)
    tests, weekly_level, model_series = common.build_model_inputs(cleaned, all_daily)
    return cleaned, all_daily, tests, weekly_level, model_series


def _effective_daily_prices(all_daily: pd.DataFrame) -> pd.DataFrame:
    if all_daily.empty:
        return pd.DataFrame()
    d = all_daily.copy()
    d["price_eff"] = d["price_pchip"].where(
        d["source"].isin(["ProducerUA", "ConsumerUA", "FarmGateUA_initial", "FarmGateUA_filled"]) & d["price_pchip"].notna(),
        d["price_real"],
    )
    d["price_eff"] = pd.to_numeric(d["price_eff"], errors="coerce")
    d["date"] = pd.to_datetime(d["date"], errors="coerce")
    d = d.dropna(subset=["date", "price_eff"]).copy()
    return d


def _best_lag(y: pd.Series, x: pd.Series, max_lag: int = 30, min_obs: int = 20) -> Tuple[int, float]:
    best_lag = 1
    best_corr = np.nan
    for lag in range(1, max_lag + 1):
        pair = pd.concat([y, x.shift(lag)], axis=1).dropna()
        if len(pair) < min_obs:
            continue
        corr = float(pair.iloc[:, 0].corr(pair.iloc[:, 1]))
        if np.isnan(best_corr) or abs(corr) > abs(best_corr):
            best_corr = corr
            best_lag = lag
    return best_lag, best_corr


def _safe_ols(y: pd.Series, xdf: pd.DataFrame, hac_lags: int = 3):
    frame = pd.concat([y.rename("y"), xdf], axis=1).dropna()
    if len(frame) < 25:
        return None, frame
    x = sm.add_constant(frame.drop(columns=["y"]), has_constant="add")
    fit = sm.OLS(frame["y"], x).fit(cov_type="HAC", cov_kwds={"maxlags": hac_lags})
    return fit, frame


def _safe_log(s: pd.Series) -> pd.Series:
    x = pd.to_numeric(s, errors="coerce")
    return np.log(x.where(x > 0))


def _pivot_product_daily(
    eff: pd.DataFrame,
    product: str,
    standardized_type: str,
    sources: List[str],
) -> pd.DataFrame:
    g = eff[(eff["product"] == product) & (eff["standardized_type"] == standardized_type)].copy()
    if g.empty:
        return pd.DataFrame()
    p = g[g["source"].isin(sources)].pivot_table(
        index="date",
        columns="source",
        values="price_eff",
        aggfunc="mean",
    ).sort_index()
    return p


def run_ardl() -> Path:
    out_dir = vpt.run_primary_model_family_report("ARDL")
    common.print_block(
        "MODEL ARDL",
        [
            f"output_dir: {out_dir}",
            "Primary chain rule: ProducerUA -> ProZorro -> Retail (Silpo/Novus/Combined).",
        ],
    )
    return out_dir


def run_ecm() -> Path:
    out_dir = vpt.run_primary_model_family_report("ECM")
    common.print_block(
        "MODEL ECM",
        [
            f"output_dir: {out_dir}",
            "ECM estimated only when series are I(1) and cointegrated; ECT sign/significance retained in output.",
        ],
    )
    return out_dir


def run_nardl() -> Path:
    out_dir = vpt.run_primary_model_family_report("NARDL")
    common.print_block(
        "MODEL NARDL",
        [
            f"output_dir: {out_dir}",
            "Asymmetry from positive/negative shock decomposition is reported in primary chain outputs.",
        ],
    )
    return out_dir


def run_vecm() -> Path:
    out_dir = vpt.run_primary_model_family_report("VECM")
    common.print_block(
        "MODEL VECM",
        [
            f"output_dir: {out_dir}",
            "VECM now constrained to primary triplet (ProducerUA, ProZorro, Retail) by standardized_type/retailer.",
        ],
    )
    return out_dir


def run_discounts() -> Path:
    cleaned, _, *_ = _prep()
    silpo = cleaned["Silpo"].copy()
    novus = cleaned["Novus"].copy()
    producer = cleaned["ProducerUA"].copy()
    prozorro = cleaned["ProZorro"].copy()
    farm_gate = cleaned["FarmGateUA_initial"].copy()
    eu = cleaned["EU"].copy()
    cme = cleaned["CME"].copy()

    cons_path = common.OUTPUT_ROOT / "primary_chain_summary" / "primary_chain_consolidated.xlsx"
    if not cons_path.exists():
        vpt.run_primary_chain_pipeline(freq="daily")
    cons = pd.read_excel(cons_path, sheet_name="Consolidated_ModelCoefficients") if cons_path.exists() else pd.DataFrame()

    incidence_rows: List[Dict[str, object]] = []
    type_rows: List[Dict[str, object]] = []
    depth_rows: List[Dict[str, object]] = []

    if not silpo.empty:
        silpo["date"] = pd.to_datetime(silpo["date"], errors="coerce")
        silpo = silpo.dropna(subset=["date"]).copy()
        silpo["markdown_rate"] = pd.to_numeric(silpo.get("markdown_rate"), errors="coerce")
        silpo["discount_present"] = pd.to_numeric(silpo.get("discount_present"), errors="coerce").fillna(0).clip(0, 1)
        silpo["discount_type"] = silpo.get("discount_type", "unknown").astype(str)
        silpo["brand_normalized"] = silpo.get("brand_normalized", silpo.get("brand", "")).astype(str)

        prod = producer.copy()
        prod["producer"] = pd.to_numeric(prod.get("price_pchip_input"), errors="coerce").where(
            pd.to_numeric(prod.get("price_pchip_input"), errors="coerce").notna(),
            pd.to_numeric(prod.get("price_linear_input"), errors="coerce"),
        )
        prod = prod.groupby(["date", "standardized_type"], as_index=False)["producer"].mean()

        pz = prozorro.copy()
        pz["prozorro"] = pd.to_numeric(pz.get("observed_price", pz.get("price")), errors="coerce")
        pz = pz.groupby(["date", "standardized_type"], as_index=False)["prozorro"].mean()

        fg = farm_gate.copy()
        fg["farm_gate"] = pd.to_numeric(fg.get("price_pchip_input"), errors="coerce").where(
            pd.to_numeric(fg.get("price_pchip_input"), errors="coerce").notna(),
            pd.to_numeric(fg.get("price_linear_input"), errors="coerce"),
        )
        fg = fg.groupby("date", as_index=False)["farm_gate"].mean()

        eu_daily = eu.copy()
        eu_daily["eu_price"] = pd.to_numeric(eu_daily.get("observed_price", eu_daily.get("price")), errors="coerce")
        eu_daily = eu_daily.groupby(["date", "standardized_type"], as_index=False)["eu_price"].mean()

        cme_daily = cme.copy()
        cme_daily["cme_price"] = pd.to_numeric(cme_daily.get("observed_price", cme_daily.get("price")), errors="coerce")
        cme_daily = cme_daily.groupby(["date", "standardized_type"], as_index=False)["cme_price"].mean()

        nov = novus.copy()
        nov["novus_price"] = pd.to_numeric(nov.get("observed_price", nov.get("price")), errors="coerce")
        nov = nov.groupby(["date", "standardized_type"], as_index=False)["novus_price"].mean()

        daily = (
            silpo.groupby(["date", "standardized_type"], as_index=False)
            .agg(
                observed_price=("observed_price", "median"),
                baseline_price=("baseline_price", "median"),
                discount_present=("discount_present", "mean"),
                markdown_rate=("markdown_rate", "mean"),
                discount_type=("discount_type", lambda s: s.mode().iloc[0] if not s.mode().empty else "unknown"),
                promo_duration=("promo_duration", "mean"),
                time_since_last_promo=("time_since_last_promo", "mean"),
                top_brand_share=("brand_normalized", lambda s: float(s.astype(str).value_counts(normalize=True, dropna=False).iloc[0]) if len(s) else np.nan),
            )
            .merge(prod, on=["date", "standardized_type"], how="left")
            .merge(pz, on=["date", "standardized_type"], how="left")
            .merge(fg, on="date", how="left")
            .merge(eu_daily, on=["date", "standardized_type"], how="left")
            .merge(cme_daily, on=["date", "standardized_type"], how="left")
            .merge(nov, on=["date", "standardized_type"], how="left")
            .sort_values(["standardized_type", "date"])
        )
        pooled_daily = daily.copy()

        for std, g in daily.groupby("standardized_type", dropna=False):
            gg = g.copy().sort_values("date")
            gg["log_observed"] = _safe_log(gg["observed_price"])
            gg["log_baseline"] = _safe_log(gg["baseline_price"])
            gg["d_producer"] = _safe_log(gg["producer"]).diff()
            gg["d_prozorro"] = _safe_log(gg["prozorro"]).diff()
            gg["d_farm_gate"] = _safe_log(gg["farm_gate"]).diff()
            gg["d_eu"] = _safe_log(gg["eu_price"]).diff()
            gg["d_cme"] = _safe_log(gg["cme_price"]).diff()
            gg["lag_discount_present"] = gg["discount_present"].shift(1)
            gg["lag_markdown_rate"] = gg["markdown_rate"].shift(1)
            gg["gap_retail_producer"] = gg["log_observed"] - _safe_log(gg["producer"])
            gg["gap_retail_prozorro"] = gg["log_observed"] - _safe_log(gg["prozorro"])
            gg["deviation_from_baseline"] = gg["log_observed"] - gg["log_baseline"]
            gg["competitor_gap"] = gg["log_observed"] - _safe_log(gg["novus_price"])
            month = gg["date"].dt.month
            gg["month_sin"] = np.sin(2 * np.pi * month / 12.0)
            gg["month_cos"] = np.cos(2 * np.pi * month / 12.0)
            gg["discount_type_markdown"] = (gg["discount_type"] == "markdown").astype(float)
            gg["discount_type_bulk"] = (gg["discount_type"] == "bulk").astype(float)

            candidate_x = [
                "d_farm_gate",
                "d_producer",
                "d_prozorro",
                "d_eu",
                "d_cme",
                "gap_retail_producer",
                "gap_retail_prozorro",
                "deviation_from_baseline",
                "lag_discount_present",
                "lag_markdown_rate",
                "promo_duration",
                "time_since_last_promo",
                "competitor_gap",
                "top_brand_share",
                "month_sin",
                "month_cos",
            ]
            usable_x = [c for c in candidate_x if c in gg.columns and gg[c].notna().sum() >= 20 and gg[c].std(skipna=True) > 0]
            if not usable_x:
                continue
            X = sm.add_constant(gg[usable_x], has_constant="add")

            y_occ = (gg["discount_present"] > 0.05).astype(int)
            occ_frame = pd.concat([y_occ.rename("y"), X], axis=1).dropna()
            if len(occ_frame) >= 35 and occ_frame["y"].nunique() > 1:
                try:
                    fit_occ = sm.Logit(occ_frame["y"], occ_frame.drop(columns=["y"])).fit(disp=False)
                    incidence_rows.append(
                        {
                            "standardized_type": std,
                            "n_obs": int(len(occ_frame)),
                            "coef_d_farm_gate": float(fit_occ.params.get("d_farm_gate", np.nan)),
                            "p_d_farm_gate": float(fit_occ.pvalues.get("d_farm_gate", np.nan)),
                            "coef_d_producer": float(fit_occ.params.get("d_producer", np.nan)),
                            "p_d_producer": float(fit_occ.pvalues.get("d_producer", np.nan)),
                            "coef_d_prozorro": float(fit_occ.params.get("d_prozorro", np.nan)),
                            "p_d_prozorro": float(fit_occ.pvalues.get("d_prozorro", np.nan)),
                            "coef_lag_discount_present": float(fit_occ.params.get("lag_discount_present", np.nan)),
                            "p_lag_discount_present": float(fit_occ.pvalues.get("lag_discount_present", np.nan)),
                            "coef_gap_retail_producer": float(fit_occ.params.get("gap_retail_producer", np.nan)),
                            "p_gap_retail_producer": float(fit_occ.pvalues.get("gap_retail_producer", np.nan)),
                            "coef_gap_retail_prozorro": float(fit_occ.params.get("gap_retail_prozorro", np.nan)),
                            "p_gap_retail_prozorro": float(fit_occ.pvalues.get("gap_retail_prozorro", np.nan)),
                            "coef_deviation_from_baseline": float(fit_occ.params.get("deviation_from_baseline", np.nan)),
                            "p_deviation_from_baseline": float(fit_occ.pvalues.get("deviation_from_baseline", np.nan)),
                            "coef_competitor_gap": float(fit_occ.params.get("competitor_gap", np.nan)),
                            "p_competitor_gap": float(fit_occ.pvalues.get("competitor_gap", np.nan)),
                            "predictors_used": ",".join(usable_x),
                            "model": "logit",
                        }
                    )
                except Exception:
                    pass

        if pooled_daily is not None and (not incidence_rows or not type_rows or not depth_rows):
            pool = pooled_daily.copy().sort_values(["standardized_type", "date"])
            grp = pool.groupby("standardized_type", dropna=False)
            pool["log_observed"] = _safe_log(pool["observed_price"])
            pool["log_baseline"] = _safe_log(pool["baseline_price"])
            pool["d_producer"] = grp["producer"].transform(lambda s: _safe_log(s).diff())
            pool["d_prozorro"] = grp["prozorro"].transform(lambda s: _safe_log(s).diff())
            pool["d_farm_gate"] = grp["farm_gate"].transform(lambda s: _safe_log(s).diff())
            pool["d_eu"] = grp["eu_price"].transform(lambda s: _safe_log(s).diff())
            pool["d_cme"] = grp["cme_price"].transform(lambda s: _safe_log(s).diff())
            pool["lag_discount_present"] = grp["discount_present"].shift(1)
            pool["lag_markdown_rate"] = grp["markdown_rate"].shift(1)
            pool["gap_retail_producer"] = pool["log_observed"] - _safe_log(pool["producer"])
            pool["gap_retail_prozorro"] = pool["log_observed"] - _safe_log(pool["prozorro"])
            pool["deviation_from_baseline"] = pool["log_observed"] - pool["log_baseline"]
            pool["competitor_gap"] = pool["log_observed"] - _safe_log(pool["novus_price"])
            month = pool["date"].dt.month
            pool["month_sin"] = np.sin(2 * np.pi * month / 12.0)
            pool["month_cos"] = np.cos(2 * np.pi * month / 12.0)
            std_dummies = pd.get_dummies(pool["standardized_type"].astype(str), prefix="std", drop_first=True)
            pool = pd.concat([pool, std_dummies], axis=1)
            candidate_x = [
                "d_farm_gate",
                "d_producer",
                "d_prozorro",
                "d_eu",
                "d_cme",
                "gap_retail_producer",
                "gap_retail_prozorro",
                "deviation_from_baseline",
                "lag_discount_present",
                "lag_markdown_rate",
                "promo_duration",
                "time_since_last_promo",
                "competitor_gap",
                "top_brand_share",
                "month_sin",
                "month_cos",
            ] + std_dummies.columns.tolist()
            usable_x = [c for c in candidate_x if c in pool.columns and pool[c].notna().sum() >= 25 and pool[c].std(skipna=True) > 0]
            if usable_x:
                X = sm.add_constant(pool[usable_x], has_constant="add")
                if not incidence_rows:
                    y_occ = (pool["discount_present"] > 0.05).astype(int)
                    occ_frame = pd.concat([y_occ.rename("y"), X], axis=1).dropna()
                    if len(occ_frame) >= 35 and occ_frame["y"].nunique() > 1:
                        try:
                            fit_occ = sm.Logit(occ_frame["y"], occ_frame.drop(columns=["y"])).fit(disp=False)
                            incidence_rows.append(
                                {
                                    "standardized_type": "ALL",
                                    "model_scope": "pooled_with_type_controls",
                                    "n_obs": int(len(occ_frame)),
                                    "coef_d_farm_gate": float(fit_occ.params.get("d_farm_gate", np.nan)),
                                    "p_d_farm_gate": float(fit_occ.pvalues.get("d_farm_gate", np.nan)),
                                    "coef_d_producer": float(fit_occ.params.get("d_producer", np.nan)),
                                    "p_d_producer": float(fit_occ.pvalues.get("d_producer", np.nan)),
                                    "coef_d_prozorro": float(fit_occ.params.get("d_prozorro", np.nan)),
                                    "p_d_prozorro": float(fit_occ.pvalues.get("d_prozorro", np.nan)),
                                    "coef_gap_retail_producer": float(fit_occ.params.get("gap_retail_producer", np.nan)),
                                    "p_gap_retail_producer": float(fit_occ.pvalues.get("gap_retail_producer", np.nan)),
                                    "coef_gap_retail_prozorro": float(fit_occ.params.get("gap_retail_prozorro", np.nan)),
                                    "p_gap_retail_prozorro": float(fit_occ.pvalues.get("gap_retail_prozorro", np.nan)),
                                    "coef_deviation_from_baseline": float(fit_occ.params.get("deviation_from_baseline", np.nan)),
                                    "p_deviation_from_baseline": float(fit_occ.pvalues.get("deviation_from_baseline", np.nan)),
                                    "coef_competitor_gap": float(fit_occ.params.get("competitor_gap", np.nan)),
                                    "p_competitor_gap": float(fit_occ.pvalues.get("competitor_gap", np.nan)),
                                    "predictors_used": ",".join(usable_x),
                                    "model": "logit",
                                }
                            )
                        except Exception:
                            pass

        if not incidence_rows or not type_rows or not depth_rows:
            row_pool = silpo[
                [
                    "date",
                    "sku_id",
                    "standardized_type",
                    "brand_normalized",
                    "observed_price",
                    "baseline_price",
                    "discount_present",
                    "markdown_rate",
                    "discount_type",
                    "promo_duration",
                    "time_since_last_promo",
                ]
            ].copy()
            row_pool = row_pool.merge(prod, on=["date", "standardized_type"], how="left")
            row_pool = row_pool.merge(pz, on=["date", "standardized_type"], how="left")
            row_pool = row_pool.merge(fg, on="date", how="left")
            row_pool = row_pool.merge(eu_daily, on=["date", "standardized_type"], how="left")
            row_pool = row_pool.merge(cme_daily, on=["date", "standardized_type"], how="left")
            row_pool = row_pool.merge(nov, on=["date", "standardized_type"], how="left")
            row_pool = row_pool.sort_values(["standardized_type", "sku_id", "date"])
            up_grp = row_pool.groupby("standardized_type", dropna=False)
            sku_grp = row_pool.groupby("sku_id", dropna=False)
            row_pool["log_observed"] = _safe_log(row_pool["observed_price"])
            row_pool["log_baseline"] = _safe_log(row_pool["baseline_price"])
            row_pool["d_producer"] = up_grp["producer"].transform(lambda s: _safe_log(s).diff())
            row_pool["d_prozorro"] = up_grp["prozorro"].transform(lambda s: _safe_log(s).diff())
            row_pool["d_farm_gate"] = up_grp["farm_gate"].transform(lambda s: _safe_log(s).diff())
            row_pool["gap_retail_producer"] = row_pool["log_observed"] - _safe_log(row_pool["producer"])
            row_pool["gap_retail_prozorro"] = row_pool["log_observed"] - _safe_log(row_pool["prozorro"])
            row_pool["deviation_from_baseline"] = row_pool["log_observed"] - row_pool["log_baseline"]
            row_pool["competitor_gap"] = row_pool["log_observed"] - _safe_log(row_pool["novus_price"])
            row_pool["lag_discount_present"] = sku_grp["discount_present"].shift(1)
            row_pool["lag_markdown_rate"] = sku_grp["markdown_rate"].shift(1)
            month = row_pool["date"].dt.month
            row_pool["month_sin"] = np.sin(2 * np.pi * month / 12.0)
            row_pool["month_cos"] = np.cos(2 * np.pi * month / 12.0)
            brand_mode = (
                row_pool.groupby("standardized_type", dropna=False)["brand_normalized"]
                .agg(lambda s: s.mode().iloc[0] if not s.mode().empty else "")
                .to_dict()
            )
            row_pool["top_brand_flag"] = [
                float(str(brand) == str(brand_mode.get(std, "")))
                for std, brand in zip(row_pool["standardized_type"], row_pool["brand_normalized"])
            ]
            std_dummies = pd.get_dummies(row_pool["standardized_type"].astype(str), prefix="std", drop_first=True)
            row_pool = pd.concat([row_pool, std_dummies], axis=1)
            row_x = [
                "d_farm_gate",
                "d_producer",
                "d_prozorro",
                "gap_retail_producer",
                "gap_retail_prozorro",
                "deviation_from_baseline",
                "lag_discount_present",
                "lag_markdown_rate",
                "promo_duration",
                "time_since_last_promo",
                "competitor_gap",
                "top_brand_flag",
                "month_sin",
                "month_cos",
            ] + std_dummies.columns.tolist()
            usable_row_x = [c for c in row_x if c in row_pool.columns and row_pool[c].notna().sum() >= 50 and row_pool[c].std(skipna=True) > 0]
            if usable_row_x:
                X = sm.add_constant(row_pool[usable_row_x], has_constant="add")
                if not incidence_rows:
                    occ_frame = pd.concat([(row_pool["discount_present"] > 0.5).astype(int).rename("y"), X], axis=1).dropna()
                    if len(occ_frame) >= 100 and occ_frame["y"].nunique() > 1:
                        try:
                            fit_occ = sm.GLM(occ_frame["y"], occ_frame.drop(columns=["y"]), family=sm.families.Binomial()).fit()
                            incidence_rows.append(
                                {
                                    "standardized_type": "ALL",
                                    "model_scope": "row_level_pooled_with_type_controls",
                                    "n_obs": int(len(occ_frame)),
                                    "coef_d_farm_gate": float(fit_occ.params.get("d_farm_gate", np.nan)),
                                    "p_d_farm_gate": float(fit_occ.pvalues.get("d_farm_gate", np.nan)),
                                    "coef_d_producer": float(fit_occ.params.get("d_producer", np.nan)),
                                    "p_d_producer": float(fit_occ.pvalues.get("d_producer", np.nan)),
                                    "coef_d_prozorro": float(fit_occ.params.get("d_prozorro", np.nan)),
                                    "p_d_prozorro": float(fit_occ.pvalues.get("d_prozorro", np.nan)),
                                    "coef_gap_retail_producer": float(fit_occ.params.get("gap_retail_producer", np.nan)),
                                    "p_gap_retail_producer": float(fit_occ.pvalues.get("gap_retail_producer", np.nan)),
                                    "coef_gap_retail_prozorro": float(fit_occ.params.get("gap_retail_prozorro", np.nan)),
                                    "p_gap_retail_prozorro": float(fit_occ.pvalues.get("gap_retail_prozorro", np.nan)),
                                    "coef_deviation_from_baseline": float(fit_occ.params.get("deviation_from_baseline", np.nan)),
                                    "p_deviation_from_baseline": float(fit_occ.pvalues.get("deviation_from_baseline", np.nan)),
                                    "coef_competitor_gap": float(fit_occ.params.get("competitor_gap", np.nan)),
                                    "p_competitor_gap": float(fit_occ.pvalues.get("competitor_gap", np.nan)),
                                    "predictors_used": ",".join(usable_row_x),
                                    "model": "glm_binomial",
                                }
                            )
                        except Exception:
                            pass
                if not type_rows:
                    type_map = {"regular": 0, "markdown": 1, "bulk": 2, "unknown": 3}
                    type_frame = pd.concat([row_pool["discount_type"].map(type_map).rename("y"), X], axis=1).dropna()
                    if len(type_frame) >= 100 and type_frame["y"].nunique() > 1:
                        try:
                            fit_type = sm.MNLogit(type_frame["y"], type_frame.drop(columns=["y"])).fit(disp=False)
                            for cls, params in fit_type.params.items():
                                cls_name = {v: k for k, v in type_map.items()}.get(int(cls), str(cls))
                                type_rows.append(
                                    {
                                        "standardized_type": "ALL",
                                        "model_scope": "row_level_pooled_with_type_controls",
                                        "discount_state": cls_name,
                                        "n_obs": int(len(type_frame)),
                                        "coef_d_farm_gate": float(params.get("d_farm_gate", np.nan)),
                                        "coef_d_producer": float(params.get("d_producer", np.nan)),
                                        "coef_d_prozorro": float(params.get("d_prozorro", np.nan)),
                                        "coef_gap_retail_producer": float(params.get("gap_retail_producer", np.nan)),
                                        "coef_gap_retail_prozorro": float(params.get("gap_retail_prozorro", np.nan)),
                                        "coef_deviation_from_baseline": float(params.get("deviation_from_baseline", np.nan)),
                                        "coef_competitor_gap": float(params.get("competitor_gap", np.nan)),
                                        "predictors_used": ",".join(usable_row_x),
                                        "model": "mnlogit",
                                    }
                                )
                        except Exception:
                            pass
                if not depth_rows:
                    depth_frame = pd.concat([row_pool["markdown_rate"].rename("y"), X], axis=1)
                    depth_frame = depth_frame[depth_frame["y"] > 0.001].dropna()
                    if len(depth_frame) >= 100:
                        try:
                            fit_depth = sm.OLS(depth_frame["y"], depth_frame.drop(columns=["y"])).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
                            depth_rows.append(
                                {
                                    "standardized_type": "ALL",
                                    "model_scope": "row_level_pooled_with_type_controls",
                                    "n_obs": int(len(depth_frame)),
                                    "coef_d_farm_gate": float(fit_depth.params.get("d_farm_gate", np.nan)),
                                    "p_d_farm_gate": float(fit_depth.pvalues.get("d_farm_gate", np.nan)),
                                    "coef_d_producer": float(fit_depth.params.get("d_producer", np.nan)),
                                    "p_d_producer": float(fit_depth.pvalues.get("d_producer", np.nan)),
                                    "coef_d_prozorro": float(fit_depth.params.get("d_prozorro", np.nan)),
                                    "p_d_prozorro": float(fit_depth.pvalues.get("d_prozorro", np.nan)),
                                    "coef_gap_retail_producer": float(fit_depth.params.get("gap_retail_producer", np.nan)),
                                    "p_gap_retail_producer": float(fit_depth.pvalues.get("gap_retail_producer", np.nan)),
                                    "coef_gap_retail_prozorro": float(fit_depth.params.get("gap_retail_prozorro", np.nan)),
                                    "p_gap_retail_prozorro": float(fit_depth.pvalues.get("gap_retail_prozorro", np.nan)),
                                    "coef_deviation_from_baseline": float(fit_depth.params.get("deviation_from_baseline", np.nan)),
                                    "p_deviation_from_baseline": float(fit_depth.pvalues.get("deviation_from_baseline", np.nan)),
                                    "coef_competitor_gap": float(fit_depth.params.get("competitor_gap", np.nan)),
                                    "p_competitor_gap": float(fit_depth.pvalues.get("competitor_gap", np.nan)),
                                    "predictors_used": ",".join(usable_row_x),
                                    "r2": float(fit_depth.rsquared),
                                    "model": "ols_hac",
                                }
                            )
                        except Exception:
                            pass
                if not type_rows:
                    type_map = {"regular": 0, "markdown": 1, "bulk": 2, "unknown": 3}
                    y_type = pool["discount_type"].map(type_map)
                    type_frame = pd.concat([y_type.rename("y"), X], axis=1).dropna()
                    if len(type_frame) >= 40 and type_frame["y"].nunique() > 1:
                        try:
                            fit_type = sm.MNLogit(type_frame["y"], type_frame.drop(columns=["y"])).fit(disp=False)
                            for cls, params in fit_type.params.items():
                                cls_name = {v: k for k, v in type_map.items()}.get(int(cls), str(cls))
                                type_rows.append(
                                    {
                                        "standardized_type": "ALL",
                                        "model_scope": "pooled_with_type_controls",
                                        "discount_state": cls_name,
                                        "n_obs": int(len(type_frame)),
                                        "coef_d_farm_gate": float(params.get("d_farm_gate", np.nan)),
                                        "coef_d_producer": float(params.get("d_producer", np.nan)),
                                        "coef_d_prozorro": float(params.get("d_prozorro", np.nan)),
                                        "coef_gap_retail_producer": float(params.get("gap_retail_producer", np.nan)),
                                        "coef_gap_retail_prozorro": float(params.get("gap_retail_prozorro", np.nan)),
                                        "coef_deviation_from_baseline": float(params.get("deviation_from_baseline", np.nan)),
                                        "coef_competitor_gap": float(params.get("competitor_gap", np.nan)),
                                        "predictors_used": ",".join(usable_x),
                                        "model": "mnlogit",
                                    }
                                )
                        except Exception:
                            pass
                if not depth_rows:
                    depth_frame = pd.concat([pool["markdown_rate"].rename("y"), X], axis=1)
                    depth_frame = depth_frame[depth_frame["y"] > 0.001].dropna()
                    if len(depth_frame) >= 25:
                        try:
                            fit_depth = sm.OLS(depth_frame["y"], depth_frame.drop(columns=["y"])).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
                            depth_rows.append(
                                {
                                    "standardized_type": "ALL",
                                    "model_scope": "pooled_with_type_controls",
                                    "n_obs": int(len(depth_frame)),
                                    "coef_d_farm_gate": float(fit_depth.params.get("d_farm_gate", np.nan)),
                                    "p_d_farm_gate": float(fit_depth.pvalues.get("d_farm_gate", np.nan)),
                                    "coef_d_producer": float(fit_depth.params.get("d_producer", np.nan)),
                                    "p_d_producer": float(fit_depth.pvalues.get("d_producer", np.nan)),
                                    "coef_d_prozorro": float(fit_depth.params.get("d_prozorro", np.nan)),
                                    "p_d_prozorro": float(fit_depth.pvalues.get("d_prozorro", np.nan)),
                                    "coef_gap_retail_producer": float(fit_depth.params.get("gap_retail_producer", np.nan)),
                                    "p_gap_retail_producer": float(fit_depth.pvalues.get("gap_retail_producer", np.nan)),
                                    "coef_gap_retail_prozorro": float(fit_depth.params.get("gap_retail_prozorro", np.nan)),
                                    "p_gap_retail_prozorro": float(fit_depth.pvalues.get("gap_retail_prozorro", np.nan)),
                                    "coef_deviation_from_baseline": float(fit_depth.params.get("deviation_from_baseline", np.nan)),
                                    "p_deviation_from_baseline": float(fit_depth.pvalues.get("deviation_from_baseline", np.nan)),
                                    "coef_competitor_gap": float(fit_depth.params.get("competitor_gap", np.nan)),
                                    "p_competitor_gap": float(fit_depth.pvalues.get("competitor_gap", np.nan)),
                                    "predictors_used": ",".join(usable_x),
                                    "r2": float(fit_depth.rsquared),
                                    "model": "ols_hac",
                                }
                            )
                        except Exception:
                            pass

            type_map = {"regular": 0, "markdown": 1, "bulk": 2, "unknown": 3}
            y_type = gg["discount_type"].map(type_map)
            type_frame = pd.concat([y_type.rename("y"), X], axis=1).dropna()
            if len(type_frame) >= 40 and type_frame["y"].nunique() > 1:
                try:
                    fit_type = sm.MNLogit(type_frame["y"], type_frame.drop(columns=["y"])).fit(disp=False)
                    for cls, params in fit_type.params.items():
                        cls_name = {v: k for k, v in type_map.items()}.get(int(cls), str(cls))
                        type_rows.append(
                            {
                                "standardized_type": std,
                                "discount_state": cls_name,
                                "n_obs": int(len(type_frame)),
                                "coef_d_farm_gate": float(params.get("d_farm_gate", np.nan)),
                                "coef_d_producer": float(params.get("d_producer", np.nan)),
                                "coef_d_prozorro": float(params.get("d_prozorro", np.nan)),
                                "coef_lag_discount_present": float(params.get("lag_discount_present", np.nan)),
                                "coef_gap_retail_producer": float(params.get("gap_retail_producer", np.nan)),
                                "coef_gap_retail_prozorro": float(params.get("gap_retail_prozorro", np.nan)),
                                "coef_deviation_from_baseline": float(params.get("deviation_from_baseline", np.nan)),
                                "coef_competitor_gap": float(params.get("competitor_gap", np.nan)),
                                "predictors_used": ",".join(usable_x),
                                "model": "mnlogit",
                            }
                        )
                except Exception:
                    pass

            depth_frame = pd.concat(
                [gg["markdown_rate"].rename("y"), X],
                axis=1,
            )
            depth_frame = depth_frame[depth_frame["y"] > 0.001].dropna()
            if len(depth_frame) >= 25:
                try:
                    fit_depth = sm.OLS(depth_frame["y"], depth_frame.drop(columns=["y"])).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
                    depth_rows.append(
                        {
                            "standardized_type": std,
                            "n_obs": int(len(depth_frame)),
                            "coef_d_farm_gate": float(fit_depth.params.get("d_farm_gate", np.nan)),
                            "p_d_farm_gate": float(fit_depth.pvalues.get("d_farm_gate", np.nan)),
                            "coef_d_producer": float(fit_depth.params.get("d_producer", np.nan)),
                            "p_d_producer": float(fit_depth.pvalues.get("d_producer", np.nan)),
                            "coef_d_prozorro": float(fit_depth.params.get("d_prozorro", np.nan)),
                            "p_d_prozorro": float(fit_depth.pvalues.get("d_prozorro", np.nan)),
                            "coef_lag_discount_present": float(fit_depth.params.get("lag_discount_present", np.nan)),
                            "p_lag_discount_present": float(fit_depth.pvalues.get("lag_discount_present", np.nan)),
                            "coef_gap_retail_producer": float(fit_depth.params.get("gap_retail_producer", np.nan)),
                            "p_gap_retail_producer": float(fit_depth.pvalues.get("gap_retail_producer", np.nan)),
                            "coef_gap_retail_prozorro": float(fit_depth.params.get("gap_retail_prozorro", np.nan)),
                            "p_gap_retail_prozorro": float(fit_depth.pvalues.get("gap_retail_prozorro", np.nan)),
                            "coef_deviation_from_baseline": float(fit_depth.params.get("deviation_from_baseline", np.nan)),
                            "p_deviation_from_baseline": float(fit_depth.pvalues.get("deviation_from_baseline", np.nan)),
                            "coef_competitor_gap": float(fit_depth.params.get("competitor_gap", np.nan)),
                            "p_competitor_gap": float(fit_depth.pvalues.get("competitor_gap", np.nan)),
                            "predictors_used": ",".join(usable_x),
                            "r2": float(fit_depth.rsquared),
                            "model": "ols_hac",
                        }
                    )
                except Exception:
                    pass

    incidence_df = pd.DataFrame(incidence_rows)
    type_df = pd.DataFrame(type_rows)
    depth_df = pd.DataFrame(depth_rows)
    if incidence_df.empty:
        incidence_df = pd.DataFrame(
            [
                {
                    "standardized_type": "ALL",
                    "model_scope": "unavailable",
                    "model": "binomial_attempt_failed",
                    "unreliable_flag": 1,
                    "reason": "Promo-incidence binomial model had insufficient stable variation or failed to converge on current data.",
                }
            ]
        )
    if type_df.empty:
        type_df = pd.DataFrame(
            [
                {
                    "standardized_type": "ALL",
                    "model_scope": "unavailable",
                    "model": "multinomial_attempt_failed",
                    "unreliable_flag": 1,
                    "reason": "Promo-state multinomial model had insufficient within-panel state variation or failed to converge on current data.",
                }
            ]
        )
    if depth_df.empty:
        depth_df = pd.DataFrame(
            [
                {
                    "standardized_type": "ALL",
                    "model_scope": "unavailable",
                    "model": "depth_attempt_failed",
                    "unreliable_flag": 1,
                    "reason": "Promo-depth conditional model had insufficient positive-markdown support or failed to converge on current data.",
                }
            ]
        )

    asym_df = pd.DataFrame()
    if not cons.empty:
        sil = cons[(cons["retailer_panel"] == "Silpo") & (cons["model_family"].isin(["ARDL", "ECM", "NARDL", "VECM"]))].copy()
        obs = sil[sil["price_variant"] == "observed"].copy()
        base = sil[sil["price_variant"] == "baseline"].copy()
        merge_keys = ["segment_name", "standardized_type", "farm_gate_source", "reconstruction_variant", "chain_direction", "stage_from", "stage_to", "model_family"]
        if not obs.empty and not base.empty:
            m = obs.merge(base, on=merge_keys, suffixes=("_obs", "_base"), how="inner")
            asym_df = pd.DataFrame(
                {
                    "segment_name": m["segment_name"],
                    "standardized_type": m["standardized_type"],
                    "farm_gate_source": m["farm_gate_source"],
                    "reconstruction_variant": m["reconstruction_variant"],
                    "chain_direction": m["chain_direction"],
                    "stage_from": m["stage_from"],
                    "stage_to": m["stage_to"],
                    "model_family": m["model_family"],
                    "observed_sr_coef": m["sr_coef_obs"],
                    "baseline_sr_coef": m["sr_coef_base"],
                    "delta_sr_coef": m["sr_coef_base"] - m["sr_coef_obs"],
                    "observed_lr_coef": m["lr_coef_obs"],
                    "baseline_lr_coef": m["lr_coef_base"],
                    "delta_lr_coef": m["lr_coef_base"] - m["lr_coef_obs"],
                    "observed_ect_coef": m["ect_coef_obs"],
                    "baseline_ect_coef": m["ect_coef_base"],
                    "delta_ect_coef": m["ect_coef_base"] - m["ect_coef_obs"],
                    "same_sign_lr": pd.Series(np.sign(pd.to_numeric(m["lr_coef_obs"], errors="coerce")), index=m.index).eq(
                        pd.Series(np.sign(pd.to_numeric(m["lr_coef_base"], errors="coerce")), index=m.index)
                    ),
                    "same_sign_ect": pd.Series(np.sign(pd.to_numeric(m["ect_coef_obs"], errors="coerce")), index=m.index).eq(
                        pd.Series(np.sign(pd.to_numeric(m["ect_coef_base"], errors="coerce")), index=m.index)
                    ),
                    "pseudo_asymmetry_likely": (
                        pd.Series(np.sign(pd.to_numeric(m["lr_coef_obs"], errors="coerce")), index=m.index).ne(
                            pd.Series(np.sign(pd.to_numeric(m["lr_coef_base"], errors="coerce")), index=m.index)
                        )
                        | (pd.to_numeric(m["sr_coef_obs"], errors="coerce") - pd.to_numeric(m["sr_coef_base"], errors="coerce")).abs().gt(0.10)
                    ).astype(int),
                }
            )

    synthesis_rows: List[Dict[str, object]] = []
    if not asym_df.empty or not depth_df.empty or not cons.empty:
        faster_effective = np.nan
        if not asym_df.empty:
            faster_effective = float((asym_df["observed_ect_coef"].abs() > asym_df["baseline_ect_coef"].abs()).mean())
        reverse_core = cons[
            (cons["chain_direction"] == "reverse")
            & (cons["stage_to"] == "FarmGateUA")
            & (cons["core_finding_flag"] == 1)
        ] if not cons.empty else pd.DataFrame()
        product_core = cons[(cons["panel_level"] == "product") & (cons["core_finding_flag"] == 1)] if not cons.empty else pd.DataFrame()
        average_core = cons[(cons["panel_level"] == "average") & (cons["core_finding_flag"] == 1)] if not cons.empty else pd.DataFrame()
        brand_core = cons[
            (cons["panel_level"] == "brand")
            & (cons["model_family"].isin(["ARDL", "ECM", "NARDL", "VECM"]))
            & (cons["core_finding_flag"] == 1)
        ] if not cons.empty else pd.DataFrame()
        depth_sig_cols = [c for c in ["p_d_farm_gate", "p_d_producer", "p_d_prozorro"] if c in depth_df.columns]
        depth_reacts = depth_df[depth_df[depth_sig_cols].lt(0.10).any(axis=1)] if depth_sig_cols else pd.DataFrame()
        synthesis_rows = [
            {
                "question": "Do promotions behave like equilibrium correction?",
                "answer": "yes" if (not asym_df.empty and (asym_df["baseline_ect_coef"] < 0).mean() > 0.5) else "mixed",
                "evidence": "Baseline Silpo ECM-style coefficients are more often negative than observed-price ones.",
            },
            {
                "question": "Does pseudo-asymmetry weaken after promo control?",
                "answer": "yes" if (not asym_df.empty and asym_df["pseudo_asymmetry_likely"].mean() > 0.5) else "mixed",
                "evidence": "Observed vs baseline coefficient gaps are summarized in Asymmetry_Observed_vs_Baseline.",
            },
            {
                "question": "Do effective prices adjust faster than baseline prices?",
                "answer": "yes" if pd.notna(faster_effective) and faster_effective > 0.5 else "mixed",
                "evidence": f"share_observed_ect_faster={faster_effective:.2f}" if pd.notna(faster_effective) else "No comparable ECM rows.",
            },
            {
                "question": "Does discount depth react to upstream shocks?",
                "answer": "yes" if not depth_reacts.empty else "mixed",
                "evidence": "Promo_State_Depth stores HAC coefficients on FarmGate/Producer/ProZorro shocks.",
            },
            {
                "question": "Do retail shocks transmit materially to farm-gate prices?",
                "answer": "yes" if not reverse_core.empty else "mixed",
                "evidence": f"reverse_core_rows={len(reverse_core)}",
            },
            {
                "question": "Is the retail-to-farmgate conclusion stable across farm-gate reconstructions?",
                "answer": "yes" if (not reverse_core.empty and reverse_core["robust_across_reconstruction"].fillna(0).mean() > 0.5) else "mixed",
                "evidence": f"reverse_robust_share={float(reverse_core['robust_across_reconstruction'].fillna(0).mean()):.2f}" if not reverse_core.empty else "No reverse core rows.",
            },
            {
                "question": "Is transmission stronger for product-specific panels than for all-products averages?",
                "answer": "yes" if (len(product_core) > len(average_core)) else "mixed",
                "evidence": f"product_core_rows={len(product_core)}; average_core_rows={len(average_core)}",
            },
            {
                "question": "Do specific retailer brands show stronger or weaker transmission?",
                "answer": "yes" if not brand_core.empty else "mixed",
                "evidence": f"brand_core_rows={len(brand_core)}",
            },
        ]
    synthesis_df = pd.DataFrame(synthesis_rows)

    out_dir = common.get_output_dir("model_discounts")
    img1 = _coef_bar(
        asym_df if not asym_df.empty else pd.DataFrame([{"standardized_type": "n/a", "delta_sr_coef": np.nan}]),
        "standardized_type",
        "delta_sr_coef",
        "Observed vs Baseline Short-Run Delta",
        out_dir / "discount_delta_short_run.png",
    )
    img2 = _coef_bar(
        depth_df if not depth_df.empty else pd.DataFrame([{"standardized_type": "n/a", "coef_d_producer": np.nan}]),
        "standardized_type",
        "coef_d_producer",
        "Promo Depth Response to Producer Shock",
        out_dir / "discount_depth_producer.png",
    )

    xlsx = out_dir / "model_discounts_output.xlsx"
    common.write_tables_xlsx(
        xlsx,
        {
            "Promo_State_Incidence": incidence_df,
            "Promo_State_Type": type_df,
            "Promo_State_Depth": depth_df,
            "Asymmetry_Observed_vs_Baseline": asym_df,
            "Discount_Strategy_Synthesis": synthesis_df,
            "Silpo_Discounts_Occurrence": incidence_df,
            "Silpo_Discounts_Depth": depth_df,
            "Silpo_Transmission_PromoCtrl": asym_df,
        },
    )
    pdf = out_dir / "model_discounts_report.pdf"
    common.save_pdf_report(
        pdf,
        "RW4 Promo-State and Discount Models",
        [
            f"incidence_rows={len(incidence_df)}",
            f"type_rows={len(type_df)}",
            f"depth_rows={len(depth_df)}",
            f"asymmetry_rows={len(asym_df)}",
        ],
        {
            "Promo_State_Incidence": incidence_df,
            "Promo_State_Type": type_df,
            "Promo_State_Depth": depth_df,
            "Asymmetry_Observed_vs_Baseline": asym_df,
            "Discount_Strategy_Synthesis": synthesis_df,
        },
        [img1, img2],
    )
    common.print_block("MODEL DISCOUNTS", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"incidence rows: {len(incidence_df)}"])
    return out_dir


def run_short_chain_regional() -> Path:
    out_dir = vpt.run_primary_chain_pipeline(freq="daily")
    common.print_block(
        "MODEL SHORT/CHAIN/REGIONAL",
        [
            f"output_dir: {out_dir}",
            "RW4 primary chain applied: FarmGateUA -> ProducerUA -> ProZorro -> Retail with reverse-flow estimates and reconstruction robustness.",
        ],
    )
    return out_dir


def run_intersection_bidirectional() -> Path:
    # Secondary module only: Silpo-Novus intersection and robustness checks.
    # ConsumerUA/EU/CME are used only as optional controls/robustness variables here.
    cleaned, all_daily, *_ = _prep()
    eff = _effective_daily_prices(all_daily)
    retail_combined, _, retail_combined_method = vpt._combined_retail_panel(
        cleaned,
        include_consumer=True,
        panel_name="Retail_combined",
    )
    retail_combined_core, _, retail_combined_core_method = vpt._combined_retail_panel(
        cleaned,
        include_consumer=False,
        panel_name="Retail_combined_core",
    )
    if eff.empty:
        out_dir = common.get_output_dir("model_intersection_bidirectional")
        xlsx = out_dir / "model_intersection_bidirectional_output.xlsx"
        note = pd.DataFrame([{"note": "No daily effective series available."}])
        common.write_tables_xlsx(xlsx, {"Bidirectional_Results": note})
        return out_dir

    bidir_rows: List[Dict[str, object]] = []
    granger_rows: List[Dict[str, object]] = []
    combo_summary: List[Dict[str, object]] = []
    combo_details: List[Dict[str, object]] = []

    for (product, standardized_type), _g in eff.groupby(["product", "standardized_type"], dropna=False):
        p = _pivot_product_daily(
            eff,
            product=product,
            standardized_type=standardized_type,
            sources=["Silpo", "Novus", "ConsumerUA", "EU", "CME", "ProducerUA"],
        )
        if p.empty or not {"Silpo", "Novus"}.issubset(set(p.columns)):
            continue
        lp = np.log(p.where(p > 0))
        dlp = lp.diff()

        # Bidirectional Silpo <-> Novus only (secondary module)
        for src, tgt in [("Silpo", "Novus"), ("Novus", "Silpo")]:
            y = dlp[tgt]
            x = dlp[src]
            lag, corr = _best_lag(y, x, max_lag=30, min_obs=20)
            frame = pd.DataFrame({"y": y, "lag_y": y.shift(1), "x_lag": x.shift(lag)})
            for ctrl in ["ConsumerUA", "EU", "CME", "ProducerUA"]:
                if ctrl in dlp.columns:
                    c_lag, _ = _best_lag(y, dlp[ctrl], max_lag=30, min_obs=20)
                    frame[f"ctrl_{ctrl}_lag{c_lag}"] = dlp[ctrl].shift(c_lag)
            xcols = [c for c in frame.columns if c != "y"]
            fit, used = _safe_ols(frame["y"], frame[xcols], hac_lags=3)
            if fit is None:
                continue
            bidir_rows.append(
                {
                    "product": product,
                    "standardized_type": standardized_type,
                    "source_from": src,
                    "source_to": tgt,
                    "best_lag_days": int(lag),
                    "corr_at_best_lag": float(corr),
                    "coef": float(fit.params.get("x_lag", np.nan)),
                    "pvalue": float(fit.pvalues.get("x_lag", np.nan)),
                    "n_obs": int(len(used)),
                    "r2": float(fit.rsquared),
                    "module_role": "secondary_intersection_robustness",
                }
            )
            try:
                gc = pd.concat([dlp[tgt], dlp[src]], axis=1).dropna()
                gc.columns = ["y", "x"]
                if len(gc) >= 35:
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore", FutureWarning)
                        res = grangercausalitytests(gc[["y", "x"]], maxlag=7, verbose=False)
                    pvals = [float(res[k][0]["ssr_ftest"][1]) for k in res]
                    granger_rows.append(
                        {
                            "product": product,
                            "standardized_type": standardized_type,
                            "source_from": src,
                            "source_to": tgt,
                            "granger_min_p_1to7": float(np.nanmin(pvals)) if pvals else np.nan,
                            "granger_best_lag_1to7": int(np.nanargmin(pvals) + 1) if pvals else np.nan,
                            "n_obs": int(len(gc)),
                            "module_role": "secondary_intersection_robustness",
                        }
                    )
            except Exception:
                pass

        # Combined intersection regressions with both the anchored and strict retailer-core chains.
        combined_specs = [
            (
                "RetailCombined",
                "retail_combined_secondary_controls",
                retail_combined,
                retail_combined_method,
            ),
            (
                "RetailCombinedCore",
                "retail_combined_core_secondary_controls",
                retail_combined_core,
                retail_combined_core_method,
            ),
        ]
        for y_label, combo_model, combo_frame, combo_method in combined_specs:
            combined_prod = combo_frame[
                (combo_frame["product"] == product)
                & (combo_frame["standardized_type"] == standardized_type)
            ][["date", "retail_observed"]].drop_duplicates().rename(columns={"retail_observed": y_label})
            if combined_prod.empty:
                continue
            dlp2 = dlp.copy()
            dlp2 = dlp2.merge(combined_prod, left_index=True, right_on="date", how="left").set_index("date")
            raw_target = pd.to_numeric(dlp2[y_label], errors="coerce")
            dlp2[y_label] = np.log(raw_target.where(raw_target > 0)).diff()
            y = dlp2[y_label]
            frame = pd.DataFrame({"y": y, "lag_y": y.shift(1)})
            for src in ["Silpo", "Novus", "EU", "CME", "ProducerUA"]:
                if src not in dlp2.columns:
                    continue
                lag, _ = _best_lag(y, dlp2[src], max_lag=30, min_obs=20)
                term = f"x_{src}_lag{lag}"
                frame[term] = dlp2[src].shift(lag)
            xcols = [c for c in frame.columns if c != "y"]
            fit, used = _safe_ols(frame["y"], frame[xcols], hac_lags=3)
            if fit is None:
                continue
            row = {
                "product": product,
                "standardized_type": standardized_type,
                "combo_model": combo_model,
                "y_source": y_label,
                "n_obs": int(len(used)),
                "r2": float(fit.rsquared),
                "adj_r2": float(fit.rsquared_adj),
                "coef_lag_y": float(fit.params.get("lag_y", np.nan)),
                "combined_rule": (
                    combo_method["construction_rule"].iloc[0]
                    if not combo_method.empty and "construction_rule" in combo_method.columns
                    else f"{y_label} constructed from the RW4 combined-retail builder."
                ),
                "module_role": "secondary_intersection_robustness",
            }
            for t in xcols:
                if t == "lag_y":
                    continue
                row[f"coef_{t}"] = float(fit.params.get(t, np.nan))
                row[f"p_{t}"] = float(fit.pvalues.get(t, np.nan))
                combo_details.append(
                    {
                        "product": product,
                        "standardized_type": standardized_type,
                        "combo_model": combo_model,
                        "term": t,
                        "coef": float(fit.params.get(t, np.nan)),
                        "pvalue": float(fit.pvalues.get(t, np.nan)),
                        "tvalue": float(fit.tvalues.get(t, np.nan)),
                        "n_obs": int(len(used)),
                    }
                )
            combo_summary.append(row)

    bidir_df = pd.DataFrame(bidir_rows)
    granger_df = pd.DataFrame(granger_rows)
    combo_sum_df = pd.DataFrame(combo_summary)
    combo_det_df = pd.DataFrame(combo_details)
    corr_all = rw2.compute_correlations(all_daily)
    corr_core = corr_all[
        corr_all["source_left"].isin(["Silpo", "Novus", "ConsumerUA", "EU", "CME"])
        & corr_all["source_right"].isin(["Silpo", "Novus", "ConsumerUA", "EU", "CME"])
    ].copy() if not corr_all.empty else pd.DataFrame()

    if bidir_df.empty:
        bidir_df = pd.DataFrame([{"note": "Insufficient Silpo-Novus overlap for bidirectional regressions."}])
    if combo_sum_df.empty:
        combo_sum_df = pd.DataFrame([{"note": "Insufficient overlap for combined secondary model."}])
    if granger_df.empty:
        granger_df = pd.DataFrame([{"note": "Insufficient overlap for Silpo-Novus Granger tests."}])

    out_dir = common.get_output_dir("model_intersection_bidirectional")
    img1 = _coef_bar(
        bidir_df,
        "source_from",
        "coef",
        "Secondary: Silpo-Novus Bidirectional Coefficients",
        out_dir / "bidirectional_coef.png",
    )
    img2 = _coef_bar(
        combo_det_df if not combo_det_df.empty else combo_sum_df,
        "combo_model" if "combo_model" in (combo_det_df.columns if not combo_det_df.empty else combo_sum_df.columns) else "note",
        "coef" if "coef" in combo_det_df.columns else "coef_lag_y",
        "Secondary Intersection Combination Coefficients",
        out_dir / "intersection_combo_coef.png",
    )

    xlsx = out_dir / "model_intersection_bidirectional_output.xlsx"
    common.write_tables_xlsx(
        xlsx,
        {
            "Bidirectional_Results": bidir_df,
            "Bidirectional_Granger": granger_df,
            "Intersection_Combination_Summary": combo_sum_df,
            "Intersection_Combination_Details": combo_det_df,
            "CrossTable_Correlations": corr_core,
        },
    )
    pdf = out_dir / "model_intersection_bidirectional_report.pdf"
    common.save_pdf_report(
        pdf,
        "Secondary Intersection Module (Silpo-Novus + Controls)",
        [
            f"bidirectional_rows={len(bidir_df)}",
            f"combo_rows={len(combo_sum_df)}",
            "ConsumerUA/EU/CME are used only as secondary robustness controls in this module.",
        ],
        {
            "Bidirectional_Results": bidir_df,
            "Intersection_Combination_Summary": combo_sum_df,
            "CrossTable_Correlations": corr_core,
        },
        [img1, img2],
    )
    common.print_block(
        "MODEL INTERSECTION/BIDIRECTIONAL",
        [f"xlsx: {xlsx}", f"pdf: {pdf}", f"rows: {len(bidir_df)}"],
    )
    return out_dir


def _knn_1d_predict(train_x: np.ndarray, train_y: np.ndarray, query_x: np.ndarray, k: int = 5) -> np.ndarray:
    if train_x.size == 0 or train_y.size == 0:
        return np.full(query_x.shape, np.nan, dtype=float)
    preds = np.full(query_x.shape, np.nan, dtype=float)
    k_eff = max(1, min(k, train_x.size))
    for i, q in enumerate(query_x):
        if np.isnan(q):
            continue
        dist = np.abs(train_x - q)
        idx = np.argsort(dist)[:k_eff]
        preds[i] = float(np.nanmean(train_y[idx]))
    return preds


def _build_product_daily(eff: pd.DataFrame, product: str) -> pd.DataFrame:
    d = eff[eff["product"] == product].copy()
    if d.empty:
        return pd.DataFrame()
    p = d.pivot_table(index="date", columns="source", values="price_eff", aggfunc="mean").sort_index()
    return p


def run_forecast_knn_synthetic() -> Path:
    cleaned, all_daily, *_ = _prep()
    eff = _effective_daily_prices(all_daily)

    forecast_sum_rows: List[Dict[str, object]] = []
    forecast_pred_rows: List[Dict[str, object]] = []
    synth_rows: List[Dict[str, object]] = []
    coef_rows: List[Dict[str, object]] = []

    if not eff.empty:
        for product in sorted([p for p in eff["product"].dropna().unique() if str(p).strip()]):
            p = _build_product_daily(eff, product)
            if p.empty:
                continue
            lp = np.log(p.where(p > 0))
            dlp = lp.diff()
            for target in ["ProducerUA", "ConsumerUA"]:
                if target not in dlp.columns:
                    continue
                y = dlp[target]
                frame = pd.DataFrame({"y": y, "lag_y": y.shift(1)})
                terms: List[str] = []
                term_strength: List[Tuple[str, float]] = []
                for src in ["Silpo", "Novus", "ProZorro", "ConsumerUA", "ProducerUA"]:
                    if src == target or src not in dlp.columns:
                        continue
                    lag, corr = _best_lag(y, dlp[src], max_lag=30, min_obs=20)
                    term = f"x_{src}_lag{lag}"
                    frame[term] = dlp[src].shift(lag)
                    terms.append(term)
                    term_strength.append((term, abs(float(corr)) if pd.notna(corr) else 0.0))
                if terms:
                    terms = [t for t, _ in sorted(term_strength, key=lambda x: x[1], reverse=True)[:3]]
                model_df = frame.dropna().copy()
                if len(model_df) < 25:
                    base = pd.DataFrame({"y": y, "lag_y": y.shift(1)}).dropna()
                    if len(base) < 25:
                        continue
                    model_df = base
                    terms = []
                holdout = min(30, max(7, int(len(model_df) * 0.2)))
                train = model_df.iloc[:-holdout].copy()
                test = model_df.iloc[-holdout:].copy()
                fit, used_train = _safe_ols(train["y"], train[["lag_y"] + terms], hac_lags=3)
                if fit is None or used_train.empty:
                    continue
                x_test = sm.add_constant(test[["lag_y"] + terms], has_constant="add")
                test["pred"] = fit.predict(x_test)
                rmse = float(np.sqrt(np.mean(np.square(test["pred"] - test["y"]))))
                mae = float(np.mean(np.abs(test["pred"] - test["y"])))

                p_target = p[target].dropna()
                if p_target.empty:
                    continue
                last_date = p_target.index.max()
                future_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=30, freq="D")
                last_dlog = float(model_df["y"].iloc[-1]) if model_df["y"].notna().any() else 0.0
                const_terms = {t: float(model_df[t].iloc[-1]) for t in terms}
                future_preds = []
                for fd in future_dates:
                    xrow = {"const": 1.0, "lag_y": last_dlog}
                    xrow.update(const_terms)
                    vals = np.array([xrow.get(c, np.nan) for c in fit.params.index], dtype=float)
                    yhat = float(np.nansum(vals * fit.params.values))
                    future_preds.append({"date": fd, "product": product, "target": target, "pred_dlog": yhat})
                    last_dlog = yhat

                for idx, r in test.iterrows():
                    forecast_pred_rows.append(
                        {
                            "date": idx,
                            "product": product,
                            "target": target,
                            "actual_dlog": float(r["y"]),
                            "pred_dlog": float(r["pred"]),
                            "segment": "holdout",
                        }
                    )
                for r in future_preds:
                    rr = dict(r)
                    rr["actual_dlog"] = np.nan
                    rr["segment"] = "future_30d"
                    forecast_pred_rows.append(rr)

                row = {
                    "product": product,
                    "target": target,
                    "n_obs": int(len(model_df)),
                    "holdout_days": int(holdout),
                    "rmse_dlog": rmse,
                    "mae_dlog": mae,
                    "r2_train": float(fit.rsquared),
                }
                for t in terms:
                    row[f"coef_{t}"] = float(fit.params.get(t, np.nan))
                    row[f"p_{t}"] = float(fit.pvalues.get(t, np.nan))
                forecast_sum_rows.append(row)

    sil = cleaned["Silpo"].copy()
    nov = cleaned["Novus"].copy()
    if not sil.empty:
        sil["entity_price"] = pd.to_numeric(sil["price"], errors="coerce")
        sil["date"] = pd.to_datetime(sil["date"], errors="coerce")
    if not nov.empty:
        nov["entity_price"] = pd.to_numeric(nov["price"], errors="coerce")
        nov["date"] = pd.to_datetime(nov["date"], errors="coerce")

    start = pd.Timestamp("2025-10-21")
    end = pd.Timestamp("2026-08-01")

    if not sil.empty or not nov.empty:
        sil_min = sil[["date", "product", "brand", "entity_price"]].rename(columns={"entity_price": "silpo_price"}) if not sil.empty else pd.DataFrame()
        nov_min = nov[["date", "product", "brand", "entity_price"]].rename(columns={"entity_price": "novus_price"}) if not nov.empty else pd.DataFrame()
        keys = pd.concat(
            [
                sil_min[["product", "brand"]] if not sil_min.empty else pd.DataFrame(columns=["product", "brand"]),
                nov_min[["product", "brand"]] if not nov_min.empty else pd.DataFrame(columns=["product", "brand"]),
            ],
            ignore_index=True,
        ).drop_duplicates()

        for _, key in keys.iterrows():
            product = key["product"]
            brand = key["brand"]
            ss = sil_min[(sil_min["product"] == product) & (sil_min["brand"] == brand)] if not sil_min.empty else pd.DataFrame(columns=["date", "silpo_price"])
            nn = nov_min[(nov_min["product"] == product) & (nov_min["brand"] == brand)] if not nov_min.empty else pd.DataFrame(columns=["date", "novus_price"])
            m = ss.merge(nn, on=["date", "product", "brand"], how="outer").sort_values("date")
            if m.empty:
                continue
            m = m[(m["date"] >= start) & (m["date"] <= end)].copy()
            if m.empty:
                continue

            m["combined_overlap_avg"] = np.where(
                m["silpo_price"].notna() & m["novus_price"].notna(),
                (pd.to_numeric(m["silpo_price"], errors="coerce") + pd.to_numeric(m["novus_price"], errors="coerce")) / 2.0,
                np.nan,
            )
            m["synthetic_retail_price"] = m["combined_overlap_avg"]

            train_nov = m[m["combined_overlap_avg"].notna() & m["novus_price"].notna()][["novus_price", "combined_overlap_avg"]].dropna()
            train_sil = m[m["combined_overlap_avg"].notna() & m["silpo_price"].notna()][["silpo_price", "combined_overlap_avg"]].dropna()

            miss_nov = m["synthetic_retail_price"].isna() & m["novus_price"].notna()
            miss_sil = m["synthetic_retail_price"].isna() & m["silpo_price"].notna()
            if miss_nov.any() and len(train_nov) >= 5:
                preds = _knn_1d_predict(
                    train_nov["novus_price"].to_numpy(dtype=float),
                    train_nov["combined_overlap_avg"].to_numpy(dtype=float),
                    m.loc[miss_nov, "novus_price"].to_numpy(dtype=float),
                    k=5,
                )
                m.loc[miss_nov, "synthetic_retail_price"] = preds
            if miss_sil.any() and len(train_sil) >= 5:
                preds = _knn_1d_predict(
                    train_sil["silpo_price"].to_numpy(dtype=float),
                    train_sil["combined_overlap_avg"].to_numpy(dtype=float),
                    m.loc[miss_sil, "silpo_price"].to_numpy(dtype=float),
                    k=5,
                )
                m.loc[miss_sil, "synthetic_retail_price"] = preds

            m["source_case"] = np.select(
                [
                    m["silpo_price"].notna() & m["novus_price"].notna(),
                    m["silpo_price"].isna() & m["novus_price"].notna(),
                    m["silpo_price"].notna() & m["novus_price"].isna(),
                ],
                [
                    "both_overlap_avg",
                    "novus_only_knn",
                    "silpo_only_knn",
                ],
                default="none",
            )

            overlap = m[m["combined_overlap_avg"].notna() & m["silpo_price"].notna() & m["novus_price"].notna()].copy()
            if len(overlap) >= 8:
                fit, used = _safe_ols(
                    overlap["combined_overlap_avg"],
                    overlap[["silpo_price", "novus_price"]],
                    hac_lags=2,
                )
                if fit is not None:
                    coef_rows.append(
                        {
                            "product": product,
                            "brand": brand,
                            "n_obs_overlap": int(len(used)),
                            "coef_silpo": float(fit.params.get("silpo_price", np.nan)),
                            "coef_novus": float(fit.params.get("novus_price", np.nan)),
                            "intercept": float(fit.params.get("const", np.nan)),
                            "r2": float(fit.rsquared),
                        }
                    )
            for _, r in m.iterrows():
                synth_rows.append(
                    {
                        "date": r["date"],
                        "product": product,
                        "brand": brand,
                        "silpo_price": float(r["silpo_price"]) if pd.notna(r["silpo_price"]) else np.nan,
                        "novus_price": float(r["novus_price"]) if pd.notna(r["novus_price"]) else np.nan,
                        "combined_overlap_avg": float(r["combined_overlap_avg"]) if pd.notna(r["combined_overlap_avg"]) else np.nan,
                        "synthetic_retail_price": float(r["synthetic_retail_price"]) if pd.notna(r["synthetic_retail_price"]) else np.nan,
                        "source_case": r["source_case"],
                    }
                )

    forecast_sum_df = pd.DataFrame(forecast_sum_rows)
    forecast_pred_df = pd.DataFrame(forecast_pred_rows)
    synth_df = pd.DataFrame(synth_rows)
    coef_df = pd.DataFrame(coef_rows)

    consumer_link_df = pd.DataFrame()
    ultimate_consumer_df = pd.DataFrame()
    if not synth_df.empty and not eff.empty:
        synth_prod = synth_df.groupby(["date", "product"], as_index=False)["synthetic_retail_price"].mean()
        cons = eff[eff["source"] == "ConsumerUA"].groupby(["date", "product"], as_index=False)["price_eff"].mean()
        prod = eff[eff["source"] == "ProducerUA"].groupby(["date", "product"], as_index=False)["price_eff"].mean().rename(columns={"price_eff": "producer_price"})
        base = synth_prod.merge(cons.rename(columns={"price_eff": "consumer_price"}), on=["date", "product"], how="inner").merge(
            prod, on=["date", "product"], how="left"
        )
        rows = []
        pred_rows = []
        for product, g in base.groupby("product", dropna=False):
            gg = g.sort_values("date").copy()
            gg["dlog_consumer"] = np.log(gg["consumer_price"].where(gg["consumer_price"] > 0)).diff()
            gg["dlog_synth"] = np.log(gg["synthetic_retail_price"].where(gg["synthetic_retail_price"] > 0)).diff()
            gg["dlog_producer"] = np.log(gg["producer_price"].where(gg["producer_price"] > 0)).diff()
            m = pd.DataFrame(
                {
                    "y": gg["dlog_consumer"],
                    "lag_y": gg["dlog_consumer"].shift(1),
                    "x_synth_l1": gg["dlog_synth"].shift(1),
                    "x_prod_l1": gg["dlog_producer"].shift(1),
                }
            ).dropna()
            fit, used = _safe_ols(m["y"], m[["lag_y", "x_synth_l1", "x_prod_l1"]], hac_lags=3)
            if fit is None:
                continue
            xfull = sm.add_constant(m[["lag_y", "x_synth_l1", "x_prod_l1"]], has_constant="add")
            m["pred_dlog_consumer"] = fit.predict(xfull)
            # Build ultimate consumer price path from predicted dlog around first valid observed point.
            first_valid = gg.loc[m.index.min(), "consumer_price"] if m.index.min() in gg.index else np.nan
            if pd.notna(first_valid) and first_valid > 0:
                level = float(first_valid)
                for idx, rr in m.iterrows():
                    level = level * float(np.exp(rr["pred_dlog_consumer"]))
                    pred_rows.append(
                        {
                            "date": gg.loc[idx, "date"] if idx in gg.index else idx,
                            "product": product,
                            "ultimate_consumer_price": level,
                            "actual_consumer_price": float(gg.loc[idx, "consumer_price"]) if idx in gg.index and pd.notna(gg.loc[idx, "consumer_price"]) else np.nan,
                            "synthetic_retail_price": float(gg.loc[idx, "synthetic_retail_price"]) if idx in gg.index and pd.notna(gg.loc[idx, "synthetic_retail_price"]) else np.nan,
                        }
                    )
            rows.append(
                {
                    "product": product,
                    "n_obs": int(len(used)),
                    "coef_synth_to_consumer": float(fit.params.get("x_synth_l1", np.nan)),
                    "p_synth_to_consumer": float(fit.pvalues.get("x_synth_l1", np.nan)),
                    "coef_producer_to_consumer": float(fit.params.get("x_prod_l1", np.nan)),
                    "p_producer_to_consumer": float(fit.pvalues.get("x_prod_l1", np.nan)),
                    "r2": float(fit.rsquared),
                }
            )
        consumer_link_df = pd.DataFrame(rows)
        ultimate_consumer_df = pd.DataFrame(pred_rows)

    if forecast_sum_df.empty:
        forecast_sum_df = pd.DataFrame([{"note": "Insufficient overlap for Producer/Consumer forecast models."}])
    if forecast_pred_df.empty:
        forecast_pred_df = pd.DataFrame([{"note": "No holdout/future forecast predictions generated."}])
    if synth_df.empty:
        synth_df = pd.DataFrame([{"note": "No synthetic retail series generated for the requested period."}])
    if coef_df.empty:
        coef_df = pd.DataFrame([{"note": "No overlap to estimate brand-product influence coefficients."}])
    if consumer_link_df.empty:
        consumer_link_df = pd.DataFrame([{"note": "No synthetic->consumer linkage model estimated."}])
    if ultimate_consumer_df.empty:
        ultimate_consumer_df = pd.DataFrame([{"note": "No ultimate_consumer_price series estimated."}])

    out_dir = common.get_output_dir("model_forecast_knn")

    if "target" in forecast_pred_df.columns:
        forecast_plot_df = forecast_pred_df[forecast_pred_df["target"].isin(["ProducerUA", "ConsumerUA"])].copy()
    else:
        forecast_plot_df = pd.DataFrame()
    img1 = _line_plot(
        forecast_plot_df if not forecast_plot_df.empty else pd.DataFrame(),
        "date",
        ["pred_dlog", "actual_dlog"],
        "Producer/Consumer dlog Forecasts (holdout+future)",
        out_dir / "forecast_producer_consumer.png",
    )

    top_entity = synth_df[synth_df.get("synthetic_retail_price").notna()].copy()
    if not top_entity.empty and "product" in top_entity.columns and "brand" in top_entity.columns:
        top_entity["n"] = top_entity.groupby(["product", "brand"])["synthetic_retail_price"].transform("count")
        best = top_entity.sort_values("n", ascending=False).iloc[0]
        one = top_entity[(top_entity["product"] == best["product"]) & (top_entity["brand"] == best["brand"])].copy()
    else:
        one = pd.DataFrame()
    img2 = _line_plot(
        one,
        "date",
        ["silpo_price", "novus_price", "synthetic_retail_price"],
        "Synthetic Retail Price (Top product-brand)",
        out_dir / "synthetic_retail_top_entity.png",
    )
    img3 = _coef_bar(
        consumer_link_df,
        "product",
        "coef_synth_to_consumer",
        "Synthetic Retail -> ConsumerUA Influence",
        out_dir / "consumer_link_coef.png",
    )

    xlsx = out_dir / "model_forecast_knn_output.xlsx"
    common.write_tables_xlsx(
        xlsx,
        {
            "Forecast_Summary": forecast_sum_df,
            "Forecast_Predictions": forecast_pred_df,
            "Synthetic_Retail_Series": synth_df,
            "Synthetic_Influence_Coefficients": coef_df,
            "Synthetic_to_Consumer_Link": consumer_link_df,
            "Ultimate_Consumer_Price": ultimate_consumer_df,
        },
    )
    pdf = out_dir / "model_forecast_knn_report.pdf"
    common.save_pdf_report(
        pdf,
        "Forecast + KNN Synthetic Retail Module",
        [
            "Goal: product-first forecasts and synthetic consumer-retail bridge.",
            "Period for synthetic build: 2025-10-21 to 2026-08-01.",
            "Interpretation option: use coefficient tables for source influence, and predictions for holdout/future behavior.",
        ],
        {
            "Forecast_Summary": forecast_sum_df,
            "Synthetic_Influence_Coefficients": coef_df,
            "Synthetic_to_Consumer_Link": consumer_link_df,
            "Ultimate_Consumer_Price": ultimate_consumer_df,
        },
        [img1, img2, img3],
    )
    common.print_block(
        "MODEL FORECAST/KNN",
        [
            f"xlsx: {xlsx}",
            f"pdf: {pdf}",
            f"forecast rows: {len(forecast_sum_df)}",
            f"synthetic rows: {len(synth_df)}",
        ],
    )
    return out_dir


def run_secondary_synthetic_consumer() -> Path:
    out_dir = vpt.run_synthetic_consumer_chain(freq="daily")
    common.print_block(
        "MODEL SECONDARY SYNTHETIC CONSUMER",
        [
            f"output_dir: {out_dir}",
            "Built after primary chain models using Silpo+Novus+ConsumerUA over ProZorro coverage.",
        ],
    )
    return out_dir


if __name__ == "__main__":
    run_ardl()
    run_ecm()
    run_nardl()
    run_vecm()
    run_discounts()
    run_short_chain_regional()
    run_intersection_bidirectional()
    run_forecast_knn_synthetic()
    run_secondary_synthetic_consumer()
