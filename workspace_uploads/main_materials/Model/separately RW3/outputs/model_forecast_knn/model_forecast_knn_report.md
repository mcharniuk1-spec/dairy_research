# RW3 Module Report - model_forecast_knn

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=model_forecast_knn
- xlsx_files=1
- png_files=3
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### model_forecast_knn_output_Forec

| date | product | target | actual_dlog | pred_dlog | segment |
| --- | --- | --- | --- | --- | --- |
| 2025-11-30 00:00:00 | Вершки | ProducerUA | -0.03093304111750506 | -0.03774108873871674 | holdout |
| 2025-12-01 00:00:00 | Вершки | ProducerUA | -0.01224326412504606 | -0.02856545768700842 | holdout |
| 2025-12-02 00:00:00 | Вершки | ProducerUA | 8.740190458889074e-05 | -0.01131223770835968 | holdout |
| 2025-12-03 00:00:00 | Вершки | ProducerUA | 0.000225369664060171 | 7.065324739551072e-05 | holdout |
| 2025-12-04 00:00:00 | Вершки | ProducerUA | 0.0003080763376743789 | 0.000198016356387113 | holdout |
| 2025-12-05 00:00:00 | Вершки | ProducerUA | 0.0003355572578493948 | 0.0002743659262157945 | holdout |
| 2025-12-06 00:00:00 | Вершки | ProducerUA | 0.0003078781437038103 | 0.0002997345735349433 | holdout |
| 2025-12-07 00:00:00 | Вершки | ProducerUA | 0.0002251046165397952 | 0.0002741829660780656 | holdout |
| 2025-12-08 00:00:00 | Вершки | ProducerUA | 8.727183181589382e-05 | 0.0001977716812807335 | holdout |
| 2025-12-09 00:00:00 | Вершки | ProducerUA | -0.0002736795051725416 | 7.053317243866912e-05 | holdout |
| 2025-12-10 00:00:00 | Вершки | ProducerUA | -0.0007633284874453139 | -0.0002626742714576152 | holdout |
| 2025-12-11 00:00:00 | Вершки | ProducerUA | -0.001166757175254496 | -0.0007146872412689858 | holdout |
| 2025-12-12 00:00:00 | Вершки | ProducerUA | -0.001484126713985567 | -0.001087107088722374 | holdout |
| 2025-12-13 00:00:00 | Вершки | ProducerUA | -0.001715286797824511 | -0.001380082573045102 | holdout |
| 2025-12-14 00:00:00 | Вершки | ProducerUA | -0.001859848815486398 | -0.001593474941416612 | holdout |
| 2025-12-15 00:00:00 | Вершки | ProducerUA | -0.001917259080641998 | -0.001726925452478579 | holdout |
| 2025-12-16 00:00:00 | Вершки | ProducerUA | -0.002775386477930297 | -0.001779922978032884 | holdout |
| 2025-12-17 00:00:00 | Вершки | ProducerUA | -0.00408316942382303 | -0.002572091914082473 | holdout |
| 2025-12-18 00:00:00 | Вершки | ProducerUA | -0.004773150179377073 | -0.003779354411592024 | holdout |
| 2025-12-19 00:00:00 | Вершки | ProducerUA | -0.004836039753266519 | -0.004416301003379148 | holdout |
| 2025-12-20 00:00:00 | Вершки | ProducerUA | -0.004260078144329604 | -0.00447435668018663 | holdout |
| 2025-12-21 00:00:00 | Вершки | ProducerUA | -0.00303503148019324 | -0.0039426653527698 | holdout |
| 2025-12-22 00:00:00 | Вершки | ProducerUA | -0.001156414675201667 | -0.002811779757453038 | holdout |
| 2025-12-23 00:00:00 | Вершки | ProducerUA | 0.0001420316153999401 | -0.001077559546843589 | holdout |
| 2025-12-24 00:00:00 | Вершки | ProducerUA | 0.0005005095647452329 | 0.0001210839410508336 | holdout |

### model_forecast_knn_output_Synth

| product | n_obs | coef_synth_to_consumer | p_synth_to_consumer | coef_producer_to_consumer | p_producer_to_consumer | r2 |
| --- | --- | --- | --- | --- | --- | --- |
| Молоко питне | 50 | 0.01753647005461285 | 0.1790711340439692 | -0.1539373703382407 | 0.8758089782929801 | 0.5682257019300552 |
| Сир твердий | 46 | -0.003448418725580535 | 0.393544581866999 | -0.1304863006531816 | 0.3633535989144401 | 0.8530481539621354 |
| Сметана | 49 | 0.56040945620913 | 0.08992558573282051 | -5.078263514758259 | 0.1164214278893085 | 0.4607852937005169 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_forecast_knn/consumer_link_coef.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_forecast_knn/forecast_producer_consumer.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_forecast_knn/synthetic_retail_top_entity.png
