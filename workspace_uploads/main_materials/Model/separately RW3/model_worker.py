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
        d["source"].isin(["ProducerUA", "ConsumerUA"]) & d["price_pchip"].notna(),
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
    _, _, _, _, model_series = _prep()
    ardl = rw2.build_ardl_summary(model_series)
    out_dir = common.get_output_dir("model_ardl")
    img = _coef_bar(ardl, "standardized_type", "short_run_coef", "ARDL Short-run Coefficients", out_dir / "ardl_short_run.png")
    xlsx = out_dir / "model_ardl_output.xlsx"
    common.write_tables_xlsx(xlsx, {"ARDL_Summary": ardl, "Model_Series": model_series})
    pdf = out_dir / "model_ardl_report.pdf"
    common.save_pdf_report(
        pdf,
        "ARDL Module",
        [
            f"rows={len(ardl)}",
            "Interpretation option: short_run_coef and long_run_coef by standardized type.",
        ],
        {"ARDL_Summary": ardl},
        [img],
    )
    common.print_block("MODEL ARDL", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"rows: {len(ardl)}"])
    return out_dir


def run_ecm() -> Path:
    _, _, _, _, model_series = _prep()
    ardl = rw2.build_ardl_summary(model_series)
    ecm = rw2.build_ecm_summary(model_series, ardl)
    out_dir = common.get_output_dir("model_ecm")
    img = _coef_bar(ecm, "standardized_type", "ect_coef", "ECM Speed of Adjustment (ECT)", out_dir / "ecm_ect.png")
    xlsx = out_dir / "model_ecm_output.xlsx"
    common.write_tables_xlsx(xlsx, {"ECM_Summary": ecm, "ARDL_Summary": ardl})
    pdf = out_dir / "model_ecm_report.pdf"
    common.save_pdf_report(
        pdf,
        "ECM Module",
        [
            f"rows={len(ecm)}",
            "Interpretation option: negative significant ECT implies convergence.",
        ],
        {"ECM_Summary": ecm},
        [img],
    )
    common.print_block("MODEL ECM", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"rows: {len(ecm)}"])
    return out_dir


def run_nardl() -> Path:
    _, _, _, _, model_series = _prep()
    nardl = rw2.build_nardl_summary(model_series)
    out_dir = common.get_output_dir("model_nardl")
    img1 = _coef_bar(nardl, "standardized_type", "short_run_coef", "NARDL Short-run Coefficients", out_dir / "nardl_short_run.png")
    img2 = _coef_bar(nardl, "standardized_type", "long_run_coef", "NARDL Long-run Asymmetry Proxy", out_dir / "nardl_long_run.png")
    xlsx = out_dir / "model_nardl_output.xlsx"
    common.write_tables_xlsx(xlsx, {"NARDL_Summary": nardl})
    pdf = out_dir / "model_nardl_report.pdf"
    common.save_pdf_report(
        pdf,
        "NARDL Module",
        [
            f"rows={len(nardl)}",
            "Interpretation option: asymmetry_short_p and asymmetry_long_p test asymmetric pass-through.",
        ],
        {"NARDL_Summary": nardl},
        [img1, img2],
    )
    common.print_block("MODEL NARDL", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"rows: {len(nardl)}"])
    return out_dir


def run_vecm() -> Path:
    _, _, _, _, model_series = _prep()
    vecm = rw2.build_vecm_summary(model_series)
    out_dir = common.get_output_dir("model_vecm")
    img = _coef_bar(vecm, "system", "adjustment_alpha_abs_mean", "VECM Adjustment Alpha (abs mean)", out_dir / "vecm_alpha.png")
    xlsx = out_dir / "model_vecm_output.xlsx"
    common.write_tables_xlsx(xlsx, {"VECM_Summary": vecm})
    pdf = out_dir / "model_vecm_report.pdf"
    common.save_pdf_report(
        pdf,
        "VECM Module",
        [
            f"rows={len(vecm)}",
            "Interpretation option: cointegration_rank>0 supports long-run system linkage.",
        ],
        {"VECM_Summary": vecm},
        [img],
    )
    common.print_block("MODEL VECM", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"rows: {len(vecm)}"])
    return out_dir


