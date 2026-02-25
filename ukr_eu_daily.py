# pip install pandas numpy openpyxl scipy

import pandas as pd
import numpy as np
from pathlib import Path

from scipy.interpolate import PchipInterpolator  # if missing: pip install scipy

BASE_OUT = Path("/Users/getapple/Documents/KSE/Master Thesis/Data/synthetic ukr producers:consumers/")

PROD_FILE = BASE_OUT / "UA_weekly_producer_UAH.xlsx"
CONS_FILE = BASE_OUT / "UA_weekly_consumer_UAH.xlsx"

OUT_PROD_DAILY = BASE_OUT / "UA_daily_producer_UAH_methods.xlsx"
OUT_CONS_DAILY = BASE_OUT / "UA_daily_consumer_UAH_methods.xlsx"

def make_daily_two_methods(df_weekly: pd.DataFrame) -> pd.DataFrame:
    df = df_weekly.copy()
    df["week_date"] = pd.to_datetime(df["week_date"])
    value_col = "synthetic"
    key_cols = [c for c in df.columns if c not in ["week_date", value_col]]
    df = df.sort_values(key_cols + ["week_date"])

    out_parts = []
    for keys, g in df.groupby(key_cols, dropna=False):
        g = g.sort_values("week_date")[["week_date", value_col]].dropna()
        if g.empty:
            continue

        start, end = g["week_date"].min(), g["week_date"].max()
        daily_idx = pd.date_range(start=start, end=end, freq="D")

        s = g.set_index("week_date")[value_col].astype(float)

        # Method 1: time-linear interpolation
        s_daily = s.reindex(daily_idx)
        price_linear = s_daily.interpolate(method="time").ffill().bfill()

        # Method 2: PCHIP (shape-preserving cubic)
        if s.index.nunique() >= 3:
            x = (s.index - s.index[0]).days.astype(float)
            y = s.values.astype(float)
            pchip = PchipInterpolator(x, y, extrapolate=True)
            xd = (daily_idx - s.index[0]).days.astype(float)
            price_pchip = pd.Series(pchip(xd), index=daily_idx).clip(lower=0)
        else:
            # if too few points: fallback to smoothed linear
            price_pchip = price_linear.rolling(7, center=True, min_periods=1).mean()

        part = pd.DataFrame({
            "date": daily_idx.date,
            "price_linear": price_linear.values,
            "price_pchip": price_pchip.values,
        })

        if not isinstance(keys, tuple):
            keys = (keys,)
        for col, val in zip(key_cols, keys):
            part[col] = val

        out_parts.append(part)

    out = pd.concat(out_parts, ignore_index=True) if out_parts else pd.DataFrame()
    cols_front = ["date"] + key_cols + [c for c in out.columns if c not in (["date"] + key_cols)]
    return out[cols_front]

# Load weekly
prod_weekly = pd.read_excel(PROD_FILE, sheet_name="synthetic_weekly")
cons_weekly = pd.read_excel(CONS_FILE, sheet_name="synthetic_weekly")

# Build daily
prod_daily = make_daily_two_methods(prod_weekly)
cons_daily = make_daily_two_methods(cons_weekly)

# Save
with pd.ExcelWriter(OUT_PROD_DAILY, engine="openpyxl") as w:
    prod_daily.to_excel(w, sheet_name="daily_methods", index=False)

with pd.ExcelWriter(OUT_CONS_DAILY, engine="openpyxl") as w:
    cons_daily.to_excel(w, sheet_name="daily_methods", index=False)

print("Saved:", OUT_PROD_DAILY)
print("Saved:", OUT_CONS_DAILY)
