# RW3 Separate Sheet Module - Novus

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
- Source sheet: Novus
- Rows (clean): 1530
- Date range: 2025-11-04 .. 2026-01-08
- Products: 9
- Stats rows: 36
- Tests rows: 36
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | sku_id | timestamp | date | title | raw_product | product | standardized_type | brand | region | price_current | price_old |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | cир ilchester з журавлиною 43% | 2025-11-04 19:45:35.319000 | 2025-11-04 00:00:00 | Cир Ilchester з журавлиною 43% | Інше | Інше/невідомо | other | Cир | Україна | 1199.0 | nan |
| Novus | cир ilchester з шоколадом і апельсином 42% | 2025-11-04 19:45:35.825000 | 2025-11-04 00:00:00 | Cир Ilchester з шоколадом і апельсином 42% | Інше | Інше/невідомо | other | Cир | Україна | 1199.0 | nan |
| Novus | cир ilchester чеддер з ароматом копченого яблука 54% | 2025-11-04 19:45:36.039000 | 2025-11-04 00:00:00 | Cир Ilchester Чеддер з ароматом копченого яблука 54% | Сир | Сир твердий | hard_cheese | Cир | Україна | 1089.0 | nan |
| Novus | cир paturages comtois брі 60% 130г | 2025-11-04 19:45:35.780000 | 2025-11-04 00:00:00 | Cир Paturages Comtois Брі 60% 130г | Інше | Інше/невідомо | other | Cир | Україна | 179.0 | nan |
| Novus | cир prego pomadore piccante твердий 45% | 2025-11-04 19:45:35.277000 | 2025-11-04 00:00:00 | Cир Prego Pomadore piccante твердий 45% | Сир | Сир твердий | hard_cheese | Cир | Україна | 469.0 | nan |
| Novus | cир запечений alpenhain камамбер та соус із журавлини 57% 200г | 2025-11-04 19:45:36.018000 | 2025-11-04 00:00:00 | Cир запечений Alpenhain Камамбер та соус із журавлини 57% 200г | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Cир | Україна | 249.0 | nan |
| Novus | айран onur турецький безлактозний 1,8% 500мл | 2025-11-04 19:45:35.725000 | 2025-11-04 00:00:00 | Айран Onur Турецький безлактозний 1,8% 500мл | Масло вершкове | Масло вершкове | butter | Айран | Україна | 62.99 | nan |
| Novus | айран onur турецький свіжа м'ята 1,8% 500мл | 2025-11-04 19:45:35.861000 | 2025-11-04 00:00:00 | Айран Onur Турецький Свіжа м'ята 1,8% 500мл | Інше | Інше/невідомо | other | Айран | Україна | 62.99 | nan |
| Novus | айран онур турецький 1,8% 0,5л | 2025-11-04 19:45:35.678000 | 2025-11-04 00:00:00 | Айран Онур Турецький 1,8% 0,5л | Інше | Інше/невідомо | other | Айран | Україна | 49.49 | nan |
| Novus | айран яготинський з базиліком 1,8% 450г | 2025-11-04 19:45:35.786000 | 2025-11-04 00:00:00 | Айран Яготинський з базиліком 1,8% 450г | Сметана | Сметана | sour_cream | Айран | Україна | 29.99 | nan |
| Novus | айран яготинський з кропом 1,8% 850г | 2025-11-04 19:45:35.545000 | 2025-11-04 00:00:00 | Айран Яготинський з кропом 1,8% 850г | Інше | Інше/невідомо | other | Айран | Україна | 64.99 | nan |
| Novus | біфідойогурт danone активіа білий 2,4% 165г | 2025-11-04 19:45:35.387000 | 2025-11-04 00:00:00 | Біфідойогурт Danone Активіа Білий 2,4% 165г | Йогурт | Йогурт | yogurt_dessert | Danone | Україна | 26.49 | nan |
| Novus | біфідойогурт zinka з козячого молока без наповнювача 2,8% 300г | 2025-11-04 19:45:36.092000 | 2025-11-04 00:00:00 | Біфідойогурт Zinka з козячого молока без наповнювача 2,8% 300г | Йогурт | Йогурт | yogurt_dessert | Zinka | Україна | 34.99 | nan |
| Novus | біфідойогурт zinka з козячого молока зі смаком злаків 2,8% 300г | 2025-11-04 19:45:36.022000 | 2025-11-04 00:00:00 | Біфідойогурт Zinka з козячого молока зі смаком злаків 2,8% 300г | Йогурт | Йогурт | yogurt_dessert | Zinka | Україна | 34.99 | nan |
| Novus | біфідойогурт zinka з козячого молока зі смаком персика та маракуйї 2,8% 300г | 2025-11-04 19:45:35.722000 | 2025-11-04 00:00:00 | Біфідойогурт Zinka з козячого молока зі смаком персика та маракуйї 2,8% 300г | Йогурт | Йогурт | yogurt_dessert | Zinka | Україна | 34.49 | nan |
| Novus | біфідойогурт zinka з козячого молока зі смаком полуниці 2,8% 300г | 2025-11-04 19:45:35.891000 | 2025-11-04 00:00:00 | Біфідойогурт Zinka з козячого молока зі смаком полуниці 2,8% 300г | Йогурт | Йогурт | yogurt_dessert | Zinka | Україна | 34.49 | nan |
| Novus | біфідойогурт активіа 5 злаків 1,5% 290г | 2025-11-04 19:45:35.265000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа 5 злаків 1,5% 290г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 80.99 | nan |
| Novus | біфідойогурт активіа 5 злаків 1,5% 800г | 2025-11-04 19:45:36.101000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа 5 злаків 1,5% 800г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 80.99 | nan |
| Novus | біфідойогурт активіа абрикос-злаки 1,2% 500г | 2025-11-04 19:45:35.502000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа Абрикос-злаки 1,2% 500г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 59.99 | nan |
| Novus | біфідойогурт активіа ананас 1,5% 290г | 2025-11-04 19:45:35.731000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа Ананас 1,5% 290г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 80.99 | nan |
| Novus | біфідойогурт активіа ананас 1,5% 800г | 2025-11-04 19:45:35.293000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа ананас 1,5% 800г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 80.99 | nan |
| Novus | біфідойогурт активіа банан-ківі безлактозний 0,8% 260г | 2025-11-04 19:45:35.301000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа Банан-ківі безлактозний 0,8% 260г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 38.79 | nan |
| Novus | біфідойогурт активіа без лактози 0,9% 260г | 2025-11-04 19:45:35.438000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа Без лактози 0,9% 260г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 38.79 | nan |
| Novus | біфідойогурт активіа без цукру 1,5% 260г | 2025-11-04 19:45:35.699000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа без цукру 1,5% 260г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 33.99 | nan |
| Novus | біфідойогурт активіа білий без цукру безлактозний 0,9% 290г | 2025-11-04 19:45:35.522000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа білий без цукру безлактозний 0,9% 290г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 38.79 | nan |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | Інше/невідомо | milk | linear | 0 | 68 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | other | linear | 0 | 595 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | yogurt_dessert | linear | 0 | 4 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | milk | pchip | 0 | 68 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | other | pchip | 0 | 595 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | yogurt_dessert | pchip | 0 | 4 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | milk | real | 5 | 63 | nan | 83.39165891472868 | 79.98666666666666 | 8.214346846934783 | 73.32000000000001 | 93.01162790697674 |
| Novus | Інше/невідомо | other | real | 50 | 545 | nan | 308.4193055571029 | 108.73397058823531 | 578.8244318973653 | 3.6495 | 3517.647058823529 |
| Novus | Інше/невідомо | yogurt_dessert | real | 4 | 0 | nan | 653.520688405797 | 423.25333333333333 | 565.143920198352 | 273.8260869565217 | 1493.75 |
| Novus | Вершки | cream | linear | 0 | 1044 | nan | nan | nan | nan | nan | nan |
| Novus | Вершки | cream | pchip | 0 | 1044 | nan | nan | nan | nan | nan | nan |
| Novus | Вершки | cream | real | 83 | 961 | nan | 417.6976886882837 | 353.2666666666667 | 341.91679788760206 | 37.66166666666666 | 1811.975 |
| Novus | Йогурт | milk | linear | 0 | 2 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | yogurt_dessert | linear | 0 | 894 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | milk | pchip | 0 | 2 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | yogurt_dessert | pchip | 0 | 894 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | milk | real | 2 | 0 | nan | 239.11916666666667 | 239.11916666666667 | 192.8126985826458 | 102.78 | 375.4583333333333 |
| Novus | Йогурт | yogurt_dessert | real | 74 | 820 | nan | 1265.2588180857383 | 156.4776984126984 | 9278.627528617262 | 62.47499999999999 | 79999.99875 |
| Novus | Кефір | milk | linear | 0 | 87 | nan | nan | nan | nan | nan | nan |
| Novus | Кефір | milk | pchip | 0 | 87 | nan | nan | nan | nan | nan | nan |
| Novus | Кефір | milk | real | 17 | 70 | nan | 75.0878285425316 | 75.28235294117647 | 10.790986388770849 | 56.99 | 92.21111111111111 |
| Novus | Масло вершкове | butter | linear | 0 | 938 | nan | nan | nan | nan | nan | nan |
| Novus | Масло вершкове | butter | pchip | 0 | 938 | nan | nan | nan | nan | nan | nan |
| Novus | Масло вершкове | butter | real | 69 | 869 | nan | 524.8726224460459 | 544.3888888888889 | 345.0101656523798 | 73.67368421052632 | 1592.0 |
| Novus | Молоко питне | milk | linear | 0 | 770 | nan | nan | nan | nan | nan | nan |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | Інше/невідомо | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | other | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | yogurt_dessert | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | other | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | yogurt_dessert | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | milk | real | 3 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | other | real | 5 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | yogurt_dessert | real | 2 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Вершки | cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Вершки | cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Вершки | cream | real | 9 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | yogurt_dessert | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | yogurt_dessert | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | milk | real | 1 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | yogurt_dessert | real | 9 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Кефір | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Кефір | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Кефір | milk | real | 5 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Масло вершкове | butter | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Масло вершкове | butter | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Масло вершкове | butter | real | 9 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_brand_trends.png
