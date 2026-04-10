# RW3 Separate Modular Pipeline (UAH-only)

This folder contains the split RW3 pipeline for vertical price transmission (VPT) in dairy products.
Analysis is product-first, supports brand and region layers, estimates two-direction influence, controls discounts, and reports correlations across sources.
Every module report is written in both `PDF` and `MD`.

Code root:
- `/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3`

Input workbook:
- `/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/full_uah.xlsx`

Output root:
- `/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs`

## 1) File structure

Core runners:
- `common.py`: shared loading, cleaning, daily variants, XLSX/PDF writers, common plotting.
- `sheet_worker.py`: per-sheet processing and diagnostics.
- `model_worker.py`: econometric modules and forecast/synthetic modules.
- `graph_worker.py`: graph and matrix modules.
- `run_all_rw3.py`: full execution + run-all summary output.

Sheet entry scripts:
- `sheet_ProducerUA.py`
- `sheet_ConsumerUA.py`
- `sheet_EU.py`
- `sheet_ProZorro.py`
- `sheet_Silpo.py`
- `sheet_Novus.py`
- `sheet_CME.py`

Model entry scripts:
- `model_ardl.py`
- `model_ecm.py`
- `model_nardl.py`
- `model_vecm.py`
- `model_discounts.py`
- `model_short_chain_regional.py`
- `model_intersection_bidirectional.py`
- `model_forecast_knn.py`

Graph entry scripts:
- `graphs_decomposition.py`
- `graphs_overlay_ln.py`
- `graphs_correlations_lags.py`
- `graphs_brand_region.py`

Doc helper:
- `build_readme_docx.py`: converts this README into `README.docx`.

## 2) Data mapping and transformations (short)

Producer_UA / Consumer_UA:
- Required: `date`, `ua_product`, `price_linear`, `price_pchip` (or `price_chip`), optional `price_real`.
- Transformation: `price = price_linear -> price_pchip -> price_real`; keep all 3 variants in daily table.

Europe:
- Required: `date`, `Product`, `Price (UAH/kg)`.
- Transformation: `price = Price (UAH/kg)`; daily variants generated.

ProZorro:
- Required: `Дата`, `Product`/`Профіль`, `Товар`, `Ціна за одиницю`, `Регіон організатора`, `Очікувана вартість`, `Сума договорів початкова`, `Сума договорів поточна`.
- Transformation: `price = Ціна за одиницю` (fallback from expected/qty when needed), plus `prozorro_unit_price_uah`, `savings_rate`.

Silpo / Novus:
- Required: `date`, `product_title`, `brand`, `price_current`, `unit_price`, promo fields when available.
- Transformation: `price = unit_price -> price_current`; Novus dedupe by latest timestamp per `(date, sku_id)`; keep promo dummies/depth/presence.

CME III:
- Required: `Date`, `CME III UAH`.
- Transformation: `price = CME III UAH`.

Common:
- Product and `standardized_type` classification from mapping logic.
- `unit_ok` flags retained.
- Daily variants: `price_real`, `price_linear`, `price_pchip`, with imputation flags.

## 3) Diagnostics and interpretation

Diagnostics are run per `source x product x standardized_type x series_variant` (weekly aggregation for tests):
- ADF (`adf_p`)
- KPSS (`kpss_p`)
- Ljung-Box (`ljungbox_p`)
- Breusch-Pagan (`bp_p`)
- White (`white_p`)
- Jarque-Bera (`jb_p`)
- Stability (`stability_flag`, `stability_drift`)

Interpretation fields added:
- `integration_class`, `ac_risk`, `het_risk`, `non_normal_risk`, `stability_risk_class`
- `recommended_action`, `recommended_model_family`, `avoid`

Fast rule:
- ADF `>0.05` and KPSS `<0.05` -> likely I(1)-like -> differences/cointegration framework.
- Ljung-Box `<0.05` -> add lag structure.
- BP/White `<0.05` -> robust/HAC errors.
- `stability_flag=1` -> split/rolling robustness.

