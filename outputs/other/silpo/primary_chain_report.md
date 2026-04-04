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
- standardized_type=other
- retailer=silpo
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | other | silpo | promo_controlled |
| prozorro | 0.9029715543675233 | 0.01 | 1.3734510184088137e-14 | 0.1 | 1.2601733598025704e-10 | 0.1 | I(1) | 1.0 | other | silpo | promo_controlled |
| retail | 0.9265122856099318 | 0.06750725547200247 | 4.000169254576139e-06 | 0.1 | 6.918723434724411e-05 | 0.04166666666666783 | I(1) | 0.0 | other | silpo | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 50 | 5.213950941002075 | 3.4576682875254376 | nan |
| other | silpo | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 48 | 0.9816109260310837 | -9.345839147206291 | -0.29588648930816513 |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ARDL | prozorro_to_retail | retail | prozorro | 0.018450979329619817 | 0.6777063249902414 | 0.06806309838224132 | 1 |
| NARDL | prozorro_to_retail | retail | prozorro | 0.07342148057897084 | 0.2666931649790291 | 1.3814940607279878e-81 | 0 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-04-14 00:00:00 | nan | 5.0 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-15 00:00:00 | nan | 5.295 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-16 00:00:00 | nan | 4.985 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-17 00:00:00 | nan | 5.43 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-18 00:00:00 | nan | 5.100000000000001 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-19 00:00:00 | nan | 5.175000000000001 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-21 00:00:00 | nan | 5.4 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-22 00:00:00 | nan | 5.25 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-23 00:00:00 | nan | 5.0600000000000005 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-24 00:00:00 | nan | 5.235 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-25 00:00:00 | nan | 5.46 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-28 00:00:00 | nan | 5.2 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-29 00:00:00 | nan | 4.72 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-30 00:00:00 | nan | 4.775 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-01 00:00:00 | nan | 5.08 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-02 00:00:00 | nan | 5.05 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-05 00:00:00 | nan | 5.100000000000001 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-06 00:00:00 | nan | 4.995 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-07 00:00:00 | nan | 5.22 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-08 00:00:00 | nan | 5.04 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-09 00:00:00 | nan | 4.675000000000001 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-12 00:00:00 | nan | 4.78 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-13 00:00:00 | nan | 4.890000000000001 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-14 00:00:00 | nan | 5.2 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-15 00:00:00 | nan | 4.95 | nan | other | silpo | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| prozorro_to_retail | 1 | 0.00916800211923433 |
| prozorro_to_retail | 2 | -0.04391836570778855 |
| prozorro_to_retail | 3 | -0.09898741784622274 |
| prozorro_to_retail | 4 | -0.1737132624652432 |
| prozorro_to_retail | 5 | -0.33876966850034373 |
| prozorro_to_retail | 6 | -0.33942308793212794 |
| prozorro_to_retail | 7 | -0.3492779064865009 |
| prozorro_to_retail | 8 | -0.41054888318660143 |
| prozorro_to_retail | 9 | -0.3720619865418977 |
| prozorro_to_retail | 10 | -0.3444874886934117 |
| prozorro_to_retail | 11 | -0.33455886476950003 |
| prozorro_to_retail | 12 | -0.28427038150998307 |
| prozorro_to_retail | 13 | -0.23827556616559672 |
| prozorro_to_retail | 14 | -0.17170479796611818 |
| prozorro_to_retail | 15 | -0.20245078372142067 |
| prozorro_to_retail | 16 | -0.22691770411699 |
| prozorro_to_retail | 17 | -0.18171814006552792 |
| prozorro_to_retail | 18 | -0.24953730761858695 |
| prozorro_to_retail | 19 | -0.22857510107389625 |
| prozorro_to_retail | 20 | -0.2569008753839704 |
| prozorro_to_retail | 21 | -0.19322411164274927 |
| prozorro_to_retail | 22 | -0.17752826301030095 |
| prozorro_to_retail | 23 | -0.1607703008590289 |
| prozorro_to_retail | 24 | -0.188453881322739 |
| prozorro_to_retail | 25 | -0.24972385400531755 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other | silpo | promo_controlled | daily | ambiguous | I(1) | I(1) | 0 | 232 | 54 | 0 | 50 |

### NARDL_Multipliers

| horizon | mult_pos | mult_neg | link |
| --- | --- | --- | --- |
| 0 | -2.656845491478793 | -3.6384564175098766 | prozorro_to_retail |
| 1 | -2.833764414561026 | -3.880740657648056 | prozorro_to_retail |
| 2 | -2.84554541780151 | -3.896874327062601 | prozorro_to_retail |
| 3 | -2.846329912952929 | -3.8979486655694284 | prozorro_to_retail |
| 4 | -2.84638215236158 | -3.898020205601494 | prozorro_to_retail |
| 5 | -2.8463856309755795 | -3.8980249694409688 | prozorro_to_retail |
| 6 | -2.8463858626159384 | -3.8980252866642893 | prozorro_to_retail |
| 7 | -2.846385878040833 | -3.8980253077881404 | prozorro_to_retail |
| 8 | -2.8463858790679746 | -3.8980253091947743 | prozorro_to_retail |
| 9 | -2.846385879136372 | -3.8980253092884416 | prozorro_to_retail |
| 10 | -2.8463858791409264 | -3.8980253092946793 | prozorro_to_retail |
| 11 | -2.8463858791412298 | -3.8980253092950945 | prozorro_to_retail |
| 12 | -2.8463858791412497 | -3.898025309295122 | prozorro_to_retail |
| 13 | -2.846385879141251 | -3.898025309295124 | prozorro_to_retail |
| 14 | -2.846385879141251 | -3.8980253092951243 | prozorro_to_retail |
| 15 | -2.846385879141251 | -3.8980253092951243 | prozorro_to_retail |
| 16 | -2.846385879141251 | -3.8980253092951243 | prozorro_to_retail |
| 17 | -2.846385879141251 | -3.8980253092951243 | prozorro_to_retail |
| 18 | -2.846385879141251 | -3.8980253092951243 | prozorro_to_retail |
| 19 | -2.846385879141251 | -3.8980253092951243 | prozorro_to_retail |
| 20 | -2.846385879141251 | -3.8980253092951243 | prozorro_to_retail |

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/other/silpo/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/other/silpo/lag_profile_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/other/silpo/nardl_multipliers_promo_controlled.png
