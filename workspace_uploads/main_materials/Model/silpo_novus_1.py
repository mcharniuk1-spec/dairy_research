import re
import time
import uuid
from pathlib import Path
from collections import Counter
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd
from pandas import DatetimeTZDtype

INPUT_PATH = "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Data/novus_silpo.xlsx"
PROZORRO_PATH = "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Data/for model/ProZorro_only.xlsx"
OUTPUT_PATH = "processed_full.xlsx"

STANDARD_COLUMNS = [
    "timestamp",
    "date",
    "product_title",
    "product_name",
    "brand",
    "entity",
    "broader_category",
    "профіль",
    "fat_pct",
    "pack_qty_final",
    "pack_unit_final",
    "qty_std",
    "unit_std",
    "price_current",
    "unit_price",
    "discount_value",
]

ENTITY_RULES = [
    ("cream_cheese", [r"\bкрем[-\s]?сир\b", r"\bcream\s*cheese\b"]),
    ("cottage_cheese", [r"\bсир\s+кисломолоч", r"\bтворог\b", r"\bтворожн"]),
    ("hard_cheese", [r"\bсир\b", r"\bпармезан\b", r"\bмоцарел", r"\bчеддер\b", r"\bгауда\b"]),
    ("sour_cream", [r"\bсметан", r"\bsour\s*cream\b"]),
    ("ryazhanka", [r"\bряжанк"]),
    ("kefir", [r"\bкефір\b", r"\bкефир\b", r"\bkefir\b"]),
    ("yogurt", [r"\bйогурт\b", r"\bйогур\b", r"\bбіфідойогурт\b", r"\bбіфойогурт\b", r"\byogurt\b"]),
    ("milk", [r"\bмолоко\b", r"\bmilk\b"]),
    ("butter", [r"\bмасло\b", r"\bвершкове\s+масло\b", r"\bbutter\b"]),
    ("dessert", [r"\bдесерт\b", r"\bпудинг\b", r"\bмус\b", r"\bглазурований\b", r"\bсирок\b"]),
    ("eggs", [r"\bяйц", r"\bяєц", r"\beggs?\b", r"\b[0-9]{1,2}\s*шт\b"]),
]

CATEGORY_BY_ENTITY = {
    "milk": "fresh_dairy",
    "yogurt": "fermented_dairy",
    "sour_cream": "fermented_dairy",
    "cottage_cheese": "fermented_dairy",
    "hard_cheese": "cheese",
    "cream_cheese": "cheese",
    "butter": "butter_fats",
    "kefir": "fermented_dairy",
    "ryazhanka": "fermented_dairy",
    "dessert": "dessert_dairy",
    "eggs": "eggs",
}

PACK_RE = re.compile(r"(?<!\d)(\d+(?:[\.,]\d+)?)\s*(кг|kg|г|гр|g|л|l|мл|ml|шт|pcs|pc|уп|упак)\b", re.IGNORECASE)
FAT_RE = re.compile(r"(\d+(?:[\.,]\d+)?)\s*%")

BRAND_STOPWORDS = {
    "на",
    "без",
    "з",
    "зі",
    "та",
    "для",
    "до",
    "від",
    "у",
    "в",
    "під",
    "із",
    "i",
}

LEADING_PRODUCT_WORDS = {
    "молоко",
    "йогурт",
    "біфідойогурт",
    "кефір",
    "кефир",
    "сметана",
    "сир",
    "сирок",
    "масло",
    "ряжанка",
    "десерт",
    "яйця",
    "яйце",
    "напій",
    "шейк",
    "коктейль",
    "вершки",
    "паста",
}

PROFILE_LABELS = (
    "Яйця курячі",
    "Масло вершкове",
    "Молоко питне",
    "Вершки",
    "Сир твердий/напівтвердий",
    "Сир кисломолочний",
    "Сметана",
    "Молоко згущене",
    "Молоко сухе",
)
PROFILE_LABEL_SET = set(PROFILE_LABELS)

UA_UNIT_TO_STD = {
    "кілограм": "kg",
    "кілограми": "kg",
    "кілограмів": "kg",
    "кг": "kg",
    "кг.": "kg",
    "літр": "l",
    "літри": "l",
    "літрів": "l",
    "л": "l",
    "л.": "l",
    "штука": "pcs",
    "штуки": "pcs",
    "штук": "pcs",
    "шт": "pcs",
    "шт.": "pcs",
}