## 4) Model modules and outputs

`model_ardl.py`:
- Output: `outputs/model_ardl/model_ardl_output.xlsx`, `...pdf`, `ardl_short_run.png`.
- Main table: `ARDL_Summary`.

`model_ecm.py`:
- Output: `outputs/model_ecm/model_ecm_output.xlsx`, `...pdf`, `ecm_ect.png`.
- Main table: `ECM_Summary`.

`model_nardl.py`:
- Output: `outputs/model_nardl/model_nardl_output.xlsx`, `...pdf`, `nardl_*.png`.
- Main table: `NARDL_Summary`.

`model_vecm.py`:
- Output: `outputs/model_vecm/model_vecm_output.xlsx`, `...pdf`, `vecm_alpha.png`.
- Main table: `VECM_Summary`.

`model_discounts.py`:
- Output: `outputs/model_discounts/model_discounts_output.xlsx`, `...pdf`, promo delta charts.
- Tables: `Silpo_Discounts_Occurrence`, `Silpo_Discounts_Depth`, `Silpo_Transmission_PromoCtrl`.

`model_short_chain_regional.py`:
- Output: `outputs/model_short_chain_regional/model_short_chain_regional_output.xlsx`, `...pdf`.
- Tables: lag matrix/profile, short-run summary/details, chain effects, ProZorro regional effects.

`model_intersection_bidirectional.py`:
- Output: `outputs/model_intersection_bidirectional/model_intersection_bidirectional_output.xlsx`, `...pdf`.
- Tables:
- `Bidirectional_Results`: both-direction influence per pair (ProducerUA/ProZorro/Silpo/Novus/ConsumerUA).
- `Bidirectional_Granger`: directionality support with Granger min p-values.
- `Intersection_Combination_Summary`: main intersection models (`silpo_only`, `novus_only`, `silpo_novus_intersection`).
- `CrossTable_Correlations`: source correlations across tables.

`model_forecast_knn.py`:
- Output: `outputs/model_forecast_knn/model_forecast_knn_output.xlsx`, `...pdf`, forecast and synthetic charts.
- Tables:
- `Forecast_Summary`: ProducerUA/ConsumerUA forecasts from retail/bulk signals.
- `Forecast_Predictions`: holdout and future 30-day predictions.
- `Synthetic_Retail_Series`: product+brand synthetic retail price for `2025-10-21..2026-08-01`.
- `Synthetic_Influence_Coefficients`: overlap coefficients by product+brand.
- `Synthetic_to_Consumer_Link`: relationship of synthetic retail to ConsumerUA.

## 5) Graph modules and outputs

`graphs_decomposition.py`:
- Trend/seasonal/residual decomposition tables + plots.

`graphs_overlay_ln.py`:
- Before/after ln tables + intersection overlay plots by product.

`graphs_correlations_lags.py`:
- Correlation tables/matrix and lag profile outputs.

`graphs_brand_region.py`:
- Brand IO metrics and ProZorro region metrics with charts.

## 6) Run commands

Run all:
```bash
python3 "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/run_all_rw3.py"
```

Run single new modules:
```bash
python3 "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/model_intersection_bidirectional.py"
python3 "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/model_forecast_knn.py"
```

Generate README docx:
```bash
python3 "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/build_readme_docx.py"
```

## 7) Run-all package

`run_all_rw3.py` writes:
- `outputs/run_all_summary/run_all_rw3_summary.xlsx`
- `outputs/run_all_summary/run_all_rw3_summary.pdf`

This is the readable index of every module execution status and output location.

## 8) PDF layout policy

Every module PDF uses non-overlapping pages:
- text page(s),
- table page(s),
- graph page(s).

No text over graph overlays are used.

## 9) Markdown report policy

Every module PDF has a same-name markdown companion in the same output folder:
- `*_report.pdf` -> `*_report.md`
- run-all summary also includes markdown: `run_all_rw3_summary.md`
