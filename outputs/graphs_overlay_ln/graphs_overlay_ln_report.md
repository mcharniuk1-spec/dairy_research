# RW3 Module Report - graphs_overlay_ln

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=graphs_overlay_ln
- xlsx_files=1
- png_files=21
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### graphs_overlay_ln_output_Before

| date | price_eff | log_price | trend_before_ln | trend_after_ln | source | product | standardized_type |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022-01-03 00:00:00 | 505.09281692 | 6.224742208268155 | nan | nan | CME | Молоко питне | milk |
| 2022-01-04 00:00:00 | 505.09281692 | 6.224742208268155 | nan | nan | CME | Молоко питне | milk |
| 2022-01-05 00:00:00 | 563.9684159999999 | 6.33499824993 | 524.7180166133334 | 6.261494222155437 | CME | Молоко питне | milk |
| 2022-01-06 00:00:00 | 560.358591 | 6.328576919869759 | 533.62816021 | 6.278264896584017 | CME | Молоко питне | milk |
| 2022-01-07 00:00:00 | 557.063979 | 6.322680096885729 | 538.315323968 | 6.287147936644359 | CME | Молоко питне | milk |
| 2022-01-10 00:00:00 | 557.378379 | 6.323244325275082 | 541.4924998066666 | 6.293164001416147 | CME | Молоко питне | milk |
| 2022-01-11 00:00:00 | 560.170926 | 6.328241962157521 | 544.1608464057143 | 6.298175138664915 | CME | Молоко питне | milk |
| 2022-01-12 00:00:00 | 560.6395339999999 | 6.329078157114704 | 552.0960917028572 | 6.313080274214421 | CME | Молоко питне | milk |
| 2022-01-13 00:00:00 | 563.012336 | 6.333301539089697 | 560.3703087142857 | 6.32858875004607 | CME | Молоко питне | milk |
| 2022-01-14 00:00:00 | 562.5104160000001 | 6.332409651240465 | 560.162023 | 6.328218950233279 | CME | Молоко питне | milk |
| 2022-01-18 00:00:00 | 568.90806 | 6.343718839348278 | 561.3833757142858 | 6.330382081587353 | CME | Молоко питне | milk |
| 2022-01-19 00:00:00 | 574.736323 | 6.353911366926919 | 563.9079962857143 | 6.334843691593238 | CME | Молоко питне | milk |
| 2022-01-20 00:00:00 | 575.17695 | 6.354677732585811 | 566.4506492857143 | 6.339334178351913 | CME | Молоко питне | milk |
| 2022-01-21 00:00:00 | 574.685844 | 6.35382353322842 | 568.5242089999999 | 6.342988688504898 | CME | Молоко питне | milk |
| 2022-01-24 00:00:00 | 574.85743 | 6.354122062227119 | 570.555337 | 6.346566389235244 | CME | Молоко питне | milk |
| 2022-01-25 00:00:00 | 575.442972 | 6.355140130289264 | 572.3311421428572 | 6.34968618797804 | CME | Молоко питне | milk |
| 2022-01-26 00:00:00 | 581.342424 | 6.365339953293228 | 575.021429 | 6.35439051684272 | CME | Молоко питне | milk |
| 2022-01-27 00:00:00 | 586.335424 | 6.3738920217254 | 577.5110524285714 | 6.358700971468023 | CME | Молоко питне | milk |
| 2022-01-28 00:00:00 | 590.193644 | 6.380450693220081 | 579.7192411428571 | 6.362492303795618 | CME | Молоко питне | milk |
| 2022-01-31 00:00:00 | 586.328043 | 6.37387943328855 | 581.3122544285714 | 6.365235403896008 | CME | Молоко питне | milk |
| 2022-02-01 00:00:00 | 580.2076450000001 | 6.36338604809136 | 582.1010831428572 | 6.366601477447857 | CME | Молоко питне | milk |
| 2022-02-02 00:00:00 | 575.13858 | 6.354611020455073 | 582.1412474285714 | 6.366671328623279 | CME | Молоко питне | milk |
| 2022-02-03 00:00:00 | 580.5264199999999 | 6.363935312591518 | 582.8674542857143 | 6.367927783237887 | CME | Молоко питне | milk |
| 2022-02-04 00:00:00 | 585.19107 | 6.371938409289278 | 583.4172608571429 | 6.368870419808751 | CME | Молоко питне | milk |
| 2022-02-07 00:00:00 | 585.45344 | 6.372386658099488 | 583.2912631428571 | 6.368655367862194 | CME | Молоко питне | milk |

### graphs_overlay_ln_output_Overla

| date | EU | Novus | Silpo | product | standardized_type | ProZorro | ProducerUA | CME | ConsumerUA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-12-30 00:00:00 | 108.8686868344615 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2021-12-31 00:00:00 | 109.4731006771231 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-03 00:00:00 | 109.5902995912 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-04 00:00:00 | 110.5836740643407 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-05 00:00:00 | 111.1243538713648 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-06 00:00:00 | 113.145457423847 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-07 00:00:00 | 113.9767274207458 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-10 00:00:00 | 114.1263676146353 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-11 00:00:00 | 115.2954956809462 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-12 00:00:00 | 116.7419322272605 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-13 00:00:00 | 117.5147461572441 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-14 00:00:00 | 118.0340030014378 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-17 00:00:00 | 120.2732265383751 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-18 00:00:00 | 120.0750681197868 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-19 00:00:00 | 120.2901482572542 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-20 00:00:00 | 119.1292245894737 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-21 00:00:00 | 119.195024283438 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-24 00:00:00 | 121.4136080202381 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-25 00:00:00 | 121.3937805726786 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-26 00:00:00 | 121.6117407669474 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-27 00:00:00 | 124.4467614592375 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-28 00:00:00 | 124.0176394512143 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-01-31 00:00:00 | 124.4681559196137 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-02-01 00:00:00 | 125.5990931256428 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |
| 2022-02-02 00:00:00 | 125.7509853663512 | nan | nan | Інше/невідомо | milk | nan | nan | nan | nan |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_01.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_02.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_03.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_04.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_05.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_06.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_07.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_08.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_09.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_10.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_11.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/before_after_ln_12.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_01.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_02.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_03.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_04.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_05.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_06.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_07.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_08.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_overlay_ln/overlay_09.png
