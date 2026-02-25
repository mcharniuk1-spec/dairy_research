# RW3 Module Report - sheet_silpo

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=sheet_silpo
- xlsx_files=1
- png_files=4
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### sheet_silpo_output_raw

| timestamp | date | product_title | product_name | brand | entity | broader_category | Product | fat_pct | pack_qty_final | pack_unit_final | qty_std |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Ряжанка Злагода Печена груша 3,6% пляшка | Ряжанка Печена груша пляшка | Злагода | ryazhanka | fermented_dairy | Вершки | 3.6 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Кефір Селянський питний 1% | Кефір питний | Селянський | kefir | fermented_dairy | Молоко питне | 1.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Йогурт «Лавка традицій» «Старий Порицьк» органічний 1% | Йогурт Старий Порицьк органічний | Лавка традицій | yogurt | fermented_dairy | Йогурт | 1.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Молоко козине Virtuoso by Lukachivka незбиране 3% | Молоко козине незбиране | Virtuoso by Lukachivka | milk | fresh_dairy | Молоко питне | 3.0 | 2.0 | шт | 2.0 |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Тістечко Моnte з шоколадом та лісовим горіхом | Моnte з шоколадом та лісовим горіхом | Тістечко | nan | nan | Сир | nan | 12.0 | шт | 12.0 |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Біфідойогурт Активіа Ягоди злаки питний 1,2% | Біфідойогурт Ягоди злаки питний | Активіа | yogurt | fermented_dairy | Йогурт | 1.2 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Йогурт Lekker По-грецьки білий натуральний 10% відро | Йогурт По-грецьки білий натуральний відро | Lekker | yogurt | fermented_dairy | Йогурт | 10.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Сирок глазурований «Дольче» кокос 15% | Сирок глазурований кокос | Дольче | dessert | dessert_dairy | Сир | 15.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Масло солодковершкове Біло Екстра 82% | Масло солодковершкове Екстра | Біло | butter | butter_fats | Масло вершкове | 82.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Йогурт Lekker По-грецьки білий 3% стакан | Йогурт По-грецьки білий стакан | Lekker | yogurt | fermented_dairy | Йогурт | 3.0 | 10.0 | шт | 10.0 |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Сирочок «Чудо» вишневий 5%, ванночка | Сирочок вишневий ванночка | Чудо | nan | nan | Сир | 5.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Масло «Селянське» солодковершкове екстра 82% | Масло солодковершкове екстра | Селянське | butter | butter_fats | Масло вершкове | 82.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Сир кисломолочний President Сирна Традиція 9%, ванночка | Сир кисломолочний Сирна Традиція ванночка | President | cottage_cheese | fermented_dairy | Сир кисломолочний | 9.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Сир кисломолочний Молокія безлактозний 5% | Сир кисломолочний безлактозний | Молокія | cottage_cheese | fermented_dairy | Сир кисломолочний | 5.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Йогурт Молокія Диня густий 2%, стакан | Йогурт Диня густий стакан | Молокія | yogurt | fermented_dairy | Йогурт | 2.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Йогурт Feels good По-грецьки смак яблуко-папая безлактозний 3% | Йогурт good По-грецьки смак яблуко-папая безлактозний | Feels | yogurt | fermented_dairy | Йогурт | 3.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Молоко «Злагода» дитяче харчування від 9 місяців 3,2% | Молоко дитяче харчування від 9 місяців | Злагода | milk | fresh_dairy | Молоко питне | 3.2 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Йогурт Яготинський Манго та ніжна маракуйя 1,5% | Йогурт Манго та ніжна маракуйя | Яготинський | yogurt | fermented_dairy | Йогурт | 1.5 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Молоко ультрапастеризоване Наше молоко для дітей від 3 років 2.5% | Молоко ультрапастеризоване молоко для дітей від 3 років | Наше | milk | fresh_dairy | Молоко питне | 2.5 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Йогурт Лавка традицій Lago Грецький безлактозний термостатний 10% | Йогурт Lago Грецький безлактозний термостатний | Лавка Традицій | yogurt | fermented_dairy | Йогурт | 10.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Айран Лавка традицій TASbio з молока буйволиць 3% | Лавка традицій TASbio з молока буйволиць | Айран | nan | nan | Молоко питне | 3.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Сметана «Лавка традицій» «Бараново» 20% | Сметана Бараново | Лавка традицій | sour_cream | fermented_dairy | Сметана | 20.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Масло солодковершкове «Лавка традицій» «Доообра ферма» 85% | Масло солодковершкове Доообра ферма | Лавка традицій | butter | butter_fats | Масло вершкове | 85.0 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Ряжанка Яготинська 3,2% стакан | Ряжанка стакан | Яготинська | ryazhanka | fermented_dairy | Сметана | 3.2 | nan | nan | nan |
| 2025-10-21 00:00:00 | 2025-10-21 00:00:00 | Йогурт Premialle Yogurt bowl бузина-лохина-льон 2,8%, стакан | Йогурт Yogurt bowl бузина-лохина-льон стакан | Premialle | yogurt | fermented_dairy | Йогурт | 2.8 | nan | nan | nan |

