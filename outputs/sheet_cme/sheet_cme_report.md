# RW3 Module Report - sheet_cme

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=sheet_cme
- xlsx_files=1
- png_files=3
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### sheet_cme_output_raw

| Date | CME III UAH |
| --- | --- |
| 2026-01-27 00:00:00 | 633.94191 |
| 2026-01-26 00:00:00 | 635.007552 |
| 2026-01-23 00:00:00 | 634.1188229999999 |
| 2026-01-22 00:00:00 | 635.981007 |
| 2026-01-21 00:00:00 | 637.5374280000001 |
| 2026-01-20 00:00:00 | 638.20005 |
| 2026-01-16 00:00:00 | 639.608398 |
| 2026-01-15 00:00:00 | 635.641864 |
| 2026-01-14 00:00:00 | 637.712474 |
| 2026-01-13 00:00:00 | 638.879304 |
| 2026-01-12 00:00:00 | 637.52036 |
| 2026-01-09 00:00:00 | 638.837344 |
| 2026-01-08 00:00:00 | 636.033795 |
| 2026-01-07 00:00:00 | 641.856072 |
| 2026-01-06 00:00:00 | 640.129872 |
| 2026-01-05 00:00:00 | 635.6818259999999 |
| 2026-01-02 00:00:00 | 635.5034069999999 |
| 2025-12-31 00:00:00 | 645.142316 |
| 2025-12-30 00:00:00 | 670.420252 |
| 2025-12-29 00:00:00 | 667.5509189999999 |
| 2025-12-26 00:00:00 | 665.058966 |
| 2025-12-24 00:00:00 | 663.9217309999999 |
| 2025-12-23 00:00:00 | 665.098596 |
| 2025-12-22 00:00:00 | 666.252537 |
| 2025-12-19 00:00:00 | 667.660798 |

### sheet_cme_output_clean

| source | date | raw_product | product | standardized_type | brand | region | price | unit_ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | 2026-01-27 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 633.94191 | 1 |
| CME | 2026-01-26 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 635.007552 | 1 |
| CME | 2026-01-23 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 634.1188229999999 | 1 |
| CME | 2026-01-22 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 635.981007 | 1 |
| CME | 2026-01-21 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 637.5374280000001 | 1 |
| CME | 2026-01-20 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 638.20005 | 1 |
| CME | 2026-01-16 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 639.608398 | 1 |
| CME | 2026-01-15 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 635.641864 | 1 |
| CME | 2026-01-14 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 637.712474 | 1 |
| CME | 2026-01-13 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 638.879304 | 1 |
| CME | 2026-01-12 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 637.52036 | 1 |
| CME | 2026-01-09 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 638.837344 | 1 |
| CME | 2026-01-08 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 636.033795 | 1 |
| CME | 2026-01-07 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 641.856072 | 1 |
| CME | 2026-01-06 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 640.129872 | 1 |
| CME | 2026-01-05 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 635.6818259999999 | 1 |
| CME | 2026-01-02 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 635.5034069999999 | 1 |
| CME | 2025-12-31 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 645.142316 | 1 |
| CME | 2025-12-30 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 670.420252 | 1 |
| CME | 2025-12-29 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 667.5509189999999 | 1 |
| CME | 2025-12-26 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 665.058966 | 1 |
| CME | 2025-12-24 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 663.9217309999999 | 1 |
| CME | 2025-12-23 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 665.098596 | 1 |
| CME | 2025-12-22 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 666.252537 | 1 |
| CME | 2025-12-19 00:00:00 | CME Class III | Молоко питне | milk | nan | US | 667.660798 | 1 |

### sheet_cme_output_daily_variants

