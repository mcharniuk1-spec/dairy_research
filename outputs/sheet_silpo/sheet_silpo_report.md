# RW3 Separate Sheet Module - Silpo

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
- Products: 9
- Stats rows: 36
- Tests rows: 36
- Interpretation option: use tests table -> recommended_action/recommended_model_family per product.

## Tables

### clean

| source | sku_id | timestamp | date | title | raw_product | product | standardized_type | brand | region | price_current | price_old |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | . ✓ власний імпорт ✓ заходьте і купуйте на сайті «сільпо»!"> | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | . ✓ Власний імпорт ✓ Заходьте і купуйте на сайті «Сільпо»!"> | Інше | Інше/невідомо | other | Сільпо | Україна | 8.99 | nan |
| Silpo | cир кисломолочний лавка традицій старий порицьк з топленого молока 9% | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Cир кисломолочний Лавка традицій Старий Порицьк з топленого молока 9% | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Cир | Україна | 77.99 | nan |
| Silpo | айран inek турецький 1,8% стакан | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Inek Турецький 1,8% стакан | Сметана | Сметана | sour_cream | Айран | Україна | 169.0 | nan |
| Silpo | айран inek турецький пляшка | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Inek Турецький пляшка | Вершки | Вершки | cream | Айран | Україна | 21.99 | nan |
| Silpo | айран inek турецький, пляшка | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Inek Турецький, пляшка | Вершки | Вершки | cream | Айран | Україна | 42.79 | nan |
| Silpo | айран onur «турецький» | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Onur «Турецький» | Інше | Інше/невідомо | other | Турецький | Україна | 30.69 | nan |
| Silpo | айран onur «турецький» 1,8% | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Onur «Турецький» 1,8% | Інше | Інше/невідомо | other | Турецький | Україна | 56.99 | nan |
| Silpo | айран onur «турецький» безлактозний | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Onur «Турецький» безлактозний | Масло вершкове | Масло вершкове | butter | Турецький | Україна | 45.39 | nan |
| Silpo | айран onur турецький безлактозний 1,8% пляшка | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Onur Турецький безлактозний 1,8% пляшка | Вершки | Вершки | cream | Айран | Україна | 99.0 | nan |
| Silpo | айран onur турецький свіжа м'ята 1,8% стакан | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Onur Турецький Свіжа м'ята 1,8% стакан | Сметана | Сметана | sour_cream | Айран | Україна | 61.49 | nan |
| Silpo | айран лавка традицій tasbio з молока буйволиць 3% | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Лавка традицій TASbio з молока буйволиць 3% | Молоко питне | Молоко питне | milk | Айран | Україна | 89.99 | nan |
| Silpo | айран міськмолзавод №1 1% | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Міськмолзавод №1 1% | Інше | Інше/невідомо | other | Айран | Україна | 19.99 | nan |
| Silpo | айран селянський 1,8% пет | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Селянський 1,8% пет | Масло вершкове | Масло вершкове | butter | Айран | Україна | 26.99 | nan |
| Silpo | айран селянський з огірком та кропом 1,6% пет | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Селянський з огірком та кропом 1,6% пет | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Айран | Україна | 54.99 | nan |
| Silpo | айран яготинський з кропом 1,8% | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Яготинський з кропом 1,8% | Інше | Інше/невідомо | other | Айран | Україна | 13.99 | nan |
| Silpo | айран яготинський класичний 2% пет | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Яготинський Класичний 2% пет | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Айран | Україна | 64.99 | nan |
| Silpo | айран яготинський традиційний 2% п/е | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Яготинський Традиційний 2% п/е | Інше | Інше/невідомо | other | Айран | Україна | 43.99 | nan |
| Silpo | айран яготинський традиційний 2% стакан | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Яготинський Традиційний 2% стакан | Сметана | Сметана | sour_cream | Айран | Україна | 92.99 | nan |
| Silpo | батончики творожні «злагода» шоколадні з ароматом карамелі 23% | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Батончики творожні «Злагода» шоколадні з ароматом карамелі 23% | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Злагода | Україна | 159.0 | nan |
| Silpo | батончики творожні злагода карамель та пломбір 23% | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Батончики творожні Злагода карамель та пломбір 23% | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Злагода | Україна | 144.0 | nan |
| Silpo | білок яєчний курячий «ясенсвіт» пастеризований | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Білок яєчний курячий «Ясенсвіт» пастеризований | Яйця курячі | Інше/невідомо | other | Ясенсвіт | Україна | 20.59 | nan |
| Silpo | бісквіт bakoma сатіно з какао і горіховою начинкою | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Бісквіт Bakoma Сатіно з какао і горіховою начинкою | Інше | Інше/невідомо | other | Бісквіт | Україна | 39.99 | nan |
| Silpo | бісквіт bakoma сатіно з какао і молочною начинкою | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Бісквіт Bakoma Сатіно з какао і молочною начинкою | Інше | Інше/невідомо | other | Бісквіт | Україна | 39.9 | nan |
| Silpo | бісквіт milino choco nut з горіховим кремом | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Бісквіт Milino Choco Nut з горіховим кремом | Інше | Інше/невідомо | other | Бісквіт | Україна | 469.0 | nan |
| Silpo | бісквіт milino з молочним кремом у шоколадній глазурі | 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Бісквіт Milino з молочним кремом у шоколадній глазурі | Інше | Інше/невідомо | other | Бісквіт | Україна | 19.9 | nan |

