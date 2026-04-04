# RW4 Sheet Module - FarmGateUA_initial

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- Input workbook: full_uah.xlsx
- Source sheet: farm_gate_daily.xlsx (daily_lin + daily_PCHIP)
- Rows (clean): 32620
- Date range: 2021-12-31 .. 2025-12-31
- Products: 1
- Stats rows: 3
- Tests rows: 3
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | date | raw_product | product | standardized_type | subcategory | unit_family | comparison_family | liter_equiv_allowed | maturation_type | mapping_quality_flag | matched_pattern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FarmGateUA_initial | 2021-12-31 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-01 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-02 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-03 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-04 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-05 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-06 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-07 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-08 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-09 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-10 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-11 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-12 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-13 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-14 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-15 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-16 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-17 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-18 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-19 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-20 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-21 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-22 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-23 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_initial | 2022-01-24 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FarmGateUA_initial | Інше/невідомо | other | linear | 32620 | 0 | 0.0 | 13.951120190864883 | 13.770783202784806 | 2.7958947865498796 | 8.293148279028083 | 20.922893951010597 |
| FarmGateUA_initial | Інше/невідомо | other | pchip | 32620 | 0 | 0.0 | 13.951740699623025 | 13.769852616054845 | 2.798197463217094 | 8.293148279028083 | 20.922893951010597 |
| FarmGateUA_initial | Інше/невідомо | other | real | 32620 | 0 | nan | 13.951120190864883 | 13.770783202784806 | 2.7958947865498796 | 8.293148279028083 | 20.922893951010597 |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FarmGateUA_initial | Інше/невідомо | other | linear | 210 | 0.7627519923605295 | 0.01 | 2.216109749182032e-07 | 0.0011196325377328324 | 1.7399701782608784e-15 | 2.538007005036659e-262 | 1 |
| FarmGateUA_initial | Інше/невідомо | other | pchip | 210 | 0.776509641922007 | 0.01 | 8.143250868561355e-07 | 0.0007239144342248877 | 7.309884125658169e-16 | 8.48372797590486e-195 | 1 |
| FarmGateUA_initial | Інше/невідомо | other | real | 210 | 0.7627519923605295 | 0.01 | 2.216109749182032e-07 | 0.0011196325377328324 | 1.7399701782608784e-15 | 2.538007005036659e-262 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_initial/sheet_farmgateua_initial_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_initial/sheet_farmgateua_initial_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_initial/sheet_farmgateua_initial_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_initial/sheet_farmgateua_initial_region_trends.png
