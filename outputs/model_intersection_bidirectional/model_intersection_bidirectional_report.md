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
| between_sources | CME | EU | Інше/невідомо | 0 | daily | price_pchip | price_pchip | 0.7663471634923666 | 0.7882030328586436 |
| between_sources | CME | EU | Інше/невідомо | 0 | weekly | price_pchip | price_pchip | 0.7759534505370373 | 0.7965518555127991 |
| between_sources | CME | EU | Інше/невідомо | 1 | weekly | price_pchip | price_pchip | 0.7655006264085082 | 0.7855533899880965 |
| between_sources | CME | EU | Інше/невідомо | 2 | weekly | price_pchip | price_pchip | 0.7520742518702174 | 0.7702893919024691 |
| between_sources | CME | EU | Інше/невідомо | 7 | daily | price_pchip | price_pchip | 0.7526606674033228 | 0.7749586166631723 |
| between_sources | CME | EU | Інше/невідомо | 14 | daily | price_pchip | price_pchip | 0.7361112713493575 | 0.7549028432571119 |
| between_sources | CME | Silpo | Інше/невідомо | 0 | daily | price_pchip | price_pchip | 0.5739242968213558 | 0.38382402145291983 |
| between_sources | CME | Silpo | Інше/невідомо | 7 | daily | price_pchip | price_pchip | 0.3940856013980496 | 0.18091277657875005 |
| between_sources | CME | Silpo | Інше/невідомо | 14 | daily | price_pchip | price_pchip | 0.2785699917966109 | 0.040787290689128626 |
| between_sources | EU | Silpo | Інше/невідомо | 0 | daily | price_pchip | price_pchip | 0.39893719735323874 | 0.01498279034557275 |
| between_sources | EU | Silpo | Інше/невідомо | 7 | daily | price_pchip | price_pchip | 0.21522155201390927 | -0.14517109024021166 |
| between_sources | EU | Silpo | Інше/невідомо | 14 | daily | price_pchip | price_pchip | 0.1737106273583781 | -0.14193156800333104 |
| between_sources | EU | Silpo | Вершки | 0 | daily | price_pchip | price_pchip | -0.2718251060802168 | -0.16694677871148458 |
| between_sources | EU | Silpo | Вершки | 7 | daily | price_pchip | price_pchip | -0.366371762868381 | -0.25882352941176473 |
| between_sources | EU | Silpo | Вершки | 14 | daily | price_pchip | price_pchip | -0.32590983103013615 | -0.19971988795518206 |
| between_sources | Novus | Silpo | Вершки | 14 | daily | price_pchip | price_pchip | 0.18841048921227418 | 0.20519480519480518 |
| between_sources | Novus | Silpo | Йогурт | 7 | daily | price_pchip | price_pchip | 0.2499770612172288 | 0.1847980319240387 |
| between_sources | Novus | Silpo | Йогурт | 14 | daily | price_pchip | price_pchip | 0.10758251404927012 | 0.1850521878605922 |
| between_sources | ConsumerUA | EU | Молоко питне | 0 | daily | price_pchip | price_pchip | 0.7126675585790723 | 0.7491931841552139 |
| between_sources | ConsumerUA | EU | Молоко питне | 0 | weekly | price_pchip | price_pchip | 0.7243015793768569 | 0.7651581201466009 |
| between_sources | ConsumerUA | EU | Молоко питне | 1 | weekly | price_pchip | price_pchip | 0.7143242699340827 | 0.7540994549383854 |
| between_sources | ConsumerUA | EU | Молоко питне | 2 | weekly | price_pchip | price_pchip | 0.7062219973746887 | 0.7448700019385678 |
| between_sources | ConsumerUA | EU | Молоко питне | 7 | daily | price_pchip | price_pchip | 0.7000585928250894 | 0.7379479170026346 |
| between_sources | ConsumerUA | EU | Молоко питне | 14 | daily | price_pchip | price_pchip | 0.6919138481746998 | 0.728943709404495 |
| between_sources | ConsumerUA | Novus | Молоко питне | 0 | daily | price_pchip | price_pchip | 0.21413422118530964 | 0.228024455376302 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_intersection_bidirectional/bidirectional_coef.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_intersection_bidirectional/intersection_combo_coef.png
