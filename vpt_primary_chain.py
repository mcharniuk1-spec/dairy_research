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


RETAIL_VARIANTS = ["silpo", "novus", "silpo_novus"]
PROMO_VARIANTS = ["observed", "promo_controlled"]

PRIMARY_CHAIN_DOC = (
    "Primary chain is strictly ProducerUA -> ProZorro -> Retail. "
    "Retail is estimated separately for silpo, novus, and silpo_novus. "
    "Combined rule: daily median of available silpo and novus standardized_type prices."
)


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


def _median_series(df: pd.DataFrame, value_col: str, group_cols: List[str]) -> pd.DataFrame:
    d = df.copy()
    d[value_col] = pd.to_numeric(d[value_col], errors="coerce")
    d = d.dropna(subset=group_cols + [value_col])
    if d.empty:
        return pd.DataFrame(columns=group_cols + [value_col])
    return d.groupby(group_cols, as_index=False)[value_col].median()


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
    try:
        sel = ardl_select_order(d["y"], max_lag, d[["x"]], max_lag, ic="aic", trend="c")
        ar = sel.model.fit(cov_type="HAC", cov_kwds={"maxlags": min(3, max(1, max_lag // 2))})
        phi = float(np.nansum([v for k, v in ar.params.items() if str(k).startswith("y.L")]))
        beta = float(np.nansum([v for k, v in ar.params.items() if str(k).startswith("x.L")]))
        lr = beta / (1.0 - phi) if abs(1.0 - phi) > 1e-8 else np.nan
        sr = float(ar.params.get("x.L0", np.nan))
        uecm_res = UECM.from_ardl(sel.model).fit(cov_type="HAC", cov_kwds={"maxlags": min(3, max(1, max_lag // 2))})
        bt = uecm_res.bounds_test(case=3)
        lower_p = float(bt.p_values.get("lower", np.nan))
        upper_p = float(bt.p_values.get("upper", np.nan))
        notes = f"bounds_lower_p={lower_p:.4g}; bounds_upper_p={upper_p:.4g}"
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
        fit = best["fit"]
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
    m_pos = []
    m_neg = []
    cur_pos = 0.0
    cur_neg = 0.0
    for _h in horizon:
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


def _fit_vecm_triplet(log_panel: pd.DataFrame, max_lag: int) -> Optional[Tuple[FitResult, pd.DataFrame]]:
    d = log_panel.dropna()
    if len(d) < 36:
        return None
    try:
        max_l = min(max_lag, 8)
        sel = select_order(d, maxlags=max_l, deterministic="ci")
        ka = sel.aic if sel.aic is not None else 2
        k_diff = max(1, int(ka) - 1)
        rank = int(select_coint_rank(d, det_order=0, k_ar_diff=k_diff, signif=0.05).rank)
        if rank < 1:
            return None
        fit = VECM(d, k_ar_diff=k_diff, coint_rank=rank, deterministic="ci").fit()
        # Retail equation assumed third in order: producer, prozorro, retail
        ect = float(fit.alpha[2, 0]) if fit.alpha.shape[0] >= 3 else np.nan
        irf = fit.irf(12).irfs
        irf_tbl = []
        names = list(d.columns)
        if irf.ndim == 3 and len(names) == irf.shape[1]:
            shock_idx = {n: i for i, n in enumerate(names)}
            i_ret = shock_idx.get("retail")
            i_prod = shock_idx.get("producer")
            i_pz = shock_idx.get("prozorro")
            for h in range(irf.shape[0]):
                irf_tbl.append(
                    {
                        "horizon": h,
                        "irf_retail_to_producer": float(irf[h, i_ret, i_prod]) if i_ret is not None and i_prod is not None else np.nan,
                        "irf_retail_to_prozorro": float(irf[h, i_ret, i_pz]) if i_ret is not None and i_pz is not None else np.nan,
                    }
                )
        irf_df = pd.DataFrame(irf_tbl)
        resid = pd.DataFrame(fit.resid, index=d.index[k_diff + 1 :], columns=d.columns).get("retail")
        return (
            FitResult(
                family="VECM",
                link="producer_prozorro_retail",
                y_series="retail",
                x_series="producer+prozorro",
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
            irf_df,
        )
    except Exception:
        return None


def _build_primary_inputs(cleaned: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    producer = cleaned["ProducerUA"].copy()
    producer["producer_price"] = pd.to_numeric(
        producer.get("price_pchip_input", np.nan), errors="coerce"
    ).fillna(pd.to_numeric(producer.get("price_linear_input", np.nan), errors="coerce")).fillna(
        pd.to_numeric(producer.get("price", np.nan), errors="coerce")
    )
    producer = _median_series(producer, "producer_price", ["date", "standardized_type"]).rename(columns={"producer_price": "producer"})

    pz = cleaned["ProZorro"].copy()
    pz["prozorro"] = pd.to_numeric(pz.get("price", np.nan), errors="coerce")
    pz = _median_series(pz, "prozorro", ["date", "standardized_type"])

    sil = cleaned["Silpo"].copy()
    sil["silpo_observed"] = pd.to_numeric(sil.get("price_current", sil.get("price", np.nan)), errors="coerce")
    sil["silpo_regular"] = pd.to_numeric(sil.get("baseline_price", sil.get("price_current", np.nan)), errors="coerce")
    sil_obs = _median_series(sil, "silpo_observed", ["date", "standardized_type"])
    sil_reg = _median_series(sil, "silpo_regular", ["date", "standardized_type"])
    sil_m = sil_obs.merge(sil_reg, on=["date", "standardized_type"], how="outer")

    nov = cleaned["Novus"].copy()
    nov["novus_observed"] = pd.to_numeric(nov.get("price_current", nov.get("price", np.nan)), errors="coerce")
    nov_regular = np.where(
        pd.to_numeric(nov.get("discount_present", 0), errors="coerce").fillna(0).astype(int) == 0,
        pd.to_numeric(nov.get("price_current", nov.get("price", np.nan)), errors="coerce"),
        np.nan,
    )
    nov["novus_regular"] = pd.Series(nov_regular, index=nov.index).fillna(
        pd.to_numeric(nov.get("price_current", nov.get("price", np.nan)), errors="coerce")
    )
    nov_obs = _median_series(nov, "novus_observed", ["date", "standardized_type"])
    nov_reg = _median_series(nov, "novus_regular", ["date", "standardized_type"])
    nov_m = nov_obs.merge(nov_reg, on=["date", "standardized_type"], how="outer")

    chain = producer.merge(pz, on=["date", "standardized_type"], how="outer")
    chain = chain.merge(sil_m, on=["date", "standardized_type"], how="outer")
    chain = chain.merge(nov_m, on=["date", "standardized_type"], how="outer")

    chain["combined_observed"] = chain[["silpo_observed", "novus_observed"]].median(axis=1, skipna=True)
    chain["combined_regular"] = chain[["silpo_regular", "novus_regular"]].median(axis=1, skipna=True)
    chain["combined_rule"] = "daily_median_of_available_silpo_novus"
    chain["date"] = pd.to_datetime(chain["date"], errors="coerce")
    chain = chain.dropna(subset=["date", "standardized_type"]).sort_values(["standardized_type", "date"])
    return chain


def _plot_timeseries(df: pd.DataFrame, out_path: Path, title: str) -> None:
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
    d = df.copy().dropna(subset=["date"])
    for col in ["producer", "prozorro", "retail"]:
        if col in d.columns:
            y = pd.to_numeric(d[col], errors="coerce")
            if y.notna().sum() > 2:
                ax.plot(d["date"], y, label=col, linewidth=1.4)
    ax.set_title(title)
    ax.set_xlabel("date")
    ax.legend(frameon=False)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def _plot_lag_profile(df: pd.DataFrame, out_path: Path, title: str) -> None:
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
    for pair in sorted(df["pair"].unique().tolist()):
        s = df[df["pair"] == pair].sort_values("lag")
        ax.plot(s["lag"], s["corr"], marker="o", label=pair)
    ax.axhline(0.0, color="#888888", linewidth=0.8)
    ax.set_title(title)
    ax.set_xlabel("lag")
    ax.set_ylabel("corr")
    ax.legend(frameon=False)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def _build_lag_profile(df: pd.DataFrame, max_lag: int) -> pd.DataFrame:
    rows = []
    for pair, a, b in [
        ("producer_to_prozorro", "prozorro", "producer"),
        ("prozorro_to_retail", "retail", "prozorro"),
        ("producer_to_retail", "retail", "producer"),
    ]:
        for lag in range(1, max_lag + 1):
            tmp = pd.concat(
                [pd.to_numeric(df[a], errors="coerce"), pd.to_numeric(df[b], errors="coerce").shift(lag)],
                axis=1,
            ).dropna()
            if len(tmp) < 10:
                continue
            rows.append({"pair": pair, "lag": lag, "corr": float(tmp.iloc[:, 0].corr(tmp.iloc[:, 1]))})
    return pd.DataFrame(rows)


def _write_variant_output(
    out_dir: Path,
    tables: Dict[str, pd.DataFrame],
    images: List[Path],
    note_lines: List[str],
) -> None:
    xlsx = out_dir / "primary_chain_output.xlsx"
    common.write_tables_xlsx(xlsx, tables)
    pdf = out_dir / "primary_chain_report.pdf"
    common.save_pdf_report(
        pdf,
        "Primary VPT Chain: ProducerUA -> ProZorro -> Retail",
        note_lines,
        tables,
        images,
    )


def run_primary_chain_pipeline(freq: str = "weekly") -> Path:
    _, raw = common.load_raw()
    cleaned = common.prepare_cleaned(raw)
    chain_daily = _build_primary_inputs(cleaned)
    if chain_daily.empty:
        out = common.get_output_dir("primary_chain_summary")
        common.write_tables_xlsx(out / "primary_chain_consolidated.xlsx", {"Consolidated_ModelCoefficients": pd.DataFrame()})
        return out

    max_lag = 10 if freq == "weekly" else 30
    consolidated_models: List[Dict[str, object]] = []
    consolidated_pretests: List[Dict[str, object]] = []
    consolidated_diags: List[Dict[str, object]] = []
    consolidated_eligibility: List[Dict[str, object]] = []

    for std in sorted(chain_daily["standardized_type"].dropna().unique().tolist()):
        base_std = chain_daily[chain_daily["standardized_type"] == std].copy()
        if base_std.empty:
            continue
        for retailer in RETAIL_VARIANTS:
            for promo in PROMO_VARIANTS:
                retail_col = {
                    ("silpo", "observed"): "silpo_observed",
                    ("silpo", "promo_controlled"): "silpo_regular",
                    ("novus", "observed"): "novus_observed",
                    ("novus", "promo_controlled"): "novus_regular",
                    ("silpo_novus", "observed"): "combined_observed",
                    ("silpo_novus", "promo_controlled"): "combined_regular",
                }[(retailer, promo)]
                d = base_std[["date", "producer", "prozorro", retail_col, "combined_rule"]].rename(columns={retail_col: "retail"})
                if freq == "weekly":
                    d = _weekly(d, ["producer", "prozorro", "retail"])
                d = d.dropna(subset=["producer", "prozorro", "retail"]).sort_values("date")
                insufficient_overlap = len(d) < 20

                # Enforce identical sample by strict inner overlap in one frame
                d = d[["date", "producer", "prozorro", "retail"]].dropna().copy()

                # Pre-tests
                pt_rows = []
                classes = {}
                for sname in ["producer", "prozorro", "retail"]:
                    st = _integration_class(d[sname])
                    classes[sname] = st["integration_class"]
                    row = {"series": sname}
                    row.update(st)
                    row["standardized_type"] = std
                    row["retailer"] = retailer
                    row["promo_variant"] = promo
                    pt_rows.append(row)
                    consolidated_pretests.append(row.copy())

                pair_rows = []
                for left, right, pname in [
                    ("producer", "prozorro", "producer_to_prozorro"),
                    ("prozorro", "retail", "prozorro_to_retail"),
                    ("producer", "retail", "producer_to_retail"),
                ]:
                    cp = np.nan
                    try:
                        cp = float(coint(_safe_log(d[left]).dropna(), _safe_log(d[right]).dropna())[1])
                    except Exception:
                        pass
                    pair_rows.append(
                        {
                            "series": pname,
                            "integration_class": "pair",
                            "adf_level_p": np.nan,
                            "kpss_level_p": np.nan,
                            "adf_diff1_p": np.nan,
                            "kpss_diff1_p": np.nan,
                            "adf_diff2_p": np.nan,
                            "kpss_diff2_p": np.nan,
                            "stability_flag": np.nan,
                            "cointegration_p": cp,
                            "standardized_type": std,
                            "retailer": retailer,
                            "promo_variant": promo,
                        }
                    )
                pretests = pd.DataFrame(pt_rows + pair_rows)

                any_i2 = any(v == "I(2)" for v in classes.values())
                eligibility_note = (
                    "Rejected for ARDL/ECM due to I(2) presence."
                    if any_i2
                    else "Admissible for ARDL/ECM subject to cointegration and diagnostics."
                )
                if insufficient_overlap:
                    eligibility_note = "Insufficient common sample after alignment; model outputs are placeholders."

                # Lag/correlation profile
                lag_profile = _build_lag_profile(d, max_lag=max_lag)

                model_rows = []
                diag_rows = []
                ect_plot_df = pd.DataFrame()
                nardl_mult = pd.DataFrame()
                irf_df = pd.DataFrame()

                if not any_i2 and not insufficient_overlap:
                    # Pair links in strict chain
                    for link, y, x in [
                        ("producer_to_prozorro", "prozorro", "producer"),
                        ("prozorro_to_retail", "retail", "prozorro"),
                    ]:
                        logy = _safe_log(d[y])
                        logx = _safe_log(d[x])
                        ar = _fit_ardl_pair(logy, logx, max_lag=max_lag)
                        if ar is not None:
                            ar.link = link
                            ar.y_series = y
                            ar.x_series = x
                            dg = _resid_diag(ar.residuals if ar.residuals is not None else pd.Series(dtype=float))
                            ar.unreliable = int(dg["unreliable_flag"])
                            ar.model_status = "unreliable" if ar.unreliable else "ok"
                            model_rows.append(ar)
                            diag_rows.append(
                                {
                                    "model_family": ar.family,
                                    "link": ar.link,
                                    "y_series": y,
                                    "x_series": x,
                                    **dg,
                                }
                            )

                        both_i1 = classes.get(y) == "I(1)" and classes.get(x) == "I(1)"
                        ec = _fit_ecm_pair(logy, logx, max_lag=max_lag) if both_i1 else None
                        if ec is not None and pd.notna(ec.ect_coef) and pd.notna(ec.ect_pvalue):
                            if not (ec.ect_coef < 0 and ec.ect_pvalue < 0.10):
                                ec.model_status = "unreliable"
                                ec.unreliable = 1
                                ec.notes = ec.notes + "; ect_not_negative_significant"
                            ec.link = link
                            ec.y_series = y
                            ec.x_series = x
                            dg = _resid_diag(ec.residuals if ec.residuals is not None else pd.Series(dtype=float))
                            ec.unreliable = int(max(ec.unreliable, dg["unreliable_flag"]))
                            if ec.unreliable:
                                ec.model_status = "unreliable"
                            model_rows.append(ec)
                            diag_rows.append(
                                {
                                    "model_family": ec.family,
                                    "link": ec.link,
                                    "y_series": y,
                                    "x_series": x,
                                    **dg,
                                }
                            )
                            ect_plot_df = pd.concat(
                                [ect_plot_df, pd.DataFrame({"date": d["date"], "y": logy, "x": logx})],
                                ignore_index=True,
                            )

                        na = _fit_nardl_pair(logy, logx, max_lag=max_lag)
                        if na is not None:
                            na_fit, na_mult = na
                            na_fit.link = link
                            na_fit.y_series = y
                            na_fit.x_series = x
                            dg = _resid_diag(na_fit.residuals if na_fit.residuals is not None else pd.Series(dtype=float))
                            na_fit.unreliable = int(dg["unreliable_flag"])
                            na_fit.model_status = "unreliable" if na_fit.unreliable else "ok"
                            model_rows.append(na_fit)
                            diag_rows.append(
                                {
                                    "model_family": na_fit.family,
                                    "link": na_fit.link,
                                    "y_series": y,
                                    "x_series": x,
                                    **dg,
                                }
                            )
                            na_mult = na_mult.copy()
                            na_mult["link"] = link
                            nardl_mult = pd.concat([nardl_mult, na_mult], ignore_index=True)

                    # VECM only if all 3 are I(1)
                    if all(classes.get(v) == "I(1)" for v in ["producer", "prozorro", "retail"]):
                        trip = pd.DataFrame(
                            {
                                "producer": _safe_log(d["producer"]),
                                "prozorro": _safe_log(d["prozorro"]),
                                "retail": _safe_log(d["retail"]),
                            },
                            index=d["date"],
                        ).dropna()
                        vr = _fit_vecm_triplet(trip, max_lag=max_lag)
                        if vr is not None:
                            vf, irf = vr
                            dg = _resid_diag(vf.residuals if vf.residuals is not None else pd.Series(dtype=float))
                            vf.unreliable = int(dg["unreliable_flag"])
                            vf.model_status = "unreliable" if vf.unreliable else "ok"
                            model_rows.append(vf)
                            diag_rows.append(
                                {
                                    "model_family": vf.family,
                                    "link": vf.link,
                                    "y_series": vf.y_series,
                                    "x_series": vf.x_series,
                                    **dg,
                                }
                            )
                            irf_df = irf.copy()

                model_coef = pd.DataFrame(
                    [
                        {
                            "standardized_type": std,
                            "retailer": retailer,
                            "promo_variant": promo,
                            "frequency": freq,
                            "link": m.link,
                            "model_family": m.family,
                            "y_series": m.y_series,
                            "x_series": m.x_series,
                            "n_obs": m.n_obs,
                            "sr_coef": m.sr_coef,
                            "lr_coef": m.lr_coef,
                            "ect_coef": m.ect_coef,
                            "ect_pvalue": m.ect_pvalue,
                            "asymmetry_short_p": m.asym_short_p,
                            "asymmetry_long_p": m.asym_long_p,
                            "vecm_rank": m.vecm_rank,
                            "model_status": m.model_status,
                            "unreliable_flag": m.unreliable,
                            "notes": m.notes,
                            "primary_chain_doc": PRIMARY_CHAIN_DOC,
                        }
                        for m in model_rows
                    ]
                )
                if model_coef.empty:
                    model_coef = pd.DataFrame(
                        [
                            {
                                "standardized_type": std,
                                "retailer": retailer,
                                "promo_variant": promo,
                                "frequency": freq,
                                "link": "none",
                                "model_family": "none",
                                "y_series": "n/a",
                                "x_series": "n/a",
                                "n_obs": int(len(d)),
                                "sr_coef": np.nan,
                                "lr_coef": np.nan,
                                "ect_coef": np.nan,
                                "ect_pvalue": np.nan,
                                "asymmetry_short_p": np.nan,
                                "asymmetry_long_p": np.nan,
                                "vecm_rank": np.nan,
                                "model_status": "unavailable",
                                "unreliable_flag": 1,
                                "notes": "No admissible model estimated for this retailer/variant in aligned sample.",
                                "primary_chain_doc": PRIMARY_CHAIN_DOC,
                            }
                        ]
                    )
                diag_df = pd.DataFrame(diag_rows)
                if diag_df.empty:
                    diag_df = pd.DataFrame(
                        [
                            {
                                "model_family": "none",
                                "link": "none",
                                "y_series": "n/a",
                                "x_series": "n/a",
                                "ljungbox_p": np.nan,
                                "arch_p": np.nan,
                                "jb_p": np.nan,
                                "unreliable_flag": 1,
                            }
                        ]
                    )

                series_used = d.copy()
                series_used["standardized_type"] = std
                series_used["retailer"] = retailer
                series_used["promo_variant"] = promo
                series_used["combined_rule"] = "daily_median_of_available_silpo_novus"

                eligibility = pd.DataFrame(
                    [
                        {
                            "standardized_type": std,
                            "retailer": retailer,
                            "promo_variant": promo,
                            "frequency": freq,
                            "integration_producer": classes.get("producer"),
                            "integration_prozorro": classes.get("prozorro"),
                            "integration_retail": classes.get("retail"),
                            "any_i2": int(any_i2),
                            "eligibility_note": eligibility_note,
                        }
                    ]
                )

                # Graphs
                out_dir = common.OUTPUT_ROOT / std / retailer
                out_dir.mkdir(parents=True, exist_ok=True)
                images: List[Path] = []
                img_ts = out_dir / f"time_series_{promo}.png"
                _plot_timeseries(series_used[["date", "producer", "prozorro", "retail"]], img_ts, f"{std} | {retailer} | {promo}")
                images.append(img_ts)
                if not lag_profile.empty:
                    img_lag = out_dir / f"lag_profile_{promo}.png"
                    _plot_lag_profile(lag_profile, img_lag, f"Lag-Correlation Profile | {std} | {retailer} | {promo}")
                    images.append(img_lag)
                if not ect_plot_df.empty:
                    img_ect = out_dir / f"ecm_adjustment_{promo}.png"
                    _plot_timeseries(
                        pd.DataFrame({"date": d["date"], "producer": _safe_log(d["producer"]), "prozorro": _safe_log(d["prozorro"]), "retail": _safe_log(d["retail"])}),
                        img_ect,
                        f"ECM Level Alignment (log) | {std} | {retailer} | {promo}",
                    )
                    images.append(img_ect)
                if not nardl_mult.empty:
                    import matplotlib.pyplot as plt

                    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
                    for link in sorted(nardl_mult["link"].unique().tolist()):
                        s = nardl_mult[nardl_mult["link"] == link]
                        ax.plot(s["horizon"], s["mult_pos"], label=f"{link}: pos")
                        ax.plot(s["horizon"], s["mult_neg"], linestyle="--", label=f"{link}: neg")
                    ax.set_title(f"NARDL Dynamic Multipliers | {std} | {retailer} | {promo}")
                    ax.set_xlabel("horizon")
                    ax.legend(frameon=False)
                    img_n = out_dir / f"nardl_multipliers_{promo}.png"
                    fig.savefig(img_n, dpi=300, bbox_inches="tight", facecolor="white")
                    plt.close(fig)
                    images.append(img_n)
                if not irf_df.empty:
                    import matplotlib.pyplot as plt

                    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
                    ax.plot(irf_df["horizon"], irf_df["irf_retail_to_producer"], label="retail<-producer shock")
                    ax.plot(irf_df["horizon"], irf_df["irf_retail_to_prozorro"], label="retail<-prozorro shock")
                    ax.axhline(0.0, color="#888888", linewidth=0.8)
                    ax.set_title(f"VECM IRF (Retail Equation) | {std} | {retailer} | {promo}")
                    ax.set_xlabel("horizon")
                    ax.legend(frameon=False)
                    img_i = out_dir / f"vecm_irf_{promo}.png"
                    fig.savefig(img_i, dpi=300, bbox_inches="tight", facecolor="white")
                    plt.close(fig)
                    images.append(img_i)

                tables = {
                    "PreTests": pretests,
                    "ModelCoefficients": model_coef,
                    "ResidualDiagnostics": diag_df,
                    "SeriesUsed": series_used,
                    "LagProfile": lag_profile,
                    "ModelEligibility": eligibility,
                    "NARDL_Multipliers": nardl_mult,
                    "VECM_IRF": irf_df,
                }
                _write_variant_output(
                    out_dir=out_dir,
                    tables=tables,
                    images=images,
                    note_lines=[
                        f"standardized_type={std}",
                        f"retailer={retailer}",
                        f"promo_variant={promo}",
                        f"frequency={freq}",
                        PRIMARY_CHAIN_DOC,
                    ],
                )

                consolidated_models.extend(model_coef.to_dict("records"))
                for r in diag_df.to_dict("records"):
                    r["standardized_type"] = std
                    r["retailer"] = retailer
                    r["promo_variant"] = promo
                    consolidated_diags.append(r)
                consolidated_eligibility.extend(eligibility.to_dict("records"))

    out_summary = common.get_output_dir("primary_chain_summary")
    cons_models = pd.DataFrame(consolidated_models)
    cons_pre = pd.DataFrame(consolidated_pretests)
    cons_diag = pd.DataFrame(consolidated_diags)
    cons_elig = pd.DataFrame(consolidated_eligibility)
    rule_df = pd.DataFrame(
        [
            {
                "primary_chain_doc": PRIMARY_CHAIN_DOC,
                "frequency_primary": freq,
                "max_lag_weekly": 10,
                "max_lag_daily": 30,
                "retail_series_rule": "silpo_price, novus_price, combined_price built per standardized_type",
                "promo_policy": "observed and promo_controlled are estimated separately and flagged",
            }
        ]
    )
    common.write_tables_xlsx(
        out_summary / "primary_chain_consolidated.xlsx",
        {
            "Consolidated_ModelCoefficients": cons_models,
            "Consolidated_PreTests": cons_pre,
            "Consolidated_ResidualDiagnostics": cons_diag,
            "Consolidated_Eligibility": cons_elig,
            "Rule_Documentation": rule_df,
        },
    )
    common.save_pdf_report(
        out_summary / "primary_chain_consolidated.pdf",
        "Primary Chain Consolidated Summary",
        [
            PRIMARY_CHAIN_DOC,
            f"model_rows={len(cons_models)}",
            f"pretest_rows={len(cons_pre)}",
            f"diagnostic_rows={len(cons_diag)}",
            f"eligibility_rows={len(cons_elig)}",
        ],
        {
            "Consolidated_ModelCoefficients": cons_models,
            "Consolidated_PreTests": cons_pre,
            "Consolidated_ResidualDiagnostics": cons_diag,
            "Consolidated_Eligibility": cons_elig,
        },
        [],
    )
    return out_summary


def _load_primary_consolidated() -> pd.DataFrame:
    p = common.OUTPUT_ROOT / "primary_chain_summary" / "primary_chain_consolidated.xlsx"
    if not p.exists():
        run_primary_chain_pipeline(freq="weekly")
    if not p.exists():
        return pd.DataFrame()
    try:
        return pd.read_excel(p, sheet_name="Consolidated_ModelCoefficients")
    except Exception:
        return pd.DataFrame()


def run_primary_model_family_report(family: str) -> Path:
    cons_path = common.OUTPUT_ROOT / "primary_chain_summary" / "primary_chain_consolidated.xlsx"
    out_primary = common.get_output_dir("primary_chain_summary")
    if not cons_path.exists():
        out_primary = run_primary_chain_pipeline(freq="weekly")
    cons = _load_primary_consolidated()
    fam = cons[cons["model_family"] == family].copy() if not cons.empty else pd.DataFrame()
    module_name = f"model_{family.lower()}"
    out = common.get_output_dir(module_name)
    common.write_tables_xlsx(out / f"{module_name}_output.xlsx", {f"{family}_Summary": fam})
    common.save_pdf_report(
        out / f"{module_name}_report.pdf",
        f"{family} Summary from Primary Chain",
        [
            PRIMARY_CHAIN_DOC,
            f"family={family}",
            f"rows={len(fam)}",
            f"source={out_primary / 'primary_chain_consolidated.xlsx'}",
        ],
        {f"{family}_Summary": fam},
        [],
    )
    return out
