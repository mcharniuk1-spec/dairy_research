# RW3 Separate Sheet Module - EU

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
- Source sheet: Europe
- Rows (clean): 111299
- Date range: 2021-12-30 .. 2026-01-15
- Products: 5
- Stats rows: 18
- Tests rows: 18
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | date | raw_product | product | standardized_type | brand | region | price | unit_ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EU | 2021-12-30 00:00:00 | WMP | Інше/невідомо | milk |  | EU | 131.262525 | 1 |
| EU | 2021-12-30 00:00:00 | EMMENTAL | Сир твердий | hard_cheese |  | EU | 161.956644993 | 1 |
| EU | 2021-12-30 00:00:00 | SMP | Інше/невідомо | milk |  | EU | 103.64797827 | 1 |
| EU | 2021-12-30 00:00:00 | DRINKING MILK | Молоко питне | milk |  | EU | 21.449223144 | 1 |
| EU | 2021-12-30 00:00:00 | WMP | Інше/невідомо | milk |  | EU | 131.880231 | 1 |
| EU | 2021-12-30 00:00:00 | WMP | Інше/невідомо | milk |  | EU | 129.83253561 | 1 |
| EU | 2021-12-30 00:00:00 | EDAM | Сир твердий | hard_cheese |  | EU | 114.75124362 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter |  | EU | 194.9601206376 | 1 |
| EU | 2021-12-30 00:00:00 | WHEYPOWDER | Інше/невідомо | other |  | EU | 37.680066 | 1 |
| EU | 2021-12-30 00:00:00 | SMP | Інше/невідомо | milk |  | EU | 106.554285 | 1 |
| EU | 2021-12-30 00:00:00 | CREAM | Вершки | cream |  | EU | 77.8080082221 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter |  | EU | 189.018036 | 1 |
| EU | 2021-12-30 00:00:00 | DRINKING MILK | Молоко питне | milk |  | EU | 15.5711019627 | 1 |
| EU | 2021-12-30 00:00:00 | DRINKING MILK | Молоко питне | milk |  | EU | 13.7691300195 | 1 |
| EU | 2021-12-30 00:00:00 | EMMENTAL | Сир твердий | hard_cheese |  | EU | 139.292703 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter |  | EU | 160.48310733 | 1 |
| EU | 2021-12-30 00:00:00 | EMMENTAL | Сир твердий | hard_cheese |  | EU | 202.342263273 | 1 |
| EU | 2021-12-30 00:00:00 | EDAM | Сир твердий | hard_cheese |  | EU | 125.8918492977 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter |  | EU | 176.663916 | 1 |
| EU | 2021-12-30 00:00:00 | WMP | Інше/невідомо | milk |  | EU | 115.00450308 | 1 |
| EU | 2021-12-30 00:00:00 | SMP | Інше/невідомо | milk |  | EU | 91.90847574 | 1 |
| EU | 2021-12-30 00:00:00 | EDAM | Сир твердий | hard_cheese |  | EU | 118.25672517 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter |  | EU | 189.39792519 | 1 |
| EU | 2021-12-30 00:00:00 | WHEYPOWDER | Інше/невідомо | other |  | EU | 33.81631497 | 1 |
| EU | 2021-12-30 00:00:00 | BUTTER | Масло вершкове | butter |  | EU | 177.4044219528 | 1 |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EU | Інше/невідомо | milk | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Інше/невідомо | other | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Інше/невідомо | milk | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Інше/невідомо | other | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Інше/невідомо | milk | real | 1056 | 422 | nan | 145.57138448241855 | 143.51450453265312 | 13.12532335471551 | 108.86868683446154 | 173.19584248243817 |
| EU | Інше/невідомо | other | real | 1056 | 422 | nan | 38.615389360917106 | 38.88307282382223 | 6.463929396161851 | 26.65921548536191 | 54.742237780337504 |
| EU | Вершки | cream | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Вершки | cream | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Вершки | cream | real | 1056 | 422 | nan | 119.0249904616937 | 117.41427340175431 | 22.779287746811825 | 81.89986716652001 | 181.66680403065857 |
| EU | Масло вершкове | butter | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Масло вершкове | butter | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Масло вершкове | butter | real | 1056 | 422 | nan | 262.92376012472243 | 251.9226003141099 | 59.42768694669505 | 175.25845388385454 | 373.9823955045714 |
| EU | Молоко питне | milk | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Молоко питне | milk | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Молоко питне | milk | real | 1056 | 422 | nan | 28.473367809692313 | 29.618358542767858 | 5.142849814691726 | 15.829236887914286 | 35.88047252341785 |
| EU | Сир твердий | hard_cheese | linear | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Сир твердий | hard_cheese | pchip | 0 | 1478 | nan | nan | nan | nan | nan | nan |
| EU | Сир твердий | hard_cheese | real | 1056 | 422 | nan | 219.88132509752987 | 218.45870645677925 | 32.51664390005512 | 140.46569360260713 | 274.4434278616792 |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EU | Інше/невідомо | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Інше/невідомо | other | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Інше/невідомо | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Інше/невідомо | other | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Інше/невідомо | milk | real | 212 | 0.1375577808090852 | 0.047674949442311806 | 0.0032081663206949378 | 0.41797248564646683 | 0.4139138885848699 | 0.0 | 1 |
| EU | Інше/невідомо | other | real | 212 | 0.9861719556426081 | 0.01 | 0.0035247886766044973 | 0.07712628004803797 | 0.07772589510508592 | 0.0 | 1 |
| EU | Вершки | cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Вершки | cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Вершки | cream | real | 212 | 0.5600203781682339 | 0.01 | 0.34395405551648484 | 0.017579559638661577 | 5.977080082142637e-05 | 1.6313943834030816e-120 | 1 |
| EU | Масло вершкове | butter | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Масло вершкове | butter | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Масло вершкове | butter | real | 212 | 0.5267216667834979 | 0.01 | 1.6293867941311686e-08 | 0.8578364022171017 | 0.32437351213264226 | 0.0 | 1 |
| EU | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Молоко питне | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Молоко питне | milk | real | 212 | 0.219904832363445 | 0.01 | 0.0289261007750083 | 0.47994041462283066 | 0.7065882516933683 | 0.0 | 1 |
| EU | Сир твердий | hard_cheese | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Сир твердий | hard_cheese | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| EU | Сир твердий | hard_cheese | real | 212 | 0.2161728016525135 | 0.01 | 0.5648061329308757 | 0.8550093177818229 | 0.4357472453890435 | 0.0 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_eu/sheet_eu_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_eu/sheet_eu_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_eu/sheet_eu_distribution.png
