# RW3 Module Report - sheet_eu

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=sheet_eu
- xlsx_files=1
- png_files=3
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### sheet_eu_output_raw

| date | Country | Product | Price (€/100kg) | EUR_UAH_rate | Price (UAH/kg) |
| --- | --- | --- | --- | --- | --- |
| 2021-12-30 00:00:00 | France | WMP | 425.0 | 30.8853 | 131.262525 |
| 2021-12-30 00:00:00 | Slovenia | EMMENTAL | 524.381 | 30.8853 | 161.956644993 |
| 2021-12-30 00:00:00 | Belgium | SMP | 335.59 | 30.8853 | 103.64797827 |
| 2021-12-30 00:00:00 | Slovenia | DRINKING MILK | 69.448 | 30.8853 | 21.449223144 |
| 2021-12-30 00:00:00 | Denmark | WMP | 427.0 | 30.8853 | 131.880231 |
| 2021-12-30 00:00:00 | Belgium | WMP | 420.37 | 30.8853 | 129.83253561 |
| 2021-12-30 00:00:00 | Spain | EDAM | 371.54 | 30.8853 | 114.75124362 |
| 2021-12-30 00:00:00 | Greece | BUTTER | 631.2392 | 30.8853 | 194.9601206376 |
| 2021-12-30 00:00:00 | Denmark | WHEYPOWDER | 122.0 | 30.8853 | 37.680066 |
| 2021-12-30 00:00:00 | Denmark | SMP | 345.0 | 30.8853 | 106.554285 |
| 2021-12-30 00:00:00 | Greece | CREAM | 251.9257 | 30.8853 | 77.8080082221 |
| 2021-12-30 00:00:00 | Denmark | BUTTER | 612.0 | 30.8853 | 189.018036 |
| 2021-12-30 00:00:00 | Croatia | DRINKING MILK | 50.4159 | 30.8853 | 15.5711019627 |
| 2021-12-30 00:00:00 | Greece | DRINKING MILK | 44.5815 | 30.8853 | 13.7691300195 |
| 2021-12-30 00:00:00 | France | EMMENTAL | 451.0 | 30.8853 | 139.292703 |
| 2021-12-30 00:00:00 | Italy | BUTTER | 519.61 | 30.8853 | 160.48310733 |
| 2021-12-30 00:00:00 | Finland | EMMENTAL | 655.141 | 30.8853 | 202.342263273 |
| 2021-12-30 00:00:00 | Greece | EDAM | 407.6109 | 30.8853 | 125.8918492977 |
| 2021-12-30 00:00:00 | France | BUTTER | 572.0 | 30.8853 | 176.663916 |
| 2021-12-30 00:00:00 | Italy | WMP | 372.36 | 30.8853 | 115.00450308 |
| 2021-12-30 00:00:00 | Italy | SMP | 297.58 | 30.8853 | 91.90847574 |
| 2021-12-30 00:00:00 | France | EDAM | 382.89 | 30.8853 | 118.25672517 |
| 2021-12-30 00:00:00 | Netherlands | BUTTER | 613.23 | 30.8853 | 189.39792519 |
| 2021-12-30 00:00:00 | Netherlands | WHEYPOWDER | 109.49 | 30.8853 | 33.81631497 |
| 2021-12-30 00:00:00 | Sweden | BUTTER | 574.3976 | 30.8853 | 177.4044219528 |

### sheet_eu_output_clean

