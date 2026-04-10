
import pandas as pd, numpy as np, re
from pathlib import Path

BASE_PATH = Path("/Users/getapple/Documents/KSE/Master Thesis/Data/")
EU_FILE = BASE_PATH / "eu_weekly_uah.xlsx"
UA_FILE = BASE_PATH / "ukraine_monthly.xlsx"

OUT_PRODUCER = BASE_PATH / "UA_weekly_producer_UAH.xlsx"
OUT_CONSUMER = BASE_PATH / "UA_weekly_consumer_UAH.xlsx"
OUT_PRODUCER_W = BASE_PATH / "UA_weekly_producer_UAH_weights.xlsx"
OUT_CONSUMER_W = BASE_PATH / "UA_weekly_consumer_UAH_weights.xlsx"

OVER_START = pd.Timestamp("2022-01-01")
OVER_END   = pd.Timestamp("2025-12-01")

CHEESE_SET = ["EDAM", "GOUDA", "EMMENTAL", "CHEDDAR"]
MILK_SET   = ["DRINKING MILK", "SMP", "WMP"]
BUTTER_SET = ["BUTTER"]
CREAM_SET  = ["CREAM"]

def prep_eu_weekly_uah(path: Path):
    eu = pd.read_excel(path)
    eu["week_date"] = pd.to_datetime(eu["Begin Date"], errors="coerce").dt.normalize()
    eu["ms_code"] = pd.to_numeric(eu["Member State"], errors="coerce").astype("Int64")
    eu["product"] = eu["Product"].astype(str).str.upper().str.strip()
    eu["price_uah_1kg"] = pd.to_numeric(eu["Price (UAH/1kg)"], errors="coerce")
    eu = eu.dropna(subset=["week_date", "ms_code", "product", "price_uah_1kg"])

    eu_weekly = eu.pivot_table(
        index="week_date",
        columns=["ms_code", "product"],
        values="price_uah_1kg",
        aggfunc="mean"
    ).sort_index()
    eu_weekly.columns = pd.MultiIndex.from_tuples(eu_weekly.columns, names=["ms_code","product"])
    eu_monthly = eu_weekly.resample("MS").mean()
    return eu_weekly, eu_monthly

def parse_month_col_to_date(col):
    if isinstance(col, (pd.Timestamp, np.datetime64)):
        dt = pd.to_datetime(col)
        return dt.to_period("M").to_timestamp()
    s = str(col).strip()
    m = re.match(r"^(\d{4})-M(\d{2})$", s)
    if m:
        return pd.Timestamp(year=int(m.group(1)), month=int(m.group(2)), day=1)
    try:
        dt = pd.to_datetime(s, errors="raise")
        return dt.to_period("M").to_timestamp()
    except Exception:
        return None

def ua_sheet_to_long(df: pd.DataFrame, sheet_name: str) -> pd.DataFrame:
    if "Розріз" in df.columns:
        product_col = "Розріз"
    elif "Тип товарів і послуг" in df.columns:
        product_col = "Тип товарів і послуг"
    else:
        product_col = None

    id_cols = [c for c in ["Показник","Територіальний розріз","Категорія розрізу","Періодичність","Одиниця виміру"] if c in df.columns]
    if product_col:
        id_cols.append(product_col)

    date_cols, date_map = [], {}
    for c in df.columns:
        if c in id_cols:
            continue
        d = parse_month_col_to_date(c)
        if d is not None:
            date_cols.append(c)
            date_map[c] = d

    long = df.melt(id_vars=id_cols, value_vars=date_cols, var_name="date_raw", value_name="value")
    long["date"] = long["date_raw"].map(date_map)
    long["value"] = pd.to_numeric(long["value"], errors="coerce")
    long = long.dropna(subset=["date","value"])

    long["ua_product"] = long[product_col].astype(str) if product_col else "UNKNOWN"
    if "Територіальний розріз" not in long.columns:
        long["Територіальний розріз"] = "UNKNOWN"
    if "Показник" not in long.columns:
        long["Показник"] = sheet_name
    if "Одиниця виміру" not in long.columns:
        long["Одиниця виміру"] = "UNKNOWN"

    return long[["date","value","Показник","Територіальний розріз","ua_product","Одиниця виміру"]].sort_values("date")

def choose_basket(ua_product: str):
    s = (ua_product or "").lower()
    if "масло" in s:
        return "butter", BUTTER_SET
    if "сметан" in s or "вершк" in s:
        return "cream", CREAM_SET + MILK_SET
    if "сир" in s:
        return "cheese", CHEESE_SET + ["WMP","SMP"]
    if "молоко" in s:
        return "milk", MILK_SET
    return "fallback_milk", MILK_SET

def feature_cols_for_products(eu_monthly_cols, products):
    return [c for c in eu_monthly_cols if c[1] in products]

