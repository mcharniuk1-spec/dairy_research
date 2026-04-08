#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch
from statsmodels.stats.stattools import jarque_bera
from statsmodels.tsa.ardl import UECM, ardl_select_order
from statsmodels.tsa.stattools import adfuller, coint, kpss
from statsmodels.tsa.vector_ar.vecm import VECM, select_coint_rank, select_order

import common
import rw4_data


FARM_GATE_SOURCE_MAP = {
    "initial": "FarmGateUA_initial",
    "all_missing_filled": "FarmGateUA_filled",
}
RECONSTRUCTION_VARIANTS = ["linear", "pchip"]
RETAIL_CONFIGS = [
    {"retailer_panel": "Silpo", "source": "Silpo", "price_variant": "observed", "value_col": "observed_price"},
    {"retailer_panel": "Silpo", "source": "Silpo", "price_variant": "baseline", "value_col": "baseline_price"},
    {"retailer_panel": "Novus", "source": "Novus", "price_variant": "observed", "value_col": "observed_price"},
    {"retailer_panel": "Retail_combined", "source": "RetailCombined", "price_variant": "observed", "value_col": "retail_observed"},
    {"retailer_panel": "Retail_combined", "source": "RetailCombined", "price_variant": "baseline", "value_col": "retail_baseline"},
    {"retailer_panel": "Retail_combined_core", "source": "RetailCombinedCore", "price_variant": "observed", "value_col": "retail_observed"},
    {"retailer_panel": "Retail_combined_core", "source": "RetailCombinedCore", "price_variant": "baseline", "value_col": "retail_baseline"},
]
PRIMARY_CHAIN_DOC = (
    "RW4 domestic vertical chain is FarmGateUA -> ProducerUA -> ProZorro -> Retail, "
    "estimated with both forward and reverse-flow pairs. Farm-gate enters from two alternative "
    "reconstruction workbooks and both linear/pchip interpolation variants are carried end-to-end. "
    "Retail_combined is the anchored downstream index built from Silpo effective prices, Novus observed prices, "
    "and a level-aligned ConsumerUA anchor, while Retail_combined_core keeps the strict retailer-only overlap for robustness."
)
MIN_STABLE_PRODUCT_DAYS = 30
MIN_BRAND_DAYS = {"Silpo": 45, "Novus": 5}
COMBINED_RETAIL_BASE_WEIGHTS = {"Silpo": 1.00, "Novus": 0.90, "ConsumerUA": 0.75}
COMBINED_RETAIL_MIN_BIAS_DAYS = 10
PREFERRED_MODEL_FAMILIES = ["ARDL", "ECM", "NARDL", "VECM"]


@dataclass
class FitResult:
    family: str
    link: str
    y_series: str
    x_series: str
    n_obs: int
    sr_coef: float
    lr_coef: float
    ect_coef: float
    ect_pvalue: float
    asym_short_p: float
    asym_long_p: float
    vecm_rank: float
    model_status: str
    unreliable: int
    notes: str
    residuals: Optional[pd.Series] = None


def _safe_log(s: pd.Series) -> pd.Series:
    x = pd.to_numeric(s, errors="coerce")
    return np.log(x.where(x > 0))


def _weekly(series_df: pd.DataFrame, value_cols: List[str], date_col: str = "date") -> pd.DataFrame:
    d = series_df.copy()
    d[date_col] = pd.to_datetime(d[date_col], errors="coerce")
    d = d.dropna(subset=[date_col]).sort_values(date_col)
    if d.empty:
        return pd.DataFrame(columns=[date_col] + value_cols)
    d = d.set_index(date_col)
    out = d[value_cols].resample("W-MON").median().reset_index()
    return out


def _integration_class(s: pd.Series) -> Dict[str, float]:
    def _adf(x: pd.Series) -> float:
        x = x.dropna()
        if len(x) < 24:
            return np.nan
        try:
            return float(adfuller(x, autolag="AIC")[1])
        except Exception:
            return np.nan

    def _kpss(x: pd.Series) -> float:
        x = x.dropna()
        if len(x) < 24:
            return np.nan
        try:
            return float(kpss(x, regression="c", nlags="auto")[1])
        except Exception:
            return np.nan

    s0 = pd.to_numeric(s, errors="coerce")
    s1 = s0.diff()
    s2 = s1.diff()
    adf0, kpss0 = _adf(s0), _kpss(s0)
    adf1, kpss1 = _adf(s1), _kpss(s1)
    adf2, kpss2 = _adf(s2), _kpss(s2)

    if pd.notna(adf0) and pd.notna(kpss0) and adf0 < 0.05 and kpss0 > 0.05:
        cls = "I(0)"
    elif pd.notna(adf1) and pd.notna(kpss1) and adf1 < 0.05 and kpss1 > 0.05:
        cls = "I(1)"
    elif pd.notna(adf2) and pd.notna(kpss2) and adf2 < 0.05 and kpss2 > 0.05:
        cls = "I(2)"
    else:
        cls = "ambiguous"

    stability_flag = 0
    x = s0.dropna()
    if len(x) >= 40:
        mid = len(x) // 2
        a, b = x.iloc[:mid], x.iloc[mid:]
        denom = float(x.std(ddof=1)) if len(x) > 1 else np.nan
        if pd.notna(denom) and denom > 0:
            stability_flag = int(abs(float(a.mean() - b.mean())) / denom > 0.75)

    return {
        "adf_level_p": adf0,
        "kpss_level_p": kpss0,
        "adf_diff1_p": adf1,
        "kpss_diff1_p": kpss1,
        "adf_diff2_p": adf2,
        "kpss_diff2_p": kpss2,
        "integration_class": cls,
        "stability_flag": stability_flag,
    }


