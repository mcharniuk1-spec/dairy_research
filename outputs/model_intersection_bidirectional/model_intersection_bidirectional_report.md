# RW3 Module Report - model_intersection_bidirectional

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=model_intersection_bidirectional
- xlsx_files=1
- png_files=2
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### model_intersection_bidirectiona

| corr_type | source_left | source_right | product | lag | freq | series_left | series_right | pearson | spearman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| between_sources | ProZorro | Silpo | Інше/невідомо | 0 | daily | price_pchip | price_pchip | 0.08501384846662308 | 0.1438520694700537 |
| between_sources | ProZorro | Silpo | Інше/невідомо | 7 | daily | price_pchip | price_pchip | 0.09382062100686524 | 0.07496584726779254 |
| between_sources | ProZorro | Silpo | Інше/невідомо | 14 | daily | price_pchip | price_pchip | -0.2028089538084511 | -0.08271680356876245 |
| between_sources | ProZorro | ProducerUA | Вершки | 0 | daily | price_pchip | price_pchip | 0.04927482212688276 | 0.07127460885841022 |
| between_sources | ProZorro | ProducerUA | Вершки | 0 | weekly | price_pchip | price_pchip | -0.06019592258574265 | -0.05523944997629207 |
| between_sources | ProZorro | ProducerUA | Вершки | 1 | weekly | price_pchip | price_pchip | 0.009115693673181538 | 0.006893533209322683 |
| between_sources | ProZorro | ProducerUA | Вершки | 2 | weekly | price_pchip | price_pchip | 0.09083690134804394 | 0.1427125506072875 |
| between_sources | ProZorro | ProducerUA | Вершки | 7 | daily | price_pchip | price_pchip | 0.07630003913768656 | 0.08652828474044104 |
| between_sources | ProZorro | ProducerUA | Вершки | 14 | daily | price_pchip | price_pchip | 0.124704533653067 | 0.1762692414620244 |
| between_sources | ProZorro | Silpo | Вершки | 0 | daily | price_pchip | price_pchip | -0.06413029313791055 | -0.2491694352159469 |
| between_sources | ProZorro | Silpo | Вершки | 7 | daily | price_pchip | price_pchip | 0.0258154009447211 | -0.00316019771493396 |
| between_sources | ProZorro | Silpo | Вершки | 14 | daily | price_pchip | price_pchip | -0.4169305791656699 | -0.2846572032618544 |
| between_sources | ProducerUA | Silpo | Вершки | 0 | daily | price_pchip | price_pchip | -0.22063926481763 | -0.299174989144594 |
| between_sources | ProducerUA | Silpo | Вершки | 7 | daily | price_pchip | price_pchip | -0.2134788461028884 | -0.1621797655232306 |
| between_sources | ProducerUA | Silpo | Вершки | 14 | daily | price_pchip | price_pchip | -0.2483021766133238 | -0.1717325227963526 |
| between_sources | Novus | Silpo | Йогурт | 7 | daily | price_pchip | price_pchip | 0.1785008270119316 | 0.3687593134659932 |
| between_sources | Novus | Silpo | Йогурт | 14 | daily | price_pchip | price_pchip | 0.06330319429279573 | 0.26996299142885 |
| between_sources | ProducerUA | Silpo | Кефір | 0 | daily | price_pchip | price_pchip | -0.4487516915580174 | -0.3847155883630048 |
| between_sources | ProducerUA | Silpo | Кефір | 7 | daily | price_pchip | price_pchip | -0.3066534227512124 | -0.1652192792010421 |
| between_sources | ProducerUA | Silpo | Кефір | 14 | daily | price_pchip | price_pchip | -0.2800580238388762 | -0.3137212331741207 |
| between_sources | ProZorro | ProducerUA | Масло вершкове | 0 | daily | price_pchip | price_pchip | 0.08345314771020476 | 0.1337363371444246 |
| between_sources | ProZorro | ProducerUA | Масло вершкове | 0 | weekly | price_pchip | price_pchip | 0.2207375752759627 | 0.2622825254404202 |
| between_sources | ProZorro | ProducerUA | Масло вершкове | 1 | weekly | price_pchip | price_pchip | 0.1876971392580341 | 0.2396761133603239 |
| between_sources | ProZorro | ProducerUA | Масло вершкове | 2 | weekly | price_pchip | price_pchip | 0.1405323077910286 | 0.1821763602251407 |
| between_sources | ProZorro | ProducerUA | Масло вершкове | 7 | daily | price_pchip | price_pchip | 0.05944760710130514 | 0.124808415831582 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_intersection_bidirectional/bidirectional_coef.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_intersection_bidirectional/intersection_combo_coef.png