| source | date | raw_product | product | standardized_type | brand | region | price | unit_ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EU | 2021-12-30 00:00:00 | WMP | Інше/невідомо | milk | nan | EU | 131.262525 | 1 |
| EU | 2021-12-30 00:00:00 | EMMENTAL | Сир твердий | hard_cheese | nan | EU | 161.956644993 | 1 |
| EU | 2021-12-30 00:00:00 | SMP | Інше/невідомо | milk | nan | EU | 103.64797827 | 1 |
| EU | 2021-12-30 00:00:00 | DRINKING MILK | Молоко питне | milk | nan | EU | 21.449223144 | 1 |
| EU | 2021-12-30 00:00:00 | WMP | Інше/невідомо | milk | nan | EU | 131.880231 | 1 |
| EU | 2021-12-30 00:00:00 | WMP | Інше/невідомо | milk | nan | EU | 129.83253561 | 1 |
| EU | 2021-12-30 00:00:00 | EDAM | Сир твердий | hard_cheese | nan | EU | 114.75124362 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter | nan | EU | 194.9601206376 | 1 |
| EU | 2021-12-30 00:00:00 | WHEYPOWDER | Інше/невідомо | other | nan | EU | 37.680066 | 1 |
| EU | 2021-12-30 00:00:00 | SMP | Інше/невідомо | milk | nan | EU | 106.554285 | 1 |
| EU | 2021-12-30 00:00:00 | CREAM | Вершки | cream | nan | EU | 77.8080082221 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter | nan | EU | 189.018036 | 1 |
| EU | 2021-12-30 00:00:00 | DRINKING MILK | Молоко питне | milk | nan | EU | 15.5711019627 | 1 |
| EU | 2021-12-30 00:00:00 | DRINKING MILK | Молоко питне | milk | nan | EU | 13.7691300195 | 1 |
| EU | 2021-12-30 00:00:00 | EMMENTAL | Сир твердий | hard_cheese | nan | EU | 139.292703 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter | nan | EU | 160.48310733 | 1 |
| EU | 2021-12-30 00:00:00 | EMMENTAL | Сир твердий | hard_cheese | nan | EU | 202.342263273 | 1 |
| EU | 2021-12-30 00:00:00 | EDAM | Сир твердий | hard_cheese | nan | EU | 125.8918492977 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter | nan | EU | 176.663916 | 1 |
| EU | 2021-12-30 00:00:00 | WMP | Інше/невідомо | milk | nan | EU | 115.00450308 | 1 |
| EU | 2021-12-30 00:00:00 | SMP | Інше/невідомо | milk | nan | EU | 91.90847574 | 1 |
| EU | 2021-12-30 00:00:00 | EDAM | Сир твердий | hard_cheese | nan | EU | 118.25672517 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter | nan | EU | 189.39792519 | 1 |
| EU | 2021-12-30 00:00:00 | WHEYPOWDER | Інше/невідомо | other | nan | EU | 33.81631497 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter | nan | EU | 177.4044219528 | 1 |

### sheet_eu_output_daily_variants

| source | date | product | standardized_type | brand | region | unit_ok | price_real | price_linear | price_pchip | imputed_flag_linear | imputed_flag_pchip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EU | 2021-12-30 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 108.8686868344615 | nan | nan | 0 | 0 |
| EU | 2021-12-31 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 109.4731006771231 | nan | nan | 0 | 0 |
| EU | 2022-01-01 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | nan | nan | nan | 0 | 0 |
| EU | 2022-01-02 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | nan | nan | nan | 0 | 0 |
| EU | 2022-01-03 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 109.5902995912 | nan | nan | 0 | 0 |
| EU | 2022-01-04 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 110.5836740643407 | nan | nan | 0 | 0 |
| EU | 2022-01-05 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 111.1243538713648 | nan | nan | 0 | 0 |
| EU | 2022-01-06 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 113.145457423847 | nan | nan | 0 | 0 |
| EU | 2022-01-07 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 113.9767274207458 | nan | nan | 0 | 0 |
| EU | 2022-01-08 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | nan | nan | nan | 0 | 0 |
| EU | 2022-01-09 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | nan | nan | nan | 0 | 0 |
| EU | 2022-01-10 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 114.1263676146353 | nan | nan | 0 | 0 |
| EU | 2022-01-11 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 115.2954956809462 | nan | nan | 0 | 0 |
| EU | 2022-01-12 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 116.7419322272605 | nan | nan | 0 | 0 |
| EU | 2022-01-13 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 117.5147461572441 | nan | nan | 0 | 0 |
| EU | 2022-01-14 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 118.0340030014378 | nan | nan | 0 | 0 |
| EU | 2022-01-15 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | nan | nan | nan | 0 | 0 |
| EU | 2022-01-16 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | nan | nan | nan | 0 | 0 |
| EU | 2022-01-17 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 120.2732265383751 | nan | nan | 0 | 0 |
| EU | 2022-01-18 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 120.0750681197868 | nan | nan | 0 | 0 |
| EU | 2022-01-19 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 120.2901482572542 | nan | nan | 0 | 0 |
| EU | 2022-01-20 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 119.1292245894737 | nan | nan | 0 | 0 |
| EU | 2022-01-21 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 119.195024283438 | nan | nan | 0 | 0 |
| EU | 2022-01-22 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | nan | nan | nan | 0 | 0 |
| EU | 2022-01-23 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | nan | nan | nan | 0 | 0 |

### sheet_eu_output_series_long