def run_discounts() -> Path:
    cleaned, all_daily, *_ = _prep()
    brand_io = rw2.build_brand_io_metrics(cleaned["Silpo"], cleaned["Novus"])
    occ, depth, trans = rw2.build_silpo_discount_modules(cleaned["Silpo"], cleaned["Novus"], all_daily, brand_io)
    out_dir = common.get_output_dir("model_discounts")
    img1 = _coef_bar(
        trans,
        "standardized_type",
        "delta_Producer",
        "Promo-Controlled Delta Producer Pass-through",
        out_dir / "discount_delta_producer.png",
    )
    img2 = _coef_bar(
        trans,
        "standardized_type",
        "delta_EU",
        "Promo-Controlled Delta EU Pass-through",
        out_dir / "discount_delta_eu.png",
    )
    xlsx = out_dir / "model_discounts_output.xlsx"
    common.write_tables_xlsx(
        xlsx,
        {
            "Silpo_Discounts_Occurrence": occ,
            "Silpo_Discounts_Depth": depth,
            "Silpo_Transmission_PromoCtrl": trans,
        },
    )
    pdf = out_dir / "model_discounts_report.pdf"
    common.save_pdf_report(
        pdf,
        "Silpo Discount Models",
        [
            f"occ_rows={len(occ)}",
            f"depth_rows={len(depth)}",
            f"trans_rows={len(trans)}",
            "Interpretation option: compare no-promo vs promo-controlled coefficients.",
        ],
        {
            "Silpo_Transmission_PromoCtrl": trans,
            "Silpo_Discounts_Occurrence": occ,
            "Silpo_Discounts_Depth": depth,
        },
        [img1, img2],
    )
    common.print_block("MODEL DISCOUNTS", [f"xlsx: {xlsx}", f"pdf: {pdf}", f"trans rows: {len(trans)}"])
    return out_dir


def run_short_chain_regional() -> Path:
    cleaned, all_daily, *_ = _prep()
    lag = rw2.build_lag_matrix_all(all_daily)
    lag_best, lag_profiles = rw2.build_lag_outputs(lag)
    short_sum, short_details = rw2.build_short_run_models(all_daily, lag_best)
    chain_sum, chain_details = rw2.build_chain_effects(all_daily, lag_best)
    pz_models, pz_matrix = rw2.build_prozorro_regional_modules(cleaned["ProZorro"], all_daily)

    out_dir = common.get_output_dir("model_short_chain_regional")
    img1 = _coef_bar(short_sum, "standardized_type", "producer_effect", "Short-run Producer Effect", out_dir / "short_run_producer_effect.png")
    img2 = _coef_bar(chain_sum, "product", "coef_retail_from_producer", "Chain: Retail from Producer", out_dir / "chain_retail_from_producer.png")
    img3 = _coef_bar(pz_models, "product", "coef_dlog_producer", "Prozorro Regional: Producer Shock Effect", out_dir / "prozorro_regional_producer_effect.png")

    xlsx = out_dir / "model_short_chain_regional_output.xlsx"
    common.write_tables_xlsx(
        xlsx,
        {
            "LagMatrix_ByProduct": lag_best,
            "LagProfiles_ByProduct": lag_profiles,
            "Models_ShortRun_Summary": short_sum,
            "ShortRun_Details": short_details,
            "Chain_Effects_Summary": chain_sum,
            "Chain_Effects_Details": chain_details,
            "Prozorro_Regional_Models": pz_models,
            "Prozorro_Regional_Effects_Matrix": pz_matrix,
        },
    )

    pdf = out_dir / "model_short_chain_regional_report.pdf"
    common.save_pdf_report(
        pdf,
        "Short-run, Chain, and Regional Modules",
        [
            f"short_run_rows={len(short_sum)}",
            f"chain_rows={len(chain_sum)}",
            f"prozorro_regional_rows={len(pz_models)}",
            "Interpretation option: compare lag-selected short-run elasticities and chain/regional differentials.",
        ],
        {
            "Models_ShortRun_Summary": short_sum,
            "Chain_Effects_Summary": chain_sum,
            "Prozorro_Regional_Models": pz_models,
        },
        [img1, img2, img3],
    )
    common.print_block("MODEL SHORT/CHAIN/REGIONAL", [f"xlsx: {xlsx}", f"pdf: {pdf}"])
    return out_dir