| source | date | product | standardized_type | brand | region | unit_ok | price_real | price_linear | price_pchip | imputed_flag_linear | imputed_flag_pchip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | 2022-01-03 00:00:00 | Молоко питне | milk | nan | US | 1 | 502.464444 | nan | nan | 0 | 0 |
| CME | 2022-01-04 00:00:00 | Молоко питне | milk | nan | US | 1 | 502.464444 | nan | nan | 0 | 0 |
| CME | 2022-01-05 00:00:00 | Молоко питне | milk | nan | US | 1 | 563.9684159999999 | nan | nan | 0 | 0 |
| CME | 2022-01-06 00:00:00 | Молоко питне | milk | nan | US | 1 | 560.358591 | nan | nan | 0 | 0 |
| CME | 2022-01-07 00:00:00 | Молоко питне | milk | nan | US | 1 | 557.063979 | nan | nan | 0 | 0 |
| CME | 2022-01-08 00:00:00 | Молоко питне | milk | nan | US | 1 | nan | nan | nan | 0 | 0 |
| CME | 2022-01-09 00:00:00 | Молоко питне | milk | nan | US | 1 | nan | nan | nan | 0 | 0 |
| CME | 2022-01-10 00:00:00 | Молоко питне | milk | nan | US | 1 | 557.378379 | nan | nan | 0 | 0 |
| CME | 2022-01-11 00:00:00 | Молоко питне | milk | nan | US | 1 | 560.170926 | nan | nan | 0 | 0 |
| CME | 2022-01-12 00:00:00 | Молоко питне | milk | nan | US | 1 | 560.6395339999999 | nan | nan | 0 | 0 |
| CME | 2022-01-13 00:00:00 | Молоко питне | milk | nan | US | 1 | 563.012336 | nan | nan | 0 | 0 |
| CME | 2022-01-14 00:00:00 | Молоко питне | milk | nan | US | 1 | 562.5104160000001 | nan | nan | 0 | 0 |
| CME | 2022-01-15 00:00:00 | Молоко питне | milk | nan | US | 1 | nan | nan | nan | 0 | 0 |
| CME | 2022-01-16 00:00:00 | Молоко питне | milk | nan | US | 1 | nan | nan | nan | 0 | 0 |
| CME | 2022-01-17 00:00:00 | Молоко питне | milk | nan | US | 1 | nan | nan | nan | 0 | 0 |
| CME | 2022-01-18 00:00:00 | Молоко питне | milk | nan | US | 1 | 568.90806 | nan | nan | 0 | 0 |
| CME | 2022-01-19 00:00:00 | Молоко питне | milk | nan | US | 1 | 574.736323 | nan | nan | 0 | 0 |
| CME | 2022-01-20 00:00:00 | Молоко питне | milk | nan | US | 1 | 575.17695 | nan | nan | 0 | 0 |
| CME | 2022-01-21 00:00:00 | Молоко питне | milk | nan | US | 1 | 574.685844 | nan | nan | 0 | 0 |
| CME | 2022-01-22 00:00:00 | Молоко питне | milk | nan | US | 1 | nan | nan | nan | 0 | 0 |
| CME | 2022-01-23 00:00:00 | Молоко питне | milk | nan | US | 1 | nan | nan | nan | 0 | 0 |
| CME | 2022-01-24 00:00:00 | Молоко питне | milk | nan | US | 1 | 574.85743 | nan | nan | 0 | 0 |
| CME | 2022-01-25 00:00:00 | Молоко питне | milk | nan | US | 1 | 575.442972 | nan | nan | 0 | 0 |
| CME | 2022-01-26 00:00:00 | Молоко питне | milk | nan | US | 1 | 581.342424 | nan | nan | 0 | 0 |
| CME | 2022-01-27 00:00:00 | Молоко питне | milk | nan | US | 1 | 586.335424 | nan | nan | 0 | 0 |

### sheet_cme_output_series_long

| source | date | product | standardized_type | brand | region | unit_ok | imputed_flag_linear | imputed_flag_pchip | series_variant | price |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | 2022-01-03 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 502.464444 |
| CME | 2022-01-04 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 502.464444 |
| CME | 2022-01-05 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 563.9684159999999 |
| CME | 2022-01-06 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 560.358591 |
| CME | 2022-01-07 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 557.063979 |
| CME | 2022-01-10 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 557.378379 |
| CME | 2022-01-11 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 560.170926 |
| CME | 2022-01-12 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 560.6395339999999 |
| CME | 2022-01-13 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 563.012336 |
| CME | 2022-01-14 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 562.5104160000001 |
| CME | 2022-01-18 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 568.90806 |
| CME | 2022-01-19 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 574.736323 |
| CME | 2022-01-20 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 575.17695 |
| CME | 2022-01-21 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 574.685844 |
| CME | 2022-01-24 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 574.85743 |
| CME | 2022-01-25 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 575.442972 |
| CME | 2022-01-26 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 581.342424 |
| CME | 2022-01-27 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 586.335424 |
| CME | 2022-01-28 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 590.193644 |
| CME | 2022-01-31 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 586.328043 |
| CME | 2022-02-01 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 580.2076450000001 |
| CME | 2022-02-02 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 575.13858 |
| CME | 2022-02-03 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 580.5264199999999 |
| CME | 2022-02-04 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 585.19107 |
| CME | 2022-02-07 00:00:00 | Молоко питне | milk | nan | US | 1 | 0 | 0 | real | 585.45344 |

### sheet_cme_output_descriptive_st

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | Молоко питне | milk | linear | 0 | 1486 | nan | nan | nan | nan | nan | nan |
| CME | Молоко питне | milk | pchip | 0 | 1486 | nan | nan | nan | nan | nan | nan |
| CME | Молоко питне | milk | real | 1023 | 463 | nan | 709.2641239530792 | 713.331402 | 95.79149583199074 | 502.464444 | 966.9001849999999 |

### sheet_cme_output_tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| CME | Молоко питне | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| CME | Молоко питне | milk | real | 214 | 0.198094907286723 | 0.04425555473715628 | 0.002331149919449167 | 0.5837986248407785 | 0.647495693005676 | 8.722972988440486e-233 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_cme/sheet_cme_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_cme/sheet_cme_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_cme/sheet_cme_timeseries_by_standardized_type.png