| source | date | product | standardized_type | brand | region | unit_ok | imputed_flag_linear | imputed_flag_pchip | series_variant | price |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EU | 2021-12-30 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 108.8686868344615 |
| EU | 2021-12-31 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 109.4731006771231 |
| EU | 2022-01-03 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 109.5902995912 |
| EU | 2022-01-04 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 110.5836740643407 |
| EU | 2022-01-05 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 111.1243538713648 |
| EU | 2022-01-06 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 113.145457423847 |
| EU | 2022-01-07 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 113.9767274207458 |
| EU | 2022-01-10 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 114.1263676146353 |
| EU | 2022-01-11 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 115.2954956809462 |
| EU | 2022-01-12 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 116.7419322272605 |
| EU | 2022-01-13 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 117.5147461572441 |
| EU | 2022-01-14 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 118.0340030014378 |
| EU | 2022-01-17 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 120.2732265383751 |
| EU | 2022-01-18 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 120.0750681197868 |
| EU | 2022-01-19 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 120.2901482572542 |
| EU | 2022-01-20 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 119.1292245894737 |
| EU | 2022-01-21 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 119.195024283438 |
| EU | 2022-01-24 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 121.4136080202381 |
| EU | 2022-01-25 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 121.3937805726786 |
| EU | 2022-01-26 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 121.6117407669474 |
| EU | 2022-01-27 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 124.4467614592375 |
| EU | 2022-01-28 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 124.0176394512143 |
| EU | 2022-01-31 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 124.4681559196137 |
| EU | 2022-02-01 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 125.5990931256428 |
| EU | 2022-02-02 00:00:00 | Інше/невідомо | milk | nan | EU | 1 | 0 | 0 | real | 125.7509853663512 |

### sheet_eu_output_descriptive_sta

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EU | Інше/невідомо | milk | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Інше/невідомо | other | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Інше/невідомо | milk | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Інше/невідомо | other | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Інше/невідомо | milk | real | 1056 | 422 | nan | 145.5713844824186 | 143.5145045326531 | 13.12532335471551 | 108.8686868344615 | 173.1958424824382 |
| EU | Інше/невідомо | other | real | 1056 | 422 | nan | 38.61538936091711 | 38.88307282382223 | 6.463929396161851 | 26.65921548536191 | 54.7422377803375 |
| EU | Вершки | cream | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Вершки | cream | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Вершки | cream | real | 1056 | 422 | nan | 119.0249904616937 | 117.4142734017543 | 22.77928774681182 | 81.89986716652001 | 181.6668040306586 |
| EU | Масло вершкове | butter | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Масло вершкове | butter | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Масло вершкове | butter | real | 1056 | 422 | nan | 262.9237601247224 | 251.9226003141099 | 59.42768694669505 | 175.2584538838545 | 373.9823955045714 |
| EU | Молоко питне | milk | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Молоко питне | milk | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Молоко питне | milk | real | 1056 | 422 | nan | 28.47336780969231 | 29.61835854276786 | 5.142849814691726 | 15.82923688791429 | 35.88047252341785 |
| EU | Сир твердий | hard_cheese | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Сир твердий | hard_cheese | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Сир твердий | hard_cheese | real | 1056 | 422 | nan | 219.8813250975299 | 218.4587064567793 | 32.51664390005512 | 140.4656936026071 | 274.4434278616792 |

### sheet_eu_output_tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EU | Інше/невідомо | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Інше/невідомо | other | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Інше/невідомо | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Інше/невідомо | other | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Інше/невідомо | milk | real | 212 | 0.1375577808090852 | 0.04767494944231181 | 0.003208166320694938 | 0.4179724856464668 | 0.4139138885848699 | 0.0 | 1 |
| EU | Інше/невідомо | other | real | 212 | 0.9861719556426081 | 0.01 | 0.003524788676604497 | 0.07712628004803797 | 0.07772589510508592 | 0.0 | 1 |
| EU | Вершки | cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Вершки | cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Вершки | cream | real | 212 | 0.5600203781682339 | 0.01 | 0.3439540555164848 | 0.01757955963866158 | 5.977080082142637e-05 | 1.631394383403082e-120 | 1 |
| EU | Масло вершкове | butter | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Масло вершкове | butter | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Масло вершкове | butter | real | 212 | 0.5267216667834979 | 0.01 | 1.629386794131169e-08 | 0.8578364022171017 | 0.3243735121326423 | 0.0 | 1 |
| EU | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Молоко питне | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Молоко питне | milk | real | 212 | 0.219904832363445 | 0.01 | 0.0289261007750083 | 0.4799404146228307 | 0.7065882516933683 | 0.0 | 1 |
| EU | Сир твердий | hard_cheese | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Сир твердий | hard_cheese | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Сир твердий | hard_cheese | real | 212 | 0.2161728016525135 | 0.01 | 0.5648061329308757 | 0.8550093177818229 | 0.4357472453890435 | 0.0 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_eu/sheet_eu_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_eu/sheet_eu_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_eu/sheet_eu_timeseries_by_standardized_type.png