GENERIC_PRODUCT_TOKENS = {
    "продукт",
    "товар",
    "дсту",
    "фасоване",
    "фасований",
    "ваговий",
    "вагове",
    "вагові",
    "натуральний",
    "натуральне",
    "натуральна",
}

PROFILE_KEYWORDS = {
    "Яйця курячі": {"яйце", "яйця", "яєч", "куряч", "десяток"},
    "Масло вершкове": {"масло", "вершков", "селянське", "екстра", "бутерброд"},
    "Молоко питне": {"молоко", "питне", "коров", "ультрапастер", "пастер"},
    "Вершки": {"вершки", "кулінарн", "для збивання", "стерил"},
    "Сир твердий/напівтвердий": {"сир", "тверд", "напівтверд", "гауда", "моцарел", "чеддер", "пармезан"},
    "Сир кисломолочний": {"сир", "кисломолоч", "творог", "творож", "зернист"},
    "Сметана": {"сметан"},
    "Молоко згущене": {"згущ", "згущен", "конденс"},
    "Молоко сухе": {"сух", "сухе", "порошок"},
}


def normalize_text(x: object) -> str:
    if pd.isna(x):
        return ""
    s = str(x).replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip()


def normalize_dummy_suffix(text: str) -> str:
    s = normalize_match_text(text)
    s = s.replace(" ", "_")
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "unknown"


def resolve_existing_path(primary_path: str, fallback_names: list[str]) -> Path:
    p = Path(primary_path)
    if p.exists():
        return p

    search_roots = [
        Path.cwd(),
        Path.cwd().parent,
        Path.home() / "Documents" / "KSE",
    ]
    for root in search_roots:
        if not root.exists():
            continue
        for name in fallback_names:
            found = list(root.rglob(name))
            if found:
                return found[0]

    raise FileNotFoundError(f"File not found: {primary_path}")


def make_excel_safe(df: pd.DataFrame) -> pd.DataFrame:
    safe = df.copy()
    for col in safe.columns:
        if isinstance(safe[col].dtype, DatetimeTZDtype):
            safe[col] = safe[col].dt.tz_localize(None)
    return safe


def tokenize_clean(text: str) -> list[str]:
    return [tok.strip('"\',().;:!?«»[]{}').strip() for tok in normalize_text(text).split() if tok.strip('"\',().;:!?«»[]{}').strip()]


def normalize_brand_key(text: str) -> str:
    return " ".join(tok.lower() for tok in tokenize_clean(text))