### sheet_silpo_output_clean

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

### sheet_silpo_output_daily_varian

| source | date | product | standardized_type | brand | region | unit_ok | price_real | price_linear | price_pchip | imputed_flag_linear | imputed_flag_pchip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | 2025-10-21 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-22 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-23 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-24 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-25 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-26 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-27 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-28 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-29 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-30 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-10-31 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-01 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-02 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-03 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-04 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-05 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-06 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-07 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-08 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-09 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-10 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-11 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-12 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-13 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |
| Silpo | 2025-11-14 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 89.99 | nan | nan | 0 | 0 |

### sheet_silpo_output_series_long

| source | date | product | standardized_type | brand | region | unit_ok | imputed_flag_linear | imputed_flag_pchip | series_variant | price |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | 2025-10-21 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-22 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-23 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-24 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-25 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-26 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-27 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-28 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-29 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-30 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-10-31 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-01 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-02 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-03 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-04 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-05 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-06 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-07 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-08 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-09 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-10 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-11 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-12 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-13 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |
| Silpo | 2025-11-14 00:00:00 | Інше/невідомо | milk | Farm | Україна | 1 | 0 | 0 | real | 89.99 |

### sheet_silpo_output_descriptive_

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Silpo | Інше/невідомо | milk | linear | 0 | 515 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | other | linear | 0 | 1836 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | yogurt_dessert | linear | 0 | 624 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | milk | pchip | 0 | 515 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | other | pchip | 0 | 1836 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | yogurt_dessert | pchip | 0 | 624 | nan | nan | nan | nan | nan | nan |
| Silpo | Інше/невідомо | milk | real | 437 | 78 | nan | 58.86474599542335 | 48.32 | 32.29122280267401 | 5.633333333333333 | 209.495 |
| Silpo | Інше/невідомо | other | real | 1628 | 208 | nan | 43.06194529940628 | 27.725 | 47.99737539014726 | 0.6995 | 370.845 |
| Silpo | Інше/невідомо | yogurt_dessert | real | 557 | 67 | nan | 73.99619351471887 | 49.99 | 69.79736917695547 | 9.9 | 699.0 |
| Silpo | Вершки | cream | linear | 0 | 2597 | nan | nan | nan | nan | nan | nan |
| Silpo | Вершки | cream | pchip | 0 | 2597 | nan | nan | nan | nan | nan | nan |
| Silpo | Вершки | cream | real | 2283 | 314 | nan | 68.42771576366285 | 56.14 | 51.68182646583946 | 0.5788421052631579 | 439.0 |
| Silpo | Йогурт | milk | linear | 0 | 301 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | yogurt_dessert | linear | 0 | 3115 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | milk | pchip | 0 | 301 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | yogurt_dessert | pchip | 0 | 3115 | nan | nan | nan | nan | nan | nan |
| Silpo | Йогурт | milk | real | 263 | 38 | nan | 79.49248109421208 | 72.48875 | 49.72289084618777 | 3.725 | 479.0 |
| Silpo | Йогурт | yogurt_dessert | real | 2765 | 350 | nan | 64.12196884860795 | 57.61305555555556 | 29.84102918969635 | 3.4995 | 387.245 |
| Silpo | Кефір | milk | linear | 0 | 1311 | nan | nan | nan | nan | nan | nan |
| Silpo | Кефір | milk | pchip | 0 | 1311 | nan | nan | nan | nan | nan | nan |
| Silpo | Кефір | milk | real | 1164 | 147 | nan | 66.04593655736923 | 47.55008333333333 | 59.43405669683452 | 12.145 | 399.0 |
| Silpo | Масло вершкове | butter | linear | 0 | 2621 | nan | nan | nan | nan | nan | nan |
| Silpo | Масло вершкове | butter | pchip | 0 | 2621 | nan | nan | nan | nan | nan | nan |
| Silpo | Масло вершкове | butter | real | 2320 | 301 | nan | 91.44371952778887 | 65.58266666666667 | 83.77769923371503 | 3.1195 | 499.0 |
| Silpo | Молоко питне | milk | linear | 0 | 3716 | nan | nan | nan | nan | nan | nan |

### sheet_silpo_output_tests

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

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_silpo/sheet_silpo_brand_trends.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_silpo/sheet_silpo_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_silpo/sheet_silpo_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_silpo/sheet_silpo_timeseries_by_standardized_type.png
