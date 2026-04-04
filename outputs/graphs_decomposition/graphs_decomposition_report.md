# Decomposition Graphs

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- series_plotted=12
- Interpretation option: trend vs seasonal strength from Decomposition_Summary.

## Tables

### Decomposition_Summary

| source | product | standardized_type | n_obs | var_trend | var_seasonal | var_resid | seasonal_strength |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CME | Інше/невідомо | other | 1023 | 0.01813256162305753 | 1.3696895894822528e-05 | 0.000302385190902191 | 0.000750381293947995 |
| ConsumerUA | Молоко питне | milk | 1821 | 0.05082708394855027 | 4.7772322855711054e-05 | 0.0008804550636545256 | 0.000911622389869363 |
| ConsumerUA | Сир твердий | hard_cheese | 1821 | 0.06246182267186745 | 1.588233859753418e-05 | 0.0007917875516346176 | 0.00024798904319668326 |
| ConsumerUA | Сметана | sour_cream | 1821 | 0.06979254233120392 | 2.424267731687577e-05 | 0.0008812011741918114 | 0.00034033498667080845 |
| EU | Інше/невідомо | other | 1056 | 0.007521984295517933 | 1.177021568873833e-05 | 0.00011649399834768124 | 0.0015453965192255487 |
| EU | Вершки | cream | 1056 | 0.035440313483320225 | 1.564491032786221e-05 | 0.00019525096597063438 | 0.00044083863823010845 |
| EU | Масло вершкове | butter | 1056 | 0.05007185698814855 | 1.7153087105487225e-05 | 0.00016442085350436037 | 0.0003429566028597069 |
| EU | Молоко питне | milk | 1056 | 0.041164677353559075 | 1.0263983734026259e-05 | 0.00010673107401726843 | 0.0002484903204859443 |
| EU | Сир твердий | hard_cheese | 1056 | 0.024663958035090486 | 1.4019045482782888e-05 | 0.00011590030606499493 | 0.0005640609064335318 |
| FarmGateUA_filled | Інше/невідомо | other | 1462 | 0.04029073178991604 | 2.8271917752467175e-06 | 3.5376510133027686e-05 | 7.033919374785217e-05 |
| FarmGateUA_initial | Інше/невідомо | other | 1462 | 0.038149688787852847 | 9.376735505304772e-06 | 5.137632724838321e-05 | 0.00024542669861241356 |
| Novus | Сир твердий | hard_cheese | 36 | 0.009931853444423908 | 0.06496814585984236 | 0.06689207513061973 | 0.4571727042339323 |
| ProZorro | Інше/невідомо | other | 232 | 0.014453029120117701 | 0.0005453592419822099 | 0.0013225961080344268 | 0.03411105573275054 |
| ProZorro | Вершки | cream | 230 | 0.006211389970793216 | 0.004095213168100825 | 0.014157947184185669 | 0.1887906378351006 |
| ProZorro | Молоко питне | milk | 226 | 0.0016187850628807837 | 0.002022497929428563 | 0.03264982774722933 | 0.05650292827484663 |
| ProZorro | Сир кисломолочний | cottage_cheese | 190 | 0.012108051846488268 | 0.012087351588816363 | 0.04139400268321678 | 0.1811938464150304 |
| ProZorro | Сир твердий | hard_cheese | 199 | 0.004911402373317763 | 0.004101490590481175 | 0.014090939723913233 | 0.18012026363774047 |
| ProZorro | Сметана | sour_cream | 188 | 0.004763630870920487 | 0.015118890000815809 | 0.03554590508699005 | 0.36644070396767503 |
| ProducerUA | Вершки | cream | 1793 | 0.0943873698974695 | 1.4096265830403553e-05 | 0.0006400070226194157 | 0.00014719942734449363 |
| ProducerUA | Кефір | milk | 1793 | 0.0529380562036402 | 4.439101480337001e-05 | 0.0008790285581210395 | 0.0008187065934145023 |
| ProducerUA | Молоко питне | milk | 1793 | 0.030350034933094492 | 5.983096341834654e-06 | 0.0005445556066356808 | 0.00018947241892933853 |
| ProducerUA | Сир твердий | hard_cheese | 1793 | 0.04249621573295978 | 1.4468515068429998e-05 | 0.0007448110454729825 | 0.00032890269628089503 |
| ProducerUA | Сметана | sour_cream | 1793 | 0.05413290701478623 | 1.3642128161575791e-05 | 0.0007549795279768394 | 0.0002464201329687289 |
| Silpo | Інше/невідомо | other | 54 | 0.23494155138245823 | 0.06609050016778388 | 0.18255417566493046 | 0.4215261157584178 |
| Silpo | Вершки | cream | 48 | 0.00047259569486014335 | 0.0008507181186179669 | 0.001267544101087887 | 0.3497241273056178 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_01.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_01.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_02.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_02.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_03.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_03.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_04.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_04.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_05.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_05.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_06.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_06.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_07.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_07.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_08.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_08.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_09.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_09.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_10.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_10.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_11.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_11.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_observed_trend_12.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_decomposition/decomp_seasonal_resid_12.png