def _resid_diag(resid: pd.Series) -> Dict[str, float]:
    r = pd.to_numeric(resid, errors="coerce").dropna()
    if len(r) < 20:
        return {
            "ljungbox_p": np.nan,
            "arch_p": np.nan,
            "jb_p": np.nan,
            "unreliable_flag": 1,
        }
    try:
        lb = float(acorr_ljungbox(r, lags=[min(10, max(2, len(r) // 5))], return_df=True)["lb_pvalue"].iloc[0])
    except Exception:
        lb = np.nan
    try:
        arch = float(het_arch(r)[1])
    except Exception:
        arch = np.nan
    try:
        jb = float(jarque_bera(r)[1])
    except Exception:
        jb = np.nan
    bad = int((pd.notna(lb) and lb < 0.05) or (pd.notna(arch) and arch < 0.05))
    return {"ljungbox_p": lb, "arch_p": arch, "jb_p": jb, "unreliable_flag": bad}


def _fit_ardl_pair(log_y: pd.Series, log_x: pd.Series, max_lag: int) -> Optional[FitResult]:
    d = pd.concat([log_y.rename("y"), log_x.rename("x")], axis=1).dropna()
    if len(d) < 30:
        return None
    for lag_try in [max_lag, min(8, max_lag), min(5, max_lag), min(3, max_lag)]:
        try:
            sel = ardl_select_order(d["y"], lag_try, d[["x"]], lag_try, ic="aic", trend="c")
            ar = sel.model.fit(cov_type="HAC", cov_kwds={"maxlags": min(3, max(1, lag_try // 2))})
            phi = float(np.nansum([v for k, v in ar.params.items() if str(k).startswith("y.L")]))
            beta = float(np.nansum([v for k, v in ar.params.items() if str(k).startswith("x.L")]))
            lr = beta / (1.0 - phi) if abs(1.0 - phi) > 1e-8 else np.nan
            sr = float(ar.params.get("x.L0", np.nan))
            uecm_res = UECM.from_ardl(sel.model).fit(cov_type="HAC", cov_kwds={"maxlags": min(3, max(1, lag_try // 2))})
            bt = uecm_res.bounds_test(case=3)
            lower_p = float(bt.p_values.get("lower", np.nan))
            upper_p = float(bt.p_values.get("upper", np.nan))
            notes = f"bounds_lower_p={lower_p:.4g}; bounds_upper_p={upper_p:.4g}; max_lag_try={lag_try}"
            return FitResult(
                family="ARDL",
                link="",
                y_series="",
                x_series="",
                n_obs=int(len(d)),
                sr_coef=sr,
                lr_coef=float(lr) if pd.notna(lr) else np.nan,
                ect_coef=np.nan,
                ect_pvalue=np.nan,
                asym_short_p=np.nan,
                asym_long_p=np.nan,
                vecm_rank=np.nan,
                model_status="ok",
                unreliable=0,
                notes=notes,
                residuals=ar.resid,
            )
        except Exception:
            continue
    return None


def _fit_ecm_pair(log_y: pd.Series, log_x: pd.Series, max_lag: int) -> Optional[FitResult]:
    d = pd.concat([log_y.rename("y"), log_x.rename("x")], axis=1).dropna()
    if len(d) < 32:
        return None
    try:
        coint_p = float(coint(d["y"], d["x"])[1])
    except Exception:
        return None
    if not (pd.notna(coint_p) and coint_p < 0.10):
        return None
    try:
        lr = sm.OLS(d["y"], sm.add_constant(d[["x"]], has_constant="add")).fit()
        d["ect_l1"] = lr.resid.shift(1)
        d["dy"] = d["y"].diff()
        d["dx"] = d["x"].diff()
        best = None
        max_l = min(max_lag, 6)
        for p in range(1, max_l + 1):
            for q in range(0, max_l + 1):
                t = d[["dy", "dx", "ect_l1"]].copy()
                for i in range(1, p + 1):
                    t[f"dy_l{i}"] = t["dy"].shift(i)
                for j in range(0, q + 1):
                    t[f"dx_l{j}"] = t["dx"].shift(j)
                t = t.dropna()
                if len(t) < 35:
                    continue
                exog_cols = [c for c in t.columns if c != "dy"]
                fit = sm.OLS(t["dy"], sm.add_constant(t[exog_cols], has_constant="add")).fit()
                if best is None or fit.aic < best["aic"]:
                    best = {"fit": fit, "table": t, "p": p, "q": q}
                    best["aic"] = float(fit.aic)
        if best is None:
            return None
        fit_hac = sm.OLS(best["table"]["dy"], sm.add_constant(best["table"].drop(columns=["dy"]), has_constant="add")).fit(
            cov_type="HAC",
            cov_kwds={"maxlags": min(3, max(1, max_lag // 2))},
        )
        return FitResult(
            family="ECM",
            link="",
            y_series="",
            x_series="",
            n_obs=int(len(best["table"])),
            sr_coef=float(fit_hac.params.get("dx_l0", np.nan)),
            lr_coef=float(lr.params.get("x", np.nan)),
            ect_coef=float(fit_hac.params.get("ect_l1", np.nan)),
            ect_pvalue=float(fit_hac.pvalues.get("ect_l1", np.nan)),
            asym_short_p=np.nan,
            asym_long_p=np.nan,
            vecm_rank=np.nan,
            model_status="ok",
            unreliable=0,
            notes=f"engle_granger_p={coint_p:.4g}; lags p={best['p']} q={best['q']}",
            residuals=fit_hac.resid,
        )
    except Exception:
        return None


def _fit_nardl_pair(log_y: pd.Series, log_x: pd.Series, max_lag: int) -> Optional[Tuple[FitResult, pd.DataFrame]]:
    d = pd.concat([log_y.rename("y"), log_x.rename("x")], axis=1).dropna()
    if len(d) < 35:
        return None
    d["dx"] = d["x"].diff()
    d["x_pos"] = d["dx"].clip(lower=0).cumsum()
    d["x_neg"] = d["dx"].clip(upper=0).abs().cumsum()
    d["dy"] = d["y"].diff()
    d["dy_l1"] = d["dy"].shift(1)
    d["dx_pos"] = d["dx"].clip(lower=0)
    d["dx_neg"] = d["dx"].clip(upper=0).abs()
    d["y_l1"] = d["y"].shift(1)
    d["x_pos_l1"] = d["x_pos"].shift(1)
    d["x_neg_l1"] = d["x_neg"].shift(1)
    t = d[["dy", "dy_l1", "dx_pos", "dx_neg", "y_l1", "x_pos_l1", "x_neg_l1"]].dropna()
    if len(t) < 35:
        return None
    fit = sm.OLS(t["dy"], sm.add_constant(t.drop(columns=["dy"]), has_constant="add")).fit(
        cov_type="HAC",
        cov_kwds={"maxlags": min(3, max(1, max_lag // 2))},
    )
    lam = float(fit.params.get("y_l1", np.nan))
    psi_p = float(fit.params.get("x_pos_l1", np.nan))
    psi_n = float(fit.params.get("x_neg_l1", np.nan))
    lr_pos = -psi_p / lam if pd.notna(lam) and abs(lam) > 1e-8 else np.nan
    lr_neg = -psi_n / lam if pd.notna(lam) and abs(lam) > 1e-8 else np.nan
    try:
        w_short = float(fit.f_test("dx_pos = dx_neg").pvalue)
    except Exception:
        w_short = np.nan
    try:
        w_long = float(fit.f_test("x_pos_l1 = x_neg_l1").pvalue)
    except Exception:
        w_long = np.nan

    horizon = np.arange(0, 21)
    phi = float(fit.params.get("dy_l1", 0.0))
    th_pos = float(fit.params.get("dx_pos", 0.0))
    th_neg = float(fit.params.get("dx_neg", 0.0))
    m_pos: List[float] = []
    m_neg: List[float] = []
    cur_pos = 0.0
    cur_neg = 0.0
    for _ in horizon:
        cur_pos = phi * cur_pos + th_pos
        cur_neg = phi * cur_neg + th_neg
        m_pos.append(cur_pos)
        m_neg.append(cur_neg)
    multipliers = pd.DataFrame({"horizon": horizon, "mult_pos": m_pos, "mult_neg": m_neg})

    return (
        FitResult(
            family="NARDL",
            link="",
            y_series="",
            x_series="",
            n_obs=int(len(t)),
            sr_coef=th_pos - th_neg,
            lr_coef=lr_pos - lr_neg if pd.notna(lr_pos) and pd.notna(lr_neg) else np.nan,
            ect_coef=lam,
            ect_pvalue=float(fit.pvalues.get("y_l1", np.nan)),
            asym_short_p=w_short,
            asym_long_p=w_long,
            vecm_rank=np.nan,
            model_status="ok",
            unreliable=0,
            notes="Wald short/long asymmetry reported; dynamic multipliers saved.",
            residuals=fit.resid,
        ),
        multipliers,
    )


def _fit_vecm_system(
    log_panel: pd.DataFrame,
    max_lag: int,
    link_name: str,
    target_name: Optional[str] = None,
) -> Optional[Tuple[FitResult, pd.DataFrame]]:
    d = log_panel.dropna()
    if len(d) < 36 or d.shape[1] < 3:
        return None
    try:
        max_l = min(max_lag, 6)
        sel = select_order(d, maxlags=max_l, deterministic="ci")
        ka = sel.aic if sel.aic is not None else 2
        k_diff = max(1, int(ka) - 1)
        rank = int(select_coint_rank(d, det_order=0, k_ar_diff=k_diff, signif=0.05).rank)
        if rank < 1:
            return None
        fit = VECM(d, k_ar_diff=k_diff, coint_rank=rank, deterministic="ci").fit()
        target_name = target_name or d.columns[-1]
        target_idx = list(d.columns).index(target_name)
        ect = float(fit.alpha[target_idx, 0]) if fit.alpha.shape[0] > target_idx else np.nan
        resid = pd.DataFrame(fit.resid, index=d.index[k_diff + 1 :], columns=d.columns).get(target_name)
        irf = fit.irf(12).irfs
        irf_rows = []
        names = list(d.columns)
        i_y = target_idx
        for h in range(irf.shape[0]):
            row = {"horizon": h}
            for nm in names:
                if nm == target_name:
                    continue
                row[f"irf_{target_name}_to_{nm}"] = float(irf[h, i_y, names.index(nm)])
            irf_rows.append(row)
        return (
            FitResult(
                family="VECM",
                link=link_name,
                y_series=target_name,
                x_series="+".join(names[:-1]),
                n_obs=int(len(d)),
                sr_coef=np.nan,
                lr_coef=np.nan,
                ect_coef=ect,
                ect_pvalue=np.nan,
                asym_short_p=np.nan,
                asym_long_p=np.nan,
                vecm_rank=float(rank),
                model_status="ok",
                unreliable=0,
                notes=f"k_ar_diff={k_diff}",
                residuals=resid,
            ),
            pd.DataFrame(irf_rows),
        )
    except Exception:
        return None


def _sign(v: object) -> float:
    x = pd.to_numeric(v, errors="coerce")
    if pd.isna(x) or float(x) == 0.0:
        return np.nan
    return float(np.sign(x))


def _national_rows(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty or "region" not in df.columns:
        return df
    reg = df["region"].astype(str).str.lower()
    nat = df[reg.isin(["україна", "ukraine"])].copy()
    return nat if not nat.empty else df


def _median_by_day(df: pd.DataFrame, value_col: str, extra_cols: List[str]) -> pd.DataFrame:
    use = df.copy()
    use["date"] = pd.to_datetime(use["date"], errors="coerce")
    use[value_col] = pd.to_numeric(use[value_col], errors="coerce")
    use = use.dropna(subset=["date", value_col])
    if use.empty:
        return pd.DataFrame(columns=["date"] + extra_cols + [value_col])
    return use.groupby(["date"] + extra_cols, as_index=False)[value_col].median()


def _first_series(df: pd.DataFrame, col: str) -> pd.Series:
    hit = df.loc[:, [c for c in df.columns if c == col]]
    if hit.empty:
        return pd.Series(np.nan, index=df.index, dtype=float)
    return hit.iloc[:, 0]


def _retail_daily_controls(cleaned: Dict[str, pd.DataFrame], source: str) -> pd.DataFrame:
    df = cleaned[source].copy()
    df = _national_rows(df)
    df = df[pd.to_numeric(df.get("admissible_for_level_model"), errors="coerce").fillna(0).eq(1)].copy()
    if df.empty:
        return pd.DataFrame()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["retail_observed"] = pd.to_numeric(df.get("observed_price"), errors="coerce")
    df["retail_baseline"] = pd.to_numeric(df.get("baseline_price"), errors="coerce")
    df["discount_present"] = pd.to_numeric(df.get("discount_present"), errors="coerce").fillna(0)
    df["markdown_rate"] = pd.to_numeric(df.get("markdown_rate"), errors="coerce").fillna(0)
    df["promo_duration"] = pd.to_numeric(df.get("promo_duration"), errors="coerce")
    df["time_since_last_promo"] = pd.to_numeric(df.get("time_since_last_promo"), errors="coerce")
    df["discount_type"] = df.get("discount_type", "unknown").astype(str)
    df["brand_normalized"] = df.get("brand_normalized", df.get("brand", "")).astype(str)
    keys = ["date", "product", "standardized_type"]
    agg = (
        df.groupby(keys, as_index=False)
        .agg(
            retail_observed=("retail_observed", "median"),
            retail_baseline=("retail_baseline", "median"),
            discount_present=("discount_present", "mean"),
            markdown_rate=("markdown_rate", "mean"),
            promo_duration=("promo_duration", "mean"),
            time_since_last_promo=("time_since_last_promo", "mean"),
            discount_type_markdown=("discount_type", lambda s: float((s.astype(str) == "markdown").mean())),
            discount_type_bulk=("discount_type", lambda s: float((s.astype(str) == "bulk").mean())),
            top_brand_share=("brand_normalized", lambda s: float(s.astype(str).value_counts(normalize=True, dropna=False).iloc[0]) if len(s) else np.nan),
        )
    )
    return agg


def _retail_source_frame(cleaned: Dict[str, pd.DataFrame], source: str) -> pd.DataFrame:
    if source == "ConsumerUA":
        cons = _benchmark_series(cleaned, "ConsumerUA")
        if cons.empty:
            return pd.DataFrame(columns=["date", "product", "standardized_type", "consumer_price"])
        return cons.rename(columns={"ConsumerUA": "consumer_price"})

    retail = _retail_daily_controls(cleaned, source)
    if retail.empty:
        return retail
    keep_cols = [
        "date",
        "product",
        "standardized_type",
        "retail_observed",
        "retail_baseline",
        "discount_present",
        "markdown_rate",
        "promo_duration",
        "time_since_last_promo",
        "discount_type_markdown",
        "discount_type_bulk",
        "top_brand_share",
    ]
    keep_cols = [c for c in keep_cols if c in retail.columns]
    return retail[keep_cols].copy()


def _coverage_weight_map(df: pd.DataFrame, price_col: str, base_weight: float) -> Dict[Tuple[str, str], float]:
    if df.empty or price_col not in df.columns:
        return {}
    work = df.copy()
    work[price_col] = pd.to_numeric(work[price_col], errors="coerce")
    rows: Dict[Tuple[str, str], float] = {}
    for (product, standardized_type), grp in work.groupby(["product", "standardized_type"], dropna=False):
        total_days = float(max(grp["date"].nunique(), 1))
        present_days = float(grp.loc[grp[price_col].notna(), "date"].nunique())
        coverage = present_days / total_days
        rows[(product, standardized_type)] = base_weight * (0.40 + 0.60 * coverage)
    return rows


def _build_combined_retail_panel(
    cleaned: Dict[str, pd.DataFrame],
    include_consumer: bool = True,
    panel_name: str = "Retail_combined",
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    sil = _retail_source_frame(cleaned, "Silpo").rename(
        columns={
            "retail_observed": "silpo_observed",
            "retail_baseline": "silpo_baseline",
            "discount_present": "silpo_discount_present",
            "markdown_rate": "silpo_markdown_rate",
            "promo_duration": "silpo_promo_duration",
            "time_since_last_promo": "silpo_time_since_last_promo",
            "discount_type_markdown": "silpo_discount_type_markdown",
            "discount_type_bulk": "silpo_discount_type_bulk",
            "top_brand_share": "silpo_top_brand_share",
        }
    )
    nov = _retail_source_frame(cleaned, "Novus").rename(
        columns={
            "retail_observed": "novus_observed",
            "retail_baseline": "novus_baseline",
            "discount_present": "novus_discount_present",
            "markdown_rate": "novus_markdown_rate",
            "promo_duration": "novus_promo_duration",
            "time_since_last_promo": "novus_time_since_last_promo",
            "discount_type_markdown": "novus_discount_type_markdown",
            "discount_type_bulk": "novus_discount_type_bulk",
            "top_brand_share": "novus_top_brand_share",
        }
    )
    cons = _retail_source_frame(cleaned, "ConsumerUA") if include_consumer else pd.DataFrame(columns=["date", "product", "standardized_type", "consumer_price"])

    frames = [df for df in [sil, nov, cons] if not df.empty]
    if not frames:
        empty = pd.DataFrame(columns=["date", "product", "standardized_type", "retail", "retail_observed", "retail_baseline", "retailer_panel", "price_variant"])
        return empty, pd.DataFrame(), pd.DataFrame()

    merged = frames[0].copy()
    for frame in frames[1:]:
        merged = merged.merge(frame, on=["date", "product", "standardized_type"], how="outer")
    if merged.empty:
        empty = pd.DataFrame(columns=["date", "product", "standardized_type", "retail", "retail_observed", "retail_baseline", "retailer_panel", "price_variant"])
        return empty, pd.DataFrame(), pd.DataFrame()

    merged["date"] = pd.to_datetime(merged["date"], errors="coerce")
    merged = merged.dropna(subset=["date"]).sort_values(["product", "standardized_type", "date"]).copy()
    source_cols = ["silpo_observed", "novus_observed"] + (["consumer_price"] if include_consumer else [])
    for col in source_cols + ["silpo_baseline"]:
        if col in merged.columns:
            merged[col] = pd.to_numeric(merged[col], errors="coerce")

    merged["source_count"] = merged[source_cols].notna().sum(axis=1)
    log_cols = []
    for col in source_cols:
        log_col = f"log_{col}"
        merged[log_col] = _safe_log(merged[col])
        log_cols.append(log_col)
    merged["log_source_median"] = merged[log_cols].median(axis=1, skipna=True)

    std_bias_records: List[Dict[str, object]] = []
    product_bias_lookup: Dict[Tuple[str, str, str], float] = {}
    product_bias_n: Dict[Tuple[str, str, str], int] = {}
    for source_name, log_col in [("Silpo", "log_silpo_observed"), ("Novus", "log_novus_observed")] + ([("ConsumerUA", "log_consumer_price")] if include_consumer else []):
        valid = merged[(merged["source_count"] >= 2) & merged[log_col].notna() & merged["log_source_median"].notna()].copy()
        if not valid.empty:
            valid["bias_component"] = valid[log_col] - valid["log_source_median"]
            for (product, standardized_type), grp in valid.groupby(["product", "standardized_type"], dropna=False):
                key = (source_name, product, standardized_type)
                product_bias_lookup[key] = float(grp["bias_component"].median())
                product_bias_n[key] = int(len(grp))
            for standardized_type, grp in valid.groupby("standardized_type", dropna=False):
                std_bias_records.append(
                    {
                        "source": source_name,
                        "standardized_type": standardized_type,
                        "bias_log": float(grp["bias_component"].median()),
                        "n_overlap_days": int(len(grp)),
                    }
                )
    std_bias_df = pd.DataFrame(std_bias_records)
    std_bias_lookup = {
        (str(r["source"]), str(r["standardized_type"])): float(r["bias_log"])
        for _, r in std_bias_df.iterrows()
    } if not std_bias_df.empty else {}

    diag_rows: List[Dict[str, object]] = []
    out_rows: List[Dict[str, object]] = []
    for (product, standardized_type), grp in merged.groupby(["product", "standardized_type"], dropna=False):
        sil_bias = product_bias_lookup.get(("Silpo", product, standardized_type), np.nan)
        nov_bias = product_bias_lookup.get(("Novus", product, standardized_type), np.nan)
        cons_bias = product_bias_lookup.get(("ConsumerUA", product, standardized_type), np.nan) if include_consumer else np.nan
        sil_bias_n = product_bias_n.get(("Silpo", product, standardized_type), 0)
        nov_bias_n = product_bias_n.get(("Novus", product, standardized_type), 0)
        cons_bias_n = product_bias_n.get(("ConsumerUA", product, standardized_type), 0) if include_consumer else 0

        if not pd.notna(sil_bias) or sil_bias_n < COMBINED_RETAIL_MIN_BIAS_DAYS:
            sil_bias = std_bias_lookup.get(("Silpo", str(standardized_type)), 0.0)
        if not pd.notna(nov_bias) or nov_bias_n < COMBINED_RETAIL_MIN_BIAS_DAYS:
            nov_bias = std_bias_lookup.get(("Novus", str(standardized_type)), 0.0)
        if include_consumer and (not pd.notna(cons_bias) or cons_bias_n < COMBINED_RETAIL_MIN_BIAS_DAYS):
            cons_bias = std_bias_lookup.get(("ConsumerUA", str(standardized_type)), 0.0)

        n_days = float(max(len(grp), 1))
        sil_present = float(grp["silpo_observed"].notna().sum()) if "silpo_observed" in grp.columns else 0.0
        nov_present = float(grp["novus_observed"].notna().sum()) if "novus_observed" in grp.columns else 0.0
        cons_present = float(grp["consumer_price"].notna().sum()) if include_consumer and "consumer_price" in grp.columns else 0.0
        sil_overlap = float(((grp["silpo_observed"].notna()) & grp["source_count"].ge(2)).sum()) if "silpo_observed" in grp.columns else 0.0
        nov_overlap = float(((grp["novus_observed"].notna()) & grp["source_count"].ge(2)).sum()) if "novus_observed" in grp.columns else 0.0
        cons_overlap = float(((grp["consumer_price"].notna()) & grp["source_count"].ge(2)).sum()) if include_consumer and "consumer_price" in grp.columns else 0.0

        def _reliability_weight(base_weight: float, present_days: float, overlap_days: float) -> float:
            if present_days <= 0:
                return 0.0
            coverage = present_days / n_days
            overlap_share = overlap_days / present_days
            return float(base_weight * (0.30 + 0.40 * coverage + 0.30 * overlap_share))

        sil_weight = _reliability_weight(COMBINED_RETAIL_BASE_WEIGHTS["Silpo"], sil_present, sil_overlap)
        nov_weight = _reliability_weight(COMBINED_RETAIL_BASE_WEIGHTS["Novus"], nov_present, nov_overlap)
        cons_weight = _reliability_weight(COMBINED_RETAIL_BASE_WEIGHTS["ConsumerUA"], cons_present, cons_overlap) if include_consumer else 0.0

        diag_rows.append(
            {
                "product": product,
                "standardized_type": standardized_type,
                "bias_log_silpo": sil_bias,
                "bias_log_novus": nov_bias,
                "bias_log_consumer": cons_bias if include_consumer else np.nan,
                "bias_days_silpo": sil_bias_n,
                "bias_days_novus": nov_bias_n,
                "bias_days_consumer": cons_bias_n if include_consumer else 0,
                "weight_silpo": sil_weight,
                "weight_novus": nov_weight,
                "weight_consumer": cons_weight if include_consumer else 0.0,
                "coverage_silpo": float(grp["silpo_observed"].notna().mean()) if "silpo_observed" in grp.columns else np.nan,
                "coverage_novus": float(grp["novus_observed"].notna().mean()) if "novus_observed" in grp.columns else np.nan,
                "coverage_consumer": float(grp["consumer_price"].notna().mean()) if include_consumer and "consumer_price" in grp.columns else np.nan,
                "retailer_overlap_share": float((grp["source_count"] >= 2).mean()),
                "n_days": int(len(grp)),
                "n_days_2plus_sources": int((grp["source_count"] >= 2).sum()),
                "panel_name": panel_name,
            }
        )

        for _, row in grp.iterrows():
            obs_logs: List[float] = []
            obs_weights: List[float] = []
            baseline_logs: List[float] = []
            baseline_weights: List[float] = []
            retailer_weight_sum = 0.0
            total_weight_sum = 0.0

            if pd.notna(row.get("silpo_observed")) and row.get("silpo_observed", np.nan) > 0:
                obs_logs.append(float(np.log(row["silpo_observed"]) - sil_bias))
                obs_weights.append(float(sil_weight))
                retailer_weight_sum += float(sil_weight)
                total_weight_sum += float(sil_weight)
            if pd.notna(row.get("novus_observed")) and row.get("novus_observed", np.nan) > 0:
                obs_logs.append(float(np.log(row["novus_observed"]) - nov_bias))
                obs_weights.append(float(nov_weight))
                retailer_weight_sum += float(nov_weight)
                total_weight_sum += float(nov_weight)
            if include_consumer and pd.notna(row.get("consumer_price")) and row.get("consumer_price", np.nan) > 0:
                obs_logs.append(float(np.log(row["consumer_price"]) - cons_bias))
                obs_weights.append(float(cons_weight))
                total_weight_sum += float(cons_weight)

            if pd.notna(row.get("silpo_baseline")) and row.get("silpo_baseline", np.nan) > 0:
                baseline_logs.append(float(np.log(row["silpo_baseline"]) - sil_bias))
                baseline_weights.append(float(sil_weight))
            elif pd.notna(row.get("silpo_observed")) and row.get("silpo_observed", np.nan) > 0:
                baseline_logs.append(float(np.log(row["silpo_observed"]) - sil_bias))
                baseline_weights.append(float(sil_weight))
            if pd.notna(row.get("novus_observed")) and row.get("novus_observed", np.nan) > 0:
                baseline_logs.append(float(np.log(row["novus_observed"]) - nov_bias))
                baseline_weights.append(float(nov_weight))
            if include_consumer and pd.notna(row.get("consumer_price")) and row.get("consumer_price", np.nan) > 0:
                baseline_logs.append(float(np.log(row["consumer_price"]) - cons_bias))
                baseline_weights.append(float(cons_weight))

            retail_observed = float(np.exp(np.average(obs_logs, weights=obs_weights))) if obs_logs and sum(obs_weights) > 0 else np.nan
            retail_baseline = float(np.exp(np.average(baseline_logs, weights=baseline_weights))) if baseline_logs and sum(baseline_weights) > 0 else np.nan
            silpo_share = float(sil_weight / sum(obs_weights)) if obs_logs and pd.notna(row.get("silpo_observed")) and sum(obs_weights) > 0 else 0.0
            retailer_support_share = float(retailer_weight_sum / total_weight_sum) if total_weight_sum > 0 else 0.0
            retailer_present_flag = int(
                (pd.notna(row.get("silpo_observed")) and row.get("silpo_observed", np.nan) > 0)
                or (pd.notna(row.get("novus_observed")) and row.get("novus_observed", np.nan) > 0)
            )
            consumer_present_flag = int(include_consumer and pd.notna(row.get("consumer_price")) and row.get("consumer_price", np.nan) > 0)
            consumer_anchor_only_flag = int(consumer_present_flag == 1 and retailer_present_flag == 0)

            out_rows.append(
                {
                    "date": row["date"],
                    "product": product,
                    "standardized_type": standardized_type,
                    "retail_observed": retail_observed,
                    "retail_baseline": retail_baseline,
                    "retail": retail_observed,
                    "discount_present": float(row.get("silpo_discount_present", 0.0)) * silpo_share,
                    "markdown_rate": float(row.get("silpo_markdown_rate", 0.0)) * silpo_share,
                    "promo_duration": row.get("silpo_promo_duration", np.nan),
                    "time_since_last_promo": row.get("silpo_time_since_last_promo", np.nan),
                    "discount_type_markdown": float(row.get("silpo_discount_type_markdown", 0.0)) * silpo_share,
                    "discount_type_bulk": float(row.get("silpo_discount_type_bulk", 0.0)) * silpo_share,
                    "top_brand_share": row.get("silpo_top_brand_share", np.nan),
                    "consumer_price_raw": row.get("consumer_price", np.nan),
                    "retailer_panel": panel_name,
                    "price_variant": "dual_variant_output",
                    "combined_rule": "weighted_geometric_mean_of_aligned_silpo_observed_novus_observed_consumer_anchor" if include_consumer else "weighted_geometric_mean_of_aligned_silpo_observed_novus_observed",
                    "source_count": int(row["source_count"]),
                    "weight_silpo": sil_weight,
                    "weight_novus": nov_weight,
                    "weight_consumer": cons_weight if include_consumer else 0.0,
                    "retailer_support_share": retailer_support_share,
                    "retailer_present_flag": retailer_present_flag,
                    "consumer_present_flag": consumer_present_flag,
                    "consumer_anchor_only_flag": consumer_anchor_only_flag,
                }
            )

    combined_df = pd.DataFrame(out_rows)
    if combined_df.empty:
        combined_df = pd.DataFrame(columns=["date", "product", "standardized_type", "retail", "retail_observed", "retail_baseline", "retailer_panel", "price_variant"])
    diagnostics_df = pd.DataFrame(diag_rows)
    methodology_df = pd.DataFrame(
        [
                {
                    "retailer_panel": panel_name,
                    "include_consumer": int(include_consumer),
                "base_weight_silpo": COMBINED_RETAIL_BASE_WEIGHTS["Silpo"],
                "base_weight_novus": COMBINED_RETAIL_BASE_WEIGHTS["Novus"],
                "base_weight_consumer": COMBINED_RETAIL_BASE_WEIGHTS["ConsumerUA"] if include_consumer else 0.0,
                "panel_name": panel_name,
                "construction_rule": "Daily weighted geometric mean after source-specific log-bias alignment; Silpo observed carries discounts as effective downward price moves.",
                "bias_fallback_rule": "Use product-level median log bias when overlap>=10 days, otherwise standardized_type-level median bias.",
                "support_rule": "Retailer support share tracks the retailer-weight share in the combined index; consumer_anchor_only_flag identifies dates carried only by ConsumerUA after alignment.",
            }
        ]
    )
    return combined_df, diagnostics_df, methodology_df


def _no_fit_row(meta: Dict[str, object], direction: str, stage_from: str, stage_to: str, n_obs: int, reason: str, promo_controls: int = 0) -> Dict[str, object]:
    return {
        **meta,
        "chain_direction": direction,
        "stage_from": stage_from,
        "stage_to": stage_to,
        "link": f"{stage_from.lower()}_to_{stage_to.lower()}",
        "model_family": "NO_FIT",
        "y_series": stage_to,
        "x_series": stage_from,
        "n_obs": int(n_obs),
        "sr_coef": np.nan,
        "lr_coef": np.nan,
        "ect_coef": np.nan,
        "ect_pvalue": np.nan,
        "asymmetry_short_p": np.nan,
        "asymmetry_long_p": np.nan,
        "vecm_rank": np.nan,
        "model_status": "unreliable",
        "unreliable_flag": 1,
        "unreliable_reason": reason,
        "shock_dummy_included": 0,
        "promo_controls_included": int(promo_controls),
        "ljungbox_p": np.nan,
        "arch_p": np.nan,
        "jb_p": np.nan,
        "notes": reason,
    }


def _producer_series(cleaned: Dict[str, pd.DataFrame], reconstruction_variant: str) -> pd.DataFrame:
    col = "price_pchip_input" if reconstruction_variant == "pchip" else "price_linear_input"
    df = cleaned["ProducerUA"].copy()
    df = _national_rows(df)
    df["producer"] = pd.to_numeric(df.get(col), errors="coerce")
    return _median_by_day(df, "producer", ["product", "standardized_type"])


def _farm_gate_series(cleaned: Dict[str, pd.DataFrame], farm_gate_source: str, reconstruction_variant: str) -> pd.DataFrame:
    source = FARM_GATE_SOURCE_MAP[farm_gate_source]
    col = "price_pchip_input" if reconstruction_variant == "pchip" else "price_linear_input"
    df = cleaned[source].copy()
    df = _national_rows(df)
    df["farm_gate"] = pd.to_numeric(df.get(col), errors="coerce")
    out = _median_by_day(df, "farm_gate", [])
    out["source"] = source
    return out


def _benchmark_series(cleaned: Dict[str, pd.DataFrame], source: str) -> pd.DataFrame:
    df = cleaned[source].copy()
    if df.empty:
        return pd.DataFrame(columns=["date", "product", "standardized_type", source])
    df = _national_rows(df)
    if source == "ConsumerUA":
        df[source] = pd.to_numeric(df.get("price_pchip_input"), errors="coerce").where(
            pd.to_numeric(df.get("price_pchip_input"), errors="coerce").notna(),
            pd.to_numeric(df.get("price_linear_input"), errors="coerce"),
        )
    else:
        df[source] = pd.to_numeric(df.get("observed_price", df.get("price")), errors="coerce")
    return _median_by_day(df, source, ["product", "standardized_type"])


def _source_value_series(df: pd.DataFrame, source_label: str, value_col: str) -> pd.DataFrame:
    use = df.copy()
    use = _national_rows(use)
    use = use[pd.to_numeric(use.get("admissible_for_level_model"), errors="coerce").fillna(0).eq(1)]
    use[source_label] = pd.to_numeric(use.get(value_col), errors="coerce")
    return _median_by_day(use, source_label, ["product", "standardized_type"])


def _retail_comparison_panel(cleaned: Dict[str, pd.DataFrame], price_variant: str) -> pd.DataFrame:
    sil_col = "baseline_price" if price_variant == "baseline" else "observed_price"
    sil = _source_value_series(cleaned["Silpo"], "silpo_cmp", sil_col)
    nov = _source_value_series(cleaned["Novus"], "novus_cmp", "observed_price")
    comp = sil.merge(nov, on=["date", "product", "standardized_type"], how="inner")
    if comp.empty:
        return comp
    comp["retail"] = comp[["silpo_cmp", "novus_cmp"]].median(axis=1, skipna=False)
    comp["retailer_panel"] = "silpo_baseline_vs_novus_observed" if price_variant == "baseline" else "silpo_vs_novus_observed"
    comp["price_variant"] = "baseline_vs_observed" if price_variant == "baseline" else "observed_comparison"
    return comp


def _combined_retail_panel(
    cleaned: Dict[str, pd.DataFrame],
    include_consumer: bool = True,
    panel_name: str = "Retail_combined",
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    return _build_combined_retail_panel(cleaned, include_consumer=include_consumer, panel_name=panel_name)


def _stable_products(df: pd.DataFrame, label_col: str = "product", min_days: int = 45) -> List[str]:
    if df.empty:
        return []
    counts = df.groupby(label_col)["date"].nunique()
    return counts[counts >= min_days].index.tolist()


def _build_shock_dummy(cleaned: Dict[str, pd.DataFrame], reconstruction_variant: str, farm_gate_source: str) -> pd.DataFrame:
    prod = _producer_series(cleaned, reconstruction_variant).rename(columns={"producer": "producer_price"})
    bench_blocks = []
    for src in ["EU", "CME"]:
        b = _benchmark_series(cleaned, src)
        if not b.empty:
            bench_blocks.append(b.rename(columns={src: "benchmark_price"}))
    bench = (
        pd.concat(bench_blocks, ignore_index=True)
        .groupby(["date", "standardized_type"], as_index=False)["benchmark_price"]
        .mean()
        if bench_blocks
        else pd.DataFrame(columns=["date", "standardized_type", "benchmark_price"])
    )
    fg = _farm_gate_series(cleaned, farm_gate_source, reconstruction_variant)
    fg_other = _farm_gate_series(cleaned, farm_gate_source, "linear" if reconstruction_variant == "pchip" else "pchip").rename(columns={"farm_gate": "farm_gate_other"})
    fg = fg.merge(fg_other[["date", "farm_gate_other"]], on="date", how="left")

    merged = prod.groupby(["date", "standardized_type"], as_index=False)["producer_price"].mean().merge(
        bench,
        on=["date", "standardized_type"],
        how="left",
    )
    merged = merged.merge(fg[["date", "farm_gate", "farm_gate_other"]], on="date", how="left")
    if merged.empty:
        return pd.DataFrame(columns=["date", "standardized_type", "shock_dummy"])
    rows = []
    for std, g in merged.groupby("standardized_type", dropna=False):
        gg = g.sort_values("date").copy()
        gg["dprod"] = _safe_log(gg["producer_price"]).diff()
        gg["dbench"] = _safe_log(gg["benchmark_price"]).diff()
        gg["spread"] = gg["dprod"] - gg["dbench"]
        spread_mean = gg["spread"].rolling(30, min_periods=8).mean()
        spread_std = gg["spread"].rolling(30, min_periods=8).std()
        gg["spread_z"] = (gg["spread"] - spread_mean) / spread_std.replace(0, np.nan)
        gg["variant_gap"] = (pd.to_numeric(gg["farm_gate"], errors="coerce") - pd.to_numeric(gg["farm_gate_other"], errors="coerce")).abs()
        gap_thr = gg["variant_gap"].quantile(0.75) if gg["variant_gap"].notna().any() else np.nan
        gg["shock_dummy"] = (
            gg["spread_z"].abs().gt(2.0)
            | (
                np.sign(gg["dprod"].fillna(0)) != np.sign(gg["dbench"].fillna(0))
            )
            | gg["variant_gap"].gt(gap_thr if pd.notna(gap_thr) else np.inf)
        ).astype(int)
        rows.append(gg[["date", "standardized_type", "shock_dummy"]])
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame(columns=["date", "standardized_type", "shock_dummy"])


def _panel_index_rows(panel_name: str, panel_level: str, df: pd.DataFrame, extra: Dict[str, object]) -> Dict[str, object]:
    row = {
        "panel_name": panel_name,
        "panel_level": panel_level,
        "n_rows": int(len(df)),
        "date_min": pd.to_datetime(df["date"], errors="coerce").min() if not df.empty else pd.NaT,
        "date_max": pd.to_datetime(df["date"], errors="coerce").max() if not df.empty else pd.NaT,
    }
    row.update(extra)
    return row


def _fit_shock_robust_pair(log_y: pd.Series, log_x: pd.Series, shock_dummy: pd.Series) -> Optional[FitResult]:
    t = pd.DataFrame({"log_y": log_y, "log_x": log_x, "shock_dummy": shock_dummy}).dropna()
    if len(t) < 35:
        return None
    t["dy"] = t["log_y"].diff()
    t["dx"] = t["log_x"].diff()
    t["dy_l1"] = t["dy"].shift(1)
    t = t.dropna()
    if len(t) < 30:
        return None
    fit = sm.OLS(t["dy"], sm.add_constant(t[["dy_l1", "dx", "shock_dummy"]], has_constant="add")).fit(
        cov_type="HAC",
        cov_kwds={"maxlags": 3},
    )
    notes = f"shock_coef={float(fit.params.get('shock_dummy', np.nan)):.4g}; shock_p={float(fit.pvalues.get('shock_dummy', np.nan)):.4g}"
    return FitResult(
        family="OLS_HAC_SHOCK",
        link="",
        y_series="",
        x_series="",
        n_obs=int(len(t)),
        sr_coef=float(fit.params.get("dx", np.nan)),
        lr_coef=np.nan,
        ect_coef=np.nan,
        ect_pvalue=np.nan,
        asym_short_p=np.nan,
        asym_long_p=np.nan,
        vecm_rank=np.nan,
        model_status="ok",
        unreliable=0,
        notes=notes,
        residuals=fit.resid,
    )


def _fit_retail_control_pair(frame: pd.DataFrame, y_col: str, x_col: str) -> Optional[FitResult]:
    needed = {
        "date": _first_series(frame, "date"),
        y_col: _first_series(frame, y_col),
        x_col: _first_series(frame, x_col),
        "shock_dummy": _first_series(frame, "shock_dummy"),
        "producer": _first_series(frame, "producer"),
        "prozorro": _first_series(frame, "prozorro"),
        "retail_observed": _first_series(frame, "retail_observed"),
        "retail_baseline": _first_series(frame, "retail_baseline"),
        "discount_present": _first_series(frame, "discount_present"),
        "markdown_rate": _first_series(frame, "markdown_rate"),
        "discount_type_markdown": _first_series(frame, "discount_type_markdown"),
        "discount_type_bulk": _first_series(frame, "discount_type_bulk"),
        "promo_duration": _first_series(frame, "promo_duration"),
        "time_since_last_promo": _first_series(frame, "time_since_last_promo"),
        "top_brand_share": _first_series(frame, "top_brand_share"),
        "competitor_price": _first_series(frame, "competitor_price"),
    }
    t = pd.DataFrame(needed)
    if t[y_col].notna().sum() == 0 or t[x_col].notna().sum() == 0:
        return None
    t["date"] = pd.to_datetime(t["date"], errors="coerce")
    t["log_y"] = _safe_log(t[y_col])
    t["log_x"] = _safe_log(t[x_col])
    t["dy"] = t["log_y"].diff()
    t["dx"] = t["log_x"].diff()
    t["dy_l1"] = t["dy"].shift(1)
    retail_obs = t["retail_observed"] if "retail_observed" in t.columns else t[y_col]
    retail_base = t["retail_baseline"] if "retail_baseline" in t.columns else t[y_col]
    if "producer" in t.columns:
        t["gap_retail_producer"] = _safe_log(retail_obs) - _safe_log(t["producer"])
    if "prozorro" in t.columns:
        t["gap_retail_prozorro"] = _safe_log(retail_obs) - _safe_log(t["prozorro"])
    t["baseline_deviation"] = _safe_log(retail_obs) - _safe_log(retail_base)
    if "competitor_price" in t.columns:
        t["competitor_gap"] = _safe_log(retail_obs) - _safe_log(t["competitor_price"])
    month = t["date"].dt.month
    t["month_sin"] = np.sin(2 * np.pi * month / 12.0)
    t["month_cos"] = np.cos(2 * np.pi * month / 12.0)
    numeric_cols = [c for c in t.columns if c not in {"date"}]
    for col in numeric_cols:
        t[col] = pd.to_numeric(t[col], errors="coerce")
    exog_cols = [
        "dy_l1",
        "dx",
        "shock_dummy",
        "discount_present",
        "markdown_rate",
        "discount_type_markdown",
        "discount_type_bulk",
        "promo_duration",
        "time_since_last_promo",
        "gap_retail_producer",
        "gap_retail_prozorro",
        "baseline_deviation",
        "competitor_gap",
        "top_brand_share",
        "month_sin",
        "month_cos",
    ]
    exog_cols = [c for c in exog_cols if c in t.columns and t[c].notna().sum() >= 20 and t[c].std(skipna=True) > 0]
    reg = t[["dy"] + exog_cols].dropna()
    if len(reg) < 35:
        return None
    fit = sm.OLS(reg["dy"], sm.add_constant(reg[exog_cols], has_constant="add")).fit(
        cov_type="HAC",
        cov_kwds={"maxlags": 3},
    )
    notes = "controls=" + ",".join(exog_cols)
    return FitResult(
        family="OLS_HAC_RETAIL_CTRL",
        link="",
        y_series="",
        x_series="",
        n_obs=int(len(reg)),
        sr_coef=float(fit.params.get("dx", np.nan)),
        lr_coef=np.nan,
        ect_coef=np.nan,
        ect_pvalue=np.nan,
        asym_short_p=np.nan,
        asym_long_p=np.nan,
        vecm_rank=np.nan,
        model_status="ok",
        unreliable=0,
        notes=notes,
        residuals=fit.resid,
    )


def _result_row(meta: Dict[str, object], fit: FitResult, direction: str, stage_from: str, stage_to: str, promo_controls: int, shock_included: int) -> Dict[str, object]:
    diag = _resid_diag(fit.residuals if fit.residuals is not None else pd.Series(dtype=float))
    unreliable_reason = []
    if int(diag["unreliable_flag"]) == 1:
        unreliable_reason.append("residual_autocorr_or_arch")
    if fit.family == "ECM" and pd.notna(fit.ect_coef) and pd.notna(fit.ect_pvalue):
        if not (fit.ect_coef < 0 and fit.ect_pvalue < 0.10):
            unreliable_reason.append("ect_not_negative_significant")
    return {
        **meta,
        "chain_direction": direction,
        "stage_from": stage_from,
        "stage_to": stage_to,
        "link": fit.link,
        "model_family": fit.family,
        "y_series": fit.y_series or stage_to,
        "x_series": fit.x_series or stage_from,
        "n_obs": fit.n_obs,
        "sr_coef": fit.sr_coef,
        "lr_coef": fit.lr_coef,
        "ect_coef": fit.ect_coef,
        "ect_pvalue": fit.ect_pvalue,
        "asymmetry_short_p": fit.asym_short_p,
        "asymmetry_long_p": fit.asym_long_p,
        "vecm_rank": fit.vecm_rank,
        "model_status": "unreliable" if unreliable_reason else fit.model_status,
        "unreliable_flag": int(bool(unreliable_reason)),
        "unreliable_reason": "; ".join(unreliable_reason),
        "shock_dummy_included": int(shock_included),
        "promo_controls_included": int(promo_controls),
        "ljungbox_p": diag["ljungbox_p"],
        "arch_p": diag["arch_p"],
        "jb_p": diag["jb_p"],
        "notes": fit.notes,
    }


def _pair_suite(meta: Dict[str, object], frame: pd.DataFrame, y_col: str, x_col: str, direction: str, stage_from: str, stage_to: str) -> Tuple[List[Dict[str, object]], List[Dict[str, object]], pd.DataFrame]:
    use = pd.DataFrame(
        {
            "date": _first_series(frame, "date"),
            y_col: _first_series(frame, y_col),
            x_col: _first_series(frame, x_col),
            "shock_dummy": _first_series(frame, "shock_dummy"),
        }
    )
    use[y_col] = pd.to_numeric(use[y_col], errors="coerce")
    use[x_col] = pd.to_numeric(use[x_col], errors="coerce")
    use = use[(use[y_col] > 0) & (use[x_col] > 0)].dropna(subset=["date", y_col, x_col]).sort_values("date")
    y_cls = _integration_class(use[y_col])
    x_cls = _integration_class(use[x_col])
    coint_p = np.nan
    if len(use) >= 30:
        try:
            coint_p = float(coint(_safe_log(use[y_col]), _safe_log(use[x_col]))[1])
        except Exception:
            coint_p = np.nan
    pretest_row = {
        **meta,
        "chain_direction": direction,
        "stage_from": stage_from,
        "stage_to": stage_to,
        "pair_n_obs": int(len(use)),
        "integration_y": y_cls["integration_class"],
        "integration_x": x_cls["integration_class"],
        "cointegration_p": coint_p,
        "stability_y": y_cls["stability_flag"],
        "stability_x": x_cls["stability_flag"],
    }
    if use.empty:
        return [pretest_row], [_no_fit_row(meta, direction, stage_from, stage_to, 0, "no_positive_overlap")], pd.DataFrame()

    models: List[Dict[str, object]] = []
    mult = pd.DataFrame()
    if len(use) < 35 or y_cls["integration_class"] == "I(2)" or x_cls["integration_class"] == "I(2)":
        reason = "insufficient_overlap" if len(use) < 35 else "i2_series_blocked"
        return [pretest_row], [_no_fit_row(meta, direction, stage_from, stage_to, len(use), reason)], mult

    log_y = _safe_log(use[y_col])
    log_x = _safe_log(use[x_col])

    ar = _fit_ardl_pair(log_y, log_x, max_lag=7)
    if ar is not None:
        ar.link = f"{stage_from.lower()}_to_{stage_to.lower()}"
        models.append(_result_row(meta, ar, direction, stage_from, stage_to, 0, 0))

    if y_cls["integration_class"] == "I(1)" and x_cls["integration_class"] == "I(1)":
        ec = _fit_ecm_pair(log_y, log_x, max_lag=6)
        if ec is not None:
            ec.link = f"{stage_from.lower()}_to_{stage_to.lower()}"
            models.append(_result_row(meta, ec, direction, stage_from, stage_to, 0, 0))

    na = _fit_nardl_pair(log_y, log_x, max_lag=6)
    if na is not None:
        na_fit, na_mult = na
        na_fit.link = f"{stage_from.lower()}_to_{stage_to.lower()}"
        models.append(_result_row(meta, na_fit, direction, stage_from, stage_to, 0, 0))
        mult = na_mult.copy()
        mult["panel_name"] = meta["panel_name"]
        mult["link"] = na_fit.link
        mult["reconstruction_variant"] = meta["reconstruction_variant"]
        mult["farm_gate_source"] = meta["farm_gate_source"]
        mult["price_variant"] = meta["price_variant"]

    shock = _fit_shock_robust_pair(log_y, log_x, use["shock_dummy"])
    if shock is not None:
        shock.link = f"{stage_from.lower()}_to_{stage_to.lower()}"
        models.append(_result_row(meta, shock, direction, stage_from, stage_to, 0, 1))

    if stage_to == "Retail":
        retail_ctrl = _fit_retail_control_pair(frame, y_col=y_col, x_col=x_col)
        if retail_ctrl is not None:
            retail_ctrl.link = f"{stage_from.lower()}_to_{stage_to.lower()}"
            models.append(_result_row(meta, retail_ctrl, direction, stage_from, stage_to, 1, 1))

    if not models:
        models.append(_no_fit_row(meta, direction, stage_from, stage_to, len(use), "no_model_converged"))

    return [pretest_row], models, mult


def _variant_robustness(model_df: pd.DataFrame) -> pd.DataFrame:
    if model_df.empty:
        return pd.DataFrame()
    rows = []
    use = model_df[model_df["model_family"].isin(["ARDL", "ECM", "NARDL", "VECM"])]
    keys = [
        "panel_level",
        "segment_name",
        "standardized_type",
        "retailer_panel",
        "brand",
        "price_variant",
        "intersection_rule",
        "farm_gate_source",
        "chain_direction",
        "stage_from",
        "stage_to",
        "model_family",
    ]
    for gkeys, g in use.groupby(keys, dropna=False):
        lin = g[g["reconstruction_variant"] == "linear"]
        pch = g[g["reconstruction_variant"] == "pchip"]
        if lin.empty or pch.empty:
            robust = 0
            interp = 1
            same_lr = same_ect = same_sr = np.nan
        else:
            lin0 = lin.iloc[0]
            pch0 = pch.iloc[0]
            same_sr = _sign(lin0["sr_coef"]) == _sign(pch0["sr_coef"])
            same_lr = _sign(lin0["lr_coef"]) == _sign(pch0["lr_coef"])
            ect_sign_ok = True
            if pd.notna(lin0["ect_coef"]) or pd.notna(pch0["ect_coef"]):
                ect_sign_ok = _sign(lin0["ect_coef"]) == _sign(pch0["ect_coef"])
            same_ect = ect_sign_ok
            mag_gap = abs(pd.to_numeric(lin0["lr_coef"], errors="coerce") - pd.to_numeric(pch0["lr_coef"], errors="coerce"))
            robust = int(bool(same_sr) and bool(same_lr) and bool(ect_sign_ok))
            interp = int((not robust) or (pd.notna(mag_gap) and mag_gap > 0.25))
        row = dict(zip(keys, gkeys if isinstance(gkeys, tuple) else (gkeys,)))
        row.update(
            {
                "same_sr_sign": same_sr,
                "same_lr_sign": same_lr,
                "same_ect_sign": same_ect,
                "robust_linear_vs_pchip": robust,
                "interpolation_sensitive": interp,
            }
        )
        rows.append(row)
    return pd.DataFrame(rows)


def _farmgate_source_comparison(model_df: pd.DataFrame) -> pd.DataFrame:
    if model_df.empty:
        return pd.DataFrame()
    rows = []
    use = model_df[model_df["model_family"].isin(["ARDL", "ECM", "NARDL", "VECM"])]
    keys = [
        "panel_level",
        "segment_name",
        "standardized_type",
        "retailer_panel",
        "brand",
        "price_variant",
        "intersection_rule",
        "reconstruction_variant",
        "chain_direction",
        "stage_from",
        "stage_to",
        "model_family",
    ]
    for gkeys, g in use.groupby(keys, dropna=False):
        ini = g[g["farm_gate_source"] == "initial"]
        fil = g[g["farm_gate_source"] == "all_missing_filled"]
        if ini.empty or fil.empty:
            robust = 0
        else:
            ini0 = ini.iloc[0]
            fil0 = fil.iloc[0]
            robust = int((_sign(ini0["lr_coef"]) == _sign(fil0["lr_coef"])) and (_sign(ini0["ect_coef"]) == _sign(fil0["ect_coef"])))
        row = dict(zip(keys, gkeys if isinstance(gkeys, tuple) else (gkeys,)))
        row["robust_across_reconstruction"] = robust
        rows.append(row)
    return pd.DataFrame(rows)


def _build_primary_panels(cleaned: Dict[str, pd.DataFrame]) -> Tuple[List[Dict[str, object]], pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    panels: List[Dict[str, object]] = []
    index_rows: List[Dict[str, object]] = []

    def _append_panel(meta: Dict[str, object], frame: pd.DataFrame) -> None:
        panels.append({"meta": meta, "frame": frame})
        index_rows.append(_panel_index_rows(str(meta["panel_name"]), str(meta["panel_level"]), frame, meta))

    def _attach_benchmarks(frame: pd.DataFrame, product: str) -> pd.DataFrame:
        merged = frame.copy()
        for src, bdf in benchmark_cache.items():
            b = bdf[bdf["product"] == product][["date", "standardized_type", src]]
            merged = merged.merge(b, on=["date", "standardized_type"], how="left")
        return merged

    producer_products = set(_stable_products(_national_rows(cleaned["ProducerUA"]), "product", min_days=MIN_STABLE_PRODUCT_DAYS))
    prozorro_products = set(_stable_products(_national_rows(cleaned["ProZorro"]), "product", min_days=MIN_STABLE_PRODUCT_DAYS))

    benchmark_cache = {src: _benchmark_series(cleaned, src) for src in ["ConsumerUA", "EU", "CME"]}
    comparison_obs = _retail_comparison_panel(cleaned, "observed")
    comparison_base = _retail_comparison_panel(cleaned, "baseline")
    combined_panel, combined_diag, combined_methodology = _combined_retail_panel(
        cleaned,
        include_consumer=True,
        panel_name="Retail_combined",
    )
    combined_core_panel, combined_core_diag, combined_core_methodology = _combined_retail_panel(
        cleaned,
        include_consumer=False,
        panel_name="Retail_combined_core",
    )
    retail_controls_cache = {src: _retail_daily_controls(cleaned, src) for src in ["Silpo", "Novus"]}
    retail_controls_cache["RetailCombined"] = combined_panel.copy()
    retail_controls_cache["RetailCombinedCore"] = combined_core_panel.copy()

    combined_diag = pd.concat([combined_diag, combined_core_diag], ignore_index=True) if not combined_core_diag.empty else combined_diag
    combined_methodology = (
        pd.concat([combined_methodology, combined_core_methodology], ignore_index=True)
        if not combined_core_methodology.empty
        else combined_methodology
    )

    for recon in RECONSTRUCTION_VARIANTS:
        producer = _producer_series(cleaned, recon)
        producer = producer[producer["product"].isin(producer_products)].copy()
        prozorro_daily = _source_value_series(cleaned["ProZorro"], "prozorro", "observed_price")
        prozorro_daily = prozorro_daily[prozorro_daily["product"].isin(prozorro_products)].copy()
        for farm_gate_source in FARM_GATE_SOURCE_MAP:
            farm = _farm_gate_series(cleaned, farm_gate_source, recon)
            shock = _build_shock_dummy(cleaned, recon, farm_gate_source)

            # Pairwise non-retail panels: do not force the narrow full-chain overlap.
            for product in sorted(producer_products):
                pp = producer[producer["product"] == product][["date", "product", "standardized_type", "producer"]]
                merged = pp.merge(farm[["date", "farm_gate"]], on="date", how="inner").merge(shock, on=["date", "standardized_type"], how="left")
                if merged.empty:
                    continue
                merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                merged = _attach_benchmarks(merged, product)
                panel_name = f"pairwise::farm_gate_producer::{product}::{farm_gate_source}::{recon}"
                meta = {
                    "panel_level": "pairwise_product",
                    "panel_name": panel_name,
                    "segment_name": product,
                    "product": product,
                    "standardized_type": merged["standardized_type"].mode().iloc[0] if not merged["standardized_type"].mode().empty else "",
                    "retailer_panel": "",
                    "brand": "",
                    "price_variant": "",
                    "reconstruction_variant": recon,
                    "farm_gate_source": farm_gate_source,
                    "frequency": "daily",
                    "intersection_rule": "pairwise_overlap",
                    "pair_scope": "farm_gate_producer",
                }
                _append_panel(meta, merged)

            for product in sorted(prozorro_products):
                zz = prozorro_daily[prozorro_daily["product"] == product][["date", "product", "standardized_type", "prozorro"]]
                merged = zz.merge(farm[["date", "farm_gate"]], on="date", how="inner").merge(shock, on=["date", "standardized_type"], how="left")
                if merged.empty:
                    continue
                merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                merged = _attach_benchmarks(merged, product)
                panel_name = f"pairwise::farm_gate_prozorro::{product}::{farm_gate_source}::{recon}"
                meta = {
                    "panel_level": "pairwise_product",
                    "panel_name": panel_name,
                    "segment_name": product,
                    "product": product,
                    "standardized_type": merged["standardized_type"].mode().iloc[0] if not merged["standardized_type"].mode().empty else "",
                    "retailer_panel": "",
                    "brand": "",
                    "price_variant": "",
                    "reconstruction_variant": recon,
                    "farm_gate_source": farm_gate_source,
                    "frequency": "daily",
                    "intersection_rule": "pairwise_overlap",
                    "pair_scope": "farm_gate_prozorro",
                }
                _append_panel(meta, merged)

            for product in sorted(producer_products.intersection(prozorro_products)):
                pp = producer[producer["product"] == product][["date", "product", "standardized_type", "producer"]]
                zz = prozorro_daily[prozorro_daily["product"] == product][["date", "product", "standardized_type", "prozorro"]]
                merged = pp.merge(zz, on=["date", "product", "standardized_type"], how="inner")
                if merged.empty:
                    continue
                merged = merged.merge(farm[["date", "farm_gate"]], on="date", how="left").merge(shock, on=["date", "standardized_type"], how="left")
                merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                merged = _attach_benchmarks(merged, product)
                panel_name = f"pairwise::producer_prozorro::{product}::{farm_gate_source}::{recon}"
                meta = {
                    "panel_level": "pairwise_product",
                    "panel_name": panel_name,
                    "segment_name": product,
                    "product": product,
                    "standardized_type": merged["standardized_type"].mode().iloc[0] if not merged["standardized_type"].mode().empty else "",
                    "retailer_panel": "",
                    "brand": "",
                    "price_variant": "",
                    "reconstruction_variant": recon,
                    "farm_gate_source": farm_gate_source,
                    "frequency": "daily",
                    "intersection_rule": "pairwise_overlap",
                    "pair_scope": "producer_prozorro",
                }
                _append_panel(meta, merged)

            for cfg in RETAIL_CONFIGS:
                retail_controls = retail_controls_cache.get(cfg["source"], pd.DataFrame()).copy()
                if retail_controls.empty:
                    continue
                if cfg["source"] in cleaned:
                    retail_base = _national_rows(cleaned[cfg["source"]])
                else:
                    retail_base = retail_controls
                retail_products = set(_stable_products(retail_base, "product", min_days=MIN_STABLE_PRODUCT_DAYS))
                common_products = sorted(producer_products.intersection(prozorro_products).intersection(retail_products))
                retail_col = "retail_baseline" if cfg["price_variant"] == "baseline" else "retail_observed"
                competitor_source = "Novus" if cfg["source"] == "Silpo" else ("Silpo" if cfg["source"] == "Novus" else None)
                competitor_daily = retail_controls_cache.get(competitor_source, pd.DataFrame())
                competitor_daily = competitor_daily[["date", "product", "standardized_type", "retail_observed"]].rename(
                    columns={"retail_observed": "competitor_price"}
                ) if (competitor_source is not None and not competitor_daily.empty) else pd.DataFrame()
                for product in common_products:
                    pp = producer[producer["product"] == product].rename(columns={"producer": "producer"})
                    zz = prozorro_daily[prozorro_daily["product"] == product][["date", "product", "standardized_type", "prozorro"]]
                    rr = retail_controls[retail_controls["product"] == product][
                        [
                            "date",
                            "product",
                            "standardized_type",
                            retail_col,
                            "retail_observed",
                            "retail_baseline",
                            "discount_present",
                            "markdown_rate",
                            "promo_duration",
                            "time_since_last_promo",
                            "discount_type_markdown",
                            "discount_type_bulk",
                            "top_brand_share",
                        ]
                    ].rename(columns={retail_col: "retail"})
                    merged = pp.merge(zz, on=["date", "product", "standardized_type"], how="inner").merge(rr, on=["date", "product", "standardized_type"], how="inner")
                    if merged.empty:
                        continue
                    if not competitor_daily.empty:
                        merged = merged.merge(competitor_daily[competitor_daily["product"] == product], on=["date", "product", "standardized_type"], how="left")
                    merged = merged.merge(farm[["date", "farm_gate"]], on="date", how="left").merge(shock, on=["date", "standardized_type"], how="left")
                    merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                    panel_name = f"product::{product}::{cfg['retailer_panel']}::{cfg['price_variant']}::{farm_gate_source}::{recon}"
                    meta = {
                        "panel_level": "product",
                        "panel_name": panel_name,
                        "segment_name": product,
                        "product": product,
                        "standardized_type": merged["standardized_type"].mode().iloc[0] if not merged["standardized_type"].mode().empty else "",
                        "retailer_panel": cfg["retailer_panel"],
                        "brand": "",
                        "price_variant": cfg["price_variant"],
                        "reconstruction_variant": recon,
                        "farm_gate_source": farm_gate_source,
                        "frequency": "daily",
                        "intersection_rule": "chain_common_support",
                        "pair_scope": "full_chain",
                    }
                    merged = _attach_benchmarks(merged, product)
                    _append_panel(meta, merged)

                # Pairwise retail panels improve extreme-point estimation without requiring the full chain.
                retail_pair_products = sorted(retail_products)
                producer_retail_products = sorted(producer_products.intersection(retail_products))
                prozorro_retail_products = sorted(prozorro_products.intersection(retail_products))

                for product in retail_pair_products:
                    rr = retail_controls[retail_controls["product"] == product][
                        [
                            "date",
                            "product",
                            "standardized_type",
                            retail_col,
                            "retail_observed",
                            "retail_baseline",
                            "discount_present",
                            "markdown_rate",
                            "promo_duration",
                            "time_since_last_promo",
                            "discount_type_markdown",
                            "discount_type_bulk",
                            "top_brand_share",
                        ]
                    ].rename(columns={retail_col: "retail"})
                    merged = rr.merge(farm[["date", "farm_gate"]], on="date", how="inner").merge(shock, on=["date", "standardized_type"], how="left")
                    if merged.empty:
                        continue
                    if not competitor_daily.empty:
                        merged = merged.merge(competitor_daily[competitor_daily["product"] == product], on=["date", "product", "standardized_type"], how="left")
                    merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                    merged = _attach_benchmarks(merged, product)
                    panel_name = f"pairwise::farm_gate_retail::{product}::{cfg['retailer_panel']}::{cfg['price_variant']}::{farm_gate_source}::{recon}"
                    meta = {
                        "panel_level": "pairwise_product",
                        "panel_name": panel_name,
                        "segment_name": product,
                        "product": product,
                        "standardized_type": merged["standardized_type"].mode().iloc[0] if not merged["standardized_type"].mode().empty else "",
                        "retailer_panel": cfg["retailer_panel"],
                        "brand": "",
                        "price_variant": cfg["price_variant"],
                        "reconstruction_variant": recon,
                        "farm_gate_source": farm_gate_source,
                        "frequency": "daily",
                        "intersection_rule": "pairwise_overlap",
                        "pair_scope": "farm_gate_retail",
                    }
                    _append_panel(meta, merged)

                for product in producer_retail_products:
                    pp = producer[producer["product"] == product][["date", "product", "standardized_type", "producer"]]
                    rr = retail_controls[retail_controls["product"] == product][
                        [
                            "date",
                            "product",
                            "standardized_type",
                            retail_col,
                            "retail_observed",
                            "retail_baseline",
                            "discount_present",
                            "markdown_rate",
                            "promo_duration",
                            "time_since_last_promo",
                            "discount_type_markdown",
                            "discount_type_bulk",
                            "top_brand_share",
                        ]
                    ].rename(columns={retail_col: "retail"})
                    merged = pp.merge(rr, on=["date", "product", "standardized_type"], how="inner")
                    if merged.empty:
                        continue
                    if not competitor_daily.empty:
                        merged = merged.merge(competitor_daily[competitor_daily["product"] == product], on=["date", "product", "standardized_type"], how="left")
                    merged = merged.merge(farm[["date", "farm_gate"]], on="date", how="left").merge(shock, on=["date", "standardized_type"], how="left")
                    merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                    merged = _attach_benchmarks(merged, product)
                    panel_name = f"pairwise::producer_retail::{product}::{cfg['retailer_panel']}::{cfg['price_variant']}::{farm_gate_source}::{recon}"
                    meta = {
                        "panel_level": "pairwise_product",
                        "panel_name": panel_name,
                        "segment_name": product,
                        "product": product,
                        "standardized_type": merged["standardized_type"].mode().iloc[0] if not merged["standardized_type"].mode().empty else "",
                        "retailer_panel": cfg["retailer_panel"],
                        "brand": "",
                        "price_variant": cfg["price_variant"],
                        "reconstruction_variant": recon,
                        "farm_gate_source": farm_gate_source,
                        "frequency": "daily",
                        "intersection_rule": "pairwise_overlap",
                        "pair_scope": "producer_retail",
                    }
                    _append_panel(meta, merged)

                for product in prozorro_retail_products:
                    zz = prozorro_daily[prozorro_daily["product"] == product][["date", "product", "standardized_type", "prozorro"]]
                    rr = retail_controls[retail_controls["product"] == product][
                        [
                            "date",
                            "product",
                            "standardized_type",
                            retail_col,
                            "retail_observed",
                            "retail_baseline",
                            "discount_present",
                            "markdown_rate",
                            "promo_duration",
                            "time_since_last_promo",
                            "discount_type_markdown",
                            "discount_type_bulk",
                            "top_brand_share",
                        ]
                    ].rename(columns={retail_col: "retail"})
                    merged = zz.merge(rr, on=["date", "product", "standardized_type"], how="inner")
                    if merged.empty:
                        continue
                    if not competitor_daily.empty:
                        merged = merged.merge(competitor_daily[competitor_daily["product"] == product], on=["date", "product", "standardized_type"], how="left")
                    merged = merged.merge(farm[["date", "farm_gate"]], on="date", how="left").merge(shock, on=["date", "standardized_type"], how="left")
                    merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                    merged = _attach_benchmarks(merged, product)
                    panel_name = f"pairwise::prozorro_retail::{product}::{cfg['retailer_panel']}::{cfg['price_variant']}::{farm_gate_source}::{recon}"
                    meta = {
                        "panel_level": "pairwise_product",
                        "panel_name": panel_name,
                        "segment_name": product,
                        "product": product,
                        "standardized_type": merged["standardized_type"].mode().iloc[0] if not merged["standardized_type"].mode().empty else "",
                        "retailer_panel": cfg["retailer_panel"],
                        "brand": "",
                        "price_variant": cfg["price_variant"],
                        "reconstruction_variant": recon,
                        "farm_gate_source": farm_gate_source,
                        "frequency": "daily",
                        "intersection_rule": "pairwise_overlap",
                        "pair_scope": "prozorro_retail",
                    }
                    _append_panel(meta, merged)

            # Average-price layer
            for cfg in RETAIL_CONFIGS:
                retail_controls = retail_controls_cache.get(cfg["source"], pd.DataFrame()).copy()
                if retail_controls.empty:
                    continue
                if cfg["source"] in cleaned:
                    retail_base = _national_rows(cleaned[cfg["source"]])
                else:
                    retail_base = retail_controls
                retail_products = set(_stable_products(retail_base, "product", min_days=MIN_STABLE_PRODUCT_DAYS))
                common_products = sorted(producer_products.intersection(prozorro_products).intersection(retail_products))
                if not common_products:
                    continue
                retail_col = "retail_baseline" if cfg["price_variant"] == "baseline" else "retail_observed"
                competitor_source = "Novus" if cfg["source"] == "Silpo" else ("Silpo" if cfg["source"] == "Novus" else None)
                competitor_daily = retail_controls_cache.get(competitor_source, pd.DataFrame())
                competitor_daily = (
                    competitor_daily[competitor_daily["product"].isin(common_products)]
                    .groupby("date", as_index=False)["retail_observed"]
                    .mean()
                    .rename(columns={"retail_observed": "competitor_price"})
                ) if (competitor_source is not None and not competitor_daily.empty) else pd.DataFrame()
                avg_components = {}
                avg_components["producer"] = (
                    producer[producer["product"].isin(common_products)]
                    .groupby("date", as_index=False)["producer"]
                    .mean()
                )
                avg_components["prozorro"] = (
                    prozorro_daily[prozorro_daily["product"].isin(common_products)]
                    .groupby("date", as_index=False)["prozorro"]
                    .mean()
                )
                avg_components["retail"] = (
                    retail_controls[retail_controls["product"].isin(common_products)]
                    .groupby("date", as_index=False)
                    .agg(
                        retail=(retail_col, "mean"),
                        retail_observed=("retail_observed", "mean"),
                        retail_baseline=("retail_baseline", "mean"),
                        discount_present=("discount_present", "mean"),
                        markdown_rate=("markdown_rate", "mean"),
                        promo_duration=("promo_duration", "mean"),
                        time_since_last_promo=("time_since_last_promo", "mean"),
                        discount_type_markdown=("discount_type_markdown", "mean"),
                        discount_type_bulk=("discount_type_bulk", "mean"),
                        top_brand_share=("top_brand_share", "mean"),
                    )
                )
                avg_components["farm_gate"] = farm[["date", "farm_gate"]]
                avg_components["shock"] = shock.groupby("date", as_index=False)["shock_dummy"].max()
                merged = avg_components["producer"].merge(avg_components["prozorro"], on="date", how="inner").merge(avg_components["retail"], on="date", how="inner").merge(avg_components["farm_gate"], on="date", how="left").merge(avg_components["shock"], on="date", how="left")
                if not competitor_daily.empty:
                    merged = merged.merge(competitor_daily, on="date", how="left")
                if merged.empty:
                    continue
                merged["product"] = "all_products_average"
                merged["standardized_type"] = "all_products_average"
                panel_name = f"average::{cfg['retailer_panel']}::{cfg['price_variant']}::{farm_gate_source}::{recon}"
                meta = {
                    "panel_level": "average",
                    "panel_name": panel_name,
                    "segment_name": "all_products_average",
                    "product": "all_products_average",
                    "standardized_type": "all_products_average",
                    "retailer_panel": cfg["retailer_panel"],
                    "brand": "",
                    "price_variant": cfg["price_variant"],
                    "reconstruction_variant": recon,
                    "farm_gate_source": farm_gate_source,
                    "frequency": "daily",
                    "intersection_rule": "chain_common_support",
                    "pair_scope": "full_chain_average",
                }
                _append_panel(meta, merged)

            # Widened retail comparison panels
            for comp in [comparison_obs, comparison_base, combined_panel, combined_core_panel]:
                if comp.empty:
                    continue
                merged = producer.groupby(["date", "product", "standardized_type"], as_index=False)["producer"].mean().merge(
                    _source_value_series(cleaned["ProZorro"], "prozorro", "observed_price"),
                    on=["date", "product", "standardized_type"],
                    how="inner",
                ).merge(
                    comp[["date", "product", "standardized_type", "retail", "retailer_panel", "price_variant"]],
                    on=["date", "product", "standardized_type"],
                    how="inner",
                )
                if merged.empty:
                    continue
                merged = merged.merge(farm[["date", "farm_gate"]], on="date", how="left").merge(shock, on=["date", "standardized_type"], how="left")
                merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                panel_name = f"comparison::{comp['retailer_panel'].iloc[0]}::{farm_gate_source}::{recon}"
                meta = {
                    "panel_level": "comparison",
                    "panel_name": panel_name,
                    "segment_name": comp["retailer_panel"].iloc[0],
                    "product": comp["retailer_panel"].iloc[0],
                    "standardized_type": "comparison_panel",
                    "retailer_panel": comp["retailer_panel"].iloc[0],
                    "brand": "",
                    "price_variant": comp["price_variant"].iloc[0],
                    "reconstruction_variant": recon,
                    "farm_gate_source": farm_gate_source,
                    "frequency": "daily",
                    "intersection_rule": "comparison_panel",
                    "pair_scope": "comparison",
                }
                _append_panel(meta, merged)

            # Brand-level retailer transmission
            for source in ["Silpo", "Novus"]:
                retailer = cleaned[source].copy()
                retailer = _national_rows(retailer)
                retailer = retailer[pd.to_numeric(retailer.get("admissible_for_level_model"), errors="coerce").fillna(0).eq(1)]
                retailer["brand_key"] = retailer.get("brand_normalized", retailer.get("brand", "")).astype(str)
                brand_days = (
                    retailer.groupby(["standardized_type", "brand_key"], as_index=False)["date"]
                    .nunique()
                    .rename(columns={"date": "n_days"})
                )
                brand_days = brand_days[brand_days["n_days"] >= MIN_BRAND_DAYS[source]].sort_values(["standardized_type", "n_days"], ascending=[True, False])
                valid = (
                    brand_days.groupby("standardized_type", as_index=False)
                    .head(1)[["brand_key", "standardized_type"]]
                    .itertuples(index=False, name=None)
                )
                competitor_source = "Novus" if source == "Silpo" else "Silpo"
                competitor_brand = retail_controls_cache.get(competitor_source, pd.DataFrame())
                competitor_brand = competitor_brand[["date", "standardized_type", "retail_observed"]].rename(
                    columns={"retail_observed": "competitor_price"}
                ) if not competitor_brand.empty else pd.DataFrame()
                for brand, std in valid:
                    rr = retailer[(retailer["brand_key"] == brand) & (retailer["standardized_type"] == std)].copy()
                    if rr.empty:
                        continue
                    rr["retail_observed"] = pd.to_numeric(rr.get("observed_price"), errors="coerce")
                    rr["retail_baseline"] = pd.to_numeric(rr.get("baseline_price"), errors="coerce")
                    rr["discount_present"] = pd.to_numeric(rr.get("discount_present"), errors="coerce").fillna(0)
                    rr["markdown_rate"] = pd.to_numeric(rr.get("markdown_rate"), errors="coerce").fillna(0)
                    rr["promo_duration"] = pd.to_numeric(rr.get("promo_duration"), errors="coerce")
                    rr["time_since_last_promo"] = pd.to_numeric(rr.get("time_since_last_promo"), errors="coerce")
                    rr["discount_type_markdown"] = (rr.get("discount_type", "unknown").astype(str) == "markdown").astype(float)
                    rr["discount_type_bulk"] = (rr.get("discount_type", "unknown").astype(str) == "bulk").astype(float)
                    rr["top_brand_share"] = 1.0
                    rr_daily = rr.groupby(["date", "standardized_type"], as_index=False).agg(
                        retail_observed=("retail_observed", "median"),
                        retail_baseline=("retail_baseline", "median"),
                        discount_present=("discount_present", "mean"),
                        markdown_rate=("markdown_rate", "mean"),
                        promo_duration=("promo_duration", "mean"),
                        time_since_last_promo=("time_since_last_promo", "mean"),
                        discount_type_markdown=("discount_type_markdown", "mean"),
                        discount_type_bulk=("discount_type_bulk", "mean"),
                        top_brand_share=("top_brand_share", "mean"),
                    )
                    pp = producer[producer["standardized_type"] == std].groupby(["date", "standardized_type"], as_index=False)["producer"].mean()
                    zz = prozorro_daily[prozorro_daily["standardized_type"] == std].groupby(["date", "standardized_type"], as_index=False)["prozorro"].mean()
                    price_variants = [("observed", "retail_observed")]
                    if source == "Silpo":
                        price_variants.append(("baseline", "retail_baseline"))
                    for price_variant, retail_value_col in price_variants:
                        rr_use = rr_daily.rename(columns={retail_value_col: "retail"})
                        merged = pp.merge(zz, on=["date", "standardized_type"], how="inner").merge(rr_use, on=["date", "standardized_type"], how="inner")
                        if merged.empty:
                            continue
                        if not competitor_brand.empty:
                            merged = merged.merge(competitor_brand, on=["date", "standardized_type"], how="left")
                        merged = merged.merge(farm[["date", "farm_gate"]], on="date", how="left").merge(shock, on=["date", "standardized_type"], how="left")
                        merged["product"] = "brand_panel"
                        merged["brand"] = brand
                        merged["shock_dummy"] = merged["shock_dummy"].fillna(0).astype(int)
                        panel_name = f"brand::{source}::{brand}::{std}::{price_variant}::{farm_gate_source}::{recon}"
                        meta = {
                            "panel_level": "brand",
                            "panel_name": panel_name,
                            "segment_name": f"{source}:{brand}:{std}",
                            "product": "brand_panel",
                            "standardized_type": std,
                            "retailer_panel": source,
                            "brand": brand,
                            "price_variant": price_variant,
                            "reconstruction_variant": recon,
                            "farm_gate_source": farm_gate_source,
                            "frequency": "daily",
                            "intersection_rule": "brand_top_sku",
                            "pair_scope": "brand_panel",
                        }
                        _append_panel(meta, merged)

    return panels, pd.DataFrame(index_rows), combined_diag, combined_methodology


def _benchmark_comparison_rows(panels: List[Dict[str, object]]) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for panel in panels:
        meta = panel["meta"]
        frame = panel["frame"]
        for bm in ["ConsumerUA", "EU", "CME"]:
            if bm not in frame.columns:
                continue
            for stage in ["farm_gate", "producer", "prozorro", "retail"]:
                if bm == "ConsumerUA" and stage == "retail" and str(meta.get("retailer_panel", "")) == "Retail_combined":
                    continue
                if stage not in frame.columns:
                    continue
                d = pd.DataFrame(
                    {
                        "date": _first_series(frame, "date"),
                        stage: _first_series(frame, stage),
                        bm: _first_series(frame, bm),
                    }
                )
                d[stage] = pd.to_numeric(d[stage], errors="coerce")
                d[bm] = pd.to_numeric(d[bm], errors="coerce")
                d = d[(d[stage] > 0) & (d[bm] > 0)].dropna()
                if len(d) < 25:
                    continue
                dy = _safe_log(d[stage]).diff()
                dx = _safe_log(d[bm]).diff()
                best_lag = np.nan
                best_corr = np.nan
                for lag in range(1, 15):
                    tmp = pd.concat([dy, dx.shift(lag)], axis=1).dropna()
                    if len(tmp) < 20:
                        continue
                    corr = float(tmp.iloc[:, 0].corr(tmp.iloc[:, 1]))
                    if pd.isna(best_corr) or abs(corr) > abs(best_corr):
                        best_corr = corr
                        best_lag = lag
                rows.append(
                    {
                        **meta,
                        "benchmark_source": bm,
                        "stage": stage,
                        "n_obs": int(len(d)),
                        "best_lag_days": best_lag,
                        "corr_at_best_lag": best_corr,
                    }
                )
    return pd.DataFrame(rows)


def _coverage_validation(model_df: pd.DataFrame, panel_index: pd.DataFrame) -> pd.DataFrame:
    required_links = [
        ("forward", "FarmGateUA", "ProducerUA"),
        ("forward", "ProducerUA", "ProZorro"),
        ("forward", "ProZorro", "Retail"),
        ("forward", "FarmGateUA", "ProZorro"),
        ("forward", "ProducerUA", "Retail"),
        ("forward", "FarmGateUA", "Retail"),
        ("reverse", "Retail", "ProZorro"),
        ("reverse", "ProZorro", "ProducerUA"),
        ("reverse", "Retail", "ProducerUA"),
        ("reverse", "ProducerUA", "FarmGateUA"),
        ("reverse", "ProZorro", "FarmGateUA"),
        ("reverse", "Retail", "FarmGateUA"),
    ]
    rows: List[Dict[str, object]] = []
    for direction, stage_from, stage_to in required_links:
        subset = model_df[
            (model_df["chain_direction"] == direction)
            & (model_df["stage_from"] == stage_from)
            & (model_df["stage_to"] == stage_to)
        ] if not model_df.empty else pd.DataFrame()
        rows.append(
            {
                "check_type": "required_link",
                "chain_direction": direction,
                "stage_from": stage_from,
                "stage_to": stage_to,
                "rows_total": int(len(subset)),
                "preferred_family_rows": int(subset["model_family"].isin(["ARDL", "ECM", "NARDL", "VECM"]).sum()) if not subset.empty else 0,
                "core_finding_rows": int(pd.to_numeric(subset.get("core_finding_flag"), errors="coerce").fillna(0).sum()) if not subset.empty else 0,
            }
        )
    rows.append(
        {
            "check_type": "brand_panels",
            "chain_direction": "",
            "stage_from": "",
            "stage_to": "",
            "rows_total": int((panel_index["panel_level"] == "brand").sum()) if not panel_index.empty else 0,
            "preferred_family_rows": int(model_df[(model_df["panel_level"] == "brand") & (model_df["model_family"].isin(["ARDL", "ECM", "NARDL", "VECM"]))].shape[0]) if not model_df.empty else 0,
            "core_finding_rows": int(model_df[(model_df["panel_level"] == "brand") & (pd.to_numeric(model_df.get("core_finding_flag"), errors="coerce").fillna(0).eq(1))].shape[0]) if not model_df.empty else 0,
        }
    )
    return pd.DataFrame(rows)


def _preferred_results(model_df: pd.DataFrame) -> pd.DataFrame:
    if model_df.empty:
        return pd.DataFrame()
    return model_df[model_df["model_family"].isin(PREFERRED_MODEL_FAMILIES)].copy()


def _farmgate_summary(model_df: pd.DataFrame, direction: str) -> pd.DataFrame:
    use = _preferred_results(model_df)
    if use.empty:
        return pd.DataFrame()
    if direction == "direct":
        use = use[(use["chain_direction"] == "forward") & (use["stage_from"] == "FarmGateUA")].copy()
    else:
        use = use[(use["chain_direction"] == "reverse") & (use["stage_to"] == "FarmGateUA")].copy()
    if use.empty:
        return pd.DataFrame()
    use["ect_negative_sig"] = (
        pd.to_numeric(use["ect_coef"], errors="coerce").lt(0)
        & pd.to_numeric(use["ect_pvalue"], errors="coerce").lt(0.10)
    ).astype(int)
    group_cols = [
        "stage_from",
        "stage_to",
        "retailer_panel",
        "price_variant",
        "panel_level",
        "intersection_rule",
        "model_family",
    ]
    out = (
        use.groupby(group_cols, dropna=False)
        .agg(
            rows_total=("panel_name", "count"),
            median_n_obs=("n_obs", "median"),
            core_finding_share=("core_finding_flag", "mean"),
            robust_linear_vs_pchip_share=("robust_linear_vs_pchip", "mean"),
            robust_across_reconstruction_share=("robust_across_reconstruction", "mean"),
            ect_negative_sig_share=("ect_negative_sig", "mean"),
            median_lr_coef=("lr_coef", "median"),
            median_sr_coef=("sr_coef", "median"),
        )
        .reset_index()
    )
    out["summary_direction"] = direction
    return out.sort_values(["stage_from", "stage_to", "retailer_panel", "intersection_rule", "model_family"]).reset_index(drop=True)


def _farmgate_variant_stability(model_df: pd.DataFrame) -> pd.DataFrame:
    use = _preferred_results(model_df)
    if use.empty:
        return pd.DataFrame()
    use = use[(use["stage_from"] == "FarmGateUA") | (use["stage_to"] == "FarmGateUA")].copy()
    if use.empty:
        return pd.DataFrame()
    group_cols = [
        "chain_direction",
        "stage_from",
        "stage_to",
        "retailer_panel",
        "price_variant",
        "panel_level",
        "intersection_rule",
        "model_family",
    ]
    out = (
        use.groupby(group_cols, dropna=False)
        .agg(
            rows_total=("panel_name", "count"),
            source_variants=("farm_gate_source", "nunique"),
            interpolation_variants=("reconstruction_variant", "nunique"),
            median_n_obs=("n_obs", "median"),
            core_finding_share=("core_finding_flag", "mean"),
            robust_linear_vs_pchip_share=("robust_linear_vs_pchip", "mean"),
            robust_across_reconstruction_share=("robust_across_reconstruction", "mean"),
        )
        .reset_index()
    )
    return out.sort_values(["chain_direction", "stage_from", "stage_to", "retailer_panel", "intersection_rule", "model_family"]).reset_index(drop=True)


def _unified_retail_comparison(model_df: pd.DataFrame, panel_index: pd.DataFrame, combined_diag: pd.DataFrame) -> pd.DataFrame:
    data_rows: List[Dict[str, object]] = []
    if not combined_diag.empty:
        for retailer_panel, grp in combined_diag.groupby("panel_name", dropna=False):
            if pd.isna(retailer_panel):
                continue
            data_rows.append(
                {
                    "comparison_block": "data",
                    "retailer_panel": retailer_panel,
                    "price_variant": "",
                    "chain_direction": "",
                    "stage_from": "",
                    "stage_to": "",
                    "intersection_rule": "",
                    "model_family": "",
                    "rows_total": int(len(grp)),
                    "products_total": int(grp["product"].nunique()) if "product" in grp.columns else 0,
                    "median_source_count": float(pd.to_numeric(grp.get("n_days_2plus_sources"), errors="coerce").median()),
                    "anchor_only_share": np.nan,
                    "core_finding_share": np.nan,
                    "median_n_obs": np.nan,
                    "robust_linear_vs_pchip_share": np.nan,
                    "robust_across_reconstruction_share": np.nan,
                }
            )
    use = _preferred_results(model_df)
    if not use.empty:
        use = use[use["retailer_panel"].isin(["Silpo", "Novus", "Retail_combined", "Retail_combined_core"])].copy()
        use = use[(use["stage_from"] == "Retail") | (use["stage_to"] == "Retail")].copy()
    if use.empty:
        return pd.DataFrame(data_rows)
    model_rows = (
        use.groupby(
            ["retailer_panel", "price_variant", "chain_direction", "stage_from", "stage_to", "intersection_rule", "model_family"],
            dropna=False,
        )
        .agg(
            rows_total=("panel_name", "count"),
            core_finding_share=("core_finding_flag", "mean"),
            median_n_obs=("n_obs", "median"),
            robust_linear_vs_pchip_share=("robust_linear_vs_pchip", "mean"),
            robust_across_reconstruction_share=("robust_across_reconstruction", "mean"),
        )
        .reset_index()
    )
    model_rows["comparison_block"] = "model"
    model_rows["products_total"] = np.nan
    model_rows["median_source_count"] = np.nan
    model_rows["anchor_only_share"] = np.nan
    cols = [
        "comparison_block",
        "retailer_panel",
        "price_variant",
        "chain_direction",
        "stage_from",
        "stage_to",
        "intersection_rule",
        "model_family",
        "rows_total",
        "products_total",
        "median_source_count",
        "anchor_only_share",
        "core_finding_share",
        "median_n_obs",
        "robust_linear_vs_pchip_share",
        "robust_across_reconstruction_share",
    ]
    base = pd.DataFrame(data_rows)
    if base.empty:
        return model_rows.loc[:, cols].reset_index(drop=True)
    return pd.concat([base.loc[:, cols], model_rows.loc[:, cols]], ignore_index=True)


def _intersection_stability(model_df: pd.DataFrame) -> pd.DataFrame:
    use = _preferred_results(model_df)
    if use.empty:
        return pd.DataFrame()
    out = (
        use.groupby(["intersection_rule", "stage_from", "stage_to", "retailer_panel", "model_family"], dropna=False)
        .agg(
            rows_total=("panel_name", "count"),
            median_n_obs=("n_obs", "median"),
            core_finding_share=("core_finding_flag", "mean"),
            robust_linear_vs_pchip_share=("robust_linear_vs_pchip", "mean"),
            robust_across_reconstruction_share=("robust_across_reconstruction", "mean"),
        )
        .reset_index()
    )
    return out.sort_values(["stage_from", "stage_to", "retailer_panel", "intersection_rule", "model_family"]).reset_index(drop=True)


def _save_primary_chain_summary_plots(
    out_dir: Path,
    farmgate_direct_df: pd.DataFrame,
    farmgate_reverse_df: pd.DataFrame,
    unified_retail_df: pd.DataFrame,
    intersection_df: pd.DataFrame,
) -> List[Path]:
    paths: List[Path] = []

    if not farmgate_direct_df.empty:
        pivot = (
            farmgate_direct_df.groupby(["stage_to", "retailer_panel"], dropna=False)["core_finding_share"]
            .mean()
            .unstack(fill_value=np.nan)
            .sort_index()
        )
        if not pivot.empty:
            fig, ax = common.plt.subplots(figsize=(10, 5), facecolor="white")
            im = ax.imshow(pivot.fillna(0).to_numpy(), aspect="auto", cmap="YlGnBu", vmin=0, vmax=1)
            ax.set_xticks(range(len(pivot.columns)))
            ax.set_xticklabels([str(c) for c in pivot.columns], rotation=30, ha="right")
            ax.set_yticks(range(len(pivot.index)))
            ax.set_yticklabels([str(i) for i in pivot.index])
            ax.set_title("Farm-gate direct core-finding share by downstream stage and retail panel")
            for i in range(pivot.shape[0]):
                for j in range(pivot.shape[1]):
                    val = pivot.iloc[i, j]
                    if pd.notna(val):
                        ax.text(j, i, f"{val:.2f}", ha="center", va="center", fontsize=8)
            fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
            p = out_dir / "farmgate_direct_heatmap.png"
            fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
            common.plt.close(fig)
            paths.append(p)

    if not farmgate_reverse_df.empty:
        rev = (
            farmgate_reverse_df.groupby("stage_from", dropna=False)["core_finding_share"]
            .mean()
            .sort_values(ascending=False)
        )
        if not rev.empty:
            fig, ax = common.plt.subplots(figsize=(8, 4.8), facecolor="white")
            ax.bar(rev.index.astype(str), rev.values, color="#4C78A8")
            ax.set_ylim(0, 1)
            ax.set_title("Reverse-to-farm-gate core-finding share")
            ax.set_ylabel("Core-finding share")
            ax.tick_params(axis="x", rotation=25)
            p = out_dir / "farmgate_reverse_corefinding.png"
            fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
            common.plt.close(fig)
            paths.append(p)

    if not unified_retail_df.empty:
        u = unified_retail_df[unified_retail_df["comparison_block"] == "model"].copy()
        u = u[u["stage_to"].eq("Retail") | u["stage_from"].eq("Retail")]
        if not u.empty:
            grp = u.groupby("retailer_panel", dropna=False)["core_finding_share"].mean().sort_values(ascending=False)
            fig, ax = common.plt.subplots(figsize=(8.5, 4.8), facecolor="white")
            ax.bar(grp.index.astype(str), grp.values, color=["#72B7B2", "#54A24B", "#E45756", "#F58518"][: len(grp)])
            ax.set_ylim(0, 1)
            ax.set_title("Retail-panel comparison of core finding share")
            ax.set_ylabel("Core-finding share")
            ax.tick_params(axis="x", rotation=25)
            p = out_dir / "unified_retail_comparison.png"
            fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
            common.plt.close(fig)
            paths.append(p)

    if not intersection_df.empty:
        inter = intersection_df.groupby("intersection_rule", dropna=False)["core_finding_share"].mean().sort_values(ascending=False)
        fig, ax = common.plt.subplots(figsize=(8, 4.6), facecolor="white")
        ax.bar(inter.index.astype(str), inter.values, color="#B279A2")
        ax.set_ylim(0, 1)
        ax.set_title("Intersection-rule stability")
        ax.set_ylabel("Core-finding share")
        ax.tick_params(axis="x", rotation=25)
        p = out_dir / "intersection_stability.png"
        fig.savefig(p, dpi=300, bbox_inches="tight", facecolor="white")
        common.plt.close(fig)
        paths.append(p)

    return paths


def run_primary_chain_pipeline(freq: str = "daily") -> Path:
    _, raw = common.load_raw()
    cleaned = common.prepare_cleaned(raw)
    all_daily = common.build_all_daily(cleaned)
    mapping_audit = rw4_data.build_mapping_audit(cleaned)
    unit_admissibility = rw4_data.build_unit_admissibility(cleaned)
    reconstruction_diag = rw4_data.build_reconstruction_diagnostics(cleaned, all_daily)
    panels, panel_index, combined_diag, combined_methodology = _build_primary_panels(cleaned)

    pretests: List[Dict[str, object]] = []
    model_rows: List[Dict[str, object]] = []
    multiplier_rows: List[pd.DataFrame] = []
    vecm_rows: List[Dict[str, object]] = []
    vecm_irf_rows: List[pd.DataFrame] = []

    for panel in panels:
        meta = panel["meta"].copy()
        frame = panel["frame"].copy()
        frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
        cols = [c for c in ["farm_gate", "producer", "prozorro", "retail", "ConsumerUA", "EU", "CME"] if c in frame.columns]
        should_weekly = freq == "weekly" or (meta["panel_level"] in {"average", "brand"} and len(frame) > 180)
        if cols and should_weekly:
            weekly_vals = _weekly(frame[["date"] + cols], cols)
            shock_week = (
                frame.assign(week=frame["date"].dt.to_period("W-MON").dt.start_time)
                .groupby("week", as_index=False)["shock_dummy"]
                .max()
                .rename(columns={"week": "date"})
            )
            frame = weekly_vals.merge(shock_week, on="date", how="left")
            frame["shock_dummy"] = frame["shock_dummy"].fillna(0).astype(int)
            frame["standardized_type"] = meta["standardized_type"]
            frame["product"] = meta["product"]
            meta["frequency"] = "weekly_from_daily"
        else:
            meta["frequency"] = "daily"

        pair_specs = [
            ("farm_gate", "producer", "forward", "FarmGateUA", "ProducerUA"),
            ("producer", "prozorro", "forward", "ProducerUA", "ProZorro"),
            ("prozorro", "retail", "forward", "ProZorro", "Retail"),
            ("farm_gate", "prozorro", "forward", "FarmGateUA", "ProZorro"),
            ("producer", "retail", "forward", "ProducerUA", "Retail"),
            ("farm_gate", "retail", "forward", "FarmGateUA", "Retail"),
            ("retail", "prozorro", "reverse", "Retail", "ProZorro"),
            ("prozorro", "producer", "reverse", "ProZorro", "ProducerUA"),
            ("retail", "producer", "reverse", "Retail", "ProducerUA"),
            ("producer", "farm_gate", "reverse", "ProducerUA", "FarmGateUA"),
            ("prozorro", "farm_gate", "reverse", "ProZorro", "FarmGateUA"),
            ("retail", "farm_gate", "reverse", "Retail", "FarmGateUA"),
        ]
        for x_col, y_col, direction, stage_from, stage_to in pair_specs:
            if x_col not in frame.columns or y_col not in frame.columns:
                continue
            pre_rows, model_res, mult = _pair_suite(
                meta,
                frame,
                y_col=y_col,
                x_col=x_col,
                direction=direction,
                stage_from=stage_from,
                stage_to=stage_to,
            )
            pretests.extend(pre_rows)
            model_rows.extend(model_res)
            if not mult.empty:
                multiplier_rows.append(mult)

        if all(c in frame.columns for c in ["farm_gate", "producer", "prozorro"]):
            trip = frame[["date", "farm_gate", "producer", "prozorro"]].dropna().copy()
            trip = trip.rename(columns={"farm_gate": "stage_1", "producer": "stage_2", "prozorro": "stage_3"}).set_index("date")
            vr = _fit_vecm_system(np.log(trip.where(trip > 0)), 6, "farmgate_producer_prozorro_triplet", target_name="stage_3")
            if vr is not None:
                fit, irf = vr
                vecm_rows.append(_result_row(meta, fit, "forward", "FarmGateUA", "ProZorro", 0, 0))
                irf["panel_name"] = meta["panel_name"]
                irf["triplet"] = "farmgate_producer_prozorro"
                vecm_irf_rows.append(irf)
        if all(c in frame.columns for c in ["producer", "prozorro", "retail"]):
            trip = frame[["date", "producer", "prozorro", "retail"]].dropna().set_index("date")
            vr = _fit_vecm_system(np.log(trip.where(trip > 0)), 6, "producer_prozorro_retail_triplet", target_name="retail")
            if vr is not None:
                fit, irf = vr
                vecm_rows.append(_result_row(meta, fit, "forward", "ProducerUA", "Retail", 0, 0))
                irf["panel_name"] = meta["panel_name"]
                irf["triplet"] = "producer_prozorro_retail"
                vecm_irf_rows.append(irf)
        if all(c in frame.columns for c in ["farm_gate", "producer", "prozorro", "retail"]):
            quad = frame[["date", "farm_gate", "producer", "prozorro", "retail"]].dropna().set_index("date")
            vr = _fit_vecm_system(np.log(quad.where(quad > 0)), 6, "farmgate_producer_prozorro_retail_system", target_name="retail")
            if vr is not None:
                fit, irf = vr
                vecm_rows.append(_result_row(meta, fit, "forward", "FarmGateUA", "Retail", 0, 0))
                irf["panel_name"] = meta["panel_name"]
                irf["triplet"] = "farmgate_producer_prozorro_retail"
                vecm_irf_rows.append(irf)

    model_df = pd.DataFrame(model_rows + vecm_rows)
    pretest_df = pd.DataFrame(pretests)
    multiplier_df = pd.concat(multiplier_rows, ignore_index=True) if multiplier_rows else pd.DataFrame()
    vecm_irf_df = pd.concat(vecm_irf_rows, ignore_index=True) if vecm_irf_rows else pd.DataFrame()

    variant_rob = _variant_robustness(model_df)
    source_rob = _farmgate_source_comparison(model_df)
    if not model_df.empty:
        merge_keys_variant = [
            "panel_level",
            "segment_name",
            "standardized_type",
            "retailer_panel",
            "brand",
            "price_variant",
            "intersection_rule",
            "farm_gate_source",
            "chain_direction",
            "stage_from",
            "stage_to",
            "model_family",
        ]
        model_df = model_df.merge(
            variant_rob[merge_keys_variant + ["robust_linear_vs_pchip", "interpolation_sensitive"]],
            on=merge_keys_variant,
            how="left",
        )
        merge_keys_source = [
            "panel_level",
            "segment_name",
            "standardized_type",
            "retailer_panel",
            "brand",
            "price_variant",
            "intersection_rule",
            "reconstruction_variant",
            "chain_direction",
            "stage_from",
            "stage_to",
            "model_family",
        ]
        model_df = model_df.merge(
            source_rob[merge_keys_source + ["robust_across_reconstruction"]],
            on=merge_keys_source,
            how="left",
        )
        model_df["robust_linear_vs_pchip"] = model_df["robust_linear_vs_pchip"].fillna(0).astype(int)
        model_df["interpolation_sensitive"] = model_df["interpolation_sensitive"].fillna(1).astype(int)
        model_df["robust_across_reconstruction"] = model_df["robust_across_reconstruction"].fillna(0).astype(int)
        model_df["core_finding_flag"] = (
            (model_df["model_status"] == "ok")
            & model_df["robust_linear_vs_pchip"].eq(1)
            & model_df["robust_across_reconstruction"].eq(1)
            & model_df["interpolation_sensitive"].eq(0)
        ).astype(int)

    benchmark_cmp = _benchmark_comparison_rows(panels)
    coverage_df = _coverage_validation(model_df, panel_index)
    reverse_df = model_df[model_df["chain_direction"] == "reverse"].copy() if not model_df.empty else pd.DataFrame()
    raw_milk_df = model_df[model_df["stage_from"] == "FarmGateUA"].copy() if not model_df.empty else pd.DataFrame()
    avg_df = model_df[model_df["panel_level"] == "average"].copy() if not model_df.empty else pd.DataFrame()
    brand_df = model_df[model_df["panel_level"] == "brand"].copy() if not model_df.empty else pd.DataFrame()
    farmgate_direct_df = _farmgate_summary(model_df, "direct")
    farmgate_reverse_df = _farmgate_summary(model_df, "reverse")
    farmgate_stability_df = _farmgate_variant_stability(model_df)
    unified_retail_df = _unified_retail_comparison(model_df, panel_index, combined_diag)
    intersection_df = _intersection_stability(model_df)

    rule_df = pd.DataFrame(
        [
            {
                "pipeline_version": "RW4",
                "primary_chain_doc": PRIMARY_CHAIN_DOC,
                "farm_gate_inputs": "farm_gate_daily.xlsx + farm_gate_all_missing_filled_daily.xlsx",
                "reconstruction_variants": "linear,pchip",
                "core_chain": "FarmGateUA -> ProducerUA -> ProZorro -> Retail",
                "reverse_chain": "Retail -> ProZorro -> ProducerUA -> FarmGateUA",
                "benchmarks_role": "ConsumerUA, EU, CME are external comparison benchmarks only",
                "retail_combined_rule": "Retail_combined is the anchored weighted geometric mean of bias-aligned Silpo observed, Novus observed, and ConsumerUA; Retail_combined_core keeps the retailer-only support window.",
                "intersection_rules": "chain_common_support, pairwise_overlap, comparison_panel, brand_top_sku",
            }
        ]
    )

    out_summary = common.get_output_dir("primary_chain_summary")
    image_paths = _save_primary_chain_summary_plots(
        out_summary,
        farmgate_direct_df,
        farmgate_reverse_df,
        unified_retail_df,
        intersection_df,
    )
    common.write_tables_xlsx(
        out_summary / "primary_chain_consolidated.xlsx",
        {
            "Consolidated_ModelCoefficients": model_df,
            "Consolidated_PreTests": pretest_df,
            "Panel_Index": panel_index,
            "ReverseFlow_ModelCoefficients": reverse_df,
            "RawMilk_To_Product_Transmission": raw_milk_df,
            "AveragePrice_Chain_Transmission": avg_df,
            "Retailer_Brand_Transmission": brand_df,
            "Variant_Robustness": variant_rob,
            "FarmGate_Source_Comparison": source_rob,
            "FarmGate_Direct_Summary": farmgate_direct_df,
            "FarmGate_Reverse_Summary": farmgate_reverse_df,
            "FarmGate_Variant_Stability": farmgate_stability_df,
            "Unified_Retail_Comparison": unified_retail_df,
            "Intersection_Stability": intersection_df,
            "Benchmark_Comparison": benchmark_cmp,
            "Coverage_Validation": coverage_df,
            "Reconstruction_Diagnostics": reconstruction_diag,
            "Mapping_Audit": mapping_audit,
            "Unit_Admissibility": unit_admissibility,
            "Retail_Combined_Diagnostics": combined_diag,
            "Retail_Combined_Methodology": combined_methodology,
            "NARDL_Multipliers": multiplier_df,
            "VECM_IRF": vecm_irf_df,
            "Rule_Documentation": rule_df,
        },
    )
    common.save_pdf_report(
        out_summary / "primary_chain_consolidated.pdf",
        "RW4 Primary Chain Consolidated Summary",
        [
            PRIMARY_CHAIN_DOC,
            f"panel_count={len(panel_index)}",
            f"model_rows={len(model_df)}",
            f"reverse_rows={len(reverse_df)}",
            f"benchmark_rows={len(benchmark_cmp)}",
        ],
        {
            "Consolidated_ModelCoefficients": model_df,
            "Variant_Robustness": variant_rob,
            "FarmGate_Source_Comparison": source_rob,
            "FarmGate_Direct_Summary": farmgate_direct_df,
            "FarmGate_Reverse_Summary": farmgate_reverse_df,
            "Unified_Retail_Comparison": unified_retail_df,
            "Intersection_Stability": intersection_df,
            "Benchmark_Comparison": benchmark_cmp,
        },
        image_paths,
    )
    return out_summary


def _load_primary_consolidated() -> pd.DataFrame:
    p = common.OUTPUT_ROOT / "primary_chain_summary" / "primary_chain_consolidated.xlsx"
    if not p.exists():
        run_primary_chain_pipeline(freq="daily")
    if not p.exists():
        return pd.DataFrame()
    try:
        return pd.read_excel(p, sheet_name="Consolidated_ModelCoefficients")
    except Exception:
        return pd.DataFrame()


def run_primary_model_family_report(family: str) -> Path:
    cons_path = common.OUTPUT_ROOT / "primary_chain_summary" / "primary_chain_consolidated.xlsx"
    if not cons_path.exists():
        run_primary_chain_pipeline(freq="daily")
    cons = _load_primary_consolidated()
    fam = cons[cons["model_family"] == family].copy() if not cons.empty else pd.DataFrame()
    module_name = f"model_{family.lower()}"
    out = common.get_output_dir(module_name)
    common.write_tables_xlsx(out / f"{module_name}_output.xlsx", {f"{family}_Summary": fam})
    common.save_pdf_report(
        out / f"{module_name}_report.pdf",
        f"{family} Summary from RW4 Primary Chain",
        [
            PRIMARY_CHAIN_DOC,
            f"family={family}",
            f"rows={len(fam)}",
            f"source={cons_path}",
        ],
        {f"{family}_Summary": fam},
        [],
    )
    return out


def run_synthetic_consumer_chain(freq: str = "daily") -> Path:
    _, raw = common.load_raw()
    cleaned = common.prepare_cleaned(raw)
    consumer = _benchmark_series(cleaned, "ConsumerUA")
    retail, _, _ = _combined_retail_panel(cleaned, include_consumer=False, panel_name="Retail_combined_core")
    producer = _producer_series(cleaned, "pchip")
    if consumer.empty or retail.empty:
        out = common.get_output_dir("secondary_synthetic_consumer")
        note = pd.DataFrame([{"note": "Consumer or combined retail series unavailable for RW4 synthetic consumer module."}])
        common.write_tables_xlsx(out / "secondary_synthetic_consumer_output.xlsx", {"Synthetic_Consumer_Link": note})
        common.save_pdf_report(out / "secondary_synthetic_consumer_report.pdf", "RW4 Synthetic Consumer", ["No sufficient overlap."], {"Synthetic_Consumer_Link": note}, [])
        return out

    rows = []
    preds = []
    for product in sorted(set(consumer["product"]).intersection(set(retail["product"]))):
        c = consumer[consumer["product"] == product][["date", "standardized_type", "ConsumerUA"]]
        r = retail[retail["product"] == product][["date", "standardized_type", "retail"]]
        p = producer[producer["product"] == product][["date", "standardized_type", "producer"]]
        d = c.merge(r, on=["date", "standardized_type"], how="inner").merge(p, on=["date", "standardized_type"], how="left")
        d = d[(d["ConsumerUA"] > 0) & (d["retail"] > 0)].dropna()
        if len(d) < 25:
            continue
        d["d_consumer"] = _safe_log(d["ConsumerUA"]).diff()
        d["d_retail"] = _safe_log(d["retail"]).diff()
        d["d_producer"] = _safe_log(d["producer"]).diff()
        reg = d[["d_consumer", "d_retail", "d_producer"]].dropna()
        if len(reg) < 20:
            continue
        fit = sm.OLS(reg["d_consumer"], sm.add_constant(reg[["d_retail", "d_producer"]], has_constant="add")).fit(cov_type="HAC", cov_kwds={"maxlags": 3})
        rows.append(
            {
                "product": product,
                "standardized_type": d["standardized_type"].mode().iloc[0] if not d["standardized_type"].mode().empty else "",
                "n_obs": int(len(reg)),
                "coef_retail": float(fit.params.get("d_retail", np.nan)),
                "p_retail": float(fit.pvalues.get("d_retail", np.nan)),
                "coef_producer": float(fit.params.get("d_producer", np.nan)),
                "p_producer": float(fit.pvalues.get("d_producer", np.nan)),
                "r2": float(fit.rsquared),
            }
        )
        preds.append(d.assign(synthetic_consumer=np.exp(np.log(d["retail"]) * float(fit.params.get("d_retail", 0.0)))))

    link_df = pd.DataFrame(rows)
    pred_df = pd.concat(preds, ignore_index=True) if preds else pd.DataFrame()
    out = common.get_output_dir("secondary_synthetic_consumer")
    common.write_tables_xlsx(out / "secondary_synthetic_consumer_output.xlsx", {"Synthetic_Consumer_Link": link_df, "Synthetic_Consumer_Predictions": pred_df})
    common.save_pdf_report(
        out / "secondary_synthetic_consumer_report.pdf",
        "RW4 Synthetic Consumer",
        [f"link_rows={len(link_df)}", PRIMARY_CHAIN_DOC],
        {"Synthetic_Consumer_Link": link_df},
        [],
    )
    return out
