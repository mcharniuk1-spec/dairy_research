# Primary VPT Chain: ProducerUA -> ProZorro -> Retail

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- standardized_type=cottage_cheese
- retailer=novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | cottage_cheese | novus | promo_controlled |
| prozorro | 1.1483227108295172e-10 | 0.01 | 4.589982408975803e-17 | 0.1 | 4.813752592554151e-10 | 0.1 | I(1) | 0.0 | cottage_cheese | novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | cottage_cheese | novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cottage_cheese | novus | promo_controlled | daily | none | none | n/a | n/a | 203 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-04-14 00:00:00 | nan | 138.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-16 00:00:00 | nan | 118.8 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-18 00:00:00 | nan | 108.9 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-21 00:00:00 | nan | 120.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-22 00:00:00 | nan | 99.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-23 00:00:00 | nan | 107.08 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-24 00:00:00 | nan | 160.2 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-29 00:00:00 | nan | 156.06 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-30 00:00:00 | nan | 226.25 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-01 00:00:00 | nan | 82.5 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-02 00:00:00 | nan | 118.08000000000001 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-05 00:00:00 | nan | 101.29499999999999 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-06 00:00:00 | nan | 115.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-07 00:00:00 | nan | 258.2 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-08 00:00:00 | nan | 145.4 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-09 00:00:00 | nan | 101.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-11 00:00:00 | nan | 89.4 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-12 00:00:00 | nan | 168.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-13 00:00:00 | nan | 131.34 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-14 00:00:00 | nan | 75.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-15 00:00:00 | nan | 152.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-16 00:00:00 | nan | 145.2 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-19 00:00:00 | nan | 98.75 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-20 00:00:00 | nan | 159.0 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-21 00:00:00 | nan | 134.04 | nan | cottage_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| prozorro_to_retail | 1 | -0.08256428191281034 |
| prozorro_to_retail | 2 | 0.03971723294061452 |
| prozorro_to_retail | 3 | -0.28299691370846675 |
| prozorro_to_retail | 4 | 0.26565078792035735 |
| prozorro_to_retail | 5 | 0.1303041354472621 |
| prozorro_to_retail | 6 | -0.26925447699907323 |
| prozorro_to_retail | 7 | -0.17216709836907204 |
| prozorro_to_retail | 8 | 0.12956079796648345 |
| prozorro_to_retail | 9 | 0.11206095766065338 |
| prozorro_to_retail | 10 | 0.2040978126322994 |
| prozorro_to_retail | 11 | 0.05589447735426344 |
| prozorro_to_retail | 12 | 0.1138962180039834 |
| prozorro_to_retail | 13 | -0.1824878791281883 |
| prozorro_to_retail | 14 | -0.3814313315470263 |
| prozorro_to_retail | 15 | -0.37383558079104423 |
| prozorro_to_retail | 16 | -0.02635756214685676 |
| prozorro_to_retail | 17 | -0.08611657567161285 |
| prozorro_to_retail | 18 | -0.023291506094282332 |
| prozorro_to_retail | 19 | 0.32564562718987905 |
| prozorro_to_retail | 20 | 0.4207617993239002 |
| prozorro_to_retail | 21 | -0.4536759346531177 |
| prozorro_to_retail | 22 | -0.5409233011486455 |
| prozorro_to_retail | 23 | -0.0802734474776812 |
| prozorro_to_retail | 24 | 0.2944740100850855 |
| prozorro_to_retail | 25 | 0.4074961775359445 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cottage_cheese | novus | promo_controlled | daily | ambiguous | I(1) | ambiguous | 0 | 190 | 20 | 0 | 17 |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cottage_cheese/novus/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cottage_cheese/novus/lag_profile_promo_controlled.png
