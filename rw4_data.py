#!/usr/bin/env python3
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import numpy as np
import pandas as pd

import rw2_extended_mapping_pipeline as rw2


PROJECT_DIR = Path(__file__).resolve().parent
PRODUCT_DICT_PATH = PROJECT_DIR / "product_dictionary.csv"
FARM_GATE_FILES = {
    "FarmGateUA_initial": PROJECT_DIR / "farm_gate_daily.xlsx",
    "FarmGateUA_filled": PROJECT_DIR / "farm_gate_all_missing_filled_daily.xlsx",
}
LEVEL_ADMISSIBLE_LIQUID_TYPES = {"milk", "cream", "farm_gate_milk"}
MASS_ONLY_TYPES = {"butter", "sour_cream", "cottage_cheese", "hard_cheese", "yogurt_dessert"}


@lru_cache(maxsize=1)
def load_product_dictionary() -> pd.DataFrame:
    df = pd.read_csv(PRODUCT_DICT_PATH)
    df["raw_pattern"] = df["raw_pattern"].astype(str).str.strip().str.lower()
    df["priority"] = pd.to_numeric(df["priority"], errors="coerce").fillna(0).astype(int)
    return df.sort_values(["priority", "raw_pattern"], ascending=[False, True]).reset_index(drop=True)


def _search_text(*fields: object) -> str:
    chunks = [rw2.ntext(v) for v in fields if v is not None and not pd.isna(v)]
    return " | ".join([c for c in chunks if c])


def _comparison_family(std: object) -> str:
    std_s = str(std or "").strip().lower()
    if std_s in {"milk", "cream", "farm_gate_milk"}:
        return "liquid_dairy"
    if std_s in MASS_ONLY_TYPES:
        return "mass_dairy"
    return std_s or "other"


def _normalize_brand(value: object) -> str:
    txt = rw2.ntext(value)
    if not txt:
        return ""
    txt = txt.replace("ё", "е")
    txt = " ".join(txt.split())
    return txt


def _match_dictionary(*fields: object) -> Dict[str, object]:
    text = _search_text(*fields)
    if not text:
        return {
            "product": "Інше/невідомо",
            "standardized_type": "other",
            "subcategory": "unknown",
            "unit_family": "unknown",
            "liter_equiv_allowed": 0,
            "maturation_type": "unknown",
            "mapping_quality_flag": "unmatched",
            "matched_pattern": "",
        }
    matches = []
    for _, row in load_product_dictionary().iterrows():
        pat = str(row["raw_pattern"]).strip().lower()
        if pat and pat in text:
            matches.append(row)
    if not matches:
        return {
            "product": "Інше/невідомо",
            "standardized_type": "other",
            "subcategory": "unknown",
            "unit_family": "unknown",
            "liter_equiv_allowed": 0,
            "maturation_type": "unknown",
            "mapping_quality_flag": "unmatched",
            "matched_pattern": "",
        }
    best = matches[0]
    return {
        "product": best["product"],
        "standardized_type": best["standardized_type"],
        "subcategory": best["subcategory"],
        "unit_family": best["unit_family"],
        "liter_equiv_allowed": int(best["liter_equiv_allowed"]),
        "maturation_type": best["maturation_type"],
        "mapping_quality_flag": "matched" if len(matches) == 1 else "multi_match",
        "matched_pattern": best["raw_pattern"],
    }


def _fat_band(value: object, *fields: object) -> str:
    fat = pd.to_numeric(value, errors="coerce")
    if pd.isna(fat):
        text = _search_text(*fields)
        import re

        m = re.search(r"(\d{1,2}(?:[\.,]\d)?)\s*%", text)
        fat = float(m.group(1).replace(",", ".")) if m else np.nan
    if pd.isna(fat):
        return "unknown"
    if fat < 2.5:
        return "low"
    if fat <= 10:
        return "mid"
    return "high"


def _pack_band(qty: object) -> str:
    q = pd.to_numeric(qty, errors="coerce")
    if pd.isna(q):
        return "unknown"
    if q < 0.35:
        return "small"
    if q <= 0.8:
        return "medium"
    return "large"


