# RW3 Module Report - sheet_novus

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=sheet_novus
- xlsx_files=1
- png_files=4
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### sheet_novus_output_raw

| timestamp | date | product_title | product_name | brand | entity | broader_category | product | fat_pct | pack_qty_final | pack_unit_final | qty_std |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-11-04 19:45:35.222000 | 2025-11-04 00:00:00 | Молоко згущене Первомайський МКК зі смаком ванілі 5% 290г | Молоко згущене зі смаком ванілі | Первомайський МКК | milk | fresh_dairy | Молоко згущене | 5.0 | 290.0 | г | 0.29 |
| 2025-11-04 19:45:35.227000 | 2025-11-04 00:00:00 | Сир Lazur Сріблястий з пліснявою 50% 100г | Сир Сріблястий з пліснявою | Lazur | hard_cheese | cheese | Сир | 50.0 | 100.0 | г | 0.1 |
| 2025-11-04 19:45:35.227000 | 2025-11-04 00:00:00 | Сир Zinka Сердечко козиний напівтвердий з прованськими травами 45% | Сир Сердечко козиний напівтвердий з прованськими травами | Zinka | hard_cheese | cheese | Сир | 45.0 | nan | nan | nan |
| 2025-11-04 19:45:35.228000 | 2025-11-04 00:00:00 | Сметана Ферма 20% 300г | Сметана | Ферма | sour_cream | fermented_dairy | Сметана | 20.0 | 300.0 | г | 0.3 |
| 2025-11-04 19:45:35.229000 | 2025-11-04 00:00:00 | Сир плавлений Пирятин Янтарний пастоподібний 50% 330г | Сир плавлений Янтарний пастоподібний | Пирятин | hard_cheese | cheese | Сир | 50.0 | 330.0 | г | 0.33 |
| 2025-11-04 19:45:35.229000 | 2025-11-04 00:00:00 | Сир Сулугуні зі смаком креветки | Сир зі смаком креветки | Сулугуні | hard_cheese | cheese | Сир | nan | nan | nan | nan |
| 2025-11-04 19:45:35.232000 | 2025-11-04 00:00:00 | Сир Garcia Baquero козячий 45% 150г | Сир Baquero козячий | Garcia | hard_cheese | cheese | Сир | 45.0 | 150.0 | г | 0.15 |
| 2025-11-04 19:45:35.233000 | 2025-11-04 00:00:00 | Напій молочний Müller Шоколад-кокос 1,6% 400г | Напій Müller Шоколад-кокос | Молочний | nan | nan | Масло вершкове | 1.6 | 400.0 | г | 0.4 |
| 2025-11-04 19:45:35.234000 | 2025-11-04 00:00:00 | Сметана President 10% 300г | Сметана | President | sour_cream | fermented_dairy | Сметана | 10.0 | 300.0 | г | 0.3 |
| 2025-11-04 19:45:35.235000 | 2025-11-04 00:00:00 | Сир Biraghi Gorgonzola DOP Гран Густо 55% 100г | Сир Gorgonzola DOP Гран Густо | Biraghi | hard_cheese | cheese | Сир | 55.0 | 100.0 | г | 0.1 |
| 2025-11-04 19:45:35.236000 | 2025-11-04 00:00:00 | Закуска Cream Valley бутербродна пастоподібна з куркою 85г | Закуска Valley бутербродна пастоподібна з куркою | Cream | nan | nan | Масло вершкове | nan | 85.0 | г | 0.085 |
| 2025-11-04 19:45:35.237000 | 2025-11-04 00:00:00 | Йогурт Фанні диня-персик 1% 750г | Йогурт диня-персик | Фанні | yogurt | fermented_dairy | Йогурт | 1.0 | 750.0 | г | 0.75 |
| 2025-11-04 19:45:35.238000 | 2025-11-04 00:00:00 | Сир Rory Бринза 42% | Сир Бринза | Rory | hard_cheese | cheese | Сир | 42.0 | nan | nan | nan |
| 2025-11-04 19:45:35.239000 | 2025-11-04 00:00:00 | Напій йогуртний з лактулозою Лактонія Закваска Злаки 1,5% 750г | Напій йогуртний з лактулозою Закваска Злаки | Лактонія | nan | nan | Йогурт | 1.5 | 750.0 | г | 0.75 |
| 2025-11-04 19:45:35.239000 | 2025-11-04 00:00:00 | Молоко безлактозне Лактель ультрапастеризоване 1,5% 950г | Молоко безлактозне ультрапастеризоване | Лактель | milk | fresh_dairy | Молоко питне | 1.5 | 950.0 | г | 0.95 |
| 2025-11-04 19:45:35.240000 | 2025-11-04 00:00:00 | Йогурт Sojasun соєвий зі шматочками вишні 100г | Йогурт соєвий зі шматочками вишні | Sojasun | yogurt | fermented_dairy | Йогурт | nan | 100.0 | г | 0.1 |
| 2025-11-04 19:45:35.240000 | 2025-11-04 00:00:00 | Сир Старокозаче Грювер 45% | Сир Грювер | Старокозаче | hard_cheese | cheese | Сир | 45.0 | nan | nan | nan |
| 2025-11-04 19:45:35.241000 | 2025-11-04 00:00:00 | Пудинг Sterilgarda Ванільний 2,8-3,5% 2шт*100г | Sterilgarda Ванільний 2,8- * | Пудинг | dessert | dessert_dairy | Вершки | 3.5 | 2.0 | шт | 2.0 |
| 2025-11-04 19:45:35.242000 | 2025-11-04 00:00:00 | Сир Cheese Gallery Емменталлер 45% | Сир Gallery Емменталлер | Cheese | hard_cheese | cheese | Сир | 45.0 | nan | nan | nan |
| 2025-11-04 19:45:35.244000 | 2025-11-04 00:00:00 | Молоко Селянське мікрофільтроване незбиране 3,4-3,8% 850г | Молоко мікрофільтроване незбиране 3,4- | Селянське | milk | fresh_dairy | Молоко питне | 3.8 | 850.0 | г | 0.85 |
| 2025-11-04 19:45:35.246000 | 2025-11-04 00:00:00 | Йогурт-пробіотик Азорель Вишня 4% 500г | Йогурт-пробіотик Вишня | Азорель | yogurt | fermented_dairy | Йогурт | 4.0 | 500.0 | г | 0.5 |
| 2025-11-04 19:45:35.247000 | 2025-11-04 00:00:00 | Напій кисломолочний Яготинський Айран 2% 450г | Напій кисломолочний Айран | Яготинський | nan | nan | Сир кисломолочний | 2.0 | 450.0 | г | 0.45 |
| 2025-11-04 19:45:35.247000 | 2025-11-04 00:00:00 | Сир Beemster Gouda витриманий 48% | Сир Gouda витриманий | Beemster | hard_cheese | cheese | Сир | 48.0 | nan | nan | nan |
| 2025-11-04 19:45:35.248000 | 2025-11-04 00:00:00 | Масло Organic Milk Селянське солодковершкове органічне 72,5% 180г | Масло Milk Селянське солодковершкове органічне | Organic | milk | fresh_dairy | Масло вершкове | 72.5 | 180.0 | г | 0.18 |
| 2025-11-04 19:45:35.249000 | 2025-11-04 00:00:00 | Напій соєвий Alpro Plant Protein 1л | Напій соєвий Plant Protein | Alpro | nan | nan | Інше | nan | 1.0 | л | 1.0 |

