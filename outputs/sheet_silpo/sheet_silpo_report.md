# RW4 Sheet Module - Silpo

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
- Source sheet: Silpo
- Rows (clean): 86765
- Date range: 2025-10-21 .. 2025-12-13
- Products: 8
- Stats rows: 24
- Tests rows: 24
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | sku_id | timestamp | date | title | raw_product | product | standardized_type | brand | region | price_current | price_old |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-22 00:00:00 | 2025-10-22 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-23 00:00:00 | 2025-10-23 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-24 00:00:00 | 2025-10-24 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-25 00:00:00 | 2025-10-25 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-26 00:00:00 | 2025-10-26 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-27 00:00:00 | 2025-10-27 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-28 00:00:00 | 2025-10-28 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-29 00:00:00 | 2025-10-29 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-30 00:00:00 | 2025-10-30 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 1.0 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-31 00:00:00 | 2025-10-31 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-01 00:00:00 | 2025-11-01 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-02 00:00:00 | 2025-11-02 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-03 00:00:00 | 2025-11-03 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-04 00:00:00 | 2025-11-04 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-05 00:00:00 | 2025-11-05 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-06 00:00:00 | 2025-11-06 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-07 00:00:00 | 2025-11-07 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-08 00:00:00 | 2025-11-08 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-09 00:00:00 | 2025-11-09 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-10 00:00:00 | 2025-11-10 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-11 00:00:00 | 2025-11-11 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-12 00:00:00 | 2025-11-12 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-13 00:00:00 | 2025-11-13 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-11-18 00:00:00 | 2025-11-18 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.79 | nan |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | Інше/невідомо | other | linear | 0 | 1836 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | other | pchip | 0 | 1836 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | other | real | 1628 | 208 | nan | 43.06194529940628 | 27.724999999999998 | 47.99737539014726 | 0.6995 | 370.845 |
| Silpo | Вершки | cream | linear | 0 | 4157 | nan | nan | nan | nan | nan | nan |
| Silpo | Вершки | cream | pchip | 0 | 4157 | nan | nan | nan | nan | nan | nan |
| Silpo | Вершки | cream | real | 3678 | 479 | nan | 83.60262824475473 | 61.99 | 73.33029560393057 | 0.5788421052631579 | 499.0 |
| Silpo | Йогурт | yogurt_dessert | linear | 0 | 3861 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | yogurt_dessert | pchip | 0 | 3861 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | yogurt_dessert | real | 3395 | 466 | nan | 64.37508890427884 | 57.489999999999995 | 34.38121705364969 | 3.4995 | 479.0 |
| Silpo | Кефір | milk | linear | 0 | 1809 | nan | nan | nan | nan | nan | nan |
| Silpo | Кефір | milk | pchip | 0 | 1809 | nan | nan | nan | nan | nan | nan |
| Silpo | Кефір | milk | real | 1584 | 225 | nan | 65.57400621567861 | 53.656666666666666 | 54.57425548622439 | 2.816666666666666 | 469.0 |
| Silpo | Молоко питне | milk | linear | 0 | 3997 | nan | nan | nan | nan | nan | nan |
| Silpo | Молоко питне | milk | pchip | 0 | 3997 | nan | nan | nan | nan | nan | nan |
| Silpo | Молоко питне | milk | real | 3524 | 473 | nan | 70.9883540152093 | 62.013666666666666 | 43.13652808916007 | 2.816666666666666 | 479.0 |
| Silpo | Сир кисломолочний | cottage_cheese | linear | 0 | 2072 | nan | nan | nan | nan | nan | nan |
| Silpo | Сир кисломолочний | cottage_cheese | pchip | 0 | 2072 | nan | nan | nan | nan | nan | nan |
| Silpo | Сир кисломолочний | cottage_cheese | real | 1819 | 253 | nan | 63.06207197995849 | 56.83428571428572 | 32.49807489562772 | 16.413666666666668 | 299.0 |
| Silpo | Сир твердий | hard_cheese | linear | 0 | 2063 | nan | nan | nan | nan | nan | nan |
| Silpo | Сир твердий | hard_cheese | pchip | 0 | 2063 | nan | nan | nan | nan | nan | nan |
| Silpo | Сир твердий | hard_cheese | real | 1815 | 248 | nan | 69.26856992211718 | 56.489999999999995 | 56.29740177971621 | 0.5788421052631579 | 699.0 |
| Silpo | Сметана | sour_cream | linear | 0 | 2325 | nan | nan | nan | nan | nan | nan |
| Silpo | Сметана | sour_cream | pchip | 0 | 2325 | nan | nan | nan | nan | nan | nan |
| Silpo | Сметана | sour_cream | real | 2065 | 260 | nan | 64.9251575611023 | 55.49 | 46.52442140804871 | 5.966666666666666 | 479.0 |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | Інше/невідомо | other | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | other | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | other | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Вершки | cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Вершки | cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Вершки | cream | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | yogurt_dessert | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | yogurt_dessert | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | yogurt_dessert | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Кефір | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Кефір | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Кефір | milk | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Молоко питне | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Молоко питне | milk | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сир кисломолочний | cottage_cheese | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сир кисломолочний | cottage_cheese | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сир кисломолочний | cottage_cheese | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сир твердий | hard_cheese | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сир твердий | hard_cheese | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сир твердий | hard_cheese | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сметана | sour_cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сметана | sour_cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Сметана | sour_cream | real | 8 | nan | nan | nan | nan | nan | nan | 0 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_brand_trends.png