def _normalize_unit_price(unit_price: pd.Series, unit_label: pd.Series) -> Tuple[pd.Series, pd.Series]:
    norm_vals: List[float] = []
    norm_units: List[str] = []
    for price, unit in zip(unit_price, unit_label):
        mult, norm = rw2._unit_to_norm_multiplier(unit)  # reuse the repo's normalization dictionary
        p = pd.to_numeric(price, errors="coerce")
        if pd.isna(p):
            norm_vals.append(np.nan)
            norm_units.append(norm or "")
            continue
        if mult is None or norm is None:
            norm_vals.append(np.nan)
            norm_units.append(norm or "unknown")
            continue
        norm_vals.append(float(p / mult))
        norm_units.append(norm)
    return pd.Series(norm_vals, index=unit_price.index), pd.Series(norm_units, index=unit_price.index)


def _retail_pack_fallback(df: pd.DataFrame) -> pd.Series:
    qty = pd.to_numeric(df.get("pack_qty"), errors="coerce")
    current = pd.to_numeric(df.get("price_current"), errors="coerce")
    unit = df.get("pack_unit", pd.Series("", index=df.index)).astype(str)
    out = pd.Series(np.nan, index=df.index, dtype=float)
    mass_mask = unit.eq("kg") & qty.gt(0)
    lit_mask = unit.eq("liter") & qty.gt(0)
    out.loc[mass_mask] = current.loc[mass_mask] / qty.loc[mass_mask]
    out.loc[lit_mask] = current.loc[lit_mask] / qty.loc[lit_mask]
    return out


