# Secondary Intersection Module (Silpo-Novus + Controls)

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- bidirectional_rows=1
- combo_rows=1
- ConsumerUA/EU/CME are used only as secondary robustness controls in this module.

## Tables

### Bidirectional_Results

| note |
| --- |
| Insufficient Silpo-Novus overlap for bidirectional regressions. |

### Intersection_Combination_Summary

| note |
| --- |
| Insufficient overlap for combined secondary model. |

### CrossTable_Correlations

| corr_type | source_left | source_right | product | lag | freq | series_left | series_right | pearson | spearman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| between_sources | EU | Silpo | Інше/невідомо | 0 | daily | price_pchip | price_pchip | 0.7036896267922405 | 0.7505738788595241 |
| between_sources | EU | Silpo | Інше/невідомо | 0 | weekly | price_pchip | price_pchip | 0.9044841052648571 | 0.8147058823529412 |
| between_sources | EU | Silpo | Інше/невідомо | 1 | weekly | price_pchip | price_pchip | 0.5604513838048434 | 0.5637254901960785 |
| between_sources | EU | Silpo | Інше/невідомо | 2 | weekly | price_pchip | price_pchip | -0.4627642563176874 | -0.40196078431372556 |
| between_sources | EU | Silpo | Інше/невідомо | 7 | daily | price_pchip | price_pchip | 0.15598452371160243 | 0.05485664719819713 |
| between_sources | EU | Silpo | Інше/невідомо | 14 | daily | price_pchip | price_pchip | -0.13670310926058685 | -0.30568589147286784 |
| between_sources | EU | Silpo | Вершки | 0 | daily | price_pchip | price_pchip | -0.15662326907638527 | -0.12212885154061627 |
| between_sources | EU | Silpo | Вершки | 7 | daily | price_pchip | price_pchip | -0.19329983287188615 | -0.21988795518207285 |
| between_sources | EU | Silpo | Вершки | 14 | daily | price_pchip | price_pchip | -0.1909864131780531 | -0.16078431372549024 |
| between_sources | Novus | Silpo | Йогурт | 7 | daily | price_pchip | price_pchip | 0.17850082701193157 | 0.3687593134659932 |
| between_sources | Novus | Silpo | Йогурт | 14 | daily | price_pchip | price_pchip | 0.06330319429279573 | 0.26996299142885 |
| between_sources | EU | Silpo | Масло вершкове | 0 | daily | price_pchip | price_pchip | -0.06635777043711011 | -0.03669467787114846 |
| between_sources | EU | Silpo | Масло вершкове | 7 | daily | price_pchip | price_pchip | -0.09762200874519522 | -0.031092436974789917 |
| between_sources | EU | Silpo | Масло вершкове | 14 | daily | price_pchip | price_pchip | -0.12873764228646645 | -0.13529411764705884 |
| between_sources | CME | ConsumerUA | Молоко питне | 0 | daily | price_pchip | price_pchip | 0.29924255319756543 | 0.30605849598441004 |
| between_sources | CME | ConsumerUA | Молоко питне | 0 | weekly | price_pchip | price_pchip | 0.31158950904159316 | 0.3193871706315173 |
| between_sources | CME | ConsumerUA | Молоко питне | 1 | weekly | price_pchip | price_pchip | 0.30300693085706926 | 0.3234376391884689 |
| between_sources | CME | ConsumerUA | Молоко питне | 2 | weekly | price_pchip | price_pchip | 0.29336450389094876 | 0.32104134224478725 |
| between_sources | CME | ConsumerUA | Молоко питне | 7 | daily | price_pchip | price_pchip | 0.29962146053707217 | 0.31689912291860545 |
| between_sources | CME | ConsumerUA | Молоко питне | 14 | daily | price_pchip | price_pchip | 0.286851015094869 | 0.3090518497776876 |
| between_sources | CME | EU | Молоко питне | 0 | daily | price_pchip | price_pchip | 0.30731977887795275 | 0.4116781373872708 |
| between_sources | CME | EU | Молоко питне | 0 | weekly | price_pchip | price_pchip | 0.3196867460688807 | 0.42296301474078657 |
| between_sources | CME | EU | Молоко питне | 1 | weekly | price_pchip | price_pchip | 0.28419083389319144 | 0.3889124862365033 |
| between_sources | CME | EU | Молоко питне | 2 | weekly | price_pchip | price_pchip | 0.2514548301665495 | 0.3539858229094981 |
| between_sources | CME | EU | Молоко питне | 7 | daily | price_pchip | price_pchip | 0.2777858248126248 | 0.3819521583233612 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_intersection_bidirectional/bidirectional_coef.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_intersection_bidirectional/intersection_combo_coef.png
