# RW4 Sheet Module - Novus

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
- Stats rows: 27
- Tests rows: 27
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | sku_id | timestamp | date | title | raw_product | product | standardized_type | brand | region | price_current | price_old |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | cир ilchester з журавлиною 43% | 2025-11-04 19:45:35.319000 | 2025-11-04 00:00:00 | Cир Ilchester з журавлиною 43% | Інше | Інше/невідомо | other | Cир | Україна | 1199.0 | nan |
| Novus | cир ilchester з шоколадом і апельсином 42% | 2025-11-04 19:45:35.825000 | 2025-11-04 00:00:00 | Cир Ilchester з шоколадом і апельсином 42% | Інше | Інше/невідомо | other | Cир | Україна | 1199.0 | nan |
| Novus | cир ilchester чеддер з ароматом копченого яблука 54% | 2025-11-04 19:45:36.039000 | 2025-11-04 00:00:00 | Cир Ilchester Чеддер з ароматом копченого яблука 54% | Сир | Сир твердий | hard_cheese | Cир | Україна | 1089.0 | nan |
| Novus | cир paturages comtois брі 60% 130г | 2025-11-04 19:45:35.780000 | 2025-11-04 00:00:00 | Cир Paturages Comtois Брі 60% 130г | Інше | Інше/невідомо | other | Cир | Україна | 179.0 | nan |
| Novus | cир prego mozzarella сarmela розсольний 45% 125г | 2026-01-08 13:25:16.123000 | 2026-01-08 00:00:00 | Cир Prego Mozzarella Сarmela розсольний 45% 125г | Сир | Сир твердий | hard_cheese | Cир | Україна | 49.99 | nan |
| Novus | cир prego pomadore piccante твердий 45% | 2025-11-04 19:45:35.277000 | 2025-11-04 00:00:00 | Cир Prego Pomadore piccante твердий 45% | Сир | Сир твердий | hard_cheese | Cир | Україна | 469.0 | nan |
| Novus | cир val de saone брі 60% 500г | 2026-01-08 13:25:16.211000 | 2026-01-08 00:00:00 | Cир Val de Saone Брі 60% 500г | Вершки | Вершки | cream | Cир | Україна | 389.0 | nan |
| Novus | cир запечений alpenhain камамбер та соус із журавлини 57% 200г | 2025-11-04 19:45:36.018000 | 2025-11-04 00:00:00 | Cир запечений Alpenhain Камамбер та соус із журавлини 57% 200г | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Cир | Україна | 249.0 | nan |
| Novus | айран onur турецький безлактозний 1,8% 500мл | 2025-11-04 19:45:35.725000 | 2025-11-04 00:00:00 | Айран Onur Турецький безлактозний 1,8% 500мл | Масло вершкове | Вершки | cream | Айран | Україна | 62.99 | nan |
| Novus | айран onur турецький свіжа м'ята 1,8% 500мл | 2025-11-04 19:45:35.861000 | 2025-11-04 00:00:00 | Айран Onur Турецький Свіжа м'ята 1,8% 500мл | Інше | Інше/невідомо | other | Айран | Україна | 62.99 | nan |
| Novus | айран онур турецький 1,8% 0,5л | 2025-11-04 19:45:35.678000 | 2025-11-04 00:00:00 | Айран Онур Турецький 1,8% 0,5л | Інше | Інше/невідомо | other | Айран | Україна | 49.49 | nan |
| Novus | айран онур турецький 1,8% 1л | 2026-01-08 13:25:16.072000 | 2026-01-08 00:00:00 | Айран Онур Турецький 1,8% 1л | Інше | Інше/невідомо | other | Айран | Україна | 68.99 | nan |
| Novus | айран онур турецький 1,8% 200г | 2025-11-05 13:53:27.347000 | 2025-11-05 00:00:00 | Айран Онур Турецький 1,8% 200г | Масло вершкове | Вершки | cream | Айран | Україна | 20.49 | nan |
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
| Novus | біфідойогурт активіа ананас 1,2% 260г | 2026-01-08 13:25:16.228000 | 2026-01-08 00:00:00 | Біфідойогурт Активіа Ананас 1,2% 260г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 36.79 | nan |
| Novus | біфідойогурт активіа ананас 1,5% 290г | 2025-11-04 19:45:35.731000 | 2025-11-04 00:00:00 | Біфідойогурт Активіа Ананас 1,5% 290г | Йогурт | Йогурт | yogurt_dessert | Активіа | Україна | 80.99 | nan |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | Інше/невідомо | other | linear | 0 | 595 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | other | pchip | 0 | 595 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | other | real | 50 | 545 | nan | 308.4193055571029 | 108.73397058823531 | 578.8244318973653 | 3.6495 | 3517.647058823529 |
| Novus | Вершки | cream | linear | 0 | 1683 | nan | nan | nan | nan | nan | nan |
| Novus | Вершки | cream | pchip | 0 | 1683 | nan | nan | nan | nan | nan | nan |
| Novus | Вершки | cream | real | 131 | 1552 | nan | 498.2859652257032 | 476.0 | 328.6917557705472 | 37.66166666666666 | 1811.975 |
| Novus | Йогурт | yogurt_dessert | linear | 0 | 979 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | yogurt_dessert | pchip | 0 | 979 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | yogurt_dessert | real | 84 | 895 | nan | 1166.1801394378008 | 163.0 | 8706.963508734492 | 62.47499999999999 | 79999.99875 |
| Novus | Кефір | milk | linear | 0 | 320 | nan | nan | nan | nan | nan | nan |
| Novus | Кефір | milk | pchip | 0 | 320 | nan | nan | nan | nan | nan | nan |
| Novus | Кефір | milk | real | 26 | 294 | nan | 81.30565361033958 | 79.42344827586206 | 14.173574554449727 | 62.21111111111111 | 124.05555555555559 |
| Novus | Масло вершкове | butter | linear | 0 | 1 | nan | nan | nan | nan | nan | nan |
| Novus | Масло вершкове | butter | pchip | 0 | 1 | nan | nan | nan | nan | nan | nan |
| Novus | Масло вершкове | butter | real | 1 | 0 | nan | 1592.0 | 1592.0 | 0.0 | 1592.0 | 1592.0 |
| Novus | Молоко питне | milk | linear | 0 | 1014 | nan | nan | nan | nan | nan | nan |
| Novus | Молоко питне | milk | pchip | 0 | 1014 | nan | nan | nan | nan | nan | nan |
| Novus | Молоко питне | milk | real | 91 | 923 | nan | 210.83802119587278 | 81.1 | 266.64860466840315 | 13.995 | 1566.333333333333 |
| Novus | Сир кисломолочний | cottage_cheese | linear | 0 | 680 | nan | nan | nan | nan | nan | nan |
| Novus | Сир кисломолочний | cottage_cheese | pchip | 0 | 680 | nan | nan | nan | nan | nan | nan |
| Novus | Сир кисломолочний | cottage_cheese | real | 62 | 618 | nan | 377.02179026832835 | 283.54285714285714 | 431.1027889083751 | 101.98 | 3390.0 |
| Novus | Сир твердий | hard_cheese | linear | 0 | 2987 | nan | nan | nan | nan | nan | nan |
| Novus | Сир твердий | hard_cheese | pchip | 0 | 2987 | nan | nan | nan | nan | nan | nan |
| Novus | Сир твердий | hard_cheese | real | 268 | 2719 | nan | 903.9736582903233 | 719.46 | 804.8128183586101 | 67.99 | 10990.0 |
| Novus | Сметана | sour_cream | linear | 0 | 395 | nan | nan | nan | nan | nan | nan |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | Інше/невідомо | other | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | other | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Інше/невідомо | other | real | 5 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Вершки | cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Вершки | cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Вершки | cream | real | 9 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | yogurt_dessert | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | yogurt_dessert | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Йогурт | yogurt_dessert | real | 9 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Кефір | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Кефір | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Кефір | milk | real | 5 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Масло вершкове | butter | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Масло вершкове | butter | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Масло вершкове | butter | real | 1 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Молоко питне | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Молоко питне | milk | real | 9 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Сир кисломолочний | cottage_cheese | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Сир кисломолочний | cottage_cheese | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Сир кисломолочний | cottage_cheese | real | 9 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Сир твердий | hard_cheese | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Сир твердий | hard_cheese | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Сир твердий | hard_cheese | real | 9 | nan | nan | nan | nan | nan | nan | 0 |
| Novus | Сметана | sour_cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_brand_trends.png
