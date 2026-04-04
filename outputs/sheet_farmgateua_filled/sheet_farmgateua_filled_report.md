# RW4 Sheet Module - FarmGateUA_filled

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
- Source sheet: farm_gate_all_missing_filled_daily.xlsx (daily_lin + daily_PCHIP)
- Rows (clean): 38012
- Date range: 2021-12-31 .. 2025-12-31
- Products: 1
- Stats rows: 3
- Tests rows: 3
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | date | raw_product | product | standardized_type | subcategory | unit_family | comparison_family | liter_equiv_allowed | maturation_type | mapping_quality_flag | matched_pattern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FarmGateUA_filled | 2021-12-31 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-01 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-02 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-03 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-04 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-05 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-06 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-07 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-08 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-09 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-10 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-11 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-12 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-13 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-14 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-15 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-16 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-17 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-18 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-19 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-20 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-21 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-22 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-23 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |
| FarmGateUA_filled | 2022-01-24 00:00:00 | Середня ціна реалізованої продукції сільського господарства | Інше/невідомо | other | unknown | unknown | other | 0 | unknown | unmatched |  |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FarmGateUA_filled | Інше/невідомо | other | linear | 38012 | 0 | 0.0 | 13.708372105804168 | 12.92577073303805 | 2.824068609681121 | 8.471487882797518 | 21.084681239808457 |
| FarmGateUA_filled | Інше/невідомо | other | pchip | 38012 | 0 | 0.0 | 13.709583456091801 | 12.927582386400498 | 2.8266235605529615 | 8.471487882797518 | 21.084681239808457 |
| FarmGateUA_filled | Інше/невідомо | other | real | 38012 | 0 | nan | 13.708372105804168 | 12.92577073303805 | 2.824068609681121 | 8.471487882797518 | 21.084681239808457 |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FarmGateUA_filled | Інше/невідомо | other | linear | 210 | 0.7779551957876938 | 0.01 | 1.2007057808531991e-06 | 0.2125648821355386 | 2.3524573074260332e-17 | 1.3141341645410218e-67 | 1 |
| FarmGateUA_filled | Інше/невідомо | other | pchip | 210 | 0.792649612268183 | 0.01 | 4.731677414985856e-06 | 0.10194221083346325 | 2.0198296592398195e-19 | 4.075183884353616e-64 | 1 |
| FarmGateUA_filled | Інше/невідомо | other | real | 210 | 0.7779551957876938 | 0.01 | 1.2007057808531991e-06 | 0.2125648821355386 | 2.3524573074260332e-17 | 1.3141341645410218e-67 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_filled/sheet_farmgateua_filled_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_filled/sheet_farmgateua_filled_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_filled/sheet_farmgateua_filled_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_filled/sheet_farmgateua_filled_region_trends.png
