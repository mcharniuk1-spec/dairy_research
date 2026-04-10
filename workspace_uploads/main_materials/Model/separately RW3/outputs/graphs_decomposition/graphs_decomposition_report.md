# RW3 Module Report - graphs_decomposition

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=graphs_decomposition
- xlsx_files=1
- png_files=24
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### graphs_decomposition_output_Dec

| date | source | product | standardized_type | observed | log_observed | trend | seasonal | resid |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2022-01-03 00:00:00 | CME | Молоко питне | milk | 505.09281692 | 6.224742208268155 | 6.28937801385405 | -0.06440037264916207 | -0.0002354329367326713 |
| 2022-01-04 00:00:00 | CME | Молоко питне | milk | 505.09281692 | 6.224742208268155 | 6.294426532077483 | 0.003697747965400232 | -0.07338207177472889 |
| 2022-01-05 00:00:00 | CME | Молоко питне | milk | 563.9684159999999 | 6.33499824993 | 6.29947157286429 | -0.004329259391739459 | 0.03985593645744956 |
| 2022-01-06 00:00:00 | CME | Молоко питне | milk | 560.358591 | 6.328576919869759 | 6.304514289599061 | 0.02330752061756797 | 0.0007551096531299706 |
| 2022-01-07 00:00:00 | CME | Молоко питне | milk | 557.063979 | 6.322680096885729 | 6.309555169343106 | 0.01354928921410869 | -0.0004243616714862952 |
| 2022-01-10 00:00:00 | CME | Молоко питне | milk | 557.378379 | 6.323244325275082 | 6.314590426689684 | 0.00956359367548714 | -0.0009096950900886469 |
| 2022-01-11 00:00:00 | CME | Молоко питне | milk | 560.170926 | 6.328241962157521 | 6.319612011209817 | 0.007735717470473674 | 0.0008942334772301663 |
| 2022-01-12 00:00:00 | CME | Молоко питне | milk | 560.6395339999999 | 6.329078157114704 | 6.324602077468575 | -0.04809791975327118 | 0.05257399939940033 |
| 2022-01-13 00:00:00 | CME | Молоко питне | milk | 563.012336 | 6.333301539089697 | 6.329450885440416 | 0.002178697267989987 | 0.001671956381291473 |
| 2022-01-14 00:00:00 | CME | Молоко питне | milk | 562.5104160000001 | 6.332409651240465 | 6.334135956642453 | -0.0001776464653807478 | -0.001548658936607161 |
| 2022-01-18 00:00:00 | CME | Молоко питне | milk | 568.90806 | 6.343718839348278 | 6.338507088340049 | 0.01853593034998433 | -0.01332417934175556 |
| 2022-01-19 00:00:00 | CME | Молоко питне | milk | 574.736323 | 6.353911366926919 | 6.34256731568385 | 0.008284056734437523 | 0.003059994508632258 |
| 2022-01-20 00:00:00 | CME | Молоко питне | milk | 575.17695 | 6.354677732585811 | 6.346317766268097 | 0.004394235813699264 | 0.003965730504014608 |
| 2022-01-21 00:00:00 | CME | Молоко питне | milk | 574.685844 | 6.35382353322842 | 6.349848299271208 | 0.003997782531895905 | -2.254857468386717e-05 |
| 2022-01-24 00:00:00 | CME | Молоко питне | milk | 574.85743 | 6.354122062227119 | 6.353079747638271 | -0.03211308688415433 | 0.03315540147300133 |
| 2022-01-25 00:00:00 | CME | Молоко питне | milk | 575.442972 | 6.355140130289264 | 6.355552608361078 | 0.000769180327452526 | -0.001181658399266539 |
| 2022-01-26 00:00:00 | CME | Молоко питне | milk | 581.342424 | 6.365339953293228 | 6.357354071030266 | 0.003386780962581623 | 0.004599101300380326 |
| 2022-01-27 00:00:00 | CME | Молоко питне | milk | 586.335424 | 6.3738920217254 | 6.35895858910984 | 0.01337507853125732 | 0.001558354084302493 |
| 2022-01-28 00:00:00 | CME | Молоко питне | milk | 590.193644 | 6.380450693220081 | 6.360480397928982 | 0.002488106329952789 | 0.01748218896114651 |
| 2022-01-31 00:00:00 | CME | Молоко питне | milk | 586.328043 | 6.37387943328855 | 6.361797057845736 | -0.001300962711682346 | 0.01338333815449566 |
| 2022-02-01 00:00:00 | CME | Молоко питне | milk | 580.2076450000001 | 6.36338604809136 | 6.362786205338093 | -0.0002840741467681539 | 0.0008839169000349756 |
| 2022-02-02 00:00:00 | CME | Молоко питне | milk | 575.13858 | 6.354611020455073 | 6.363571658313828 | -0.009458899703390554 | 0.000498261844635195 |
| 2022-02-03 00:00:00 | CME | Молоко питне | milk | 580.5264199999999 | 6.363935312591518 | 6.364143238394486 | -0.0005602302257795876 | 0.0003523044228117556 |
| 2022-02-04 00:00:00 | CME | Молоко питне | milk | 585.19107 | 6.371938409289278 | 6.364601917360616 | 0.007097272167523171 | 0.0002392197611387203 |
| 2022-02-07 00:00:00 | CME | Молоко питне | milk | 585.45344 | 6.372386658099488 | 6.365113645349121 | 0.007993564137147352 | -0.0007205513867800661 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_01.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_02.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_03.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_04.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_05.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_06.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_07.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_08.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_09.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_10.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_11.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_observed_trend_12.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_01.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_02.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_03.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_04.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_05.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_06.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_07.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_08.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_09.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_10.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_11.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/graphs_decomposition/decomp_seasonal_resid_12.png
