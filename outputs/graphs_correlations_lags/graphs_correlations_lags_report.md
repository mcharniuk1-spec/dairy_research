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
- corr_rows=296
- lag_profiles_rows=872
- Interpretation option: inspect strongest co-movements and dominant lag distances.

## Tables

### Corr_Matrix

| source | CME | ConsumerUA | EU | FarmGateUA_filled | FarmGateUA_initial | Novus | ProZorro | ProducerUA | Silpo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CME | 1.0 | nan | 0.771150307014702 | 0.39636130313793916 | 0.3818437732242314 | nan | -0.6686712585676096 | nan | 0.5739242968213558 |
| ConsumerUA | nan | 1.0 | 0.7331215385198419 | nan | nan | 0.02681338042040181 | 0.023872483772892125 | 0.9649157171256739 | -0.12751976664861955 |
| EU | 0.771150307014702 | 0.7331215385198419 | 1.0 | 0.401960553922201 | 0.4146037200401722 | 0.05411886372768958 | -0.39911500996322974 | 0.6367201119481288 | 0.04231622485451459 |
| FarmGateUA_filled | 0.39636130313793916 | nan | 0.401960553922201 | 1.0 | 0.9826279956426046 | nan | -0.30096320420445527 | nan | 0.3955558075899114 |
| FarmGateUA_initial | 0.3818437732242314 | nan | 0.4146037200401722 | 0.9826279956426046 | 1.0 | nan | -0.26589910003639705 | nan | 0.27660878164542574 |
| Novus | nan | 0.02681338042040181 | 0.05411886372768958 | nan | nan | 1.0 | -0.12065550374558552 | -0.043920496619733594 | 0.048276373219172226 |
| ProZorro | -0.6686712585676096 | 0.023872483772892125 | -0.39911500996322974 | -0.30096320420445527 | -0.26589910003639705 | -0.12065550374558552 | 1.0 | 0.07811082527179705 | -0.009897940313521869 |
| ProducerUA | nan | 0.9649157171256739 | 0.6367201119481288 | nan | nan | -0.043920496619733594 | 0.07811082527179705 | 1.0 | -0.21091575035180385 |
| Silpo | 0.5739242968213558 | -0.12751976664861955 | 0.04231622485451459 | 0.3955558075899114 | 0.27660878164542574 | 0.048276373219172226 | -0.009897940313521869 | -0.21091575035180385 | 1.0 |

### Lag_Best

| product | standardized_type | pair_left | pair_right | lag_days | corr | is_best_lag |
| --- | --- | --- | --- | --- | --- | --- |
| Сир кисломолочний | cottage_cheese | Novus | Silpo | 14 | 0.24523627303555948 | 1 |
| Вершки | cream | EU | ProZorro | 28 | -0.44201120383867126 | 1 |
| Вершки | cream | EU | ProducerUA | 1 | 0.7270788393994388 | 1 |
| Вершки | cream | EU | Silpo | 10 | -0.6044676898703678 | 1 |
| Вершки | cream | Novus | Silpo | 9 | 0.4556649937689249 | 1 |
| Вершки | cream | ProducerUA | Novus | 18 | -0.32517453059128315 | 1 |
| Вершки | cream | ProducerUA | ProZorro | 20 | -0.08491389732601401 | 1 |
| Вершки | cream | ProducerUA | Silpo | 7 | -0.4180798655236148 | 1 |
| Сир твердий | hard_cheese | EU | ProZorro | 11 | -0.26333701523095143 | 1 |
| Сир твердий | hard_cheese | EU | ProducerUA | 27 | 0.686007360451993 | 1 |
| Сир твердий | hard_cheese | EU | Silpo | 24 | -0.4607038146699059 | 1 |
| Сир твердий | hard_cheese | Novus | Silpo | 7 | -0.4926293986262085 | 1 |
| Сир твердий | hard_cheese | ProducerUA | ConsumerUA | 1 | 0.9861527112372024 | 1 |
| Сир твердий | hard_cheese | ProducerUA | Novus | 30 | -0.43688233284645367 | 1 |
| Сир твердий | hard_cheese | ProducerUA | ProZorro | 30 | -0.112574663105113 | 1 |
| Сир твердий | hard_cheese | ProducerUA | Silpo | 16 | -0.37374547140444553 | 1 |
| Кефір | milk | ProducerUA | Silpo | 18 | -0.36968876199061973 | 1 |
| Молоко питне | milk | EU | ProZorro | 27 | 0.19798230710584866 | 1 |
| Молоко питне | milk | EU | ProducerUA | 27 | 0.5301098856434086 | 1 |
| Молоко питне | milk | EU | Silpo | 8 | -0.5219797447000611 | 1 |
| Молоко питне | milk | Novus | Silpo | 11 | -0.4761644911108315 | 1 |
| Молоко питне | milk | ProducerUA | ConsumerUA | 1 | 0.9068263834913155 | 1 |
| Молоко питне | milk | ProducerUA | Novus | 14 | 0.5727037857042536 | 1 |
| Молоко питне | milk | ProducerUA | ProZorro | 26 | -0.07547451021848318 | 1 |
| Молоко питне | milk | ProducerUA | Silpo | 15 | -0.5247120883607513 | 1 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_correlations_lags/corr_matrix_sources.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_correlations_lags/lag_best_bar.png
