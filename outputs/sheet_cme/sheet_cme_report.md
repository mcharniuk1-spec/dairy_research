# RW3 Separate Sheet Module - CME

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
- Source sheet: CME III
- Rows (clean): 1023
- Date range: 2022-01-03 .. 2026-01-27
- Products: 1
- Stats rows: 3
- Tests rows: 3
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | date | raw_product | product | standardized_type | brand | region | price | unit_ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | 2026-01-27 00:00:00 | CME Class III | Молоко питне | milk |  | US | 633.94191 | 1 |
| CME | 2026-01-26 00:00:00 | CME Class III | Молоко питне | milk |  | US | 635.007552 | 1 |
| CME | 2026-01-23 00:00:00 | CME Class III | Молоко питне | milk |  | US | 634.1188229999999 | 1 |
| CME | 2026-01-22 00:00:00 | CME Class III | Молоко питне | milk |  | US | 635.981007 | 1 |
| CME | 2026-01-21 00:00:00 | CME Class III | Молоко питне | milk |  | US | 637.5374280000001 | 1 |
| CME | 2026-01-20 00:00:00 | CME Class III | Молоко питне | milk |  | US | 638.20005 | 1 |
| CME | 2026-01-16 00:00:00 | CME Class III | Молоко питне | milk |  | US | 639.608398 | 1 |
| CME | 2026-01-15 00:00:00 | CME Class III | Молоко питне | milk |  | US | 635.641864 | 1 |
| CME | 2026-01-14 00:00:00 | CME Class III | Молоко питне | milk |  | US | 637.712474 | 1 |
| CME | 2026-01-13 00:00:00 | CME Class III | Молоко питне | milk |  | US | 638.879304 | 1 |
| CME | 2026-01-12 00:00:00 | CME Class III | Молоко питне | milk |  | US | 637.52036 | 1 |
| CME | 2026-01-09 00:00:00 | CME Class III | Молоко питне | milk |  | US | 638.837344 | 1 |
| CME | 2026-01-08 00:00:00 | CME Class III | Молоко питне | milk |  | US | 636.033795 | 1 |
| CME | 2026-01-07 00:00:00 | CME Class III | Молоко питне | milk |  | US | 641.856072 | 1 |
| CME | 2026-01-06 00:00:00 | CME Class III | Молоко питне | milk |  | US | 640.129872 | 1 |
| CME | 2026-01-05 00:00:00 | CME Class III | Молоко питне | milk |  | US | 635.6818259999999 | 1 |
| CME | 2026-01-02 00:00:00 | CME Class III | Молоко питне | milk |  | US | 635.5034069999999 | 1 |
| CME | 2025-12-31 00:00:00 | CME Class III | Молоко питне | milk |  | US | 645.142316 | 1 |
| CME | 2025-12-30 00:00:00 | CME Class III | Молоко питне | milk |  | US | 670.420252 | 1 |
| CME | 2025-12-29 00:00:00 | CME Class III | Молоко питне | milk |  | US | 667.5509189999999 | 1 |
| CME | 2025-12-26 00:00:00 | CME Class III | Молоко питне | milk |  | US | 665.058966 | 1 |
| CME | 2025-12-24 00:00:00 | CME Class III | Молоко питне | milk |  | US | 663.9217309999999 | 1 |
| CME | 2025-12-23 00:00:00 | CME Class III | Молоко питне | milk |  | US | 665.098596 | 1 |
| CME | 2025-12-22 00:00:00 | CME Class III | Молоко питне | milk |  | US | 666.252537 | 1 |
| CME | 2025-12-19 00:00:00 | CME Class III | Молоко питне | milk |  | US | 667.660798 | 1 |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | Молоко питне | milk | linear | 0 | 1486 | nan | nan | nan | nan | nan | nan |
| CME | Молоко питне | milk | pchip | 0 | 1486 | nan | nan | nan | nan | nan | nan |
| CME | Молоко питне | milk | real | 1023 | 463 | nan | 709.2641239530792 | 713.331402 | 95.79149583199074 | 502.464444 | 966.9001849999999 |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| CME | Молоко питне | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| CME | Молоко питне | milk | real | 214 | 0.19809490728672302 | 0.044255554737156276 | 0.0023311499194491672 | 0.5837986248407785 | 0.647495693005676 | 8.722972988440486e-233 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_cme/sheet_cme_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_cme/sheet_cme_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_cme/sheet_cme_distribution.png
