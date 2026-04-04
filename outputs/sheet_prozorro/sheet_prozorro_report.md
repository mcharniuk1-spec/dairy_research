# RW4 Sheet Module - ProZorro

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
- Source sheet: Prozorro
- Rows (clean): 10927
- Date range: 2025-04-14 .. 2026-01-09
- Products: 6
- Stats rows: 18
- Tests rows: 18
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | date | raw_product | title | product | standardized_type | brand | region | qty | unit | unit_price | expected |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ProZorro | 2026-01-09 00:00:00 | Яйця курячі | Яйця столові курячі | Інше/невідомо | other |  | Чернівецька | 14400.0 | штука | 7.0 | 100800.0 |
| ProZorro | 2026-01-08 00:00:00 | Молоко питне | Молоко коров'яче | Молоко питне | milk |  | Вінницька | 1000.0 | кілограм | 41.94 | 52000.0 |
| ProZorro | 2026-01-08 00:00:00 | Яйця курячі | Яйце куряче столове, категорія Відбірні (XL) | Інше/невідомо | other |  | Житомирська | 60000.0 | штука | 5.8 | 453180.0 |
| ProZorro | 2026-01-08 00:00:00 | Молоко питне | Молоко коров'яче | Молоко питне | milk |  | Чернігівська | 3700.0 | кілограм | 39.84 | 148000.0 |
| ProZorro | 2026-01-08 00:00:00 | Сметана | Сметана 21%, фасування 400г, плівка поліетиленова, ДСТУ 4418 | Сметана | sour_cream |  | Житомирська | 1000.0 | кілограм | 120.0 | 164830.0 |
| ProZorro | 2026-01-08 00:00:00 | Сир твердий/напівтвердий | Сир твердий 50%, ДСТУ 6003/ДСТУ 4421 | Сир твердий | hard_cheese |  | Хмельницька | 2.5 | кілограм | 310.8 | 874.4 |
| ProZorro | 2026-01-08 00:00:00 | Масло вершкове | Масло солодковершкове фасоване | Вершки | cream |  | Чернігівська | 500.0 | кілограм | 411.96 | 207500.0 |
| ProZorro | 2026-01-08 00:00:00 | Вершки | Молоко коров'яче ультрапастеризоване, 2,5%, пакет картонний (плоский), ДСТУ 2661, 900г | Молоко питне | milk |  | Дніпропетровська | 1890.0 | кілограм | 32.0 | 94500.0 |
| ProZorro | 2026-01-08 00:00:00 | Сир твердий/напівтвердий | Сир твердий ваговий | Сир твердий | hard_cheese |  | Тернопільська | 51.0 | кілограм | 290.0 | 17850.0 |
| ProZorro | 2026-01-08 00:00:00 | Масло вершкове | Масло солодковершкове 73%, фасування 200г | Вершки | cream |  | Сумська | 587.0 | кілограм | 390.0 | 303479.0 |
| ProZorro | 2026-01-08 00:00:00 | Сметана | Сметана | Сметана | sour_cream |  | Чернівецька | 200.0 | кілограм | 140.0 | 28000.0 |
| ProZorro | 2026-01-08 00:00:00 | Яйця курячі | Яйця столові курячі | Інше/невідомо | other |  | Тернопільська | 6000.0 | штука | 4.850000000000001 | 30000.0 |
| ProZorro | 2026-01-08 00:00:00 | Масло вершкове | Масло солодковершкове вагове | Вершки | cream |  | Житомирська | 120.0 | кілограм | 360.0 | 54000.0 |
| ProZorro | 2026-01-08 00:00:00 | Молоко питне | Молоко коров'яче | Молоко питне | milk |  | Хмельницька | 3900.0 | кілограм | 42.9 | 167700.0 |
| ProZorro | 2026-01-08 00:00:00 | Яйця курячі | Яйце куряче столове, категорія Перша (M) | Інше/невідомо | other |  | Рівненська | 37000.0 | штука | 6.4 | 255000.0 |
| ProZorro | 2026-01-08 00:00:00 | Масло вершкове | Масло солодковершкове 73%, ДСТУ 4399 | Вершки | cream |  | Київська | 500.0 | кілограм | 403.8 | 202000.0 |
| ProZorro | 2026-01-08 00:00:00 | Сир кисломолочний | Сир кисломолочний фасований | Сир кисломолочний | cottage_cheese |  | Тернопільська | 341.6 | кілограм | 226.5 | 77884.8 |
| ProZorro | 2026-01-08 00:00:00 | Вершки | Молоко коров'яче пастеризоване, 2,5%, плівка поліетиленова, ДСТУ 2661, 1000г | Молоко питне | milk |  | Рівненська | 7800.0 | кілограм | 43.5 | 351000.0 |
| ProZorro | 2026-01-08 00:00:00 | Масло вершкове | Масло солодковершкове фасоване | Вершки | cream |  | Тернопільська | 133.2 | кілограм | 558.0 | 74369.56 |
| ProZorro | 2026-01-08 00:00:00 | Яйця курячі | Яйце куряче столове, категорія Перша (M) | Інше/невідомо | other |  | Одеська | 60000.0 | штука | 6.89 | 450000.0 |
| ProZorro | 2026-01-08 00:00:00 | Молоко питне | Молоко коров'яче | Молоко питне | milk |  | Тернопільська | 1917.0 | кілограм | 51.6 | 99684.0 |
| ProZorro | 2026-01-08 00:00:00 | Молоко питне | Молоко коров'яче | Молоко питне | milk |  | Житомирська | 950.0 | кілограм | 41.0 | 47500.0 |
| ProZorro | 2026-01-08 00:00:00 | Яйця курячі | Яйце куряче столове, категорія Вища (L) | Інше/невідомо | other |  | Житомирська | 15030.0 | штука | 6.0 | 120240.0 |
| ProZorro | 2026-01-07 00:00:00 | Масло вершкове | Масло солодковершкове 73,5%, ДСТУ 4399 | Вершки | cream |  | Волинська | 500.0 | кілограм | 290.0 | 200000.0 |
| ProZorro | 2026-01-07 00:00:00 | Яйця курячі | Яйце куряче столове, категорія Вища (L) | Інше/невідомо | other |  | Черкаська | 18600.0 | штука | 5.3 | 119040.0 |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ProZorro | Інше/невідомо | other | linear | 0 | 6464 | nan | nan | nan | nan | nan | nan |
| ProZorro | Інше/невідомо | other | pchip | 0 | 6464 | nan | nan | nan | nan | nan | nan |
| ProZorro | Інше/невідомо | other | real | 1889 | 4575 | nan | 5.838001118981797 | 5.800000000000001 | 0.9638980378419787 | 2.7 | 16.51571428571429 |
| ProZorro | Вершки | cream | linear | 0 | 6311 | nan | nan | nan | nan | nan | nan |
| ProZorro | Вершки | cream | pchip | 0 | 6311 | nan | nan | nan | nan | nan | nan |
| ProZorro | Вершки | cream | real | 1680 | 4631 | nan | 373.834379138322 | 374.2 | 86.20483760000837 | 137.7 | 700.0 |
| ProZorro | Молоко питне | milk | linear | 0 | 6211 | nan | nan | nan | nan | nan | nan |
| ProZorro | Молоко питне | milk | pchip | 0 | 6211 | nan | nan | nan | nan | nan | nan |
| ProZorro | Молоко питне | milk | real | 1788 | 4423 | nan | 48.49254521129857 | 41.72 | 29.687501199024183 | 21.91 | 820.0 |
| ProZorro | Сир кисломолочний | cottage_cheese | linear | 0 | 5511 | nan | nan | nan | nan | nan | nan |
| ProZorro | Сир кисломолочний | cottage_cheese | pchip | 0 | 5511 | nan | nan | nan | nan | nan | nan |
| ProZorro | Сир кисломолочний | cottage_cheese | real | 649 | 4862 | nan | 147.40594966615308 | 133.98 | 82.03494450033084 | 60.0 | 660.0 |
| ProZorro | Сир твердий | hard_cheese | linear | 0 | 5541 | nan | nan | nan | nan | nan | nan |
| ProZorro | Сир твердий | hard_cheese | pchip | 0 | 5541 | nan | nan | nan | nan | nan | nan |
| ProZorro | Сир твердий | hard_cheese | real | 695 | 4846 | nan | 291.4129160671463 | 284.04 | 70.20390883296758 | 117.0 | 604.0 |
| ProZorro | Сметана | sour_cream | linear | 0 | 5237 | nan | nan | nan | nan | nan | nan |
| ProZorro | Сметана | sour_cream | pchip | 0 | 5237 | nan | nan | nan | nan | nan | nan |
| ProZorro | Сметана | sour_cream | real | 538 | 4699 | nan | 121.71241171003719 | 123.0 | 30.082614564504212 | 57.0 | 212.0 |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ProZorro | Інше/невідомо | other | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Інше/невідомо | other | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Інше/невідомо | other | real | 40 | 0.6870461976229786 | 0.012971264945479098 | 0.07276232112735213 | 0.2594432985227212 | 0.37587104171614477 | 0.5274778796297352 | 1 |
| ProZorro | Вершки | cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Вершки | cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Вершки | cream | real | 40 | 0.218875716984755 | 0.03717534083537155 | 0.40159092808143304 | 0.754072940692235 | 0.9087430926338447 | 0.24729770775780144 | 1 |
| ProZorro | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Молоко питне | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Молоко питне | milk | real | 40 | 0.29486317098961157 | 0.01 | 0.13302072839339238 | 0.049085486993071824 | 0.0704755506389102 | 5.153843462129121e-15 | 1 |
| ProZorro | Сир кисломолочний | cottage_cheese | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Сир кисломолочний | cottage_cheese | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Сир кисломолочний | cottage_cheese | real | 40 | 0.21762425415666892 | 0.020158325763386862 | 0.008572596301612789 | 0.9739630993548387 | 0.6869582481513895 | 0.9123171456867544 | 1 |
| ProZorro | Сир твердий | hard_cheese | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Сир твердий | hard_cheese | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Сир твердий | hard_cheese | real | 40 | 0.15681711714781005 | 0.1 | 0.12192247174395353 | 0.1479193470941406 | 0.09935412328815665 | 0.9177981113812061 | 1 |
| ProZorro | Сметана | sour_cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Сметана | sour_cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| ProZorro | Сметана | sour_cream | real | 40 | 6.217449032740301e-07 | 0.1 | 0.01939030447207143 | 0.9332341974423672 | 0.899607181164749 | 0.7444399147654036 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_prozorro/sheet_prozorro_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_prozorro/sheet_prozorro_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_prozorro/sheet_prozorro_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_prozorro/sheet_prozorro_region_trends.png