### sheet_novus_output_clean

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

### sheet_novus_output_daily_varian

| source | date | product | standardized_type | brand | region | unit_ok | price_real | price_linear | price_pchip | imputed_flag_linear | imputed_flag_pchip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | 2026-01-08 00:00:00 | Інше/невідомо | milk | ПростоНаше | Україна | 1 | 90.65333333333332 | nan | nan | 0 | 0 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | milk | Слов'яночка | Україна | 1 | 93.01162790697674 | nan | nan | 0 | 0 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | 79.98666666666666 | nan | nan | 0 | 0 |
| Novus | 2025-11-05 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-06 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-07 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-08 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-09 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-10 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-11 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-12 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | 79.98666666666666 | nan | nan | 0 | 0 |
| Novus | 2025-11-13 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-14 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-15 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-16 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-17 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-18 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-19 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-20 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-21 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-22 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-23 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-24 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-25 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |
| Novus | 2025-11-26 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | nan | nan | nan | 0 | 0 |

### sheet_novus_output_series_long

| source | date | product | standardized_type | brand | region | unit_ok | imputed_flag_linear | imputed_flag_pchip | series_variant | price |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | 2026-01-08 00:00:00 | Інше/невідомо | milk | ПростоНаше | Україна | 1 | 0 | 0 | real | 90.65333333333332 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | milk | Слов'яночка | Україна | 1 | 0 | 0 | real | 93.01162790697674 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | 0 | 0 | real | 79.98666666666666 |
| Novus | 2025-11-12 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | 0 | 0 | real | 79.98666666666666 |
| Novus | 2026-01-08 00:00:00 | Інше/невідомо | milk | Яготинська | Україна | 1 | 0 | 0 | real | 73.32000000000001 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Albeniz | Україна | 1 | 0 | 0 | real | 992.0 |
| Novus | 2026-01-06 00:00:00 | Інше/невідомо | other | Alive | Україна | 1 | 0 | 0 | real | 370.7916666666667 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Alpro | Україна | 1 | 0 | 0 | real | 273.73 |
| Novus | 2025-12-05 00:00:00 | Інше/невідомо | other | Alpro | Україна | 1 | 0 | 0 | real | 164.0 |
| Novus | 2026-01-06 00:00:00 | Інше/невідомо | other | Alpro | Україна | 1 | 0 | 0 | real | 119.0 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Cир | Україна | 1 | 0 | 0 | real | 1258.307692307692 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Dinoster | Україна | 1 | 0 | 0 | real | 447.0 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Green | Україна | 1 | 0 | 0 | real | 120.3266666666667 |
| Novus | 2025-11-05 00:00:00 | Інше/невідомо | other | Green | Україна | 1 | 0 | 0 | real | 99.99 |
| Novus | 2026-01-08 00:00:00 | Інше/невідомо | other | Green | Україна | 1 | 0 | 0 | real | 59.99 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Joya | Україна | 1 | 0 | 0 | real | 199.0 |
| Novus | 2026-01-08 00:00:00 | Інше/невідомо | other | Marka | Україна | 1 | 0 | 0 | real | 6.898999999999999 |
| Novus | 2026-01-08 00:00:00 | Інше/невідомо | other | Novus | Україна | 1 | 0 | 0 | real | 5.74925 |
| Novus | 2025-11-26 00:00:00 | Інше/невідомо | other | Organic | Україна | 1 | 0 | 0 | real | 10.9 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Toblerone | Україна | 1 | 0 | 0 | real | 3517.647058823529 |
| Novus | 2026-01-08 00:00:00 | Інше/невідомо | other | Valio | Україна | 1 | 0 | 0 | real | 533.2666666666667 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Yommy | Україна | 1 | 0 | 0 | real | 116.995 |
| Novus | 2026-01-08 00:00:00 | Інше/невідомо | other | Zlata | Україна | 1 | 0 | 0 | real | 8.1075 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Іспанський | Україна | 1 | 0 | 0 | real | 999.0 |
| Novus | 2025-11-04 00:00:00 | Інше/невідомо | other | Агропрод | Україна | 1 | 0 | 0 | real | 242.3333333333333 |