### descriptive_stats

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | Інше/невідомо | milk | linear | 0 | 515 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | other | linear | 0 | 1836 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | yogurt_dessert | linear | 0 | 624 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | milk | pchip | 0 | 515 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | other | pchip | 0 | 1836 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | yogurt_dessert | pchip | 0 | 624 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | milk | real | 437 | 78 | nan | 58.86474599542335 | 48.32 | 32.291222802674014 | 5.633333333333333 | 209.495 |
| Silpo | Інше/невідомо | other | real | 1628 | 208 | nan | 43.06194529940628 | 27.724999999999998 | 47.99737539014726 | 0.6995 | 370.845 |
| Silpo | Інше/невідомо | yogurt_dessert | real | 557 | 67 | nan | 73.99619351471887 | 49.99 | 69.79736917695547 | 9.9 | 699.0 |
| Silpo | Вершки | cream | linear | 0 | 2597 | nan | nan | nan | nan | nan | nan |
| Silpo | Вершки | cream | pchip | 0 | 2597 | nan | nan | nan | nan | nan | nan |
| Silpo | Вершки | cream | real | 2283 | 314 | nan | 68.42771576366285 | 56.14 | 51.681826465839464 | 0.5788421052631579 | 439.0 |
| Silpo | Йогурт | milk | linear | 0 | 301 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | yogurt_dessert | linear | 0 | 3115 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | milk | pchip | 0 | 301 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | yogurt_dessert | pchip | 0 | 3115 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | milk | real | 263 | 38 | nan | 79.49248109421208 | 72.48875 | 49.722890846187774 | 3.725 | 479.0 |
| Silpo | Йогурт | yogurt_dessert | real | 2765 | 350 | nan | 64.12196884860795 | 57.61305555555556 | 29.841029189696354 | 3.4995 | 387.245 |
| Silpo | Кефір | milk | linear | 0 | 1311 | nan | nan | nan | nan | nan | nan |
| Silpo | Кефір | milk | pchip | 0 | 1311 | nan | nan | nan | nan | nan | nan |
| Silpo | Кефір | milk | real | 1164 | 147 | nan | 66.04593655736923 | 47.55008333333333 | 59.43405669683452 | 12.145 | 399.0 |
| Silpo | Масло вершкове | butter | linear | 0 | 2621 | nan | nan | nan | nan | nan | nan |
| Silpo | Масло вершкове | butter | pchip | 0 | 2621 | nan | nan | nan | nan | nan | nan |
| Silpo | Масло вершкове | butter | real | 2320 | 301 | nan | 91.44371952778887 | 65.58266666666667 | 83.77769923371503 | 3.1195 | 499.0 |
| Silpo | Молоко питне | milk | linear | 0 | 3716 | nan | nan | nan | nan | nan | nan |

### tests

| source | product | standardized_type | series_variant | n_obs | adf_p | kpss_p | ljungbox_p | bp_p | white_p | jb_p | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | Інше/невідомо | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | other | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | yogurt_dessert | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | other | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | yogurt_dessert | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | milk | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | other | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Інше/невідомо | yogurt_dessert | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Вершки | cream | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Вершки | cream | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Вершки | cream | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | yogurt_dessert | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | yogurt_dessert | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | milk | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Йогурт | yogurt_dessert | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Кефір | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Кефір | milk | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Кефір | milk | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Масло вершкове | butter | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Масло вершкове | butter | pchip | 0 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Масло вершкове | butter | real | 8 | nan | nan | nan | nan | nan | nan | 0 |
| Silpo | Молоко питне | milk | linear | 0 | nan | nan | nan | nan | nan | nan | 0 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_timeseries_by_standardized_type.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_brand_trends.png
