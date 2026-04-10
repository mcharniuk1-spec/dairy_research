#!/usr/bin/env python3
from __future__ import annotations

import html
import os
import re
import warnings
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from zipfile import ZIP_DEFLATED, ZipFile


BASE_DIR = Path(__file__).resolve().parents[1]
STAGE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "Main materials" / "Model" / "Charniuk_Dairy_Research"
FULL_UAH = MODEL_DIR / "full_uah.xlsx"
FARM_GATE_FILES = {
    "initial": MODEL_DIR / "farm_gate_daily.xlsx",
    "filled": MODEL_DIR / "farm_gate_all_missing_filled_daily.xlsx",
}
OUTPUT_DIR = STAGE_DIR / "outputs"
DATA_DIR = STAGE_DIR / "data"
FIG_DIR = STAGE_DIR / "figures"
DOC_DIR = STAGE_DIR / "documents"

os.environ.setdefault("MPLCONFIGDIR", str(STAGE_DIR / "_mplconfig"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch
from statsmodels.stats.stattools import jarque_bera


warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

PRODUCT_LABELS = {
    "milk": "Milk / fermented milk",
    "butter": "Butter",
    "sour_cream": "Sour cream",
    "cream": "Cream",
    "hard_cheese": "Hard cheese",
    "cottage_cheese": "Cottage cheese",
    "yogurt_dessert": "Yogurt / dessert",
    "condensed_milk": "Condensed milk",
    "milk_powder": "Milk powder",
}

LITERAL_LABELS = {
    "milk": "Milk",
    "kefir": "Kefir",
    "ryazhanka": "Ryazhanka",
    "ayran": "Ayran / fermented milk drink",
    "yogurt": "Yogurt",
    "dessert": "Dairy dessert / glazed snack",
    "cottage_cheese": "Cottage cheese / tvorog",
    "hard_cheese": "Hard / semi-hard cheese",
    "sour_cream": "Sour cream",
    "cream": "Cream",
    "butter": "Butter",
    "condensed_milk": "Condensed milk",
    "milk_powder": "Milk powder",
    "other_dairy": "Other dairy",
}

RETAIL_STOPWORDS = {
    "молоко",
    "сир",
    "сметана",
    "вершки",
    "йогурт",
    "кефір",
    "ряжанка",
    "масло",
    "сирок",
    "кисломолочний",
    "питний",
    "солодковершкове",
    "ультрапастеризоване",
    "пастеризоване",
    "стерилізовані",
    "стерилізоване",
    "домашній",
    "ванночка",
    "стакан",
    "пляшка",
    "пакет",
    "пастоподібний",
    "білий",
    "натуральний",
    "термостатна",
    "термостатний",
    "екстра",
    "селянське",
    "селянська",
    "родинне",
    "особливе",
    "т",
    "б",
    "п",
    "е",
    "pet",
    "тетрапак",
    "шт",
}

GENERIC_BRANDS = {
    "",
    "nan",
    "продукт",
    "молочний",
    "напій",
    "сир",
    "яйця",
    "тістечко",
    "milk",
    "butter",
    "cream",
    "yogurt",
    "dessert",
    "cottage_cheese",
    "sour_cream",
}

PLANT_BASED_BRANDS = {
    "alpro",
    "oatly",
    "sojasun",
    "joya",
    "wanted",
    "wanted vegan",
    "green smile",
    "vega",
    "vega milk",
    "feels good",
}

HORIZONS = [0, 1, 3, 7, 14, 21]
MIN_LP_OBS = 32
MIN_MARGIN_OBS = 32
MIN_DISCOUNT_OBS = 30
MAX_HAC_LAG = 7


def ensure_dirs() -> None:
    for path in [OUTPUT_DIR, DATA_DIR, FIG_DIR, DOC_DIR, Path(os.environ["MPLCONFIGDIR"])]:
        path.mkdir(parents=True, exist_ok=True)


def ntext(value: object) -> str:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return ""
    text = str(value).strip().lower()
    text = text.replace("’", "'").replace("`", "'")
    text = re.sub(r"\s+", " ", text)
    return text


def normalize_retail_text(value: object) -> str:
    text = ntext(value)
    text = text.replace("м’який", "мякий").replace("’", "'")
    text = re.sub(r"[%]", " % ", text)
    text = re.sub(r"[^\w\s%]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_brand_name(brand: object, entity: object = "") -> str:
    b = normalize_retail_text(brand)
    e = normalize_retail_text(entity)
    b = "" if b in GENERIC_BRANDS else b
    e = "" if e in GENERIC_BRANDS else e
    return b or e


def retail_full_text(*fields: object) -> str:
    return normalize_retail_text(" ".join(ntext(v) for v in fields if ntext(v)))


def is_non_dairy_retail(text: str, brand_norm: str) -> bool:
    if brand_norm in PLANT_BASED_BRANDS:
        return True
    strong_patterns = [
        r"\bтофу\b",
        r"\bvegan\b",
        r"\bвеган",
        r"\bрослин",
        r"\bсоєв",
        r"\bsoy\b",
        r"\bsoya\b",
        r"\bвівся",
        r"\boat\b",
        r"\bмигдал",
        r"\balmond\b",
        r"\bbarista\b",
        r"сирно[\s-]?рослин",
        r"рослинно[\s-]?вершков",
    ]
    context_patterns = [
        r"snail.+кокосовому крем",
        r"кокосов.+рис",
        r"рис.+кокос",
        r"напій.+кокосов",
        r"напій.+рисов",
        r"напій.+мигдал",
    ]
    for pattern in strong_patterns + context_patterns:
        if re.search(pattern, text):
            return True
    return False


def literal_retail_type(*fields: object) -> str:
    text = retail_full_text(*fields)
    if not text:
        return "other_dairy"
    if any(token in text for token in ["молоко сух", "сухе молоко", "сухі вершки"]):
        return "milk_powder"
    if "згущ" in text:
        return "condensed_milk"
    if "масло" in text:
        return "butter"
    if "сметан" in text:
        return "sour_cream"
    if "вершк" in text:
        return "cream"
    if any(token in text for token in ["сирок", "десерт", "пудинг"]):
        return "dessert"
    if any(token in text for token in ["сир кисломолоч", "творог", "творож", "cottage cheese", "творожна"]):
        return "cottage_cheese"
    if any(token in text for token in ["йогурт", "скір", "skyr"]):
        return "yogurt"
    if "айран" in text:
        return "ayran"
    if "ряжан" in text:
        return "ryazhanka"
    if "кеф" in text:
        return "kefir"
    cheese_tokens = ["моцарел", "гауда", "gouda", "edam", "едам", "чеддер", "cheddar", "маасдам", "сулугун", "камамбер", "брі", "пармезан"]
    if "сир" in text or any(token in text for token in cheese_tokens):
        return "hard_cheese"
    if any(token in text for token in ["молоко", "молочний", "коктейль", "закваска"]):
        return "milk"
    return "other_dairy"


def retail_product_from_literal(literal_type: str) -> str:
    if literal_type in {"milk", "kefir", "ryazhanka", "ayran"}:
        return "milk"
    if literal_type in {"yogurt", "dessert"}:
        return "yogurt_dessert"
    if literal_type in {"cottage_cheese"}:
        return "cottage_cheese"
    if literal_type in {"hard_cheese"}:
        return "hard_cheese"
    if literal_type in {"sour_cream"}:
        return "sour_cream"
    if literal_type in {"cream"}:
        return "cream"
    if literal_type in {"butter"}:
        return "butter"
    if literal_type in {"condensed_milk"}:
        return "condensed_milk"
    if literal_type in {"milk_powder"}:
        return "milk_powder"
    return "other"


def extract_pack_std(row: pd.Series) -> Tuple[float, str]:
    qty = safe_num(pd.Series([row.get("qty_std", np.nan)])).iloc[0]
    unit = normalize_retail_text(row.get("unit_std", ""))
    if pd.notna(qty) and qty > 0 and unit in {"kg", "l", "liter"}:
        return float(qty), "kg" if unit == "kg" else "l"
    qty2 = safe_num(pd.Series([row.get("pack_qty_final", np.nan)])).iloc[0]
    unit2 = normalize_retail_text(row.get("pack_unit_final", ""))
    if pd.isna(qty2) or qty2 <= 0:
        return np.nan, ""
    if unit2 in {"г", "g", "гр"}:
        return float(qty2) / 1000.0, "kg"
    if unit2 in {"кг", "kg"}:
        return float(qty2), "kg"
    if unit2 in {"мл", "ml"}:
        return float(qty2) / 1000.0, "l"
    if unit2 in {"л", "l", "liter"}:
        return float(qty2), "l"
    return np.nan, ""


def canonical_item_name(product_name: object, product_title: object, brand_norm: str, product_type: str) -> str:
    text = normalize_retail_text(product_name or product_title)
    if brand_norm:
        for token in brand_norm.split():
            if len(token) >= 3:
                text = re.sub(rf"\b{re.escape(token)}\b", " ", text)
    text = re.sub(r"\b\d+[,.]?\d*\s*%\b", " ", text)
    text = re.sub(r"\b\d+[,.]?\d*\b", " ", text)
    tokens = []
    for tok in text.split():
        if tok in RETAIL_STOPWORDS:
            continue
        if len(tok) <= 1:
            continue
        tokens.append(tok)
    if not tokens:
        fallback = [t for t in normalize_retail_text(product_name).split() if t not in RETAIL_STOPWORDS]
        tokens = fallback[:5] if fallback else [product_type]
    return " ".join(tokens[:8]).strip()


def item_key(product: str, brand_norm: str, canonical_name: str) -> str:
    return "|".join([product or "na", brand_norm or "na", canonical_name or "na"])


def item_key_strict(product: str, brand_norm: str, canonical_name: str, fat_pct: object, pack_std: object, pack_unit: str) -> str:
    fat = safe_num(pd.Series([fat_pct])).iloc[0]
    fat_key = "na" if pd.isna(fat) else f"{float(fat):.1f}"
    pack_val = safe_num(pd.Series([pack_std])).iloc[0]
    pack_key = "na" if pd.isna(pack_val) else f"{float(pack_val):.3f}"
    return "|".join([product or "na", brand_norm or "na", canonical_name or "na", fat_key, pack_key, pack_unit or "na"])


def standardize_product(*fields: object) -> str:
    text = " | ".join(ntext(v) for v in fields if ntext(v))
    if not text:
        return "other"
    if "яйц" in text:
        return "eggs"
    if "сух" in text and "молок" in text:
        return "milk_powder"
    if "згущ" in text:
        return "condensed_milk"
    if "кисломолоч" in text or "творог" in text or "cottage" in text:
        return "cottage_cheese"
    if "масло" in text or "butter" in text:
        return "butter"
    if "сметан" in text or "sour cream" in text:
        return "sour_cream"
    if "вершк" in text or "cream" in text:
        return "cream"
    if "йогурт" in text or "десерт" in text or "yogurt" in text:
        return "yogurt_dessert"
    if "сир" in text or "cheese" in text or "gouda" in text or "edam" in text or "cheddar" in text:
        return "hard_cheese"
    if "кеф" in text or "ряжан" in text or "молок" in text or "milk" in text:
        return "milk"
    return "other"


def as_date(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, errors="coerce").dt.normalize()


def safe_num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def safe_log(series: pd.Series) -> pd.Series:
    values = safe_num(series)
    return np.log(values.where(values > 0))


def winsorize_by_group(df: pd.DataFrame, value_col: str, group_cols: Sequence[str], lo: float = 0.01, hi: float = 0.99) -> pd.Series:
    out = safe_num(df[value_col]).copy()
    for _, idx in df.groupby(list(group_cols), dropna=False).groups.items():
        vals = out.loc[idx].dropna()
        if len(vals) < 8:
            continue
        lower = vals.quantile(lo)
        upper = vals.quantile(hi)
        out.loc[idx] = out.loc[idx].clip(lower, upper)
    return out


def interpolate_panel(panel: pd.DataFrame, cols: Sequence[str], limits: Dict[str, int]) -> pd.DataFrame:
    out = panel.sort_values(["product", "date"]).copy()
    for col in cols:
        limit = limits.get(col, 0)
        model_col = f"{col}_model"
        if limit <= 0:
            out[model_col] = out[col]
            continue
        pieces = []
        for _, g in out[["product", "date", col]].groupby("product", dropna=False):
            s = g.set_index("date")[col].sort_index()
            s_interp = s.interpolate(method="time", limit=limit, limit_area="inside")
            pieces.append(s_interp.rename(model_col).reset_index().assign(product=g["product"].iloc[0]))
        interp = pd.concat(pieces, ignore_index=True) if pieces else pd.DataFrame(columns=["date", "product", model_col])
        out = out.drop(columns=[model_col], errors="ignore").merge(interp, on=["product", "date"], how="left")
    return out


def load_farm_gate() -> pd.DataFrame:
    rows: List[pd.DataFrame] = []
    for source, path in FARM_GATE_FILES.items():
        for sheet, variant in [("daily_lin", "linear"), ("daily_PCHIP", "pchip")]:
            df = pd.read_excel(path, sheet_name=sheet)
            df = df.rename(
                columns={
                    "Дата": "date",
                    "Територіальний розріз": "region",
                    "Ціна грн/кг": "price",
                }
            )
            df["date"] = as_date(df["date"])
            df["price"] = safe_num(df["price"])
            df = df.dropna(subset=["date", "price"])
            national = df[df["region"].astype(str).str.strip().eq("Україна")].copy()
            if national.empty:
                national = df.groupby("date", as_index=False)["price"].median()
                national["region"] = "regional_median"
            national = national[["date", "price"]].copy()
            national["farm_gate_source"] = source
            national["reconstruction_variant"] = variant
            national["product"] = "raw_milk"
            rows.append(national)
    long = pd.concat(rows, ignore_index=True)
    wide = long.pivot_table(index="date", columns=["farm_gate_source", "reconstruction_variant"], values="price", aggfunc="median")
    wide.columns = [f"farmgate_{src}_{var}" for src, var in wide.columns]
    wide = wide.reset_index()
    return wide


def load_producer() -> pd.DataFrame:
    df = pd.read_excel(FULL_UAH, sheet_name="Producer_UA")
    df["date"] = as_date(df["date"])
    df["product"] = df["ua_product"].apply(standardize_product)
    df["producer_linear"] = safe_num(df["price_linear"])
    df["producer_pchip"] = safe_num(df["price_pchip"])
    df = df[~df["product"].isin(["other", "eggs"])]
    out = (
        df.groupby(["date", "product"], as_index=False)[["producer_linear", "producer_pchip"]]
        .median()
        .sort_values(["product", "date"])
    )
    return out


def load_prozorro() -> pd.DataFrame:
    df = pd.read_excel(FULL_UAH, sheet_name="Prozorro")
    df = df.rename(
        columns={
            "Дата": "date",
            "Product": "raw_product",
            "Одиниця виміру": "unit",
            "Ціна за одиницю": "unit_price",
            "Регіон організатора": "region",
        }
    )
    df["date"] = as_date(df["date"])
    df["product"] = df["raw_product"].apply(standardize_product)
    df["unit_norm"] = df["unit"].astype(str).str.lower().str.strip()
    df["price"] = safe_num(df["unit_price"])
    unit_ok = df["unit_norm"].str.contains("кілограм|кг|kg|літр|л", regex=True, na=False)
    df = df[unit_ok & ~df["product"].isin(["other", "eggs"]) & df["price"].gt(0)].copy()
    df["price"] = winsorize_by_group(df, "price", ["product"])
    out = (
        df.groupby(["date", "product"], as_index=False)
        .agg(prozorro=("price", "median"), prozorro_n=("price", "size"), prozorro_regions=("region", pd.Series.nunique))
        .sort_values(["product", "date"])
    )
    return out


def load_consumer() -> pd.DataFrame:
    df = pd.read_excel(FULL_UAH, sheet_name="Consumer_UA")
    df["date"] = as_date(df["date"])
    df["product"] = df["ua_product"].apply(standardize_product)
    df["consumer_linear"] = safe_num(df["price_linear"])
    df["consumer_pchip"] = safe_num(df["price_pchip"])
    df = df[~df["product"].isin(["other", "eggs"])].copy()
    out = (
        df.groupby(["date", "product"], as_index=False)[["consumer_linear", "consumer_pchip"]]
        .median()
        .sort_values(["product", "date"])
    )
    return out


def load_retail_items(sheet: str, product_col: str, retailer: str) -> pd.DataFrame:
    df = pd.read_excel(FULL_UAH, sheet_name=sheet).copy()
    df["date"] = as_date(df["date"])
    df["retailer"] = retailer
    df["brand_norm"] = [normalize_brand_name(b, e) for b, e in zip(df.get("brand", ""), df.get("entity", ""))]
    df["raw_sheet_product"] = df[product_col].apply(ntext)
    df["retail_text"] = [
        retail_full_text(sheet_prod, pn, pt, b, e)
        for sheet_prod, pn, pt, b, e in zip(
            df[product_col],
            df.get("product_name", ""),
            df.get("product_title", ""),
            df.get("brand", ""),
            df.get("entity", ""),
        )
    ]
    literals = []
    for sheet_prod, pn, pt, b, e in zip(
        df[product_col],
        df.get("product_name", ""),
        df.get("product_title", ""),
        df.get("brand", ""),
        df.get("entity", ""),
    ):
        literal = literal_retail_type(pn, pt, b, e)
        if literal == "other_dairy":
            literal = literal_retail_type(sheet_prod, pn, pt, b, e)
        literals.append(literal)
    df["product_literal"] = literals
    df["product"] = df["product_literal"].map(retail_product_from_literal)
    df["non_dairy_flag"] = [int(is_non_dairy_retail(text, brand)) for text, brand in zip(df["retail_text"], df["brand_norm"])]
    df = df[df["non_dairy_flag"].eq(0) & ~df["product"].isin(["other", "eggs"])].copy()
    df["effective_price"] = safe_num(df.get("price_current", pd.Series(np.nan, index=df.index)))
    df["discount_amount"] = safe_num(df.get("discount_value", pd.Series(np.nan, index=df.index))).fillna(0)
    df["discount_dummy_discount"] = safe_num(df.get("discount_dummy_discount", pd.Series(0, index=df.index))).fillna(0).astype(int)
    df["discount_dummy_bulk"] = safe_num(df.get("discount_dummy_bulk", pd.Series(0, index=df.index))).fillna(0).astype(int)
    df["discount_dummy_regular"] = safe_num(df.get("discount_dummy_regular", pd.Series(0, index=df.index))).fillna(0).astype(int)
    df["discount_present"] = (
        df["discount_dummy_discount"].eq(1)
        | df["discount_dummy_bulk"].eq(1)
        | df["discount_amount"].gt(0)
    ).astype(int)
    df["discount_type"] = np.select(
        [df["discount_dummy_bulk"].eq(1), df["discount_dummy_discount"].eq(1), df["discount_present"].eq(0)],
        ["bulk", "markdown", "regular"],
        default="unknown",
    )
    df["baseline_price"] = np.where(df["discount_amount"].gt(0), df["effective_price"] + df["discount_amount"], df["effective_price"])
    df["markdown_rate"] = np.where(df["baseline_price"].gt(0), (df["baseline_price"] - df["effective_price"]) / df["baseline_price"], np.nan)
    packs = df.apply(extract_pack_std, axis=1, result_type="expand")
    df["pack_std"] = packs[0]
    df["pack_std_unit"] = packs[1]
    df["unit_effective_price"] = safe_num(df.get("unit_price", pd.Series(np.nan, index=df.index)))
    need_fallback = df["unit_effective_price"].isna() & df["pack_std"].gt(0)
    df.loc[need_fallback, "unit_effective_price"] = df.loc[need_fallback, "effective_price"] / df.loc[need_fallback, "pack_std"]
    df["unit_baseline_price"] = np.where(df["pack_std"].gt(0), df["baseline_price"] / df["pack_std"], np.nan)
    df["fat_pct_clean"] = safe_num(df.get("fat_pct", pd.Series(np.nan, index=df.index)))
    df["canonical_name"] = [
        canonical_item_name(pn, pt, bn, prod)
        for pn, pt, bn, prod in zip(df.get("product_name", ""), df.get("product_title", ""), df["brand_norm"], df["product"])
    ]
    df["item_key"] = [item_key(prod, bn, cn) for prod, bn, cn in zip(df["product"], df["brand_norm"], df["canonical_name"])]
    df["item_key_strict"] = [
        item_key_strict(prod, bn, cn, fat, pack, unit)
        for prod, bn, cn, fat, pack, unit in zip(
            df["product"], df["brand_norm"], df["canonical_name"], df["fat_pct_clean"], df["pack_std"], df["pack_std_unit"]
        )
    ]
    keep = [
        "retailer",
        "date",
        "product",
        "product_literal",
        "brand_norm",
        "canonical_name",
        "item_key",
        "item_key_strict",
        "raw_sheet_product",
        "retail_text",
        "product_title",
        "product_name",
        "brand",
        "entity",
        "fat_pct_clean",
        "pack_std",
        "pack_std_unit",
        "effective_price",
        "baseline_price",
        "unit_effective_price",
        "unit_baseline_price",
        "discount_amount",
        "discount_present",
        "discount_type",
        "markdown_rate",
        "discount_dummy_discount",
        "discount_dummy_bulk",
        "discount_dummy_regular",
    ]
    df = df[keep].copy()
    df = df[df["effective_price"].gt(0)].copy()
    df["effective_price"] = winsorize_by_group(df, "effective_price", ["product", "retailer"])
    df["baseline_price"] = winsorize_by_group(df, "baseline_price", ["product", "retailer"])
    df["unit_effective_price"] = df["unit_effective_price"].where(df["unit_effective_price"].between(0.5, 5000))
    df["unit_baseline_price"] = df["unit_baseline_price"].where(df["unit_baseline_price"].between(0.5, 5000))
    return df.sort_values(["retailer", "date", "product", "item_key"])


def build_retail_catalog_and_matches(silpo_items: pd.DataFrame, novus_items: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    all_items = pd.concat([silpo_items, novus_items], ignore_index=True)
    catalog = (
        all_items.groupby(["retailer", "item_key"], as_index=False)
        .agg(
            product=("product", "first"),
            brand_norm=("brand_norm", "first"),
            canonical_name=("canonical_name", "first"),
            n_strict_keys=("item_key_strict", pd.Series.nunique),
            fat_pct=("fat_pct_clean", "median"),
            pack_std=("pack_std", "median"),
            pack_std_unit=("pack_std_unit", "first"),
            first_title=("product_title", "first"),
            first_name=("product_name", "first"),
            n_rows=("effective_price", "size"),
            date_min=("date", "min"),
            date_max=("date", "max"),
        )
        .sort_values(["retailer", "product", "brand_norm", "canonical_name"])
    )
    sil = catalog[catalog["retailer"].eq("Silpo")].drop(columns=["retailer"]).rename(columns=lambda c: f"silpo_{c}" if c != "item_key" else c)
    nov = catalog[catalog["retailer"].eq("Novus")].drop(columns=["retailer"]).rename(columns=lambda c: f"novus_{c}" if c != "item_key" else c)
    audit = sil.merge(nov, on="item_key", how="outer", indicator=True)
    audit["match_status"] = audit["_merge"].map({"both": "matched_both_shops", "left_only": "silpo_only", "right_only": "novus_only"})
    audit["strict_alignment_flag"] = np.where(
        audit["match_status"].eq("matched_both_shops")
        & audit["silpo_n_strict_keys"].fillna(0).eq(1)
        & audit["novus_n_strict_keys"].fillna(0).eq(1),
        1,
        0,
    )
    audit = audit.drop(columns=["_merge"])
    return catalog, audit


def aggregate_retail_items(items: pd.DataFrame, prefix: str = "") -> pd.DataFrame:
    grouped = (
        items.groupby(["date", "product"], as_index=False)
        .agg(
            observed=("effective_price", "median"),
            baseline=("baseline_price", "median"),
            unit_observed=("unit_effective_price", "median"),
            unit_baseline=("unit_baseline_price", "median"),
            discount_share=("discount_present", "mean"),
            discount_depth=("markdown_rate", "median"),
            discount_amount_median=("discount_amount", "median"),
            n_items=("effective_price", "size"),
            n_item_keys=("item_key", pd.Series.nunique),
            n_brands=("brand_norm", pd.Series.nunique),
            n_literal_types=("product_literal", pd.Series.nunique),
            n_unit=("unit_effective_price", lambda s: int(s.notna().sum())),
        )
        .sort_values(["product", "date"])
    )
    grouped["discount_depth"] = grouped["discount_depth"].fillna(0)
    if prefix:
        rename = {c: f"{prefix}_{c}" for c in grouped.columns if c not in {"date", "product"}}
        grouped = grouped.rename(columns=rename)
    return grouped


def build_consumer_linked_retail(retail: pd.DataFrame, consumer: pd.DataFrame) -> pd.DataFrame:
    merged = retail.merge(consumer, on=["date", "product"], how="left")
    merged["retail_consumer_observed"] = merged[["retail_observed", "consumer_linear"]].median(axis=1, skipna=True)
    merged["retail_consumer_baseline"] = merged[["retail_baseline", "consumer_linear"]].median(axis=1, skipna=True)
    merged["consumer_support_flag"] = merged["consumer_linear"].notna().astype(int)
    merged["consumer_retail_gap"] = safe_log(merged["retail_observed"]) - safe_log(merged["consumer_linear"])
    keep_cols = list(retail.columns) + ["retail_consumer_observed", "retail_consumer_baseline", "consumer_support_flag", "consumer_retail_gap"]
    return merged[keep_cols]


def build_retail_brand_panels(items: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    brand_daily = (
        items.groupby(["date", "product", "product_literal", "retailer", "brand_norm"], as_index=False)
        .agg(
            observed=("effective_price", "median"),
            baseline=("baseline_price", "median"),
            discount_share=("discount_present", "mean"),
            markdown_rate=("markdown_rate", "median"),
            n_items=("effective_price", "size"),
            n_item_keys=("item_key", pd.Series.nunique),
        )
        .sort_values(["product", "retailer", "brand_norm", "date"])
    )
    brand_support = (
        items.groupby(["product", "product_literal", "retailer", "brand_norm"], as_index=False)
        .agg(
            n_rows=("effective_price", "size"),
            n_dates=("date", pd.Series.nunique),
            n_item_keys=("item_key", pd.Series.nunique),
            matched_share=("matched_cross_shop", "mean"),
            mean_discount_share=("discount_present", "mean"),
            median_price=("effective_price", "median"),
        )
        .sort_values(["product", "retailer", "n_rows", "n_dates"], ascending=[True, True, False, False])
    )
    return brand_daily, brand_support


def build_retail_literal_summary(items: pd.DataFrame) -> pd.DataFrame:
    return (
        items.groupby(["product", "product_literal", "retailer"], as_index=False)
        .agg(
            n_rows=("effective_price", "size"),
            n_dates=("date", pd.Series.nunique),
            n_item_keys=("item_key", pd.Series.nunique),
            n_brands=("brand_norm", pd.Series.nunique),
            matched_share=("matched_cross_shop", "mean"),
            mean_discount_share=("discount_present", "mean"),
            median_price=("effective_price", "median"),
        )
        .sort_values(["product", "retailer", "n_item_keys"], ascending=[True, True, False])
    )


def build_reconciliation_examples(audit: pd.DataFrame) -> pd.DataFrame:
    if audit.empty:
        return pd.DataFrame()
    matched = audit[audit["match_status"].eq("matched_both_shops")].copy()
    if matched.empty:
        return matched
    matched["combined_rows"] = matched["silpo_n_rows"].fillna(0) + matched["novus_n_rows"].fillna(0)
    cols = [
        "item_key",
        "silpo_product",
        "silpo_brand_norm",
        "silpo_canonical_name",
        "silpo_first_name",
        "novus_brand_norm",
        "novus_canonical_name",
        "novus_first_name",
        "silpo_n_rows",
        "novus_n_rows",
        "strict_alignment_flag",
        "combined_rows",
    ]
    return matched[cols].sort_values(["strict_alignment_flag", "combined_rows"], ascending=[False, False]).head(250)


def retail_candidate_specs(include_optimal: bool = False) -> List[Dict[str, str]]:
    specs = [
        {
            "candidate": "retail_merged",
            "label": "Retail merged full list",
            "observed_col": "retail_observed_model",
            "baseline_col": "retail_baseline_model",
            "discount_col": "retail_discount_share",
            "support_col": "retail_n_item_keys",
            "link_forward": "ProZorro -> Retail merged",
            "link_reverse": "Retail merged -> ProZorro",
        },
        {
            "candidate": "retail_matched",
            "label": "Retail matched cross-shop",
            "observed_col": "retail_matched_observed_model",
            "baseline_col": "retail_matched_baseline_model",
            "discount_col": "retail_matched_discount_share",
            "support_col": "retail_matched_n_item_keys",
            "link_forward": "ProZorro -> Retail matched",
            "link_reverse": "Retail matched -> ProZorro",
        },
        {
            "candidate": "silpo",
            "label": "Silpo only",
            "observed_col": "silpo_observed_model",
            "baseline_col": "silpo_baseline_model",
            "discount_col": "silpo_discount_share",
            "support_col": "silpo_n_item_keys",
            "link_forward": "ProZorro -> Silpo",
            "link_reverse": "Silpo -> ProZorro",
        },
        {
            "candidate": "novus",
            "label": "Novus only",
            "observed_col": "novus_observed_model",
            "baseline_col": "novus_observed_model",
            "discount_col": "novus_discount_share",
            "support_col": "novus_n_item_keys",
            "link_forward": "ProZorro -> Novus",
            "link_reverse": "Novus -> ProZorro",
        },
        {
            "candidate": "retail_consumer",
            "label": "Retail plus ConsumerUA",
            "observed_col": "retail_consumer_observed_model",
            "baseline_col": "retail_consumer_baseline_model",
            "discount_col": "retail_discount_share",
            "support_col": "retail_n_item_keys",
            "link_forward": "ProZorro -> Retail+Consumer",
            "link_reverse": "Retail+Consumer -> ProZorro",
        },
    ]
    if include_optimal:
        specs.append(
            {
                "candidate": "retail_optimal",
                "label": "Optimal retail level",
                "observed_col": "retail_optimal_observed_model",
                "baseline_col": "retail_optimal_baseline_model",
                "discount_col": "retail_optimal_discount_share",
                "support_col": "retail_optimal_n_item_keys",
                "link_forward": "ProZorro -> Retail optimal",
                "link_reverse": "Retail optimal -> ProZorro",
            }
        )
    return specs


def best_abs_lag_corr(x: pd.Series, y: pd.Series, max_lag: int = 28) -> Tuple[float, float, int]:
    best_corr = np.nan
    best_lag = np.nan
    best_n = 0
    lx = safe_log(x)
    ly = safe_log(y)
    for lag in range(0, max_lag + 1):
        d = pd.concat([lx.shift(lag).rename("x"), ly.rename("y")], axis=1).dropna()
        if len(d) < 20:
            continue
        corr = d["x"].corr(d["y"])
        if pd.isna(corr):
            continue
        if pd.isna(best_corr) or abs(corr) > abs(best_corr):
            best_corr = float(corr)
            best_lag = float(lag)
            best_n = int(len(d))
    return best_corr, best_lag, best_n


def select_optimal_retail_levels(panel: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    records: List[Dict[str, object]] = []
    for product, g in panel.groupby("product"):
        g = g.sort_values("date").copy()
        for spec in retail_candidate_specs(include_optimal=False):
            obs_col = spec["observed_col"]
            support_col = spec["support_col"]
            disc_col = spec["discount_col"]
            if obs_col not in g.columns:
                continue
            n_obs = int(g[obs_col].notna().sum())
            if n_obs < MIN_LP_OBS:
                continue
            prozorro_series = g["prozorro_model"] if "prozorro_model" in g.columns else pd.Series(np.nan, index=g.index)
            consumer_series = g["consumer_linear_model"] if "consumer_linear_model" in g.columns else pd.Series(np.nan, index=g.index)
            corr_p, lag_p, n_p = best_abs_lag_corr(prozorro_series, g[obs_col], max_lag=28)
            corr_c, lag_c, n_c = best_abs_lag_corr(consumer_series, g[obs_col], max_lag=14)
            discount_std = float(safe_num(g.get(disc_col, pd.Series(np.nan, index=g.index))).std(skipna=True))
            median_support = float(safe_num(g.get(support_col, pd.Series(np.nan, index=g.index))).median(skipna=True))
            records.append(
                {
                    "product": product,
                    "product_label": PRODUCT_LABELS.get(product, product),
                    "candidate": spec["candidate"],
                    "candidate_label": spec["label"],
                    "observed_col": obs_col,
                    "baseline_col": spec["baseline_col"],
                    "discount_col": disc_col,
                    "support_col": support_col,
                    "n_obs": n_obs,
                    "coverage_share": float(g[obs_col].notna().mean()),
                    "best_corr_prozorro": corr_p,
                    "best_lag_prozorro": lag_p,
                    "best_corr_consumer": corr_c,
                    "best_lag_consumer": lag_c,
                    "discount_std": discount_std,
                    "median_item_support": median_support,
                    "overlap_prozorro_n": n_p,
                    "overlap_consumer_n": n_c,
                }
            )
    score_df = pd.DataFrame(records)
    if score_df.empty:
        return score_df, score_df

    for col in ["coverage_share", "best_corr_prozorro", "best_corr_consumer", "discount_std", "median_item_support"]:
        base = score_df[col].abs() if "corr" in col else score_df[col]
        denom = base.max()
        score_df[f"{col}_scaled"] = 0.0 if pd.isna(denom) or denom <= 0 else (base / denom).fillna(0)

    score_df["selection_score"] = (
        0.30 * score_df["coverage_share_scaled"]
        + 0.30 * score_df["best_corr_prozorro_scaled"]
        + 0.15 * score_df["best_corr_consumer_scaled"]
        + 0.15 * score_df["median_item_support_scaled"]
        + 0.10 * score_df["discount_std_scaled"]
    )
    chosen = (
        score_df.sort_values(
            ["product", "selection_score", "best_corr_prozorro_scaled", "coverage_share_scaled"],
            ascending=[True, False, False, False],
        )
        .groupby("product", as_index=False)
        .head(1)
        .reset_index(drop=True)
    )
    chosen["rank_note"] = "Highest composite score across coverage, procurement alignment, consumer alignment, item support, and discount variation."
    return score_df.sort_values(["product", "selection_score"], ascending=[True, False]), chosen


def build_panel() -> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, pd.DataFrame]]:
    farm = load_farm_gate()
    producer = load_producer()
    prozorro = load_prozorro()
    consumer = load_consumer()
    silpo_items = load_retail_items("Silpo", "Product", "Silpo")
    novus_items = load_retail_items("Novus", "product", "Novus")
    retail_catalog, retail_match_audit = build_retail_catalog_and_matches(silpo_items, novus_items)
    matched_keys = set(retail_match_audit.loc[retail_match_audit["match_status"].eq("matched_both_shops"), "item_key"])
    silpo_items["matched_cross_shop"] = silpo_items["item_key"].isin(matched_keys).astype(int)
    novus_items["matched_cross_shop"] = novus_items["item_key"].isin(matched_keys).astype(int)
    retail_items_full = pd.concat([silpo_items, novus_items], ignore_index=True).sort_values(["date", "product", "retailer", "item_key"])
    retail_brand_daily, retail_brand_support = build_retail_brand_panels(retail_items_full)
    retail_literal_summary = build_retail_literal_summary(retail_items_full)
    reconciliation_examples = build_reconciliation_examples(retail_match_audit)
    silpo = aggregate_retail_items(silpo_items, prefix="silpo")
    novus = aggregate_retail_items(novus_items, prefix="novus")
    retail = aggregate_retail_items(retail_items_full, prefix="retail")
    matched_only = aggregate_retail_items(retail_items_full[retail_items_full["matched_cross_shop"].eq(1)].copy(), prefix="retail_matched")
    retail = retail.merge(matched_only, on=["date", "product"], how="left")
    retail = retail.merge(silpo, on=["date", "product"], how="left")
    retail = retail.merge(novus, on=["date", "product"], how="left")
    retail = build_consumer_linked_retail(retail, consumer)

    products = sorted(
        set(producer["product"]).union(prozorro["product"]).union(retail["product"]).union(consumer["product"]) - {"other", "eggs"}
    )
    min_date = min(producer["date"].min(), farm["date"].min(), prozorro["date"].min(), retail["date"].min(), consumer["date"].min())
    max_date = max(producer["date"].max(), farm["date"].max(), prozorro["date"].max(), retail["date"].max(), consumer["date"].max())
    grid = pd.MultiIndex.from_product(
        [pd.date_range(min_date, max_date, freq="D"), products],
        names=["date", "product"],
    ).to_frame(index=False)

    panel = grid.merge(farm, on="date", how="left")
    panel = panel.merge(producer, on=["date", "product"], how="left")
    panel = panel.merge(prozorro, on=["date", "product"], how="left")
    panel = panel.merge(consumer, on=["date", "product"], how="left")
    panel = panel.merge(retail, on=["date", "product"], how="left")
    panel["product_label"] = panel["product"].map(PRODUCT_LABELS).fillna(panel["product"])

    model_limits = {
        "prozorro": 14,
        "consumer_linear": 7,
        "consumer_pchip": 7,
        "retail_observed": 3,
        "retail_baseline": 3,
        "retail_consumer_observed": 3,
        "retail_consumer_baseline": 3,
        "retail_matched_observed": 3,
        "retail_matched_baseline": 3,
        "silpo_observed": 3,
        "silpo_baseline": 3,
        "novus_observed": 3,
        "retail_unit_observed": 3,
    }
    price_cols = [
        "farmgate_initial_linear",
        "farmgate_initial_pchip",
        "farmgate_filled_linear",
        "farmgate_filled_pchip",
        "producer_linear",
        "producer_pchip",
        "consumer_linear",
        "consumer_pchip",
        "prozorro",
        "retail_observed",
        "retail_baseline",
        "retail_consumer_observed",
        "retail_consumer_baseline",
        "retail_matched_observed",
        "retail_matched_baseline",
        "silpo_observed",
        "silpo_baseline",
        "novus_observed",
        "retail_unit_observed",
    ]
    panel = interpolate_panel(panel, [c for c in price_cols if c in panel.columns], model_limits)

    level_scores, level_chosen = select_optimal_retail_levels(panel)
    if not level_chosen.empty:
        panel = panel.merge(
            level_chosen[["product", "candidate", "observed_col", "baseline_col", "discount_col", "support_col"]],
            on="product",
            how="left",
        )
        panel["retail_optimal_observed"] = np.nan
        panel["retail_optimal_baseline"] = np.nan
        panel["retail_optimal_observed_model"] = np.nan
        panel["retail_optimal_baseline_model"] = np.nan
        panel["retail_optimal_discount_share"] = np.nan
        panel["retail_optimal_n_item_keys"] = np.nan
        for row in level_chosen.itertuples():
            mask = panel["product"].eq(row.product)
            raw_observed_col = row.observed_col.replace("_model", "")
            raw_baseline_col = row.baseline_col.replace("_model", "")
            if raw_observed_col in panel.columns:
                panel.loc[mask, "retail_optimal_observed"] = panel.loc[mask, raw_observed_col]
            if raw_baseline_col in panel.columns:
                panel.loc[mask, "retail_optimal_baseline"] = panel.loc[mask, raw_baseline_col]
            panel.loc[mask, "retail_optimal_observed_model"] = panel.loc[mask, row.observed_col]
            panel.loc[mask, "retail_optimal_baseline_model"] = panel.loc[mask, row.baseline_col]
            panel.loc[mask, "retail_optimal_discount_share"] = panel.loc[mask, row.discount_col] if row.discount_col in panel.columns else np.nan
            panel.loc[mask, "retail_optimal_n_item_keys"] = panel.loc[mask, row.support_col] if row.support_col in panel.columns else np.nan
        panel = panel.drop(columns=["candidate", "observed_col", "baseline_col", "discount_col", "support_col"], errors="ignore")

    source_frames = {
        "farm_gate": farm,
        "producer": producer,
        "consumer": consumer,
        "prozorro": prozorro,
        "silpo_daily": silpo,
        "novus_daily": novus,
        "retail_combined": retail,
        "retail_items_full": retail_items_full,
        "retail_catalog": retail_catalog,
        "retail_match_audit": retail_match_audit,
        "retail_brand_daily": retail_brand_daily,
        "retail_brand_support": retail_brand_support,
        "retail_literal_summary": retail_literal_summary,
        "retail_name_reconciliation": reconciliation_examples,
        "retail_level_scores": level_scores,
        "retail_level_selection": level_chosen,
    }
    inventory_rows = []
    for name, df in source_frames.items():
        inventory_rows.append(
            {
                "source": name,
                "rows": len(df),
                "products": df["product"].nunique() if "product" in df.columns else np.nan,
                "date_min": df["date"].min() if "date" in df.columns else pd.NaT,
                "date_max": df["date"].max() if "date" in df.columns else pd.NaT,
                "columns": ", ".join(map(str, df.columns[:20])),
            }
        )
    inventory = pd.DataFrame(inventory_rows)
    return panel, inventory, source_frames


def coverage_table(panel: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "farmgate_initial_linear",
        "farmgate_filled_linear",
        "producer_linear",
        "consumer_linear",
        "prozorro",
        "prozorro_model",
        "retail_observed",
        "retail_observed_model",
        "retail_baseline",
        "retail_baseline_model",
        "retail_consumer_observed",
        "retail_consumer_observed_model",
        "retail_consumer_baseline",
        "retail_consumer_baseline_model",
        "retail_matched_observed",
        "retail_matched_observed_model",
        "retail_optimal_observed",
        "retail_optimal_observed_model",
        "retail_optimal_baseline",
        "retail_optimal_baseline_model",
        "retail_discount_share",
        "retail_unit_observed",
        "retail_unit_observed_model",
        "silpo_observed",
        "silpo_observed_model",
        "novus_observed",
        "novus_observed_model",
    ]
    rows = []
    for product, g in panel.groupby("product"):
        row = {
            "product": product,
            "product_label": PRODUCT_LABELS.get(product, product),
            "date_min": g["date"].min(),
            "date_max": g["date"].max(),
            "n_days": len(g),
        }
        for col in cols:
            if col in g.columns:
                row[f"{col}_n"] = int(g[col].notna().sum())
                row[f"{col}_share"] = float(g[col].notna().mean())
        rows.append(row)
    return pd.DataFrame(rows).sort_values("product")


def fit_hac_ols(y: pd.Series, x: pd.DataFrame, hac_lag: int) -> Optional[sm.regression.linear_model.RegressionResultsWrapper]:
    d = pd.concat([y.rename("_y"), x], axis=1).replace([np.inf, -np.inf], np.nan).dropna()
    if len(d) < 20:
        return None
    y2 = d["_y"]
    x2 = d.drop(columns=["_y"])
    if x2.empty:
        return None
    x2 = sm.add_constant(x2, has_constant="add")
    if x2.drop(columns=["const"], errors="ignore").std(numeric_only=True).fillna(0).sum() <= 0:
        return None
    try:
        return sm.OLS(y2, x2).fit(cov_type="HAC", cov_kwds={"maxlags": int(max(1, min(MAX_HAC_LAG, hac_lag)))})
    except Exception:
        return None


def residual_diagnostics(resid: pd.Series) -> Dict[str, float]:
    r = pd.Series(resid).replace([np.inf, -np.inf], np.nan).dropna()
    if len(r) < 20:
        return {"ljungbox_p": np.nan, "arch_p": np.nan, "jb_p": np.nan}
    lag = min(10, max(2, len(r) // 5))
    try:
        lb = float(acorr_ljungbox(r, lags=[lag], return_df=True)["lb_pvalue"].iloc[0])
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
    return {"ljungbox_p": lb, "arch_p": arch, "jb_p": jb}


def run_local_projection_for_pair(
    g: pd.DataFrame,
    product: str,
    y_col: str,
    x_col: str,
    link: str,
    link_direction: str,
    price_variant: str,
    farm_gate_source: str,
    reconstruction_variant: str,
) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    data = g[["date", y_col, x_col, "retail_discount_share", "retail_discount_depth"]].copy()
    data["ly"] = safe_log(data[y_col])
    data["lx"] = safe_log(data[x_col])
    data["dy"] = data["ly"].diff()
    data["dx"] = data["lx"].diff()
    data["dy_l1"] = data["dy"].shift(1)
    data["dx_l1"] = data["dx"].shift(1)
    data["discount_share"] = safe_num(data["retail_discount_share"]).fillna(0)
    data["discount_depth"] = safe_num(data["retail_discount_depth"]).fillna(0)
    if data[[y_col, x_col]].dropna().shape[0] < MIN_LP_OBS:
        return rows

    for h in HORIZONS:
        data[f"response_h{h}"] = data["ly"].shift(-h) - data["ly"].shift(1)
        base = data[["date", f"response_h{h}", "dx", "dy_l1", "dx_l1", "discount_share", "discount_depth"]].copy()
        control_cols = ["dy_l1", "dx_l1"]
        if base["discount_share"].std(skipna=True) > 1e-8:
            control_cols.append("discount_share")
        if base["discount_depth"].std(skipna=True) > 1e-8:
            control_cols.append("discount_depth")

        fit = fit_hac_ols(base[f"response_h{h}"], base[["dx"] + control_cols], max(1, h))
        if fit is not None:
            d_used = pd.concat([base[f"response_h{h}"], base[["dx"] + control_cols]], axis=1).dropna()
            diag = residual_diagnostics(fit.resid)
            rows.append(
                {
                    "model": "LP_linear",
                    "product": product,
                    "product_label": PRODUCT_LABELS.get(product, product),
                    "link": link,
                    "link_direction": link_direction,
                    "price_variant": price_variant,
                    "farm_gate_source": farm_gate_source,
                    "reconstruction_variant": reconstruction_variant,
                    "horizon_days": h,
                    "n_obs": int(len(d_used)),
                    "coef": float(fit.params.get("dx", np.nan)),
                    "pvalue": float(fit.pvalues.get("dx", np.nan)),
                    "stderr": float(fit.bse.get("dx", np.nan)),
                    "r2": float(getattr(fit, "rsquared", np.nan)),
                    "core_signal": int((len(d_used) >= MIN_LP_OBS) and (float(fit.pvalues.get("dx", 1.0)) < 0.10)),
                    **diag,
                }
            )

        asym = base.copy()
        asym["dx_pos"] = asym["dx"].clip(lower=0)
        asym["dx_neg_abs"] = (-asym["dx"].clip(upper=0)).clip(lower=0)
        asym_controls = ["dx_pos", "dx_neg_abs"] + control_cols
        if asym[["dx_pos", "dx_neg_abs"]].std(skipna=True).fillna(0).sum() > 1e-8:
            fit_a = fit_hac_ols(asym[f"response_h{h}"], asym[asym_controls], max(1, h))
            if fit_a is not None:
                d_used = pd.concat([asym[f"response_h{h}"], asym[asym_controls]], axis=1).dropna()
                try:
                    wald = fit_a.wald_test("dx_pos = dx_neg_abs", scalar=True)
                    asym_p = float(wald.pvalue)
                except Exception:
                    asym_p = np.nan
                diag = residual_diagnostics(fit_a.resid)
                rows.append(
                    {
                        "model": "LP_asymmetric",
                        "product": product,
                        "product_label": PRODUCT_LABELS.get(product, product),
                        "link": link,
                        "link_direction": link_direction,
                        "price_variant": price_variant,
                        "farm_gate_source": farm_gate_source,
                        "reconstruction_variant": reconstruction_variant,
                        "horizon_days": h,
                        "n_obs": int(len(d_used)),
                        "coef_positive_shock": float(fit_a.params.get("dx_pos", np.nan)),
                        "p_positive_shock": float(fit_a.pvalues.get("dx_pos", np.nan)),
                        "coef_negative_shock_abs": float(fit_a.params.get("dx_neg_abs", np.nan)),
                        "p_negative_shock_abs": float(fit_a.pvalues.get("dx_neg_abs", np.nan)),
                        "asymmetry_pvalue": asym_p,
                        "asymmetry_gap": float(fit_a.params.get("dx_pos", np.nan) - fit_a.params.get("dx_neg_abs", np.nan)),
                        "r2": float(getattr(fit_a, "rsquared", np.nan)),
                        "core_signal": int(
                            (len(d_used) >= MIN_LP_OBS)
                            and (
                                float(fit_a.pvalues.get("dx_pos", 1.0)) < 0.10
                                or float(fit_a.pvalues.get("dx_neg_abs", 1.0)) < 0.10
                            )
                        ),
                        **diag,
                    }
                )
    return rows


def lp_link_specs() -> List[Dict[str, str]]:
    specs: List[Dict[str, str]] = []
    for variant in ["linear", "pchip"]:
        producer = f"producer_{variant}_model"
        for fg_source in ["initial", "filled"]:
            farm = f"farmgate_{fg_source}_{variant}_model"
            specs.extend(
                [
                    {
                        "x": farm,
                        "y": producer,
                        "link": "FarmGateUA -> ProducerUA",
                        "direction": "forward",
                        "price_variant": "processor_price",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "x": farm,
                        "y": "prozorro_model",
                        "link": "FarmGateUA -> ProZorro",
                        "direction": "forward",
                        "price_variant": "procurement_price",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                {
                    "x": farm,
                    "y": "retail_observed_model",
                    "link": "FarmGateUA -> Retail",
                    "direction": "forward",
                        "price_variant": "retail_observed",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "x": farm,
                        "y": "retail_consumer_observed_model",
                        "link": "FarmGateUA -> Retail+Consumer",
                        "direction": "forward",
                        "price_variant": "retail_consumer_observed",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "x": "retail_observed_model",
                        "y": farm,
                        "link": "Retail -> FarmGateUA",
                        "direction": "reverse",
                        "price_variant": "retail_observed",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "x": "retail_consumer_observed_model",
                        "y": farm,
                        "link": "Retail+Consumer -> FarmGateUA",
                        "direction": "reverse",
                        "price_variant": "retail_consumer_observed",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "x": producer,
                        "y": farm,
                        "link": "ProducerUA -> FarmGateUA",
                        "direction": "reverse",
                        "price_variant": "processor_price",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "x": farm,
                        "y": "retail_optimal_observed_model",
                        "link": "FarmGateUA -> Retail optimal",
                        "direction": "forward",
                        "price_variant": "retail_optimal_observed",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "x": "retail_optimal_observed_model",
                        "y": farm,
                        "link": "Retail optimal -> FarmGateUA",
                        "direction": "reverse",
                        "price_variant": "retail_optimal_observed",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                ]
            )
        specs.extend(
            [
                {
                    "x": producer,
                    "y": "prozorro_model",
                    "link": "ProducerUA -> ProZorro",
                    "direction": "forward",
                    "price_variant": "procurement_price",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "retail_observed_model",
                    "link": "ProZorro -> Retail",
                    "direction": "forward",
                    "price_variant": "retail_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "retail_consumer_observed_model",
                    "link": "ProZorro -> Retail+Consumer",
                    "direction": "forward",
                    "price_variant": "retail_consumer_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "retail_baseline_model",
                    "link": "ProZorro -> Retail",
                    "direction": "forward",
                    "price_variant": "retail_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "retail_consumer_baseline_model",
                    "link": "ProZorro -> Retail+Consumer",
                    "direction": "forward",
                    "price_variant": "retail_consumer_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "retail_observed_model",
                    "y": "prozorro_model",
                    "link": "Retail -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "retail_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "retail_consumer_observed_model",
                    "y": "prozorro_model",
                    "link": "Retail+Consumer -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "retail_consumer_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "retail_baseline_model",
                    "y": "prozorro_model",
                    "link": "Retail -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "retail_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "retail_consumer_baseline_model",
                    "y": "prozorro_model",
                    "link": "Retail+Consumer -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "retail_consumer_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": producer,
                    "link": "ProZorro -> ProducerUA",
                    "direction": "reverse",
                    "price_variant": "processor_price",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
            ]
        )
        specs.extend(
            [
                {
                    "x": "prozorro_model",
                    "y": "retail_matched_observed_model",
                    "link": "ProZorro -> Retail matched",
                    "direction": "forward",
                    "price_variant": "retail_matched_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "retail_matched_baseline_model",
                    "link": "ProZorro -> Retail matched",
                    "direction": "forward",
                    "price_variant": "retail_matched_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "retail_matched_observed_model",
                    "y": "prozorro_model",
                    "link": "Retail matched -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "retail_matched_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "retail_matched_baseline_model",
                    "y": "prozorro_model",
                    "link": "Retail matched -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "retail_matched_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "silpo_observed_model",
                    "link": "ProZorro -> Silpo",
                    "direction": "forward",
                    "price_variant": "silpo_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "silpo_baseline_model",
                    "link": "ProZorro -> Silpo",
                    "direction": "forward",
                    "price_variant": "silpo_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "silpo_observed_model",
                    "y": "prozorro_model",
                    "link": "Silpo -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "silpo_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "silpo_baseline_model",
                    "y": "prozorro_model",
                    "link": "Silpo -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "silpo_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "novus_observed_model",
                    "link": "ProZorro -> Novus",
                    "direction": "forward",
                    "price_variant": "novus_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "novus_observed_model",
                    "y": "prozorro_model",
                    "link": "Novus -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "novus_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "retail_optimal_observed_model",
                    "link": "ProZorro -> Retail optimal",
                    "direction": "forward",
                    "price_variant": "retail_optimal_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "prozorro_model",
                    "y": "retail_optimal_baseline_model",
                    "link": "ProZorro -> Retail optimal",
                    "direction": "forward",
                    "price_variant": "retail_optimal_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "retail_optimal_observed_model",
                    "y": "prozorro_model",
                    "link": "Retail optimal -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "retail_optimal_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "x": "retail_optimal_baseline_model",
                    "y": "prozorro_model",
                    "link": "Retail optimal -> ProZorro",
                    "direction": "reverse",
                    "price_variant": "retail_optimal_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
            ]
        )
    return specs


def run_local_projections(panel: pd.DataFrame) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    specs = lp_link_specs()
    available = set(panel.columns)
    for product, g in panel.groupby("product"):
        g = g.sort_values("date")
        for spec in specs:
            if spec["x"] not in available or spec["y"] not in available:
                continue
            rows.extend(
                run_local_projection_for_pair(
                    g,
                    product=product,
                    y_col=spec["y"],
                    x_col=spec["x"],
                    link=spec["link"],
                    link_direction=spec["direction"],
                    price_variant=spec["price_variant"],
                    farm_gate_source=spec["farm_gate_source"],
                    reconstruction_variant=spec["reconstruction_variant"],
                )
            )
    return pd.DataFrame(rows)


def summarize_lp(lp: pd.DataFrame) -> pd.DataFrame:
    if lp.empty:
        return pd.DataFrame()
    linear = lp[lp["model"].eq("LP_linear")].copy()
    if linear.empty:
        return pd.DataFrame()
    summary = (
        linear.groupby(["link", "link_direction", "price_variant", "horizon_days"], as_index=False)
        .agg(
            models=("coef", "size"),
            products=("product", pd.Series.nunique),
            variants=("reconstruction_variant", pd.Series.nunique),
            mean_coef=("coef", "mean"),
            median_coef=("coef", "median"),
            mean_abs_coef=("coef", lambda s: float(np.nanmean(np.abs(s)))),
            sig_share=("pvalue", lambda s: float(np.nanmean(s < 0.10))),
            core_share=("core_signal", "mean"),
            median_n_obs=("n_obs", "median"),
        )
        .sort_values(["horizon_days", "link"])
    )
    return summary


def margin_specs() -> List[Dict[str, str]]:
    specs = []
    for variant in ["linear", "pchip"]:
        producer = f"producer_{variant}_model"
        for fg_source in ["initial", "filled"]:
            farm = f"farmgate_{fg_source}_{variant}_model"
            specs.extend(
                [
                    {
                        "upstream": farm,
                        "downstream": producer,
                        "spread": "ProducerUA / FarmGateUA",
                        "stage": "producer_farmgate",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                {
                    "upstream": farm,
                    "downstream": "retail_observed_model",
                    "spread": "Retail observed / FarmGateUA",
                        "stage": "retail_farmgate_observed",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "upstream": farm,
                        "downstream": "retail_baseline_model",
                        "spread": "Retail baseline / FarmGateUA",
                        "stage": "retail_farmgate_baseline",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                    {
                        "upstream": farm,
                        "downstream": "retail_consumer_observed_model",
                        "spread": "Retail+Consumer observed / FarmGateUA",
                        "stage": "retail_consumer_farmgate_observed",
                        "farm_gate_source": fg_source,
                        "reconstruction_variant": variant,
                    },
                ]
            )
        specs.extend(
            [
                {
                    "upstream": producer,
                    "downstream": "prozorro_model",
                    "spread": "ProZorro / ProducerUA",
                    "stage": "procurement_producer",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "retail_observed_model",
                    "spread": "Retail observed / ProZorro",
                    "stage": "retail_procurement_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "retail_baseline_model",
                    "spread": "Retail baseline / ProZorro",
                    "stage": "retail_procurement_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "retail_consumer_observed_model",
                    "spread": "Retail+Consumer observed / ProZorro",
                    "stage": "retail_consumer_procurement_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "retail_consumer_baseline_model",
                    "spread": "Retail+Consumer baseline / ProZorro",
                    "stage": "retail_consumer_procurement_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "retail_matched_observed_model",
                    "spread": "Retail matched observed / ProZorro",
                    "stage": "retail_matched_procurement_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "retail_matched_baseline_model",
                    "spread": "Retail matched baseline / ProZorro",
                    "stage": "retail_matched_procurement_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "silpo_observed_model",
                    "spread": "Silpo observed / ProZorro",
                    "stage": "silpo_procurement_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "silpo_baseline_model",
                    "spread": "Silpo baseline / ProZorro",
                    "stage": "silpo_procurement_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "novus_observed_model",
                    "spread": "Novus observed / ProZorro",
                    "stage": "novus_procurement_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "retail_optimal_observed_model",
                    "spread": "Retail optimal observed / ProZorro",
                    "stage": "retail_optimal_procurement_observed",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
                {
                    "upstream": "prozorro_model",
                    "downstream": "retail_optimal_baseline_model",
                    "spread": "Retail optimal baseline / ProZorro",
                    "stage": "retail_optimal_procurement_baseline",
                    "farm_gate_source": "not_applicable",
                    "reconstruction_variant": variant,
                },
            ]
        )
    return specs


def run_margin_models(panel: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    rows: List[Dict[str, object]] = []
    spread_rows: List[Dict[str, object]] = []
    specs = margin_specs()
    for product, g in panel.groupby("product"):
        g = g.sort_values("date").copy()
        for spec in specs:
            if spec["upstream"] not in g.columns or spec["downstream"] not in g.columns:
                continue
            d = g[["date", spec["upstream"], spec["downstream"], "retail_discount_share", "retail_discount_depth"]].copy()
            d["lu"] = safe_log(d[spec["upstream"]])
            d["ld"] = safe_log(d[spec["downstream"]])
            d["spread"] = d["ld"] - d["lu"]
            d["dspread"] = d["spread"].diff()
            d["lag_spread"] = d["spread"].shift(1)
            d["du"] = d["lu"].diff()
            d["upstream_pos"] = d["du"].clip(lower=0)
            d["upstream_neg_abs"] = (-d["du"].clip(upper=0)).clip(lower=0)
            d["discount_share"] = safe_num(d["retail_discount_share"]).fillna(0)
            d["discount_depth"] = safe_num(d["retail_discount_depth"]).fillna(0)
            usable = d[["spread", "dspread", "lag_spread", "upstream_pos", "upstream_neg_abs"]].dropna()
            if len(usable) < MIN_MARGIN_OBS:
                continue
            exog_cols = ["lag_spread", "upstream_pos", "upstream_neg_abs"]
            if d["discount_share"].std(skipna=True) > 1e-8:
                exog_cols.append("discount_share")
            if d["discount_depth"].std(skipna=True) > 1e-8:
                exog_cols.append("discount_depth")
            fit = fit_hac_ols(d["dspread"], d[exog_cols], hac_lag=7)
            spread_clean = d["spread"].dropna()
            spread_rows.append(
                {
                    "product": product,
                    "product_label": PRODUCT_LABELS.get(product, product),
                    "stage": spec["stage"],
                    "spread": spec["spread"],
                    "farm_gate_source": spec["farm_gate_source"],
                    "reconstruction_variant": spec["reconstruction_variant"],
                    "n_obs": int(len(spread_clean)),
                    "mean_log_spread": float(spread_clean.mean()),
                    "median_log_spread": float(spread_clean.median()),
                    "sd_log_spread": float(spread_clean.std(ddof=1)),
                    "mean_price_ratio": float(np.exp(spread_clean.mean())),
                    "date_min": d.loc[d["spread"].notna(), "date"].min(),
                    "date_max": d.loc[d["spread"].notna(), "date"].max(),
                }
            )
            if fit is None:
                continue
            used = pd.concat([d["dspread"], d[exog_cols]], axis=1).dropna()
            try:
                wald = fit.wald_test("upstream_pos = upstream_neg_abs", scalar=True)
                asym_p = float(wald.pvalue)
            except Exception:
                asym_p = np.nan
            diag = residual_diagnostics(fit.resid)
            rows.append(
                {
                    "product": product,
                    "product_label": PRODUCT_LABELS.get(product, product),
                    "stage": spec["stage"],
                    "spread": spec["spread"],
                    "farm_gate_source": spec["farm_gate_source"],
                    "reconstruction_variant": spec["reconstruction_variant"],
                    "n_obs": int(len(used)),
                    "lag_spread_coef": float(fit.params.get("lag_spread", np.nan)),
                    "lag_spread_p": float(fit.pvalues.get("lag_spread", np.nan)),
                    "upstream_pos_coef": float(fit.params.get("upstream_pos", np.nan)),
                    "upstream_pos_p": float(fit.pvalues.get("upstream_pos", np.nan)),
                    "upstream_neg_abs_coef": float(fit.params.get("upstream_neg_abs", np.nan)),
                    "upstream_neg_abs_p": float(fit.pvalues.get("upstream_neg_abs", np.nan)),
                    "asymmetry_pvalue": asym_p,
                    "discount_share_coef": float(fit.params.get("discount_share", np.nan)),
                    "discount_share_p": float(fit.pvalues.get("discount_share", np.nan)),
                    "discount_depth_coef": float(fit.params.get("discount_depth", np.nan)),
                    "discount_depth_p": float(fit.pvalues.get("discount_depth", np.nan)),
                    "r2": float(getattr(fit, "rsquared", np.nan)),
                    "persistent_margin_flag": int(
                        not (
                            float(fit.params.get("lag_spread", 0)) < 0
                            and float(fit.pvalues.get("lag_spread", 1.0)) < 0.10
                        )
                    ),
                    "asymmetric_margin_flag": int(pd.notna(asym_p) and asym_p < 0.10),
                    **diag,
                }
            )
    return pd.DataFrame(rows), pd.DataFrame(spread_rows)


def run_discount_models(panel: pd.DataFrame) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for product, g in panel.groupby("product"):
        g = g.sort_values("date").copy()
        cols = ["retail_discount_share", "retail_discount_depth", "retail_observed_model", "retail_baseline_model", "prozorro_model", "producer_linear_model", "farmgate_filled_linear_model"]
        if any(c not in g.columns for c in cols):
            continue
        d = g[["date"] + cols].copy()
        d["discount_share"] = safe_num(d["retail_discount_share"]).fillna(0)
        if d["discount_share"].std(skipna=True) <= 1e-8:
            continue
        d["retail_gap"] = safe_log(d["retail_baseline_model"]) - safe_log(d["retail_observed_model"])
        d["retail_procurement_spread"] = safe_log(d["retail_baseline_model"]) - safe_log(d["prozorro_model"])
        d["d_producer"] = safe_log(d["producer_linear_model"]).diff()
        d["d_prozorro"] = safe_log(d["prozorro_model"]).diff()
        d["d_farmgate"] = safe_log(d["farmgate_filled_linear_model"]).diff()
        d["abs_d_producer"] = d["d_producer"].abs()
        d["abs_d_prozorro"] = d["d_prozorro"].abs()
        d["abs_d_farmgate"] = d["d_farmgate"].abs()
        d["lag_discount"] = d["discount_share"].shift(1)
        d["lag_spread"] = d["retail_procurement_spread"].shift(1)
        exog_cols = ["lag_discount", "lag_spread", "abs_d_producer", "abs_d_prozorro", "abs_d_farmgate"]
        used = d[["discount_share"] + exog_cols].replace([np.inf, -np.inf], np.nan).dropna()
        if len(used) < MIN_DISCOUNT_OBS:
            continue
        fit = fit_hac_ols(d["discount_share"], d[exog_cols], hac_lag=7)
        if fit is None:
            continue
        rows.append(
            {
                "product": product,
                "product_label": PRODUCT_LABELS.get(product, product),
                "n_obs": int(len(used)),
                "mean_discount_share": float(d["discount_share"].mean()),
                "lag_discount_coef": float(fit.params.get("lag_discount", np.nan)),
                "lag_discount_p": float(fit.pvalues.get("lag_discount", np.nan)),
                "lag_spread_coef": float(fit.params.get("lag_spread", np.nan)),
                "lag_spread_p": float(fit.pvalues.get("lag_spread", np.nan)),
                "abs_d_producer_coef": float(fit.params.get("abs_d_producer", np.nan)),
                "abs_d_producer_p": float(fit.pvalues.get("abs_d_producer", np.nan)),
                "abs_d_prozorro_coef": float(fit.params.get("abs_d_prozorro", np.nan)),
                "abs_d_prozorro_p": float(fit.pvalues.get("abs_d_prozorro", np.nan)),
                "abs_d_farmgate_coef": float(fit.params.get("abs_d_farmgate", np.nan)),
                "abs_d_farmgate_p": float(fit.pvalues.get("abs_d_farmgate", np.nan)),
                "r2": float(getattr(fit, "rsquared", np.nan)),
                "discount_strategy_signal": int(
                    float(fit.pvalues.get("lag_spread", 1.0)) < 0.10
                    or float(fit.pvalues.get("abs_d_producer", 1.0)) < 0.10
                    or float(fit.pvalues.get("abs_d_prozorro", 1.0)) < 0.10
                ),
            }
        )
    return pd.DataFrame(rows)


def robust_findings(lp: pd.DataFrame, margins: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    if not lp.empty:
        linear = lp[(lp["model"].eq("LP_linear")) & (lp["horizon_days"].isin([7, 14]))].copy()
        linear["sign"] = np.sign(linear["coef"])
        grouped = linear.groupby(["link", "product", "price_variant"], dropna=False)
        for (link, product, price_variant), g in grouped:
            core = g[g["core_signal"].eq(1)]
            if core.empty:
                continue
            signs = core["sign"].dropna().unique()
            rows.append(
                {
                    "finding_type": "local_projection",
                    "link_or_stage": link,
                    "product": product,
                    "product_label": PRODUCT_LABELS.get(product, product),
                    "price_variant": price_variant,
                    "n_core_rows": int(len(core)),
                    "median_coef": float(core["coef"].median()),
                    "directionally_stable": int(len(signs) == 1),
                    "interpretation_flag": "stronger" if len(core) >= 3 and len(signs) == 1 else "selective",
                }
            )
    if not margins.empty:
        for _, row in margins[margins.get("asymmetric_margin_flag", 0).eq(1) | margins.get("persistent_margin_flag", 0).eq(1)].iterrows():
            rows.append(
                {
                    "finding_type": "margin_power_proxy",
                    "link_or_stage": row["stage"],
                    "product": row["product"],
                    "product_label": row["product_label"],
                    "price_variant": row["spread"],
                    "n_core_rows": 1,
                    "median_coef": row.get("lag_spread_coef", np.nan),
                    "directionally_stable": np.nan,
                    "interpretation_flag": "proxy_only",
                }
            )
    if not discounts.empty:
        for _, row in discounts[discounts.get("discount_strategy_signal", 0).eq(1)].iterrows():
            rows.append(
                {
                    "finding_type": "discount_strategy",
                    "link_or_stage": "Silpo/retail discount incidence",
                    "product": row["product"],
                    "product_label": row["product_label"],
                    "price_variant": "discount_share",
                    "n_core_rows": 1,
                    "median_coef": row.get("lag_spread_coef", np.nan),
                    "directionally_stable": np.nan,
                    "interpretation_flag": "retail_price_management_signal",
                }
            )
    return pd.DataFrame(rows)


def save_plot(fig_path: Path) -> None:
    plt.tight_layout()
    plt.savefig(fig_path, dpi=180, bbox_inches="tight")
    plt.close()


def plot_outputs(panel: pd.DataFrame, coverage: pd.DataFrame, lp_summary: pd.DataFrame, margins_summary: pd.DataFrame, discounts: pd.DataFrame, source_frames: Dict[str, pd.DataFrame]) -> None:
    cov_cols = [c for c in coverage.columns if c.endswith("_n") and any(k in c for k in ["producer", "prozorro", "retail_observed", "retail_consumer", "farmgate_filled", "consumer"])]
    if cov_cols:
        data = coverage.set_index("product_label")[cov_cols].fillna(0)
        plt.figure(figsize=(11, max(4, 0.45 * len(data))))
        plt.imshow(data.values, aspect="auto", cmap="Blues")
        plt.colorbar(label="non-missing product-days")
        plt.yticks(range(len(data.index)), data.index)
        plt.xticks(range(len(data.columns)), [c.replace("_n", "") for c in data.columns], rotation=45, ha="right")
        plt.title("Second-stage panel coverage by product and source")
        save_plot(FIG_DIR / "01_panel_coverage.png")

    if not lp_summary.empty:
        focus = lp_summary[
            lp_summary["link"].isin(
                [
                    "FarmGateUA -> ProZorro",
                    "ProducerUA -> ProZorro",
                    "ProZorro -> Retail",
                    "ProZorro -> Retail+Consumer",
                    "Retail -> ProZorro",
                    "Retail+Consumer -> ProZorro",
                    "Retail -> FarmGateUA",
                    "Retail+Consumer -> FarmGateUA",
                ]
            )
            & lp_summary["price_variant"].isin(["retail_observed", "retail_consumer_observed", "procurement_price", "processor_price"])
        ].copy()
        if not focus.empty:
            plt.figure(figsize=(11, 6))
            for label, g in focus.groupby("link"):
                h = g.groupby("horizon_days", as_index=False)["mean_coef"].mean()
                plt.plot(h["horizon_days"], h["mean_coef"], marker="o", label=label)
            plt.axhline(0, color="black", linewidth=0.8)
            plt.xlabel("Horizon, days")
            plt.ylabel("Mean local-projection coefficient")
            plt.title("Local-projection pass-through by horizon")
            plt.legend(fontsize=8)
            save_plot(FIG_DIR / "02_lp_pass_through_horizons.png")

        h7 = lp_summary[lp_summary["horizon_days"].isin([7, 14])].copy()
        if not h7.empty:
            chart = h7.groupby(["link_direction", "link"], as_index=False)["core_share"].mean().sort_values("core_share")
            plt.figure(figsize=(11, max(4, 0.35 * len(chart))))
            colors = chart["link_direction"].map({"forward": "#2c7fb8", "reverse": "#f03b20"}).fillna("#969696")
            plt.barh(chart["link"], chart["core_share"], color=colors)
            plt.xlabel("Core-signal share at 7/14-day horizons")
            plt.title("Forward versus reverse second-stage evidence")
            save_plot(FIG_DIR / "03_forward_reverse_core_share.png")

    if not margins_summary.empty:
        chart = margins_summary.groupby("spread", as_index=False)["mean_price_ratio"].median().sort_values("mean_price_ratio")
        plt.figure(figsize=(10, max(4, 0.35 * len(chart))))
        plt.barh(chart["spread"], chart["mean_price_ratio"], color="#756bb1")
        plt.axvline(1, color="black", linewidth=0.8)
        plt.xlabel("Median exp(mean log spread)")
        plt.title("Vertical spread / market-power proxy by chain segment")
        save_plot(FIG_DIR / "04_vertical_spread_proxy.png")

    if not discounts.empty:
        chart = discounts.sort_values("mean_discount_share")
        plt.figure(figsize=(9, max(4, 0.45 * len(chart))))
        plt.barh(chart["product_label"], chart["mean_discount_share"], color="#31a354")
        plt.xlabel("Mean discount share")
        plt.title("Retail discount incidence by product")
        save_plot(FIG_DIR / "05_discount_incidence.png")

    if "retail_match_audit" in source_frames:
        audit = source_frames["retail_match_audit"].copy()
        if not audit.empty and "match_status" in audit.columns:
            chart = audit["match_status"].value_counts().rename_axis("match_status").reset_index(name="n")
            plt.figure(figsize=(8, 5))
            plt.bar(chart["match_status"], chart["n"], color=["#238b45", "#9ecae1", "#fc9272"][: len(chart)])
            plt.ylabel("Unique harmonized item keys")
            plt.title("Cross-shop retail item harmonization status")
            plt.xticks(rotation=15, ha="right")
            save_plot(FIG_DIR / "06_cross_shop_match_status.png")

    literal_summary = source_frames.get("retail_literal_summary", pd.DataFrame())
    if not literal_summary.empty:
        chart = (
            literal_summary.groupby(["product", "product_literal"], as_index=False)["n_item_keys"]
            .sum()
            .assign(product_label=lambda d: d["product"].map(PRODUCT_LABELS).fillna(d["product"]))
        )
        pivot = chart.pivot_table(index="product_label", columns="product_literal", values="n_item_keys", aggfunc="sum", fill_value=0)
        if not pivot.empty:
            plt.figure(figsize=(12, max(4, 0.45 * len(pivot))))
            plt.imshow(pivot.values, aspect="auto", cmap="YlGnBu")
            plt.colorbar(label="Unique item keys")
            plt.yticks(range(len(pivot.index)), pivot.index)
            plt.xticks(range(len(pivot.columns)), [LITERAL_LABELS.get(c, c) for c in pivot.columns], rotation=45, ha="right")
            plt.title("Retail literal-product mix after dairy-only reconciliation")
            save_plot(FIG_DIR / "07_retail_literal_mix.png")

    brand_support = source_frames.get("retail_brand_support", pd.DataFrame())
    if not brand_support.empty:
        brand_support = brand_support.copy()
        brand_support["brand_norm"] = brand_support["brand_norm"].fillna("").astype(str).str.strip()
        brand_support["brand_named_flag"] = brand_support["brand_norm"].ne("").astype(int)
        top_brand = (
            brand_support.sort_values(["product", "retailer", "brand_named_flag", "n_rows"], ascending=[True, True, False, False])
            .groupby(["product", "retailer"], as_index=False)
            .head(1)
            .copy()
        )
        if not top_brand.empty:
            top_brand["brand_label"] = top_brand["brand_norm"].replace("", "unlabeled brand")
            top_brand["label"] = top_brand["product"].map(PRODUCT_LABELS).fillna(top_brand["product"]) + " | " + top_brand["retailer"] + " | " + top_brand["brand_label"]
            top_brand = top_brand.sort_values("n_item_keys")
            plt.figure(figsize=(12, max(4, 0.35 * len(top_brand))))
            plt.barh(top_brand["label"], top_brand["n_item_keys"], color="#3182bd")
            plt.xlabel("Unique item keys in dominant reconciled brand")
            plt.title("Dominant retailer-brand support by dairy product")
            save_plot(FIG_DIR / "08_dominant_brand_support.png")

    level_scores = source_frames.get("retail_level_scores", pd.DataFrame())
    if not level_scores.empty:
        pivot = level_scores.pivot_table(index="product_label", columns="candidate_label", values="selection_score", aggfunc="max", fill_value=0)
        if not pivot.empty:
            plt.figure(figsize=(11, max(4, 0.45 * len(pivot))))
            plt.imshow(pivot.values, aspect="auto", cmap="PuBu")
            plt.colorbar(label="Composite selection score")
            plt.yticks(range(len(pivot.index)), pivot.index)
            plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=45, ha="right")
            plt.title("Retail-level candidate scores by product")
            save_plot(FIG_DIR / "09_retail_level_scores.png")

    level_selection = source_frames.get("retail_level_selection", pd.DataFrame())
    if not level_selection.empty:
        chosen = level_selection.sort_values("selection_score")
        codes = {label: idx for idx, label in enumerate(sorted(chosen["candidate_label"].unique()))}
        colors = [plt.cm.Set2(codes[label] / max(1, len(codes) - 1)) for label in chosen["candidate_label"]]
        plt.figure(figsize=(11, max(4, 0.45 * len(chosen))))
        plt.barh(chosen["product_label"], chosen["selection_score"], color=colors)
        plt.xlabel("Composite selection score")
        plt.title("Chosen optimal retail level by product")
        save_plot(FIG_DIR / "10_optimal_retail_level.png")

    if not lp_summary.empty:
        candidate_links = [
            "ProZorro -> Retail",
            "ProZorro -> Retail+Consumer",
            "ProZorro -> Retail matched",
            "ProZorro -> Silpo",
            "ProZorro -> Novus",
            "ProZorro -> Retail optimal",
        ]
        chart = (
            lp_summary[
                lp_summary["link"].isin(candidate_links)
                & lp_summary["horizon_days"].isin([7, 14])
                & lp_summary["price_variant"].isin(
                    [
                        "retail_observed",
                        "retail_consumer_observed",
                        "retail_matched_observed",
                        "silpo_observed",
                        "novus_observed",
                        "retail_optimal_observed",
                    ]
                )
            ]
            .groupby("link", as_index=False)["core_share"]
            .mean()
            .sort_values("core_share")
        )
        if not chart.empty:
            plt.figure(figsize=(10, max(4, 0.45 * len(chart))))
            plt.barh(chart["link"], chart["core_share"], color="#dd3497")
            plt.xlabel("Mean 7/14-day core share")
            plt.title("Candidate downstream levels in procurement-to-retail LP tests")
            save_plot(FIG_DIR / "11_candidate_downstream_core_share.png")

    items = source_frames.get("retail_items_full", pd.DataFrame())
    if not items.empty:
        chart = (
            items.groupby(["retailer", "product"], as_index=False)
            .agg(mean_discount_share=("discount_present", "mean"), median_markdown=("markdown_rate", "median"))
            .assign(product_label=lambda d: d["product"].map(PRODUCT_LABELS).fillna(d["product"]))
        )
        pivot1 = chart.pivot_table(index="product_label", columns="retailer", values="mean_discount_share", aggfunc="mean", fill_value=0)
        pivot2 = chart.pivot_table(index="product_label", columns="retailer", values="median_markdown", aggfunc="mean", fill_value=0)
        if not pivot1.empty and not pivot2.empty:
            fig, axes = plt.subplots(1, 2, figsize=(12, max(4, 0.45 * len(pivot1))), sharey=True)
            im1 = axes[0].imshow(pivot1.values, aspect="auto", cmap="Greens")
            axes[0].set_title("Mean discount share")
            axes[0].set_xticks(range(len(pivot1.columns)))
            axes[0].set_xticklabels(pivot1.columns, rotation=45, ha="right")
            axes[0].set_yticks(range(len(pivot1.index)))
            axes[0].set_yticklabels(pivot1.index)
            fig.colorbar(im1, ax=axes[0], fraction=0.046, pad=0.04)
            im2 = axes[1].imshow(pivot2.values, aspect="auto", cmap="OrRd")
            axes[1].set_title("Median markdown depth")
            axes[1].set_xticks(range(len(pivot2.columns)))
            axes[1].set_xticklabels(pivot2.columns, rotation=45, ha="right")
            fig.colorbar(im2, ax=axes[1], fraction=0.046, pad=0.04)
            fig.suptitle("Retail discount environment by product and retailer")
            save_plot(FIG_DIR / "12_discount_environment.png")


def write_excel_outputs(
    panel: pd.DataFrame,
    inventory: pd.DataFrame,
    source_frames: Dict[str, pd.DataFrame],
    coverage: pd.DataFrame,
    lp: pd.DataFrame,
    lp_summary: pd.DataFrame,
    margins: pd.DataFrame,
    margin_spreads: pd.DataFrame,
    discounts: pd.DataFrame,
    findings: pd.DataFrame,
) -> None:
    out_xlsx = OUTPUT_DIR / "second_stage_model_outputs.xlsx"
    readme = pd.DataFrame(
        [
            {
                "item": "analysis_scope",
                "value": "Second-stage daily product-panel analysis using local projections and margin/discount proxy models.",
            },
            {
                "item": "input_workbook",
                "value": str(FULL_UAH),
            },
            {
                "item": "farm_gate_inputs",
                "value": "; ".join(str(p) for p in FARM_GATE_FILES.values()),
            },
            {
                "item": "method_difference_from_rw4",
                "value": "Uses local projections and spread regressions rather than the prior ARDL/ECM/NARDL/VECM stack.",
            },
            {
                "item": "created",
                "value": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },
        ]
    )
    with pd.ExcelWriter(out_xlsx, engine="openpyxl") as writer:
        readme.to_excel(writer, sheet_name="README", index=False)
        inventory.to_excel(writer, sheet_name="Data_Inventory", index=False)
        coverage.to_excel(writer, sheet_name="Panel_Coverage", index=False)
        if "retail_catalog" in source_frames:
            source_frames["retail_catalog"].to_excel(writer, sheet_name="Retail_Item_Catalog", index=False)
        if "retail_match_audit" in source_frames:
            source_frames["retail_match_audit"].to_excel(writer, sheet_name="Retail_Match_Audit", index=False)
        if "retail_brand_support" in source_frames:
            source_frames["retail_brand_support"].to_excel(writer, sheet_name="Retail_Brand_Support", index=False)
        if "retail_literal_summary" in source_frames:
            source_frames["retail_literal_summary"].to_excel(writer, sheet_name="Retail_Literal_Summary", index=False)
        if "retail_name_reconciliation" in source_frames:
            source_frames["retail_name_reconciliation"].to_excel(writer, sheet_name="Retail_Name_Recon", index=False)
        if "retail_level_scores" in source_frames:
            source_frames["retail_level_scores"].to_excel(writer, sheet_name="Retail_Level_Scores", index=False)
        if "retail_level_selection" in source_frames:
            source_frames["retail_level_selection"].to_excel(writer, sheet_name="Retail_Level_Choice", index=False)
        if "consumer" in source_frames:
            source_frames["consumer"].to_excel(writer, sheet_name="ConsumerUA_Clean", index=False)
        lp.to_excel(writer, sheet_name="Local_Projections", index=False)
        lp_summary.to_excel(writer, sheet_name="LP_Summary", index=False)
        margins.to_excel(writer, sheet_name="Margin_Models", index=False)
        margin_spreads.to_excel(writer, sheet_name="Spread_Summary", index=False)
        discounts.to_excel(writer, sheet_name="Discount_Models", index=False)
        findings.to_excel(writer, sheet_name="Robust_Findings", index=False)
    panel.to_csv(DATA_DIR / "second_stage_daily_panel.csv", index=False)
    coverage.to_csv(DATA_DIR / "second_stage_panel_coverage.csv", index=False)
    optimal_cols = [c for c in ["date", "product", "product_label", "retail_optimal_observed", "retail_optimal_baseline", "retail_optimal_observed_model", "retail_optimal_baseline_model", "retail_optimal_discount_share", "retail_optimal_n_item_keys"] if c in panel.columns]
    if optimal_cols:
        panel[optimal_cols].to_csv(DATA_DIR / "retail_optimal_daily.csv", index=False)
    if "retail_items_full" in source_frames:
        source_frames["retail_items_full"].to_csv(DATA_DIR / "retail_items_full_harmonized.csv", index=False)
    if "retail_catalog" in source_frames:
        source_frames["retail_catalog"].to_csv(DATA_DIR / "retail_item_catalog.csv", index=False)
    if "retail_match_audit" in source_frames:
        source_frames["retail_match_audit"].to_csv(DATA_DIR / "retail_match_audit.csv", index=False)
    if "retail_brand_daily" in source_frames:
        source_frames["retail_brand_daily"].to_csv(DATA_DIR / "retail_brand_daily.csv", index=False)
    if "retail_brand_support" in source_frames:
        source_frames["retail_brand_support"].to_csv(DATA_DIR / "retail_brand_support.csv", index=False)
    if "retail_literal_summary" in source_frames:
        source_frames["retail_literal_summary"].to_csv(DATA_DIR / "retail_literal_summary.csv", index=False)
    if "retail_name_reconciliation" in source_frames:
        source_frames["retail_name_reconciliation"].to_csv(DATA_DIR / "retail_name_reconciliation_examples.csv", index=False)
    if "retail_level_scores" in source_frames:
        source_frames["retail_level_scores"].to_csv(DATA_DIR / "retail_level_scores.csv", index=False)
    if "retail_level_selection" in source_frames:
        source_frames["retail_level_selection"].to_csv(DATA_DIR / "retail_level_selection.csv", index=False)
    if "consumer" in source_frames:
        source_frames["consumer"].to_csv(DATA_DIR / "consumerua_clean_daily.csv", index=False)
    lp.to_csv(OUTPUT_DIR / "local_projection_coefficients.csv", index=False)
    lp_summary.to_csv(OUTPUT_DIR / "local_projection_summary.csv", index=False)
    margins.to_csv(OUTPUT_DIR / "margin_market_power_models.csv", index=False)
    margin_spreads.to_csv(OUTPUT_DIR / "vertical_spread_summary.csv", index=False)
    discounts.to_csv(OUTPUT_DIR / "discount_strategy_models.csv", index=False)
    findings.to_csv(OUTPUT_DIR / "robust_findings.csv", index=False)


def fmt_pct(value: float, digits: int = 1) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{100 * float(value):.{digits}f}%"


def fmt_num(value: float, digits: int = 3) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{float(value):.{digits}f}"


def top_lp_sentence(lp_summary: pd.DataFrame) -> str:
    if lp_summary.empty:
        return "No local-projection models passed the minimum-overlap screen."
    h = lp_summary[lp_summary["horizon_days"].isin([7, 14])].copy()
    if h.empty:
        h = lp_summary.copy()
    # The farm-gate/producer diagnostic is long and smooth because both sides are reconstructed.
    # Keep it in the workbook, but do not make it the headline thesis signal.
    thesis_focus = h[~h["link"].isin(["FarmGateUA -> ProducerUA", "ProducerUA -> FarmGateUA"])].copy()
    if not thesis_focus.empty:
        h = thesis_focus
    best = h.sort_values(["core_share", "sig_share", "models"], ascending=False).head(5)
    parts = [
        f"{r.link} ({r.price_variant}, h={int(r.horizon_days)}): core share {fmt_pct(r.core_share)}, median coefficient {fmt_num(r.median_coef)}"
        for r in best.itertuples()
    ]
    return "; ".join(parts) + "."


def top_brand_sentence(brand_support: pd.DataFrame) -> str:
    if brand_support.empty:
        return "No brand-level retail support table was generated."
    brand_support = brand_support.copy()
    brand_support["brand_norm"] = brand_support["brand_norm"].fillna("").astype(str).str.strip()
    brand_support["brand_named_flag"] = brand_support["brand_norm"].ne("").astype(int)
    top = (
        brand_support.sort_values(["product", "retailer", "brand_named_flag", "n_rows"], ascending=[True, True, False, False])
        .groupby(["product", "retailer"], as_index=False)
        .head(1)
        .head(6)
    )
    parts = [
        f"{PRODUCT_LABELS.get(r.product, r.product)} in {r.retailer}: {r.brand_norm or 'unlabeled brand'} ({int(r.n_item_keys)} item keys, {int(r.n_dates)} days)"
        for r in top.itertuples()
    ]
    return "; ".join(parts) + "."


def top_literal_sentence(literal_summary: pd.DataFrame) -> str:
    if literal_summary.empty:
        return "No literal retail-type summary was generated."
    top = (
        literal_summary.groupby(["product", "product_literal"], as_index=False)["n_item_keys"]
        .sum()
        .sort_values("n_item_keys", ascending=False)
        .head(6)
    )
    parts = [
        f"{PRODUCT_LABELS.get(r.product, r.product)} -> {LITERAL_LABELS.get(r.product_literal, r.product_literal)} ({int(r.n_item_keys)} item keys)"
        for r in top.itertuples()
    ]
    return "; ".join(parts) + "."


def level_selection_sentence(level_selection: pd.DataFrame) -> str:
    if level_selection.empty:
        return "No retail-level candidate was selected."
    parts = [
        f"{r.product_label}: {r.candidate_label} (score {fmt_num(r.selection_score, 2)})"
        for r in level_selection.itertuples()
    ]
    return "; ".join(parts) + "."


def candidate_core_sentence(lp_summary: pd.DataFrame) -> str:
    if lp_summary.empty:
        return "Candidate downstream LP comparisons are not available."
    focus = lp_summary[
        lp_summary["link"].isin(
            [
                "ProZorro -> Retail",
                "ProZorro -> Retail+Consumer",
                "ProZorro -> Retail matched",
                "ProZorro -> Silpo",
                "ProZorro -> Novus",
                "ProZorro -> Retail optimal",
            ]
        )
        & lp_summary["horizon_days"].isin([7, 14])
    ].copy()
    if focus.empty:
        return "Candidate downstream LP comparisons are not available."
    top = focus.groupby("link", as_index=False)["core_share"].mean().sort_values("core_share", ascending=False).head(5)
    parts = [f"{r.link}: mean 7/14-day core share {fmt_pct(r.core_share)}" for r in top.itertuples()]
    return "; ".join(parts) + "."


def write_summary_documents(
    inventory: pd.DataFrame,
    source_frames: Dict[str, pd.DataFrame],
    coverage: pd.DataFrame,
    lp: pd.DataFrame,
    lp_summary: pd.DataFrame,
    margins: pd.DataFrame,
    margin_spreads: pd.DataFrame,
    discounts: pd.DataFrame,
    findings: pd.DataFrame,
) -> None:
    lp_linear = lp[lp["model"].eq("LP_linear")] if not lp.empty else pd.DataFrame()
    total_models = len(lp_linear)
    core_models = int(lp_linear["core_signal"].sum()) if not lp_linear.empty else 0
    core_share = core_models / total_models if total_models else np.nan
    n_products = coverage["product"].nunique() if not coverage.empty else 0
    margin_flags = int(margins.get("persistent_margin_flag", pd.Series(dtype=float)).fillna(0).sum()) if not margins.empty else 0
    asym_flags = int(margins.get("asymmetric_margin_flag", pd.Series(dtype=float)).fillna(0).sum()) if not margins.empty else 0
    discount_signals = int(discounts.get("discount_strategy_signal", pd.Series(dtype=float)).fillna(0).sum()) if not discounts.empty else 0
    match_audit = source_frames.get("retail_match_audit", pd.DataFrame())
    matched_keys = int(match_audit["match_status"].eq("matched_both_shops").sum()) if not match_audit.empty else 0
    silpo_only = int(match_audit["match_status"].eq("silpo_only").sum()) if not match_audit.empty else 0
    novus_only = int(match_audit["match_status"].eq("novus_only").sum()) if not match_audit.empty else 0

    lines = [
        "# Second-Stage Estimation Summary",
        "",
        "## Analytical Purpose",
        "This second-stage run keeps the thesis chain as FarmGateUA -> ProducerUA -> ProZorro -> Retail, but estimates it with a different empirical design from the earlier RW4 ARDL/ECM/NARDL/VECM workflow. The aim is to check whether the same economic story survives when the model is rebuilt as a daily product-panel local-projection exercise and a vertical spread/discount market-power proxy exercise.",
        "",
        "The model uses the active `full_uah.xlsx`, `farm_gate_daily.xlsx`, and `farm_gate_all_missing_filled_daily.xlsx` workbooks from the nested Charniuk dairy research project. Farm-gate variants remain explicit (`initial` and `filled`, each with `linear` and `pchip` reconstruction), while retail is separated into observed and baseline price paths to keep discount behavior visible.",
        "",
        "## Data Coverage",
        f"The cleaned second-stage panel covers {n_products} standardized product groups. The strongest retail coverage remains in Silpo, while Novus is useful mainly as a thinner cross-retailer robustness layer. ProZorro is treated as an institutional procurement layer and is locally interpolated only across short gaps to avoid inventing long contract windows.",
        "",
        f"The retail-preparation block now works at item level before product-level aggregation. Silpo and Novus rows are harmonized with normalized brand names, canonical item names, standardized dairy product types, fat percentage, and pack-size fields. This produced {matched_keys} unique harmonized item keys observed in both shops, against {silpo_only} Silpo-only keys and {novus_only} Novus-only keys. Effective price keeps the discount inside the price, while discount amount, discount-type dummies, and markdown depth remain as separate covariates.",
        "",
        "![Panel coverage](../figures/01_panel_coverage.png)",
        "",
        "![Cross-shop match status](../figures/06_cross_shop_match_status.png)",
        "",
        "## Model Design",
        "The first model block uses local projections. For each admissible product and chain link, the cumulative change in the downstream log price over horizons 0, 1, 3, 7, 14, and 21 days is regressed on the current upstream log shock with HAC inference. A parallel asymmetric version separates positive and negative upstream shocks. This is intentionally different from the thesis draft's ECM/NARDL core and therefore functions as a robustness redesign rather than a simple rerun.",
        "",
        "The second model block estimates vertical spread equations. The dependent variable is the change in the log spread between downstream and upstream stages; regressors include the lagged spread, positive and negative upstream shocks, and retail discount measures where they vary. This is a market-power proxy, not a direct structural proof of conduct: persistent or asymmetric spreads and discount-responsive retail margins are interpreted as evidence consistent with timing control and category management.",
        "",
        "A new consumer-linked endpoint is also added. `Retail+Consumer` combines the harmonized merged-shop retail layer with ConsumerUA, so the rerun can test whether conclusions survive once the retailer-facing endpoint is blended with the official consumer-price environment instead of using retail-only prices alone.",
        "",
        "## Main Local-Projection Results",
        f"The local-projection block estimated {total_models} linear pass-through equations, of which {core_models} met the p<0.10 and overlap screen ({fmt_pct(core_share)}). The strongest thesis-relevant 7/14-day signals, excluding the mechanically smooth reconstructed FarmGateUA-ProducerUA diagnostic, are: {top_lp_sentence(lp_summary)}",
        "",
        "The FarmGateUA -> ProducerUA and ProducerUA -> FarmGateUA local-projection rows are retained in the workbook, but they should not be promoted as headline causal evidence. Both sides are reconstructed over a long common daily horizon, so high fit can reflect shared smoothing and benchmark coherence rather than a clean product-level farm-to-processor response. This is consistent with the corrected-format draft's conservative farm-gate interpretation.",
        "",
        "![Local-projection pass-through](../figures/02_lp_pass_through_horizons.png)",
        "",
        "![Forward versus reverse evidence](../figures/03_forward_reverse_core_share.png)",
        "",
        "## Market-Power And Discount Results",
        f"The spread model produced {len(margins)} usable margin equations. Persistent-margin flags appear in {margin_flags} rows and asymmetric-margin flags appear in {asym_flags} rows. These flags should be read as market-power proxies: they indicate where spreads do not quickly mean-revert or where upstream increases and decreases affect margins differently.",
        "",
        f"The discount model produced {len(discounts)} usable product equations, with {discount_signals} discount-strategy signals. In this data structure, the discount result is strongest as a retail-pricing mechanism rather than as a farm-gate mechanism: discount variables are directly observed only for Silpo, while ProducerUA, ProZorro, and FarmGateUA do not contain comparable markdown variables.",
        "",
        "![Vertical spread proxy](../figures/04_vertical_spread_proxy.png)",
        "",
        "![Discount incidence](../figures/05_discount_incidence.png)",
        "",
        "## Thesis Interpretation",
        "The second-stage run supports a cautious but coherent interpretation. Vertical coordination remains visible, but it is not a single cost-plus coefficient. The local-projection redesign shows that short-horizon evidence is selective and product-dependent, while the spread regressions show where timing control, discount smoothing, and asymmetric margin behavior are plausible. This strengthens the thesis argument that downstream market power is better described as control over timing, visibility, and discount-mediated adjustment than as one static markup wedge.",
        "",
        "Farm-gate results should still be written conservatively. The farm-gate benchmark is economically necessary as the raw-milk origin of the chain, but it is much smoother and less product-specific than the retail and procurement data. The second-stage results therefore use FarmGateUA as an upstream benchmark and robustness dimension, not as a literal product-level farm-to-shelf elasticity for every dairy category.",
        "",
        "## Output Files",
        "- `outputs/second_stage_model_outputs.xlsx` contains all model tables.",
        "- `data/second_stage_daily_panel.csv` contains the cleaned daily panel used by the models.",
        "- `data/retail_items_full_harmonized.csv` contains the full harmonized Silpo-Novus item list.",
        "- `data/retail_match_audit.csv` contains the cross-shop item-match audit.",
        "- `data/consumerua_clean_daily.csv` contains the cleaned ConsumerUA daily layer used in the consumer-linked rerun.",
        "- `outputs/local_projection_coefficients.csv`, `outputs/margin_market_power_models.csv`, and `outputs/discount_strategy_models.csv` contain the main machine-readable estimates.",
    ]
    (DOC_DIR / "second_stage_estimation_summary.md").write_text("\n".join(lines), encoding="utf-8")
    write_html(DOC_DIR / "second_stage_estimation_summary.html", "Second-Stage Estimation Summary", lines)
    write_simple_docx(DOC_DIR / "second_stage_estimation_summary.docx", lines, force_bold=False)

    correction_lines = [
        "# **Bold Corrections And Additions For The Corrected-Format Draft**",
        "",
        "**Target file reviewed: `Charniuk_Maksym_MScThesis_Draft_correctedformat.docx`. These notes are intentionally separate from the main draft, as requested.**",
        "",
        "- **Correct the farm-gate share statement: the 4.8% core-finding share belongs to FarmGateUA -> ProZorro, not FarmGateUA -> ProducerUA. FarmGateUA -> ProducerUA has 8 core findings out of 709 rows, about 1.1%, so it should be described as the weakest direct farm-gate link.**",
        "- **Use `institutional procurement layer` for ProZorro instead of saying it can simply be interpreted as processors. ProducerUA is the processor-level domestic producer-price layer; ProZorro is a procurement-contract layer.**",
        "- **Keep EU, CME, and ConsumerUA outside the endogenous domestic chain. They should be described as external benchmarks, reconstruction anchors, diagnostics, or robustness checks, not as extra structural stages.**",
        "- **State explicitly that the farm-gate raw-milk benchmark is not a processed-product price. It is an upstream raw-milk anchor, so direct FarmGateUA-to-retail coefficients must be interpreted conservatively.**",
        "- **Write reverse-flow findings as price-leadership or coordination evidence, not as proof of literal reverse causality. Retail -> ProZorro and Retail -> FarmGateUA coefficients show that downstream price setting contains information reflected upstream, but they do not by themselves prove causal control.**",
        "- **For Silpo, keep the distinction between observed price and baseline price. Observed price is the effective shelf price after markdown; baseline price is the regular-price proxy. For Novus, do not infer a promotion baseline because the workbook has no comparable discount signal.**",
        "- **Correct the ConsumerUA caption in the methodology/data text where it says `Ukrainian producer prices by products`; it should say `Ukrainian consumer prices by products`.**",
        "- **Correct `U.S. CME III stock prices distribution` to `U.S. CME Class III milk futures price distribution`.**",
        "- **Correct visible typos in the figure list and prose: `balalnce` -> `balance`, `Ukraine(gross` -> `Ukraine (gross`, `frequenct` -> `frequency`, `bee hind` / `bee hind` style fragments -> `behind`, `presenet` -> `present`, and `standartisation` -> `standardization` or `standardisation` consistently.**",
        "- **The Casey thesis/reference was not found by filename or searchable DOCX text in this folder. I therefore aligned the separate documents to the available KSE thesis style and the latest corrected-format draft. If the Casey thesis exists under another filename or only as a scanned PDF, add/identify it before final formatting imitation.**",
        "- **Do not headline the second-stage FarmGateUA -> ProducerUA local-projection coefficient even when it is statistically strong. Both sides are reconstructed/smoothed over a long horizon, so this block should be treated as reconstruction coherence rather than direct causal farm-to-processor evidence.**",
        "- **Add the second-stage robustness sentence after the RW4 estimation discussion: `As a robustness redesign, the second-stage local-projection and spread-proxy models keep the same four-stage chain but avoid relying on the same ARDL/ECM/NARDL/VECM identification stack; the resulting evidence remains selective and product-specific, which supports a conservative interpretation of market power as timing and discount-mediated coordination rather than a single universal markup.`**",
    ]
    (DOC_DIR / "corrected_format_additions_bold.md").write_text("\n".join(correction_lines), encoding="utf-8")
    write_html(DOC_DIR / "corrected_format_additions_bold.html", "Bold Corrections And Additions", correction_lines)
    write_simple_docx(DOC_DIR / "corrected_format_additions_bold.docx", correction_lines, force_bold=True)


def write_thesis_style_chapters(
    inventory: pd.DataFrame,
    source_frames: Dict[str, pd.DataFrame],
    coverage: pd.DataFrame,
    lp: pd.DataFrame,
    lp_summary: pd.DataFrame,
    margins: pd.DataFrame,
    margin_spreads: pd.DataFrame,
    discounts: pd.DataFrame,
    findings: pd.DataFrame,
) -> None:
    retail_items = source_frames.get("retail_items_full", pd.DataFrame())
    match_audit = source_frames.get("retail_match_audit", pd.DataFrame())
    literal_summary = source_frames.get("retail_literal_summary", pd.DataFrame())
    brand_support = source_frames.get("retail_brand_support", pd.DataFrame())
    level_selection = source_frames.get("retail_level_selection", pd.DataFrame())
    level_scores = source_frames.get("retail_level_scores", pd.DataFrame())
    reconciliation = source_frames.get("retail_name_reconciliation", pd.DataFrame())

    matched_keys = int(match_audit["match_status"].eq("matched_both_shops").sum()) if not match_audit.empty else 0
    silpo_only = int(match_audit["match_status"].eq("silpo_only").sum()) if not match_audit.empty else 0
    novus_only = int(match_audit["match_status"].eq("novus_only").sum()) if not match_audit.empty else 0
    strict_matches = int(match_audit.get("strict_alignment_flag", pd.Series(dtype=float)).fillna(0).sum()) if not match_audit.empty else 0
    n_literal = int(retail_items["product_literal"].nunique()) if not retail_items.empty else 0
    n_brands = int(retail_items["brand_norm"].nunique()) if not retail_items.empty else 0
    n_products = int(coverage["product"].nunique()) if not coverage.empty else 0
    total_models = int(lp[lp["model"].eq("LP_linear")].shape[0]) if not lp.empty else 0
    core_models = int(lp[(lp["model"].eq("LP_linear")) & (lp["core_signal"].eq(1))].shape[0]) if not lp.empty else 0
    margin_flags = int(margins.get("persistent_margin_flag", pd.Series(dtype=float)).fillna(0).sum()) if not margins.empty else 0
    asym_flags = int(margins.get("asymmetric_margin_flag", pd.Series(dtype=float)).fillna(0).sum()) if not margins.empty else 0
    discount_signals = int(discounts.get("discount_strategy_signal", pd.Series(dtype=float)).fillna(0).sum()) if not discounts.empty else 0

    data_lines = [
        "# Chapter 5. Second-stage data and retail harmonisation",
        "",
        "This chapter documents the second-stage data architecture used to complement the corrected master-thesis draft. The logic is intentionally close to the main thesis: each source is still treated as an institutional pricing layer, but the downstream retail block is rebuilt more deeply at item level so that Novus and Silpo contribute directly to the stage-4 model rather than only through broad category pooling.",
        "",
        "The practical goal of the redesign is not to overturn the master-thesis structure. It is to improve it where the original bottleneck was strongest: retailer product naming, brand reconciliation, literal dairy-product typing, and explicit discount-aware construction of the effective retail price.",
        "",
        "## 5.1 Data sources and analytical layers",
        "The second-stage chain still follows FarmGateUA -> ProducerUA -> ProZorro -> Retail. FarmGateUA remains the raw-milk benchmark, ProducerUA remains the processor-level domestic price layer, ProZorro remains the institutional procurement layer, and the retail block is rebuilt from harmonised Novus and Silpo product records. ConsumerUA is added as a downstream robustness environment, not as a replacement for the retailer-facing stage.",
        "",
        f"The cleaned second-stage panel covers {n_products} thesis product groups. The retail input after dairy-only reconciliation contains {len(retail_items)} product-day observations, {n_brands} normalised brand identifiers, and {n_literal} literal dairy-product types. This is materially deeper downstream preparation than the summary-level retail block in the earlier second-stage run.",
        "",
        "Figure 5.1. Second-stage panel coverage by product and source.",
        "![Figure 5.1. Second-stage panel coverage by product and source.](../figures/01_panel_coverage.png)",
        "Source: author's calculations based on the second-stage panel coverage table.",
        "",
        "## 5.1.1 Retail reconstruction from Novus and Silpo",
        "Retail preparation now begins at the item level. Each row keeps the effective observed shelf price, meaning the discount is already embedded in the price actually faced by the buyer. At the same time, the discount amount, discount state, discount type, and markdown depth are retained as separate variables so that retail adjustment can be studied both through the price itself and through the promotional mechanism behind it.",
        "",
        "Literal dairy typing is also made explicit. Instead of trusting the raw shop category alone, product titles, product names, brands, and auxiliary entity labels are cleaned jointly and mapped into literal dairy types such as milk, kefir, yogurt, hard cheese, cottage cheese, sour cream, cream, butter, condensed milk, and milk powder. Plant-based analogues and other non-comparable items are screened out before aggregation, which keeps the downstream series closer to the real dairy chain addressed in the thesis.",
        "",
        f"The reconciled literal mix is selective rather than generic: {top_literal_sentence(literal_summary)}",
        "",
        "Figure 5.2. Retail literal-product mix after dairy-only reconciliation.",
        "![Figure 5.2. Retail literal-product mix after dairy-only reconciliation.](../figures/07_retail_literal_mix.png)",
        "Source: author's calculations based on the harmonised retail literal summary.",
        "",
        "## 5.1.2 Cross-shop name reconciliation and brand harmonisation",
        "The core reconciliation object is the harmonised item key. It combines the thesis product group, the cleaned brand, and a canonicalised item name stripped of redundant pack and percentage tokens. This step is necessary because Novus and Silpo often refer to the same item with slightly different wording, word order, or packaging notation.",
        "",
        f"The resulting audit identifies {matched_keys} matched cross-shop item keys, {silpo_only} Silpo-only keys, and {novus_only} Novus-only keys. Among the matched keys, {strict_matches} cases also align one-for-one on the stricter fat-and-pack diagnostic key. This is exactly the kind of retailer-name adaptation that was missing from the broad category view.",
        "",
        "Figure 5.3. Cross-shop retail item harmonisation status.",
        "![Figure 5.3. Cross-shop retail item harmonisation status.](../figures/06_cross_shop_match_status.png)",
        "Source: author's calculations based on the retail match audit.",
        "",
        f"Brand support remains economically meaningful after reconciliation: {top_brand_sentence(brand_support)}",
        "",
        "Figure 5.4. Dominant retailer-brand support by dairy product.",
        "![Figure 5.4. Dominant retailer-brand support by dairy product.](../figures/08_dominant_brand_support.png)",
        "Source: author's calculations based on the reconciled retail brand-support table.",
        "",
        "## 5.2 Downstream levels tested for the four-stage model",
        "The retail endpoint is not forced into one representation. Instead, the second-stage pipeline constructs and keeps several candidate downstream levels: merged full-list retail, matched cross-shop retail, Silpo-only retail, Novus-only retail, and a retail-plus-ConsumerUA endpoint. Each level is useful for a different reason. The merged series maximises assortment support, the matched series maximises cross-shop comparability, Silpo and Novus preserve retailer-specific pricing behaviour, and the ConsumerUA-linked variant extends the downstream environment when retailer support is thin.",
        "",
        "Candidate levels are compared product by product using a composite score that combines coverage, procurement alignment, consumer alignment, item-support depth, and discount variation. This complements the master-thesis draft because it keeps the same four-stage chain but tests whether stage 4 is better represented by a broader retail pool, a stricter matched subset, a retailer-specific panel, or a consumer-linked endpoint.",
        "",
        f"The selected level by product is as follows: {level_selection_sentence(level_selection)}",
        "",
        "Figure 5.5. Candidate downstream retail scores by product.",
        "![Figure 5.5. Candidate downstream retail scores by product.](../figures/09_retail_level_scores.png)",
        "Source: author's calculations based on the retail-level selection table.",
        "",
        "Figure 5.6. Chosen optimal retail level by product.",
        "![Figure 5.6. Chosen optimal retail level by product.](../figures/10_optimal_retail_level.png)",
        "Source: author's calculations based on the selected retail-level hierarchy.",
        "",
        "## 5.3 Discount-aware downstream environment",
        "Discount variables remain central because the user requested that the final effective price should include the markdown while the markdown mechanism itself remains modelled separately. This design matches the master-thesis interpretation more closely than a raw regular-price series would. It treats retail adjustment as a combination of baseline repricing and promotional smoothing, not as one undifferentiated observed price path.",
        "",
        "Figure 5.7. Retail discount environment by product and retailer.",
        "![Figure 5.7. Retail discount environment by product and retailer.](../figures/12_discount_environment.png)",
        "Source: author's calculations based on retailer-product discount states in the harmonised retail panel.",
        "",
        "## 5.4 What remains after second-stage preparation",
        "After reconciliation, the downstream data are no longer a loose category average. They are a hierarchy of comparable retail series supported by explicit item keys, literal product types, brand structure, and discount metadata. That makes the second-stage outputs much easier to defend as a robustness complement to the corrected thesis draft: the master thesis keeps the broader structural story, while this second-stage data chapter shows that the downstream block has been rebuilt in a more disciplined way.",
        "",
        "The most important dataset files produced by this chapter are `data/retail_items_full_harmonized.csv`, `data/retail_brand_daily.csv`, `data/retail_literal_summary.csv`, `data/retail_level_selection.csv`, and `data/retail_optimal_daily.csv`. Together they document exactly how the stage-4 retail block was built before the models were rerun.",
    ]

    estimation_lines = [
        "# Chapter 6. Second-stage estimation results",
        "",
        "The second-stage estimation chapter is designed to complement the corrected master-thesis draft rather than duplicate it. The draft already uses the richer RW4 ARDL/ECM/NARDL/VECM stack as the main structural evidence. This chapter therefore asks a narrower but important question: if the retail stage is rebuilt more carefully from Novus and Silpo item-level data, do the main economic conclusions survive under a different modelling design?",
        "",
        "The answer is broadly yes, but the evidence remains selective and product-dependent. That is precisely why the second-stage methods are useful: they stress-test the thesis argument without pretending to replace the draft's main identification logic.",
        "",
        "## 6.1 Model families and their role",
        "The first model family uses local projections. It estimates cumulative downstream responses over 0, 1, 3, 7, 14, and 21 days with HAC inference. This complements the main draft because it avoids forcing each link into one equilibrium-correction structure and instead asks where timing evidence is stable across horizons.",
        "",
        "The second model family uses vertical spread equations. These are not direct market-power proofs, but they are useful proxies for timing control, asymmetric margin adjustment, and discount-mediated smoothing. The third block keeps a focused discount model in which retail discount incidence is related to lagged discount states and upstream price variation.",
        "",
        f"In total, the second-stage local-projection block estimates {total_models} linear models, of which {core_models} pass the p<0.10 and overlap screen. The leading 7/14-day thesis-relevant signals are: {top_lp_sentence(lp_summary)}",
        "",
        "Figure 6.1. Local-projection pass-through by horizon.",
        "![Figure 6.1. Local-projection pass-through by horizon.](../figures/02_lp_pass_through_horizons.png)",
        "Source: author's calculations based on the second-stage local-projection summary.",
        "",
        "Figure 6.2. Forward versus reverse second-stage evidence.",
        "![Figure 6.2. Forward versus reverse second-stage evidence.](../figures/03_forward_reverse_core_share.png)",
        "Source: author's calculations based on the second-stage local-projection summary.",
        "",
        "## 6.2 Procurement to retail under alternative downstream levels",
        "A key improvement relative to the earlier second-stage run is that procurement-to-retail evidence is not evaluated only on one pooled retail line. The pipeline now tests merged retail, matched retail, retailer-specific series, the ConsumerUA-linked series, and the selected optimal series. This directly addresses the concern that stage-4 measurement can change the interpretation of market power.",
        "",
        f"The candidate comparison shows the following ranking of downstream LP evidence: {candidate_core_sentence(lp_summary)}",
        "",
        "Figure 6.3. Candidate downstream levels in procurement-to-retail local-projection tests.",
        "![Figure 6.3. Candidate downstream levels in procurement-to-retail local-projection tests.](../figures/11_candidate_downstream_core_share.png)",
        "Source: author's calculations based on 7/14-day LP core shares across retail candidates.",
        "",
        "This comparison is economically useful because it separates three ideas that are often conflated. First, more coverage is not always better if it comes from a weaker retailer-grounded series. Second, stricter matched-item support is cleaner but shorter. Third, the ConsumerUA-linked endpoint can help with continuity, but it should still be treated as a robustness extension rather than as the literal shelf-price stage. That logic mirrors the corrected master-thesis draft rather than competing with it.",
        "",
        "## 6.3 Vertical spreads, market power, and discount effects",
        f"The spread block produces {len(margins)} usable equations. Persistent-margin flags appear in {margin_flags} rows and asymmetric-margin flags appear in {asym_flags} rows. This does not prove structural market power on its own, but it is consistent with downstream timing control, selective margin adjustment, and retailer category management.",
        "",
        "Figure 6.4. Vertical spread and market-power proxy by chain segment.",
        "![Figure 6.4. Vertical spread and market-power proxy by chain segment.](../figures/04_vertical_spread_proxy.png)",
        "Source: author's calculations based on the vertical spread summary.",
        "",
        f"The discount block remains more cautious than the main RW4 draft: it yields {len(discounts)} usable equations and {discount_signals} formal discount-strategy signals. That weaker statistical result does not mean discounts are unimportant. Instead, it suggests that in this reduced-form second-stage design the discount mechanism is most visible as part of the retail data-generating process rather than as a stand-alone structural driver.",
        "",
        "Figure 6.5. Retail discount incidence by product.",
        "![Figure 6.5. Retail discount incidence by product.](../figures/05_discount_incidence.png)",
        "Source: author's calculations based on the second-stage discount model table.",
        "",
        "## 6.4 Interpretation relative to the corrected thesis draft",
        "The second-stage results support the same broad market interpretation as the master-thesis draft, but through a different route. Procurement still behaves like an institutional buffer rather than a frictionless conduit. Retail still behaves like a managed adjustment layer. The main economic story still points toward product-specific vertical coordination rather than toward one universal pass-through elasticity.",
        "",
        "What changes is the emphasis. The second-stage redesign gives more weight to the downstream data-generating process itself: how item names are reconciled, how brand structure survives aggregation, how discount states are retained inside and outside price, and how the choice of retail endpoint changes the strength of the stage-4 model. That is exactly why this chapter complements the corrected draft: it improves the credibility of the retail stage without forcing the whole thesis to depend on one extra modelling family.",
        "",
        "Farm-gate results should remain conservative here as well. The second-stage run still shows that direct FarmGateUA -> ProducerUA evidence can look mechanically strong because both sides are reconstructed and smooth. The more defensible interpretation remains the same as in the corrected draft: FarmGateUA is an upstream benchmark and robustness dimension, not a literal product-level farm-to-shelf elasticity generator.",
        "",
        "## 6.5 Conclusion and practical implication",
        "The strongest contribution of the second-stage chapter is methodological. It shows that once the retail block is rebuilt at item level, filtered to literal dairy products, reconciled across Novus and Silpo, and tested across multiple downstream levels, the core thesis still holds. The retail stage does not behave like a passive residual of upstream costs. It behaves like a strategic adjustment layer in which timing, discount use, brand structure, and category management matter for observed price transmission.",
        "",
        "This strengthens the corrected master-thesis draft rather than displacing it. The draft can continue to rely on the richer ECM/NARDL evidence as the main structural story, while the second-stage chapter demonstrates that the downstream interpretation survives deeper retail cleaning and a different empirical design.",
    ]

    combined_lines = data_lines + ["", ""] + estimation_lines

    outputs = [
        ("second_stage_data_chapter", "Second-stage data chapter", data_lines),
        ("second_stage_estimation_chapter", "Second-stage estimation chapter", estimation_lines),
        ("second_stage_data_estiamtion_updated_conclusion", "Second-stage data and estimation updated conclusion", combined_lines),
    ]
    for stem, title, lines in outputs:
        (DOC_DIR / f"{stem}.md").write_text("\n".join(lines), encoding="utf-8")
        write_html(DOC_DIR / f"{stem}.html", title, lines)
        write_simple_docx(DOC_DIR / f"{stem}.docx", lines, force_bold=False)


def write_html(path: Path, title: str, md_lines: Sequence[str]) -> None:
    body = []
    for line in md_lines:
        if line.startswith("# "):
            body.append(f"<h1>{markdown_inline(line[2:])}</h1>")
        elif line.startswith("## "):
            body.append(f"<h2>{markdown_inline(line[3:])}</h2>")
        elif line.startswith("- "):
            body.append(f"<p>&bull; {markdown_inline(line[2:])}</p>")
        elif line.startswith("![") and "](" in line:
            alt = line[2 : line.find("]")]
            src = line[line.find("(") + 1 : line.rfind(")")]
            body.append(f'<figure><img src="{html.escape(src)}" alt="{html.escape(alt)}" style="max-width: 900px;"><figcaption>{html.escape(alt)}</figcaption></figure>')
        elif not line.strip():
            body.append("")
        else:
            body.append(f"<p>{markdown_inline(line)}</p>")
    html_doc = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 980px; margin: 32px auto; line-height: 1.45; }}
    h1, h2 {{ font-family: Arial, sans-serif; }}
    img {{ border: 1px solid #ddd; padding: 4px; }}
    code {{ background: #f6f6f6; padding: 1px 3px; }}
  </style>
</head>
<body>
{chr(10).join(body)}
</body>
</html>
"""
    path.write_text(html_doc, encoding="utf-8")


def markdown_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def clean_md_text(line: str) -> Tuple[str, str]:
    stripped = line.strip()
    style = "normal"
    if stripped.startswith("# "):
        style = "title"
        stripped = stripped[2:].strip()
    elif stripped.startswith("## "):
        style = "heading"
        stripped = stripped[3:].strip()
    elif stripped.startswith("- "):
        style = "bullet"
        stripped = stripped[2:].strip()
    elif stripped.startswith("![") and "](" in stripped:
        alt = stripped[2 : stripped.find("]")]
        src = stripped[stripped.find("(") + 1 : stripped.rfind(")")]
        stripped = f"Figure: {alt} ({src})"
        style = "figure"
    stripped = stripped.replace("**", "").replace("`", "")
    return stripped, style


def docx_run(text: str, bold: bool = False, size: Optional[int] = None) -> str:
    props = []
    if bold:
        props.append("<w:b/>")
    if size:
        props.append(f'<w:sz w:val="{size}"/>')
    rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{html.escape(text)}</w:t></w:r>'


def docx_paragraph(text: str, style: str = "normal", force_bold: bool = False) -> str:
    if not text.strip():
        return "<w:p/>"
    bold = force_bold or style in {"title", "heading"}
    size = 32 if style == "title" else 26 if style == "heading" else None
    prefix = "• " if style == "bullet" else ""
    return f"<w:p>{docx_run(prefix + text, bold=bold, size=size)}</w:p>"


def write_simple_docx(path: Path, md_lines: Sequence[str], force_bold: bool = False) -> None:
    paragraphs = []
    for line in md_lines:
        text, style = clean_md_text(line)
        paragraphs.append(docx_paragraph(text, style=style, force_bold=force_bold))
    document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {''.join(paragraphs)}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
'''
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
'''
    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
'''
    with ZipFile(path, "w", compression=ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", rels)
        zf.writestr("word/document.xml", document_xml)


def write_readme() -> None:
    readme = [
        "# Analysis Second Stage",
        "",
        "This folder contains a non-destructive second-stage robustness redesign for the master thesis dairy price-transmission analysis.",
        "",
        "## Main Files",
        "- `run_second_stage_analysis.py`: reproducible runner for the second-stage daily panel, local-projection models, margin/market-power proxy models, discount models, figures, and documents.",
        "- `outputs/second_stage_model_outputs.xlsx`: consolidated workbook of model outputs.",
        "- `data/second_stage_daily_panel.csv`: cleaned model panel.",
        "- `documents/second_stage_estimation_summary.md`: thesis-style estimation summary with figure references.",
        "- `documents/second_stage_data_estiamtion_updated_conclusion.docx`: thesis-style second-stage chapter document aligned to the main draft structure.",
        "- `documents/corrected_format_additions_bold.md`: separate bolded correction/addition notes for the corrected-format draft.",
        "",
        "## Method Note",
        "The second-stage design intentionally differs from RW4. It uses local projections and spread/discount proxy equations instead of repeating the same ARDL, ECM, NARDL, and VECM model ladder.",
        "",
        "The current version also adds deeper retail preparation: harmonized Silpo-Novus item keys, dairy-only literal product typing, brand/item reconciliation outputs, tested downstream retail levels, an optimal retail endpoint, and a ConsumerUA-linked retail endpoint.",
    ]
    (STAGE_DIR / "README.md").write_text("\n".join(readme), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    if not FULL_UAH.exists():
        raise FileNotFoundError(FULL_UAH)
    for path in FARM_GATE_FILES.values():
        if not path.exists():
            raise FileNotFoundError(path)

    panel, inventory, source_frames = build_panel()
    coverage = coverage_table(panel)
    lp = run_local_projections(panel)
    lp_summary = summarize_lp(lp)
    margins, margin_spreads = run_margin_models(panel)
    discounts = run_discount_models(panel)
    findings = robust_findings(lp, margins, discounts)

    write_excel_outputs(panel, inventory, source_frames, coverage, lp, lp_summary, margins, margin_spreads, discounts, findings)
    plot_outputs(panel, coverage, lp_summary, margin_spreads, discounts, source_frames)
    write_summary_documents(inventory, source_frames, coverage, lp, lp_summary, margins, margin_spreads, discounts, findings)
    write_thesis_style_chapters(inventory, source_frames, coverage, lp, lp_summary, margins, margin_spreads, discounts, findings)
    write_readme()

    print("Second-stage analysis completed.")
    print(f"Output workbook: {OUTPUT_DIR / 'second_stage_model_outputs.xlsx'}")
    print(f"Summary document: {DOC_DIR / 'second_stage_estimation_summary.md'}")
    print(f"Bold corrections: {DOC_DIR / 'corrected_format_additions_bold.md'}")


if __name__ == "__main__":
    main()