def normalize_match_text(text: str) -> str:
    s = normalize_text(text).lower()
    s = s.replace("`", "'")
    s = re.sub(r"[^0-9a-zа-яіїєґ'\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def normalize_unit_ua(unit_value: object) -> Optional[str]:
    u = normalize_match_text(str(unit_value) if not pd.isna(unit_value) else "")
    if not u:
        return None
    if u in UA_UNIT_TO_STD:
        return UA_UNIT_TO_STD[u]
    # deterministic fallback for inflected forms
    if u.startswith("кг") or u.startswith("кілограм"):
        return "kg"
    if u.startswith("л") or u.startswith("літр"):
        return "l"
    if u.startswith("шт") or u.startswith("штук") or u.startswith("шту"):
        return "pcs"
    return None


def normalize_fat_key(value: Optional[float]) -> Optional[float]:
    if value is None or pd.isna(value):
        return None
    return round(float(value), 1)


def stem_uk_token(token: str) -> str:
    t = token.lower()
    t = re.sub(r"[^0-9a-zа-яіїєґ]", "", t)
    for suf in (
        "ями", "ами", "ові", "еві", "ого", "ому", "ими", "ій", "ий", "а", "я", "е", "и", "і", "у", "ю", "о"
    ):
        if len(t) > 4 and t.endswith(suf):
            t = t[: -len(suf)]
            break
    return t


def title_tokens_for_profile(text: str) -> set[str]:
    tokens = set()
    for tok in normalize_match_text(text).split():
        st = stem_uk_token(tok)
        if len(st) < 2:
            continue
        if st in GENERIC_PRODUCT_TOKENS:
            continue
        tokens.add(st)
    return tokens


def build_profile_model(prozorro_df: pd.DataFrame) -> Dict[str, Counter]:
    model: Dict[str, Counter] = {p: Counter() for p in PROFILE_LABELS}
    for _, row in prozorro_df.iterrows():
        profile = normalize_text(row.get("Профіль"))
        if profile not in PROFILE_LABEL_SET:
            continue
        product = normalize_text(row.get("Товар"))
        if not product:
            continue
        toks = title_tokens_for_profile(product)
        if not toks:
            continue
        model[profile].update(toks)
    return model


def to_float(x: object) -> Optional[float]:
    if pd.isna(x):
        return None
    s = normalize_text(x)
    if not s:
        return None
    s = s.replace(" ", "").replace(",", ".")
    s = re.sub(r"[^0-9.\-]", "", s)
    if s in {"", ".", "-", "-."}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def canonical_unit(unit_raw: Optional[str]) -> Optional[str]:
    if unit_raw is None:
        return None
    u = normalize_text(unit_raw).lower()
    if u in {"г", "гр", "g", "kg", "кг", "мл", "ml", "л", "l", "шт", "pcs", "pc", "уп", "упак"}:
        if u in {"г", "гр", "g", "kg", "кг"}:
            return "kg"
        if u in {"мл", "ml", "л", "l"}:
            return "l"
        if u in {"шт", "pcs", "pc", "уп", "упак"}:
            return "pcs"
    return None


def std_qty(value: Optional[float], unit_raw: Optional[str]) -> Tuple[Optional[float], Optional[str]]:
    if value is None or unit_raw is None:
        return None, None
    u = normalize_text(unit_raw).lower()
    if u in {"кг", "kg"}:
        return value, "kg"
    if u in {"г", "гр", "g"}:
        return value / 1000.0, "kg"
    if u in {"л", "l"}:
        return value, "l"
    if u in {"мл", "ml"}:
        return value / 1000.0, "l"
    if u in {"шт", "pcs", "pc", "уп", "упак"}:
        return value, "pcs"
    return None, None


def extract_fat_from_title(title: str) -> Optional[float]:
    m = FAT_RE.search(title.lower())
    if not m:
        return None
    return to_float(m.group(1))


def extract_pack_from_title(title: str) -> Tuple[Optional[float], Optional[str]]:
    m = PACK_RE.search(title.lower())
    if not m:
        return None, None
    qty = to_float(m.group(1))
    unit = m.group(2)
    return qty, unit


def build_brand_dictionary(silpo_df: pd.DataFrame, novus_df: pd.DataFrame) -> Dict[str, str]:
    brands: Dict[str, str] = {}

    if "brand" in silpo_df.columns:
        for b in silpo_df["brand"].dropna().astype(str):
            b_clean = normalize_text(b)
            if b_clean:
                brands[normalize_brand_key(b_clean)] = b_clean

    for title in pd.concat([silpo_df.get("product_title", pd.Series(dtype=str)), novus_df.get("product_title", pd.Series(dtype=str))], ignore_index=True):
        t = normalize_text(title)
        if not t:
            continue
        tokens = tokenize_clean(t)
        if len(tokens) < 2:
            continue
        candidate = tokens[1].strip()
        if re.search(r"\d", candidate):
            continue
        if FAT_RE.search(candidate):
            continue
        if candidate.lower() in BRAND_STOPWORDS:
            continue
        if candidate[0].isupper() or re.search(r"[A-Za-z]", candidate):
            brands.setdefault(normalize_brand_key(candidate), candidate)

    return brands


def infer_brand(title: str, explicit_brand: Optional[str], brand_dict: Dict[str, str]) -> Optional[str]:
    if explicit_brand and normalize_text(explicit_brand):
        return normalize_text(explicit_brand)

    t = normalize_text(title)
    if not t:
        return None

    tokens = tokenize_clean(t)
    if len(tokens) < 2:
        return None

    start_idx = 1 if tokens[0].lower() in LEADING_PRODUCT_WORDS else 0
    max_i = min(len(tokens), start_idx + 5)

    # Prefer longest dictionary phrase near the title start.
    for i in range(start_idx, max_i):
        for n in (3, 2, 1):
            if i + n > len(tokens):
                continue
            phrase = " ".join(tokens[i:i + n])
            key = normalize_brand_key(phrase)
            if key and key in brand_dict:
                return brand_dict[key]

    # Deterministic positional extraction from title start after entity token.
    for idx in range(start_idx, max_i):
        if idx >= len(tokens):
            break
        tok = tokens[idx]
        tok_low = tok.lower()
        if tok_low in BRAND_STOPWORDS:
            continue
        if re.search(r"\d", tok) or FAT_RE.search(tok) or PACK_RE.search(tok):
            continue
        if len(tok) <= 1:
            continue
        if tok and (tok[0].isupper() or re.search(r"[A-Za-z]", tok)):
            return tok

    return None


def classify_entity(title: str) -> Optional[str]:
    text = normalize_text(title).lower()
    if not text:
        return None

    # Explicit disambiguation priority is encoded by rule order.
    for entity, patterns in ENTITY_RULES:
        for pat in patterns:
            if re.search(pat, text):
                return entity
    return None


def assign_profile(
    product_title: str,
    profile_model: Dict[str, Counter],
) -> str:
    title = normalize_match_text(product_title)
    toks = title_tokens_for_profile(title)

    # Hard deterministic patterns with highest priority.
    if re.search(r"\b(?:яйц|яєц)\w*\b", title):
        return "Яйця курячі"
    if re.search(r"\bмолок\w*\s+згущ", title):
        return "Молоко згущене"
    if re.search(r"\bмолок\w*\s+сух", title):
        return "Молоко сухе"
    if re.search(r"\bсметан", title):
        return "Сметана"
    if re.search(r"\bсир\s+кисломолоч|\bтворог|\bтворож", title):
        return "Сир кисломолочний"
    if re.search(r"\bвершк", title):
        return "Вершки"
    if re.search(r"\bмасл", title) and not re.search(r"\bмаргарин|спред|рослинн", title):
        return "Масло вершкове"

    # Similarity scoring across only allowed labels.
    scores: Dict[str, float] = {}
    for profile in PROFILE_LABELS:
        score = 0.0

        # Keyword hits from curated profile dictionary.
        for kw in PROFILE_KEYWORDS[profile]:
            kw_parts = [stem_uk_token(x) for x in normalize_match_text(kw).split() if stem_uk_token(x)]
            if kw_parts and all(any(tok.startswith(part) for tok in toks) for part in kw_parts):
                score += 2.5

        # Overlap with ProZorro profile token model.
        model_tokens = set(profile_model.get(profile, Counter()).keys())
        if toks and model_tokens:
            overlap = len(toks & model_tokens) / len(toks)
            score += 3.0 * overlap

        # Frequency-weighted evidence from ProZorro terms.
        weighted = 0.0
        for tok in toks:
            weighted += min(profile_model.get(profile, Counter()).get(tok, 0), 5)
        score += 0.2 * weighted

        scores[profile] = score

    best = max(scores, key=scores.get)
    if scores[best] > 0:
        return best

    # Deterministic final fallback to allowed set.
    return "Молоко питне"


def make_product_name(title: str, brand: Optional[str]) -> str:
    t = normalize_text(title)
    if not t:
        return ""

    t = re.sub(FAT_RE, " ", t)
    t = re.sub(PACK_RE, " ", t)

    tokens = tokenize_clean(t)
    if not tokens:
        return ""

    if brand:
        b_tokens = tokenize_clean(brand)
        if len(tokens) >= len(b_tokens):
            for i in range(0, min(8, len(tokens) - len(b_tokens) + 1)):
                if [x.lower() for x in tokens[i:i + len(b_tokens)]] == [x.lower() for x in b_tokens]:
                    del tokens[i:i + len(b_tokens)]
                    break

    # remove isolated unit remnants and empty tokens
    cleaned = []
    for tok in tokens:
        low = tok.lower()
        if not tok:
            continue
        if low in {"г", "гр", "кг", "kg", "л", "l", "мл", "ml", "шт", "pcs", "pc", "уп", "упак"}:
            continue
        cleaned.append(tok)

    return " ".join(cleaned).strip()


def process_silpo(df: pd.DataFrame, brand_dict: Dict[str, str], profile_model: Dict[str, Counter]) -> pd.DataFrame:
    out = pd.DataFrame()
    out["product_title"] = df["product_title"].map(normalize_text)
    out["timestamp"] = pd.to_datetime(df["upload_ts"], errors="coerce", utc=True).dt.tz_localize(None)
    out["date"] = out["timestamp"].dt.date
    out["price_current"] = df["price_current"].map(to_float)

    out["brand"] = [infer_brand(t, b, brand_dict) for t, b in zip(out["product_title"], df.get("brand", pd.Series(index=df.index, dtype=object)))]
    out["fat_pct"] = df.get("fat_pct", pd.Series(index=df.index, dtype=object)).map(to_float)
    missing_fat = out["fat_pct"].isna()
    out.loc[missing_fat, "fat_pct"] = out.loc[missing_fat, "product_title"].map(extract_fat_from_title)

    qty_col = df.get("pack_qty", pd.Series(index=df.index, dtype=object)).map(to_float)
    unit_col = df.get("pack_unit", pd.Series(index=df.index, dtype=object)).map(normalize_text)

    title_pack = out["product_title"].map(extract_pack_from_title)
    title_qty = title_pack.map(lambda x: x[0])
    title_unit = title_pack.map(lambda x: x[1])

    out["pack_qty_final"] = qty_col.where(qty_col.notna(), title_qty)
    out["pack_unit_final"] = unit_col.where(unit_col.astype(str).str.len() > 0, title_unit)

    std_pairs = [std_qty(q, u) for q, u in zip(out["pack_qty_final"], out["pack_unit_final"])]
    out["qty_std"] = [x[0] for x in std_pairs]
    out["unit_std"] = [x[1] for x in std_pairs]

    out["entity"] = out["product_title"].map(classify_entity)
    out["broader_category"] = out["entity"].map(CATEGORY_BY_ENTITY)
    out["product_name"] = [make_product_name(t, b) for t, b in zip(out["product_title"], out["brand"])]
    out["профіль"] = out["product_title"].map(lambda t: assign_profile(t, profile_model))

    fallback_price = df.get("price_per_l_or_kg_or_piece", pd.Series(index=df.index, dtype=object)).map(to_float)
    out["unit_price"] = np.where(out["qty_std"].notna() & (out["qty_std"] > 0), out["price_current"] / out["qty_std"], fallback_price)
    out["discount_value"] = df.get("discount_pct", pd.Series(index=df.index, dtype=object)).map(to_float)

    # Fallback discount calculation when discount_pct is missing.
    price_old = df.get("price_old", pd.Series(index=df.index, dtype=object)).map(to_float)
    calc_discount = np.where(
        (price_old.notna()) & (price_old > 0) & (out["price_current"].notna()),
        (price_old - out["price_current"]) / price_old * 100.0,
        np.nan,
    )
    out["discount_value"] = out["discount_value"].where(out["discount_value"].notna(), calc_discount)

    # One deterministic dummy per Silpo discount type.
    raw_discount_type = df.get("price_type", pd.Series(index=df.index, dtype=object)).map(normalize_text)
    discount_types = sorted({x for x in raw_discount_type.dropna().tolist() if x})
    dummy_cols = []
    for dtype in discount_types:
        col = f"discount_dummy_{normalize_dummy_suffix(dtype)}"
        out[col] = (raw_discount_type == dtype).astype(int)
        dummy_cols.append(col)

    if isinstance(out["timestamp"].dtype, DatetimeTZDtype):
        out["timestamp"] = out["timestamp"].dt.tz_localize(None)

    out = out.sort_values("timestamp").drop_duplicates(subset=["date", "product_title"], keep="last")
    return out[STANDARD_COLUMNS + dummy_cols]


def process_novus(df: pd.DataFrame, brand_dict: Dict[str, str], profile_model: Dict[str, Counter]) -> pd.DataFrame:
    out = pd.DataFrame()
    out["product_title"] = df["title"].map(normalize_text)

    date_str = pd.to_datetime(df["date"], errors="coerce").dt.strftime("%Y-%m-%d")
    time_raw = df["time"].map(normalize_text)
    has_embedded_date = time_raw.str.contains(r"\d{4}-\d{2}-\d{2}", regex=True, na=False)
    time_as_ts = pd.to_datetime(time_raw.where(has_embedded_date), errors="coerce", utc=True, format="ISO8601")

    combined_str = date_str.fillna("") + " " + time_raw.fillna("")
    ts = pd.to_datetime(combined_str, errors="coerce", utc=True)
    ts = ts.where(~has_embedded_date, time_as_ts)
    ts = ts.dt.tz_localize(None)
    out["timestamp"] = ts
    if isinstance(out["timestamp"].dtype, DatetimeTZDtype):
        out["timestamp"] = out["timestamp"].dt.tz_localize(None)
    out["date"] = out["timestamp"].dt.date

    out["price_current"] = df["price"].map(to_float)
    out["brand"] = [infer_brand(t, None, brand_dict) for t in out["product_title"]]

    out["fat_pct"] = out["product_title"].map(extract_fat_from_title)

    title_pack = out["product_title"].map(extract_pack_from_title)
    out["pack_qty_final"] = title_pack.map(lambda x: x[0])
    out["pack_unit_final"] = title_pack.map(lambda x: x[1])

    std_pairs = [std_qty(q, u) for q, u in zip(out["pack_qty_final"], out["pack_unit_final"])]
    out["qty_std"] = [x[0] for x in std_pairs]
    out["unit_std"] = [x[1] for x in std_pairs]

    out["entity"] = out["product_title"].map(classify_entity)
    out["broader_category"] = out["entity"].map(CATEGORY_BY_ENTITY)
    out["product_name"] = [make_product_name(t, b) for t, b in zip(out["product_title"], out["brand"])]
    out["профіль"] = out["product_title"].map(lambda t: assign_profile(t, profile_model))

    out["unit_price"] = np.where(out["qty_std"].notna() & (out["qty_std"] > 0), out["price_current"] / out["qty_std"], np.nan)
    out["discount_value"] = np.nan

    # Keep schema aligned with Silpo output.
    silpo_discount_types = (
        pd.read_excel(resolve_existing_path(INPUT_PATH, ["novus_silpo.xlsx"]), sheet_name="silpo", usecols=["price_type"])["price_type"]
        .dropna()
        .astype(str)
        .map(normalize_text)
    )
    discount_types = sorted({x for x in silpo_discount_types.tolist() if x})
    dummy_cols = []
    for dtype in discount_types:
        col = f"discount_dummy_{normalize_dummy_suffix(dtype)}"
        out[col] = 0
        dummy_cols.append(col)

    out = out.sort_values("timestamp").drop_duplicates(subset=["date", "product_title"], keep="last")
    return out[STANDARD_COLUMNS + dummy_cols]


def main() -> None:
    input_file = resolve_existing_path(INPUT_PATH, ["novus_silpo.xlsx"])
    prozorro_file = resolve_existing_path(PROZORRO_PATH, ["ProZorro_only.xlsx"])

    silpo = pd.read_excel(input_file, sheet_name="silpo")
    novus = pd.read_excel(input_file, sheet_name="novus")
    prozorro = pd.read_excel(prozorro_file, sheet_name="ProZorro")

    brand_dict = build_brand_dictionary(silpo, novus.rename(columns={"title": "product_title"}))
    profile_model = build_profile_model(prozorro)

    silpo_clean = process_silpo(silpo, brand_dict, profile_model)
    novus_clean = process_novus(novus, brand_dict, profile_model)

    silpo_clean = make_excel_safe(silpo_clean)
    novus_clean = make_excel_safe(novus_clean)

    output_path = Path(OUTPUT_PATH)
    final_path = output_path
    write_ok = False
    last_exc: Optional[Exception] = None

    # Retry to handle transient file lock / cloud-sync write timeouts.
    for attempt in range(1, 6):
        temp_output = output_path.with_name(
            f"{output_path.stem}__tmp_{uuid.uuid4().hex}{output_path.suffix}"
        )
        try:
            with pd.ExcelWriter(temp_output, engine="openpyxl") as writer:
                silpo_clean.to_excel(writer, sheet_name="silpo_clean", index=False)
                novus_clean.to_excel(writer, sheet_name="novus_clean", index=False)
            temp_output.replace(output_path)
            write_ok = True
            final_path = output_path
            break
        except (TimeoutError, OSError) as exc:
            last_exc = exc
            try:
                if temp_output.exists():
                    temp_output.unlink()
            except OSError:
                pass
            time.sleep(min(2 * attempt, 8))

    if not write_ok:
        fallback = output_path.with_name(f"{output_path.stem}_new{output_path.suffix}")
        temp_output = fallback.with_name(f"{fallback.stem}__tmp_{uuid.uuid4().hex}{fallback.suffix}")
        with pd.ExcelWriter(temp_output, engine="openpyxl") as writer:
            silpo_clean.to_excel(writer, sheet_name="silpo_clean", index=False)
            novus_clean.to_excel(writer, sheet_name="novus_clean", index=False)
        temp_output.replace(fallback)
        final_path = fallback
        if last_exc:
            print(f"Warning: main output write failed ({last_exc}); saved to fallback file.")

    print(f"Processed file saved: {final_path}")
    print(f"Silpo rows: {len(silpo_clean)}")
    print(f"Novus rows: {len(novus_clean)}")


if __name__ == "__main__":
    main()