### sheet_novus_output_descriptive_

| source | product | standardized_type | series_variant | count | missing | imputed_share | mean | median | std | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Novus | Інше/невідомо | milk | linear | 0 | 68 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | other | linear | 0 | 595 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | yogurt_dessert | linear | 0 | 4 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | milk | pchip | 0 | 68 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | other | pchip | 0 | 595 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | yogurt_dessert | pchip | 0 | 4 | nan | nan | nan | nan | nan | nan |
| Novus | Інше/невідомо | milk | real | 5 | 63 | nan | 83.39165891472868 | 79.98666666666666 | 8.214346846934783 | 73.32000000000001 | 93.01162790697674 |
| Novus | Інше/невідомо | other | real | 50 | 545 | nan | 308.4193055571029 | 108.7339705882353 | 578.8244318973653 | 3.6495 | 3517.647058823529 |
| Novus | Інше/невідомо | yogurt_dessert | real | 4 | 0 | nan | 653.520688405797 | 423.2533333333333 | 565.143920198352 | 273.8260869565217 | 1493.75 |
| Novus | Вершки | cream | linear | 0 | 1044 | nan | nan | nan | nan | nan | nan |
| Novus | Вершки | cream | pchip | 0 | 1044 | nan | nan | nan | nan | nan | nan |
| Novus | Вершки | cream | real | 83 | 961 | nan | 417.6976886882837 | 353.2666666666667 | 341.9167978876021 | 37.66166666666666 | 1811.975 |
| Novus | Йогурт | milk | linear | 0 | 2 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | yogurt_dessert | linear | 0 | 894 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | milk | pchip | 0 | 2 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | yogurt_dessert | pchip | 0 | 894 | nan | nan | nan | nan | nan | nan |
| Novus | Йогурт | milk | real | 2 | 0 | nan | 239.1191666666667 | 239.1191666666667 | 192.8126985826458 | 102.78 | 375.4583333333333 |
| Novus | Йогурт | yogurt_dessert | real | 74 | 820 | nan | 1265.258818085738 | 156.4776984126984 | 9278.627528617262 | 62.47499999999999 | 79999.99875 |
| Novus | Кефір | milk | linear | 0 | 87 | nan | nan | nan | nan | nan | nan |
| Novus | Кефір | milk | pchip | 0 | 87 | nan | nan | nan | nan | nan | nan |
| Novus | Кефір | milk | real | 17 | 70 | nan | 75.0878285425316 | 75.28235294117647 | 10.79098638877085 | 56.99 | 92.21111111111111 |
| Novus | Масло вершкове | butter | linear | 0 | 938 | nan | nan | nan | nan | nan | nan |
| Novus | Масло вершкове | butter | pchip | 0 | 938 | nan | nan | nan | nan | nan | nan |
| Novus | Масло вершкове | butter | real | 69 | 869 | nan | 524.8726224460459 | 544.3888888888889 | 345.0101656523798 | 73.67368421052632 | 1592.0 |
| Novus | Молоко питне | milk | linear | 0 | 770 | nan | nan | nan | nan | nan | nan |

### sheet_novus_output_tests

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

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_novus/sheet_novus_brand_trends.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_novus/sheet_novus_distribution.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_novus/sheet_novus_timeseries_by_product.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/sheet_novus/sheet_novus_timeseries_by_standardized_type.png