def corr_weights(y_m: pd.Series, X_m: pd.DataFrame) -> pd.Series:
    w = {}
    for col in X_m.columns:
        tmp = pd.concat([y_m.rename("y"), X_m[col].rename("x")], axis=1).dropna()
        if len(tmp) < 8:
            w[col] = 0.0
        else:
            c = tmp["y"].corr(tmp["x"])
            w[col] = float(max(c, 0.0)) if not np.isnan(c) else 0.0
    w = pd.Series(w, dtype=float)
    if w.sum() <= 0:
        w = pd.Series(1.0, index=X_m.columns, dtype=float)
    w = w / w.sum()
    if isinstance(w.index, pd.MultiIndex):
        w.index = pd.MultiIndex.from_tuples(w.index.tolist(), names=["ms_code","product"])
    return w

def weekly_composite_safe(eu_weekly: pd.DataFrame, weights: pd.Series) -> pd.Series:
    cols = list(weights.index)
    X = eu_weekly.reindex(columns=cols)
    w = weights.reindex(X.columns).to_numpy(float)
    Xv = X.to_numpy(float)
    mask = ~np.isnan(Xv)
    numerator = np.nansum(Xv * w, axis=1)
    denom = np.sum(mask * w, axis=1)
    denom = np.where(denom == 0, np.nan, denom)
    return pd.Series(numerator / denom, index=X.index, name="z")

def chowlin_fit(y_monthly: pd.Series, z_weekly: pd.Series):
    z_monthly = z_weekly.resample("MS").mean()
    df = pd.concat([y_monthly.rename("y"), z_monthly.rename("z")], axis=1).dropna()
    if len(df) < 8:
        return 0.0, 1.0
    X = np.column_stack([np.ones(len(df)), df["z"].values])
    b = np.linalg.lstsq(X, df["y"].values, rcond=None)[0]
    return float(b[0]), float(b[1])

def build_month_templates(prelim_weekly: pd.Series) -> dict:
    s = prelim_weekly.dropna().copy()
    if s.empty:
        return {}
    df = s.to_frame("p")
    df["month"] = df.index.to_period("M")
    rows = []
    for m, g in df.groupby("month"):
        p = g["p"]
        denom = p.sum()
        if denom <= 0 or np.isnan(denom):
            continue
        g = g.copy()
        g["share"] = p / denom
        g["moy"] = int(m.month)
        g["k"] = len(g)
        g["pos"] = np.arange(1, len(g) + 1)
        rows.append(g[["moy","k","pos","share"]])
    if not rows:
        return {}
    allw = pd.concat(rows)
    templ = allw.groupby(["moy","k","pos"])["share"].mean().reset_index()
    templates = {}
    for (moy, k), sub in templ.groupby(["moy","k"]):
        ww = sub.sort_values("pos")["share"].values
        ww = ww / ww.sum() if ww.sum() > 0 else np.ones(len(ww))/len(ww)
        templates[(int(moy), int(k))] = ww
    return templates

def denton_proportional_full(monthly_df: pd.DataFrame, weekly_prelim: pd.Series, templates: dict) -> pd.DataFrame:
    mdf = monthly_df.copy()
    mdf["month"] = mdf["date"].dt.to_period("M")
    out = []
    for _, r in mdf.sort_values("date").iterrows():
        month_key = r["month"]
        target = float(r["value"])
        ms = month_key.to_timestamp()
        me = month_key.to_timestamp() + pd.offsets.MonthEnd(0)
        weeks = pd.date_range(start=ms, end=me, freq="W-MON")
        if len(weeks) == 0:
            continue
        p = weekly_prelim.reindex(weeks)
        if p.notna().sum() >= 2 and p.fillna(0).sum() > 0:
            pp = p.fillna(p.mean()).clip(lower=1e-9)
            ww = pp.values
            ww = ww / ww.sum()
        else:
            moy = int(month_key.month)
            k = len(weeks)
            ww = templates.get((moy, k))
            if ww is None or len(ww) != k:
                ww = np.ones(k) / k
        out.append(pd.DataFrame({"week_date": weeks, "synthetic": target * ww}))
    out = pd.concat(out).sort_values("week_date").reset_index(drop=True)
    out["week_date"] = pd.to_datetime(out["week_date"]).dt.date
    return out