def run_intersection_bidirectional() -> Path:
    cleaned, all_daily, *_ = _prep()
    eff = _effective_daily_prices(all_daily)
    if eff.empty:
        out_dir = common.get_output_dir("model_intersection_bidirectional")
        xlsx = out_dir / "model_intersection_bidirectional_output.xlsx"
        note = pd.DataFrame([{"note": "No daily effective series available."}])
        common.write_tables_xlsx(xlsx, {"Bidirectional_Results": note})
        return out_dir

    pairs = [
        ("ProducerUA", "ProZorro"),
        ("ProducerUA", "Silpo"),
        ("ProducerUA", "Novus"),
        ("ProducerUA", "ConsumerUA"),
        ("ProZorro", "Silpo"),
        ("ProZorro", "Novus"),
        ("Silpo", "ConsumerUA"),
        ("Novus", "ConsumerUA"),
        ("Silpo", "Novus"),
    ]

    bidir_rows: List[Dict[str, object]] = []
    granger_rows: List[Dict[str, object]] = []
    combo_summary: List[Dict[str, object]] = []
    combo_details: List[Dict[str, object]] = []

    for (product, standardized_type), _g in eff.groupby(["product", "standardized_type"], dropna=False):
        p = _pivot_product_daily(
            eff,
            product=product,
            standardized_type=standardized_type,
            sources=["ProducerUA", "ConsumerUA", "ProZorro", "Silpo", "Novus"],
        )
        if p.empty:
            continue
        lp = np.log(p.where(p > 0))
        dlp = lp.diff()

        for left, right in pairs:
            if left not in dlp.columns or right not in dlp.columns:
                continue
            for src, tgt in [(left, right), (right, left)]:
                y = dlp[tgt]
                x = dlp[src]
                lag, corr = _best_lag(y, x, max_lag=30, min_obs=20)
                frame = pd.DataFrame(
                    {
                        "y": y,
                        "lag_y": y.shift(1),
                        "x_lag": x.shift(lag),
                    }
                )
                fit, used = _safe_ols(frame["y"], frame[["lag_y", "x_lag"]], hac_lags=3)
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
                        "lag_y_coef": float(fit.params.get("lag_y", np.nan)),
                        "n_obs": int(len(used)),
                        "r2": float(fit.rsquared),
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
                            }
                        )
                except Exception:
                    pass

        combo_defs = {
            "silpo_only": ("Silpo", ["ProducerUA", "ProZorro", "ConsumerUA"]),
            "novus_only": ("Novus", ["ProducerUA", "ProZorro", "ConsumerUA"]),
            "silpo_novus_intersection": ("RetailCombined", ["ProducerUA", "ProZorro", "ConsumerUA", "Silpo", "Novus"]),
        }
        retail_combined = p[["Silpo", "Novus"]].mean(axis=1) if {"Silpo", "Novus"}.intersection(set(p.columns)) else pd.Series(dtype=float)
        dlp2 = dlp.copy()
        if not retail_combined.empty:
            dlp2["RetailCombined"] = np.log(retail_combined.where(retail_combined > 0)).diff()

        for combo_name, (y_source, x_sources) in combo_defs.items():
            if y_source not in dlp2.columns:
                continue
            y = dlp2[y_source]
            frame = pd.DataFrame({"y": y, "lag_y": y.shift(1)})
            used_terms: List[str] = []
            for xs in x_sources:
                if xs not in dlp2.columns:
                    continue
                lag, _corr = _best_lag(y, dlp2[xs], max_lag=30, min_obs=20)
                cname = f"x_{xs}_lag{lag}"
                frame[cname] = dlp2[xs].shift(lag)
                used_terms.append(cname)
            if not used_terms:
                continue
            fit, used = _safe_ols(frame["y"], frame[["lag_y"] + used_terms], hac_lags=3)
            if fit is None:
                continue
            row = {
                "product": product,
                "standardized_type": standardized_type,
                "combo_model": combo_name,
                "y_source": y_source,
                "n_obs": int(len(used)),
                "r2": float(fit.rsquared),
                "adj_r2": float(fit.rsquared_adj),
                "coef_lag_y": float(fit.params.get("lag_y", np.nan)),
            }
            for t in used_terms:
                row[f"coef_{t}"] = float(fit.params.get(t, np.nan))
                row[f"p_{t}"] = float(fit.pvalues.get(t, np.nan))
                combo_details.append(
                    {
                        "product": product,
                        "standardized_type": standardized_type,
                        "combo_model": combo_name,
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
        corr_all["source_left"].isin(["ProducerUA", "ProZorro", "Silpo", "Novus", "ConsumerUA"])
        & corr_all["source_right"].isin(["ProducerUA", "ProZorro", "Silpo", "Novus", "ConsumerUA"])
    ].copy() if not corr_all.empty else pd.DataFrame()

    if bidir_df.empty:
        bidir_df = pd.DataFrame([{"note": "Insufficient overlap for bidirectional regressions."}])
    if combo_sum_df.empty:
        combo_sum_df = pd.DataFrame([{"note": "Insufficient overlap for combination intersection models."}])
    if granger_df.empty:
        granger_df = pd.DataFrame([{"note": "Insufficient overlap for Granger tests."}])

    out_dir = common.get_output_dir("model_intersection_bidirectional")
    img1 = _coef_bar(
        bidir_df,
        "source_from",
        "coef",
        "Bidirectional Influence Coefficients",
        out_dir / "bidirectional_coef.png",
    )
    img2 = _coef_bar(
        combo_det_df if not combo_det_df.empty else combo_sum_df,
        "combo_model" if "combo_model" in (combo_det_df.columns if not combo_det_df.empty else combo_sum_df.columns) else "note",
        "coef" if "coef" in combo_det_df.columns else "coef_lag_y",
        "Intersection Combination Coefficients",
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
        "Intersection Bidirectional VPT Module",
        [
            f"bidirectional_rows={len(bidir_df)}",
            f"combo_rows={len(combo_sum_df)}",
            "Interpretation option: coefficient signs/magnitudes and granger_min_p_1to7 for both directions by product.",
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
    if not synth_df.empty and not eff.empty:
        synth_prod = synth_df.groupby(["date", "product"], as_index=False)["synthetic_retail_price"].mean()
        cons = eff[eff["source"] == "ConsumerUA"].groupby(["date", "product"], as_index=False)["price_eff"].mean()
        prod = eff[eff["source"] == "ProducerUA"].groupby(["date", "product"], as_index=False)["price_eff"].mean().rename(columns={"price_eff": "producer_price"})
        base = synth_prod.merge(cons.rename(columns={"price_eff": "consumer_price"}), on=["date", "product"], how="inner").merge(
            prod, on=["date", "product"], how="left"
        )
        rows = []
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


if __name__ == "__main__":
    run_ardl()
    run_ecm()
    run_nardl()
    run_vecm()
    run_discounts()
    run_short_chain_regional()
    run_intersection_bidirectional()
    run_forecast_knn_synthetic()