def _baseline_from_nonpromo(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
    work = df.sort_values(["sku_id", "date", "timestamp"]).copy()
    regular_ref = work["observed_price"].where(work["discount_type"] == "regular")
    work["_regular_ref"] = regular_ref
    work["_regular_ffill"] = work.groupby("sku_id")["_regular_ref"].transform(lambda s: s.ffill())
    work["_regular_bfill"] = work.groupby("sku_id")["_regular_ref"].transform(lambda s: s.bfill())
    work["_regular_med"] = work.groupby("sku_id")["_regular_ref"].transform("median")

    baseline_from_discount = pd.Series(np.nan, index=work.index, dtype=float)
    discount_value = pd.to_numeric(work.get("discount_value"), errors="coerce")
    observed = pd.to_numeric(work.get("observed_price"), errors="coerce")
    baseline_from_discount = observed + discount_value

    price_old = pd.to_numeric(work.get("price_old"), errors="coerce")
    price_current = pd.to_numeric(work.get("price_current"), errors="coerce")
    price_old_norm = observed * (price_old / price_current.replace(0, np.nan))
    baseline = (
        baseline_from_discount.where(baseline_from_discount.gt(observed))
        .where(lambda s: s.notna(), price_old_norm.where(price_old_norm.gt(observed)))
        .where(lambda s: s.notna(), work["_regular_ffill"])
        .where(lambda s: s.notna(), work["_regular_bfill"])
        .where(lambda s: s.notna(), work["_regular_med"])
        .where(lambda s: s.notna(), observed)
    )
    quality = np.select(
        [
            baseline_from_discount.gt(observed).fillna(False),
            price_old_norm.gt(observed).fillna(False),
            work["_regular_ffill"].notna(),
            work["_regular_bfill"].notna(),
            work["_regular_med"].notna(),
        ],
        [
            "discount_value_plus_current",
            "price_old_scaled",
            "regular_ffill",
            "regular_bfill",
            "regular_group_median",
        ],
        default="observed_fallback",
    )
    return baseline, pd.Series(quality, index=work.index)


def _compute_promo_state(df: pd.DataFrame) -> pd.DataFrame:
    out = df.sort_values(["sku_id", "date", "timestamp"]).copy()
    observed = pd.to_numeric(out.get("observed_price"), errors="coerce")
    baseline = pd.to_numeric(out.get("baseline_price"), errors="coerce")
    out["old_price_present"] = pd.to_numeric(out.get("price_old"), errors="coerce").notna().astype(int)
    out["discount_present"] = (
        pd.to_numeric(out.get("discount_present"), errors="coerce")
        .fillna(0)
        .clip(0, 1)
        .astype(int)
    )
    out["markdown_rate"] = np.where(
        baseline.gt(0),
        (baseline - observed) / baseline,
        np.nan,
    )
    bulk = pd.to_numeric(out.get("discount_dummy_bulk"), errors="coerce").fillna(0).gt(0)
    markdown = (
        pd.to_numeric(out.get("discount_dummy_discount"), errors="coerce").fillna(0).gt(0)
        | out["markdown_rate"].fillna(0).gt(0.001)
    )
    regular = pd.to_numeric(out.get("discount_dummy_regular"), errors="coerce").fillna(0).gt(0)
    out["discount_type"] = np.select(
        [bulk, markdown, regular | out["discount_present"].eq(0)],
        ["bulk", "markdown", "regular"],
        default="unknown",
    )

    grp = out.groupby("sku_id", dropna=False)
    out["_promo_start"] = out["discount_present"].eq(1) & grp["discount_present"].shift(fill_value=0).eq(0)
    out["_promo_end"] = out["discount_present"].eq(1) & grp["discount_present"].shift(-1, fill_value=0).eq(0)
    out["promo_start_flag"] = out["_promo_start"].astype(int)
    out["promo_end_flag"] = out["_promo_end"].astype(int)
    out["promo_spell_id"] = grp["_promo_start"].cumsum().where(out["discount_present"].eq(1), 0).astype(int)
    out["promo_duration"] = 0
    active = out["promo_spell_id"].gt(0)
    out.loc[active, "promo_duration"] = (
        out.loc[active]
        .groupby(["sku_id", "promo_spell_id"], dropna=False)["date"]
        .transform("size")
        .astype(int)
    )

    last_nonpromo = grp["date"].transform(lambda s: s.where(out.loc[s.index, "discount_present"].eq(0)).ffill())
    out["time_since_last_promo"] = (
        pd.to_datetime(out["date"], errors="coerce") - pd.to_datetime(last_nonpromo, errors="coerce")
    ).dt.days
    out["promo_signal_quality"] = np.where(out["discount_type"].eq("unknown"), "weak", "strong")
    return out.drop(columns=["_promo_start", "_promo_end"], errors="ignore")


def load_farm_gate_sources() -> Dict[str, pd.DataFrame]:
    out: Dict[str, pd.DataFrame] = {}
    for source, path in FARM_GATE_FILES.items():
        lin = pd.read_excel(path, sheet_name="daily_lin")
        pchip = pd.read_excel(path, sheet_name="daily_PCHIP")
        lin = lin.rename(
            columns={
                rw2.find_column(lin, ["Показник", "indicator"]) or "Показник": "raw_product",
                rw2.find_column(lin, ["Територіальний розріз", "region"]) or "Територіальний розріз": "region",
                rw2.find_column(lin, ["Дата", "date"]) or "Дата": "date",
                rw2.find_column(lin, ["Ціна грн/кг", "price"]) or "Ціна грн/кг": "price_linear_input",
            }
        )
        pchip = pchip.rename(
            columns={
                rw2.find_column(pchip, ["Показник", "indicator"]) or "Показник": "raw_product",
                rw2.find_column(pchip, ["Територіальний розріз", "region"]) or "Територіальний розріз": "region",
                rw2.find_column(pchip, ["Дата", "date"]) or "Дата": "date",
                rw2.find_column(pchip, ["Ціна грн/кг", "price"]) or "Ціна грн/кг": "price_pchip_input",
            }
        )
        merged = lin[["raw_product", "region", "date", "price_linear_input"]].merge(
            pchip[["raw_product", "region", "date", "price_pchip_input"]],
            on=["raw_product", "region", "date"],
            how="outer",
        )
        merged["source"] = source
        out[source] = merged
    return out


def prep_farm_gate(df: pd.DataFrame, source: str) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    out = df.copy()
    out["date"] = pd.to_datetime(out["date"], errors="coerce")
    out = out.dropna(subset=["date"]).copy()
    out["raw_product"] = out["raw_product"].fillna("Сире молоко")
    out["product"] = "Сире молоко"
    out["standardized_type"] = "farm_gate_milk"
    out["subcategory"] = "raw_milk"
    out["unit_family"] = "mass"
    out["comparison_family"] = "liquid_dairy"
    out["liter_equiv_allowed"] = 1
    out["maturation_type"] = "raw"
    out["mapping_quality_flag"] = "matched"
    out["matched_pattern"] = "farm_gate"
    out["brand"] = ""
    out["brand_normalized"] = ""
    out["price_real_input"] = np.nan
    out["price_linear_input"] = pd.to_numeric(out["price_linear_input"], errors="coerce")
    out["price_pchip_input"] = pd.to_numeric(out["price_pchip_input"], errors="coerce")
    out["price"] = out["price_pchip_input"].where(out["price_pchip_input"].notna(), out["price_linear_input"])
    out["observed_price"] = out["price"]
    out["baseline_price"] = out["price"]
    out["price_variant"] = "observed"
    out["reconstruction_variant"] = "both"
    out["admissible_for_level_model"] = out["price"].notna().astype(int)
    out["admissibility_reason"] = np.where(out["admissible_for_level_model"].eq(1), "uah_per_kg", "missing_price")
    out["unit_ok"] = out["admissible_for_level_model"]
    out["fat_band"] = "unknown"
    out["pack_band"] = "unknown"
    out["segment_key"] = "farm_gate_milk|raw_milk|unknown|unknown|raw"
    out["shock_dummy"] = 0
    return out[
        [
            "source",
            "date",
            "raw_product",
            "product",
            "standardized_type",
            "subcategory",
            "unit_family",
            "comparison_family",
            "liter_equiv_allowed",
            "maturation_type",
            "mapping_quality_flag",
            "matched_pattern",
            "brand",
            "brand_normalized",
            "region",
            "price",
            "observed_price",
            "baseline_price",
            "price_variant",
            "reconstruction_variant",
            "price_real_input",
            "price_linear_input",
            "price_pchip_input",
            "admissible_for_level_model",
            "admissibility_reason",
            "unit_ok",
            "fat_band",
            "pack_band",
            "segment_key",
            "shock_dummy",
        ]
    ]


def _apply_common_metadata(df: pd.DataFrame, source: str) -> pd.DataFrame:
    if df.empty:
        return df
    out = df.copy()
    raw = out.get("raw_product", pd.Series("", index=out.index))
    title = out.get("title", pd.Series("", index=out.index))
    keys = pd.DataFrame({"raw_product": raw.fillna("").astype(str), "title": title.fillna("").astype(str)}, index=out.index)
    pair_key = keys["raw_product"] + "||" + keys["title"]
    unique_meta = {
        k: _match_dictionary(*(k.split("||", 1)))
        for k in pair_key.drop_duplicates().tolist()
    }
    meta = pd.DataFrame([unique_meta[k] for k in pair_key.tolist()], index=out.index)
    for col in meta.columns:
        out[col] = meta[col]

    if "product" in out.columns:
        out["product"] = np.where(out["product"].isin(["Інше/невідомо", "", None]), meta["product"], out["product"])
    else:
        out["product"] = meta["product"]
    if "standardized_type" in out.columns:
        out["standardized_type"] = np.where(out["standardized_type"].isin(["other", "", None]), meta["standardized_type"], out["standardized_type"])
    else:
        out["standardized_type"] = meta["standardized_type"]

    out["subcategory"] = meta["subcategory"]
    out["unit_family"] = meta["unit_family"]
    out["comparison_family"] = out["standardized_type"].map(_comparison_family)
    out["liter_equiv_allowed"] = meta["liter_equiv_allowed"]
    out["maturation_type"] = meta["maturation_type"]
    out["mapping_quality_flag"] = meta["mapping_quality_flag"]
    out["matched_pattern"] = meta["matched_pattern"]

    out["price_variant"] = out.get("price_variant", "observed")
    out["reconstruction_variant"] = out.get("reconstruction_variant", "observed")
    out["observed_price"] = pd.to_numeric(out.get("observed_price", out.get("price")), errors="coerce")
    out["baseline_price"] = pd.to_numeric(out.get("baseline_price", out.get("observed_price", out.get("price"))), errors="coerce")
    out["fat_band"] = [
        _fat_band(v, r, t)
        for v, r, t in zip(out.get("fat_pct", pd.Series(np.nan, index=out.index)), raw, title)
    ]
    out["pack_band"] = [_pack_band(v) for v in out.get("pack_qty", pd.Series(np.nan, index=out.index))]
    brand_src = out["brand"] if "brand" in out.columns else pd.Series("", index=out.index)
    out["brand_normalized"] = brand_src.map(_normalize_brand)
    out["segment_key"] = (
        out["standardized_type"].fillna("unknown").astype(str)
        + "|"
        + out["subcategory"].fillna("unknown").astype(str)
        + "|"
        + out["fat_band"].fillna("unknown").astype(str)
        + "|"
        + out["pack_band"].fillna("unknown").astype(str)
        + "|"
        + out["maturation_type"].fillna("unknown").astype(str)
    )
    shock_series = out["shock_dummy"] if "shock_dummy" in out.columns else pd.Series(0, index=out.index)
    out["shock_dummy"] = pd.to_numeric(shock_series, errors="coerce").fillna(0).astype(int)

    if source in {"ProducerUA", "ConsumerUA", "EU", "CME"}:
        out["observed_price"] = pd.to_numeric(out.get("price"), errors="coerce")
        out["baseline_price"] = out["observed_price"]
        out["admissible_for_level_model"] = out["observed_price"].notna().astype(int)
        out["admissibility_reason"] = np.where(out["admissible_for_level_model"].eq(1), "uah_per_kg", "missing_price")
        out["unit_ok"] = out["admissible_for_level_model"]
        return out

    if source == "ProZorro":
        unit_price = pd.to_numeric(out.get("unit_price"), errors="coerce")
        unit_norm_price, unit_norm = _normalize_unit_price(unit_price, out.get("unit", pd.Series("", index=out.index)).astype(str))
        out["unit_norm"] = unit_norm
        liter_allowed = out["standardized_type"].isin(LEVEL_ADMISSIBLE_LIQUID_TYPES)
        admissible = unit_norm.eq("kg") | (unit_norm.eq("liter") & liter_allowed)
        out["observed_price"] = unit_norm_price
        out["baseline_price"] = out["observed_price"]
        out["admissible_for_level_model"] = admissible & out["observed_price"].notna()
        out["admissibility_reason"] = np.select(
            [
                out["observed_price"].isna(),
                unit_norm.eq("piece"),
                unit_norm.eq("liter") & ~liter_allowed,
                out["admissible_for_level_model"].eq(1),
            ],
            [
                "missing_unit_normalized_price",
                "piece_units_blocked",
                "liter_not_comparable_for_product_family",
                "normalized_unit_price",
            ],
            default="unknown_unit_rule",
        )
        out["price"] = unit_price.where(unit_price.notna(), out.get("price"))
        out["unit_ok"] = out["admissible_for_level_model"].astype(int)
        return out

    if source in {"Silpo", "Novus"}:
        out["discount_value"] = pd.to_numeric(out.get("discount_value"), errors="coerce")
        out["observed_price"] = pd.to_numeric(out.get("unit_price_uah_per_kg_or_l"), errors="coerce")
        pack_fallback = _retail_pack_fallback(out)
        out["observed_price"] = out["observed_price"].where(out["observed_price"].notna() & out["observed_price"].gt(0), pack_fallback)
        out["price"] = out["observed_price"].where(out["observed_price"].notna(), pd.to_numeric(out.get("price_current"), errors="coerce"))
        out["price_variant"] = "observed"
        out["reconstruction_variant"] = "observed"
        base = out.sort_values(["sku_id", "date", "timestamp"]).copy()
        base["discount_present"] = (
            pd.to_numeric(base.get("discount_present"), errors="coerce")
            .fillna(0)
            .clip(0, 1)
            .astype(int)
        )
        bulk = pd.to_numeric(base.get("discount_dummy_bulk"), errors="coerce").fillna(0).gt(0)
        markdown = (
            pd.to_numeric(base.get("discount_dummy_discount"), errors="coerce").fillna(0).gt(0)
            | pd.to_numeric(base.get("discount_value"), errors="coerce").fillna(0).gt(0)
            | (
                pd.to_numeric(base.get("price_old"), errors="coerce").fillna(np.nan)
                > pd.to_numeric(base.get("price_current"), errors="coerce").fillna(np.nan)
            )
        )
        regular = pd.to_numeric(base.get("discount_dummy_regular"), errors="coerce").fillna(0).gt(0)
        base["discount_type"] = np.select(
            [bulk, markdown, regular | base["discount_present"].eq(0)],
            ["bulk", "markdown", "regular"],
            default="unknown",
        )
        if source == "Novus":
            base["discount_type"] = "regular"
            base["baseline_price"] = base["observed_price"]
            base["baseline_quality"] = "no_promo_signal"
            base["discount_present"] = 0
            base["markdown_rate"] = 0.0
            base = _compute_promo_state(base)
            out = base
        else:
            baseline, quality = _baseline_from_nonpromo(base)
            base["baseline_price"] = baseline
            base["baseline_quality"] = quality
            base = _compute_promo_state(base)
            out = base
        unit_label = out.get("pack_unit", pd.Series("", index=out.index)).astype(str)
        liter_allowed = out["standardized_type"].isin(LEVEL_ADMISSIBLE_LIQUID_TYPES)
        inadmissible_liter = unit_label.eq("liter") & ~liter_allowed
        out["admissible_for_level_model"] = out["observed_price"].notna() & ~inadmissible_liter
        out["admissibility_reason"] = np.select(
            [
                out["observed_price"].isna(),
                inadmissible_liter,
                out["admissible_for_level_model"].eq(1),
            ],
            [
                "missing_unit_normalized_price",
                "liter_not_comparable_for_product_family",
                "unit_price_or_pack_normalized",
            ],
            default="descriptive_only_price_current",
        )
        out["unit_ok"] = out["admissible_for_level_model"].astype(int)
        return out

    return out


def harmonize_cleaned(cleaned: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    out: Dict[str, pd.DataFrame] = {}
    for source, df in cleaned.items():
        out[source] = _apply_common_metadata(df.copy(), source)
    return out


def build_mapping_audit(cleaned: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for source, df in cleaned.items():
        if df.empty:
            continue
        raw_col = "raw_product" if "raw_product" in df.columns else "product"
        title_col = "title" if "title" in df.columns else raw_col
        sample = df[[raw_col]].copy()
        sample["title"] = df.get(title_col, "")
        sample["mapping_quality_flag"] = df.get("mapping_quality_flag", "unknown")
        sample["matched_pattern"] = df.get("matched_pattern", "")
        sample["product"] = df.get("product", "")
        sample["standardized_type"] = df.get("standardized_type", "")
        sample["admissibility_reason"] = df.get("admissibility_reason", "")
        sample["lexical_anomaly_flag"] = sample[raw_col].astype(str).str.contains(r"[^\w\s%/().,-]", regex=True).astype(int)
        grp = (
            sample.groupby([raw_col, "title", "product", "standardized_type", "mapping_quality_flag", "matched_pattern", "admissibility_reason", "lexical_anomaly_flag"], dropna=False)
            .size()
            .reset_index(name="rows")
        )
        grp.insert(0, "source", source)
        grp = grp.rename(columns={raw_col: "raw_label"})
        grp["economically_comparable_flag"] = (~grp["standardized_type"].eq("other")).astype(int)
        rows.append(grp)
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()


def build_unit_admissibility(cleaned: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for source, df in cleaned.items():
        if df.empty:
            rows.append({"source": source, "rows": 0})
            continue
        for reason, g in df.groupby("admissibility_reason", dropna=False):
            rows.append(
                {
                    "source": source,
                    "admissibility_reason": reason,
                    "rows": int(len(g)),
                    "admissible_share": float(pd.to_numeric(g.get("admissible_for_level_model"), errors="coerce").fillna(0).mean()),
                    "unit_family_mode": g.get("unit_family", pd.Series(["unknown"])).mode().iloc[0] if "unit_family" in g.columns and not g["unit_family"].mode().empty else "unknown",
                }
            )
    return pd.DataFrame(rows)


def build_reconstruction_diagnostics(cleaned: Dict[str, pd.DataFrame], all_daily: pd.DataFrame) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for source in ["ProducerUA", "FarmGateUA_initial", "FarmGateUA_filled"]:
        df = cleaned.get(source, pd.DataFrame())
        if df.empty:
            continue
        for region, g in df.groupby(df.get("region", pd.Series(["Україна"] * len(df))), dropna=False):
            work = g.copy().sort_values("date")
            lin = pd.to_numeric(work.get("price_linear_input"), errors="coerce")
            pchip = pd.to_numeric(work.get("price_pchip_input"), errors="coerce")
            if lin.notna().sum() < 5 and pchip.notna().sum() < 5:
                continue
            gap = (pchip - lin).abs()
            dlog_lin = np.log(lin.where(lin > 0)).diff()
            dlog_pchip = np.log(pchip.where(pchip > 0)).diff()
            spike_lin = dlog_lin.abs().gt(dlog_lin.std(skipna=True) * 3 if dlog_lin.std(skipna=True) and not pd.isna(dlog_lin.std(skipna=True)) else np.inf).sum()
            spike_pchip = dlog_pchip.abs().gt(dlog_pchip.std(skipna=True) * 3 if dlog_pchip.std(skipna=True) and not pd.isna(dlog_pchip.std(skipna=True)) else np.inf).sum()
            monthly = work.copy()
            monthly["month"] = pd.to_datetime(monthly["date"], errors="coerce").dt.to_period("M").dt.to_timestamp()
            m_lin = monthly.groupby("month")["price_linear_input"].mean()
            m_pchip = monthly.groupby("month")["price_pchip_input"].mean()
            rows.append(
                {
                    "source": source,
                    "region": region,
                    "rows": int(len(work)),
                    "date_min": pd.to_datetime(work["date"], errors="coerce").min(),
                    "date_max": pd.to_datetime(work["date"], errors="coerce").max(),
                    "linear_spike_count": int(spike_lin),
                    "pchip_spike_count": int(spike_pchip),
                    "mean_abs_variant_gap": float(gap.mean()) if gap.notna().any() else np.nan,
                    "max_abs_variant_gap": float(gap.max()) if gap.notna().any() else np.nan,
                    "monthly_reaggregation_gap": float((m_pchip - m_lin).abs().mean()) if len(m_lin) and len(m_pchip) else np.nan,
                    "monthly_anchor_status": "monthly_eom_anchored_filled_benchmark" if source == "FarmGateUA_filled" else ("monthly_eom_anchored_initial_benchmark" if source == "FarmGateUA_initial" else "producer_input_variant"),
                }
            )
    if not all_daily.empty:
        var_daily = all_daily[all_daily["source"].isin(["ProducerUA", "FarmGateUA_initial", "FarmGateUA_filled"])].copy()
        if not var_daily.empty:
            extra = (
                var_daily.groupby(["source", "standardized_type"], dropna=False)[["imputed_flag_linear", "imputed_flag_pchip"]]
                .mean()
                .reset_index()
                .rename(columns={"imputed_flag_linear": "imputed_share_linear", "imputed_flag_pchip": "imputed_share_pchip"})
            )
            base = pd.DataFrame(rows)
            if not base.empty:
                base = base.merge(extra, on="source", how="left")
                return base
    return pd.DataFrame(rows)
