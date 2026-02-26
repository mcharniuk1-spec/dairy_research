# Correlations and Lags Graphs

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- corr_rows=273
- lag_profiles_rows=1025
- Interpretation option: inspect strongest co-movements and dominant lag distances.

## Tables

### Corr_Matrix

| source | CME | ConsumerUA | EU | Novus | ProZorro | ProducerUA | Silpo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CME | 1.0 | 0.30541603111957927 | 0.31350326247341676 | nan | 0.4309873151505198 | 0.3261217580643905 | 0.194237213355106 |
| ConsumerUA | 0.30541603111957927 | 1.0 | 0.7331215385198419 | 0.003320968190273582 | 0.006878099899064877 | 0.9931196793937417 | -0.06557523486993877 |
| EU | 0.31350326247341676 | 0.7331215385198419 | 1.0 | -0.0802936107605772 | 0.06313225435055486 | 0.6312783645531165 | 0.26221890542675513 |
| Novus | nan | 0.003320968190273582 | -0.0802936107605772 | 1.0 | -0.20114383934801688 | -0.16236003168570914 | 0.11924189327160514 |
| ProZorro | 0.4309873151505198 | 0.006878099899064877 | 0.06313225435055486 | -0.20114383934801688 | 1.0 | 0.03964845513664411 | -0.009934571222856589 |
| ProducerUA | 0.3261217580643905 | 0.9931196793937417 | 0.6312783645531165 | -0.16236003168570914 | 0.03964845513664411 | 1.0 | -0.16734499420066853 |
| Silpo | 0.194237213355106 | -0.06557523486993877 | 0.26221890542675513 | 0.11924189327160514 | -0.009934571222856589 | -0.16734499420066853 | 1.0 |

### Lag_Best

| product | standardized_type | pair_left | pair_right | lag_days | corr | is_best_lag |
| --- | --- | --- | --- | --- | --- | --- |
| Масло вершкове | butter | EU | ProZorro | 28 | -0.44070593855241375 | 1 |
| Масло вершкове | butter | EU | ProducerUA | 1 | 0.7908068169800365 | 1 |
| Масло вершкове | butter | EU | Silpo | 10 | -0.25693434003769594 | 1 |
| Масло вершкове | butter | Novus | Silpo | 24 | -0.6048939452964793 | 1 |
| Масло вершкове | butter | ProducerUA | Novus | 1 | -0.1049819509606759 | 1 |
| Масло вершкове | butter | ProducerUA | ProZorro | 20 | -0.09608571873513129 | 1 |
| Масло вершкове | butter | ProducerUA | Silpo | 8 | -0.2508594893128858 | 1 |
| Сир кисломолочний | cottage_cheese | Novus | Silpo | 10 | 0.44922039851458306 | 1 |
| Вершки | cream | EU | ProZorro | 1 | 0.18843455826795666 | 1 |
| Вершки | cream | EU | ProducerUA | 5 | 0.34445442438330837 | 1 |
| Вершки | cream | EU | Silpo | 20 | -0.4042612208416311 | 1 |
| Вершки | cream | Novus | Silpo | 23 | 0.3696569431871244 | 1 |
| Вершки | cream | ProducerUA | Novus | 10 | 0.19692193365974955 | 1 |
| Вершки | cream | ProducerUA | ProZorro | 9 | -0.08444260136425842 | 1 |
| Вершки | cream | ProducerUA | Silpo | 15 | -0.25412341759401047 | 1 |
| Сир твердий | hard_cheese | EU | ProZorro | 11 | -0.26333701523095143 | 1 |
| Сир твердий | hard_cheese | EU | ProducerUA | 27 | 0.686007360451993 | 1 |
| Сир твердий | hard_cheese | EU | Silpo | 24 | -0.47036741987526826 | 1 |
| Сир твердий | hard_cheese | Novus | Silpo | 7 | -0.4139767649030091 | 1 |
| Сир твердий | hard_cheese | ProducerUA | ConsumerUA | 1 | 0.9861527112372024 | 1 |
| Сир твердий | hard_cheese | ProducerUA | Novus | 30 | -0.35218643143168815 | 1 |
| Сир твердий | hard_cheese | ProducerUA | ProZorro | 30 | -0.112574663105113 | 1 |
| Сир твердий | hard_cheese | ProducerUA | Silpo | 16 | -0.42088622791084473 | 1 |
| Інше/невідомо | milk | EU | Silpo | 10 | 0.38129618404588617 | 1 |
| Кефір | milk | ProducerUA | Silpo | 1 | -0.4427213767975084 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_correlations_lags/corr_matrix_sources.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_correlations_lags/lag_best_bar.png