def process_sheet(sheet_long: pd.DataFrame, eu_weekly: pd.DataFrame, eu_monthly: pd.DataFrame, sheet_name: str):
    keys = sheet_long[["Показник","Територіальний розріз","ua_product","Одиниця виміру"]].drop_duplicates()
    weekly_rows, weight_rows, diag_rows = [], [], []
    for _, k in keys.iterrows():
        indicator = k["Показник"]
        region = k["Територіальний розріз"]
        ua_product = k["ua_product"]
        unit = k["Одиниця виміру"]

        ydf = sheet_long[
            (sheet_long["Показник"] == indicator) &
            (sheet_long["Територіальний розріз"] == region) &
            (sheet_long["ua_product"] == ua_product) &
            (sheet_long["Одиниця виміру"] == unit)
        ][["date","value"]].groupby("date", as_index=False)["value"].mean().sort_values("date")

        if len(ydf) < 6:
            continue

        cls, basket = choose_basket(ua_product)
        feat_cols = feature_cols_for_products(eu_monthly.columns, basket)
        if not feat_cols:
            continue

        y_overlap = ydf[(ydf["date"] >= OVER_START) & (ydf["date"] <= OVER_END)].set_index("date")["value"]
        X_overlap = eu_monthly.loc[:, feat_cols]
        X_overlap = X_overlap[(X_overlap.index >= OVER_START) & (X_overlap.index <= OVER_END)]

        w = corr_weights(y_overlap, X_overlap)
        z_weekly = weekly_composite_safe(eu_weekly, w)

        alpha, beta = chowlin_fit(y_overlap, z_weekly)
        prelim = (alpha + beta * z_weekly).clip(lower=1e-9)

        templ = build_month_templates(prelim[(prelim.index >= OVER_START) & (prelim.index <= pd.Timestamp("2025-12-31"))])
        weekly_out = denton_proportional_full(ydf, prelim, templ)

        weekly_out["sheet"] = sheet_name
        weekly_out["ua_indicator"] = indicator
        weekly_out["region"] = region
        weekly_out["ua_product"] = ua_product
        weekly_out["unit"] = unit
        weekly_out["eu_class"] = cls
        weekly_out["eu_price_unit"] = "UAH/1kg"
        weekly_out["method"] = "corr-weights(monthly 2022–2025) -> Chow–Lin(y~z) -> Denton proportional (full period)"
        weekly_rows.append(weekly_out)

        for (ms, prod), ww in w.items():
            if ww > 0:
                weight_rows.append({
                    "sheet": sheet_name,
                    "ua_indicator": indicator,
                    "region": region,
                    "ua_product": ua_product,
                    "eu_class": cls,
                    "ms_code": int(ms),
                    "eu_product": prod,
                    "weight": float(ww),
                })

        diag_rows.append({
            "sheet": sheet_name,
            "ua_indicator": indicator,
            "region": region,
            "ua_product": ua_product,
            "eu_class": cls,
            "ua_months": int(len(ydf)),
            "overlap_months": int(len(y_overlap)),
            "n_features": int(len(w)),
            "alpha": alpha,
            "beta": beta,
            "ua_start": str(ydf["date"].min().date()),
            "ua_end": str(ydf["date"].max().date()),
        })

    weekly_all = pd.concat(weekly_rows, ignore_index=True) if weekly_rows else pd.DataFrame()
    weights_all = pd.DataFrame(weight_rows)
    diag_all = pd.DataFrame(diag_rows)
    return weekly_all, weights_all, diag_all

# Run
eu_weekly, eu_monthly = prep_eu_weekly_uah(EU_FILE)
xls = pd.ExcelFile(UA_FILE)

prod_df = pd.read_excel(xls, sheet_name="producer_prices")
cons_df = pd.read_excel(xls, sheet_name="price_consumer")

prod_long = ua_sheet_to_long(prod_df, "producer_prices")
cons_long = ua_sheet_to_long(cons_df, "price_consumer")

prod_weekly, prod_weights, prod_diag = process_sheet(prod_long, eu_weekly, eu_monthly, "producer_prices")
cons_weekly, cons_weights, cons_diag = process_sheet(cons_long, eu_weekly, eu_monthly, "price_consumer")

with pd.ExcelWriter(OUT_PRODUCER, engine="openpyxl") as w:
    prod_weekly.to_excel(w, sheet_name="synthetic_weekly", index=False)
with pd.ExcelWriter(OUT_PRODUCER_W, engine="openpyxl") as w:
    prod_weights.to_excel(w, sheet_name="weights", index=False)
    prod_diag.to_excel(w, sheet_name="diagnostics", index=False)

with pd.ExcelWriter(OUT_CONSUMER, engine="openpyxl") as w:
    cons_weekly.to_excel(w, sheet_name="synthetic_weekly", index=False)
with pd.ExcelWriter(OUT_CONSUMER_W, engine="openpyxl") as w:
    cons_weights.to_excel(w, sheet_name="weights", index=False)
    cons_diag.to_excel(w, sheet_name="diagnostics", index=False)

(str(OUT_PRODUCER), str(OUT_CONSUMER), prod_weekly.shape, cons_weekly.shape)