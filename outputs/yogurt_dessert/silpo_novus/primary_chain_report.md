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
- standardized_type=yogurt_dessert
- retailer=silpo_novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | yogurt_dessert | silpo_novus | promo_controlled |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | yogurt_dessert | silpo_novus | promo_controlled |
| retail | 5.695496839419695e-10 | 0.1 | 1.468661222075579e-08 | 0.1 | 1.0051134444285687e-05 | 0.1 | I(0) | 0.0 | yogurt_dessert | silpo_novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | yogurt_dessert | silpo_novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | yogurt_dessert | silpo_novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | yogurt_dessert | silpo_novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| yogurt_dessert | silpo_novus | promo_controlled | daily | none | none | n/a | n/a | 59 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-10-21 00:00:00 | nan | nan | 53.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-22 00:00:00 | nan | nan | 51.39 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-23 00:00:00 | nan | nan | 54.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-24 00:00:00 | nan | nan | 53.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-25 00:00:00 | nan | nan | 52.9 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-26 00:00:00 | nan | nan | 53.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-27 00:00:00 | nan | nan | 53.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-28 00:00:00 | nan | nan | 52.9 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-29 00:00:00 | nan | nan | 52.695 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-30 00:00:00 | nan | nan | 52.9 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-10-31 00:00:00 | nan | nan | 52.49 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-01 00:00:00 | nan | nan | 52.695 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-02 00:00:00 | nan | nan | 52.49 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-03 00:00:00 | nan | nan | 53.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-04 00:00:00 | nan | nan | 50.74 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-05 00:00:00 | nan | nan | 51.44 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-06 00:00:00 | nan | nan | 53.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-07 00:00:00 | nan | nan | 46.24 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-08 00:00:00 | nan | nan | 50.74 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-09 00:00:00 | nan | nan | 52.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-10 00:00:00 | nan | nan | 46.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-11 00:00:00 | nan | nan | 44.89 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-12 00:00:00 | nan | nan | 53.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-13 00:00:00 | nan | nan | 52.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-14 00:00:00 | nan | nan | 46.99 | yogurt_dessert | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

_No rows_

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| yogurt_dessert | silpo_novus | promo_controlled | daily | ambiguous | ambiguous | I(0) | 0 | 0 | 59 | 0 | 0 |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/yogurt_dessert/silpo_novus/time_series_promo_controlled.png
