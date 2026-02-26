# Overlay and Before/After ln Graphs

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- before_after_series=38
- overlay_products=9
- Interpretation option: compare trend shifts and cross-layer alignment windows.

## Tables

### BeforeAfterLN_Index

| source | product | standardized_type | sheet_name |
| --- | --- | --- | --- |
| CME | Молоко питне | milk | BeforeAfterLN_CME_Молоко_питне |
| ConsumerUA | Молоко питне | milk | BeforeAfterLN_ConsumerUA_М_f9b2 |
| ConsumerUA | Сир твердий | hard_cheese | BeforeAfterLN_ConsumerUA_С_5f55 |
| ConsumerUA | Сметана | sour_cream | BeforeAfterLN_ConsumerUA_С_301e |
| EU | Інше/невідомо | milk | BeforeAfterLN_EU_Інше_невідомо |
| EU | Інше/невідомо | other | BeforeAfterLN_EU_Інше_невідомо |
| EU | Вершки | cream | BeforeAfterLN_EU_Вершки |
| EU | Масло вершкове | butter | BeforeAfterLN_EU_Масло_вершкове |
| EU | Молоко питне | milk | BeforeAfterLN_EU_Молоко_питне |
| EU | Сир твердий | hard_cheese | BeforeAfterLN_EU_Сир_твердий |
| Novus | Вершки | cream | BeforeAfterLN_Novus_Вершки |
| Novus | Йогурт | yogurt_dessert | BeforeAfterLN_Novus_Йогурт |
| Novus | Масло вершкове | butter | BeforeAfterLN_Novus_Масло__4a24 |
| Novus | Молоко питне | milk | BeforeAfterLN_Novus_Молоко_a46c |
| Novus | Сир кисломолочний | cottage_cheese | BeforeAfterLN_Novus_Сир_ки_9b86 |
| Novus | Сир твердий | hard_cheese | BeforeAfterLN_Novus_Сир_твердий |
| Novus | Сметана | sour_cream | BeforeAfterLN_Novus_Сметана |
| ProZorro | Інше/невідомо | other | BeforeAfterLN_ProZorro_Інш_6ed0 |
| ProZorro | Вершки | cream | BeforeAfterLN_ProZorro_Вершки |
| ProZorro | Масло вершкове | butter | BeforeAfterLN_ProZorro_Мас_8043 |
| ProZorro | Молоко питне | milk | BeforeAfterLN_ProZorro_Мол_d696 |
| ProZorro | Сир кисломолочний | cottage_cheese | BeforeAfterLN_ProZorro_Сир_fdf5 |
| ProZorro | Сир твердий | hard_cheese | BeforeAfterLN_ProZorro_Сир_2060 |
| ProZorro | Сметана | sour_cream | BeforeAfterLN_ProZorro_Сметана |
| ProducerUA | Вершки | cream | BeforeAfterLN_ProducerUA_Вершки |

### Overlay_Index

| product | standardized_type | window | sheet_name |
| --- | --- | --- | --- |
| Інше/невідомо | milk | intersection | Charts_Overlay_Інше_невідо_4357 |
| Інше/невідомо | other | intersection | Charts_Overlay_Інше_невідо_4357 |
| Інше/невідомо | yogurt_dessert | intersection | Charts_Overlay_Інше_невідо_4357 |
| Вершки | cream | intersection | Charts_Overlay_Вершки_inte_0e98 |
| Йогурт | milk | intersection | Charts_Overlay_Йогурт_inte_2711 |
| Йогурт | yogurt_dessert | intersection | Charts_Overlay_Йогурт_inte_2711 |
| Кефір | milk | intersection | Charts_Overlay_Кефір_inter_f01a |
| Масло вершкове | butter | intersection | Charts_Overlay_Масло_вершк_d742 |
| Молоко питне | milk | intersection | Charts_Overlay_Молоко_питн_3fa9 |
| Сир кисломолочний | cottage_cheese | intersection | Charts_Overlay_Сир_кисломо_25c3 |
| Сир твердий | hard_cheese | intersection | Charts_Overlay_Сир_твердий_8f76 |
| Сметана | sour_cream | intersection | Charts_Overlay_Сметана_int_d728 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_01.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_02.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_03.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_04.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_05.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_06.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_07.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_08.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_09.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_10.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_11.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_12.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_01.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_02.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_03.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_04.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_05.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_06.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_07.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_08.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/overlay_09.png
