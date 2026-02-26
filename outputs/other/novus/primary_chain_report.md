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
- retailer=novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | other | novus | promo_controlled |
| prozorro | 0.9029715543675231 | 0.01 | 1.3734510184087591e-14 | 0.1 | 1.260173359802745e-10 | 0.1 | I(1) | 1.0 | other | novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | other | novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | other | novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | other | novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | other | novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other | novus | promo_controlled | daily | none | none | n/a | n/a | 236 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-04-14 00:00:00 | nan | 5.0 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-15 00:00:00 | nan | 5.295 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-16 00:00:00 | nan | 4.985 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-17 00:00:00 | nan | 5.43 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-18 00:00:00 | nan | 5.100000000000001 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-19 00:00:00 | nan | 5.175000000000001 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-21 00:00:00 | nan | 5.4 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-22 00:00:00 | nan | 5.25 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-23 00:00:00 | nan | 5.0600000000000005 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-24 00:00:00 | nan | 5.235 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-25 00:00:00 | nan | 5.46 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-28 00:00:00 | nan | 5.2 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-29 00:00:00 | nan | 4.72 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-30 00:00:00 | nan | 4.775 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-01 00:00:00 | nan | 5.08 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-02 00:00:00 | nan | 5.05 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-05 00:00:00 | nan | 5.100000000000001 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-06 00:00:00 | nan | 4.995 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-07 00:00:00 | nan | 5.22 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-08 00:00:00 | nan | 5.04 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-09 00:00:00 | nan | 4.675000000000001 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-12 00:00:00 | nan | 4.78 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-13 00:00:00 | nan | 4.890000000000001 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-14 00:00:00 | nan | 5.2 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-15 00:00:00 | nan | 4.95 | nan | other | novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

_No rows_

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other | novus | promo_controlled | daily | ambiguous | I(1) | ambiguous | 0 | 232 | 7 | 0 | 7 |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/other/novus/time_series_promo_controlled.png
