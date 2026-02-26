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
- standardized_type=cream
- retailer=silpo_novus
- promo_variant=promo_controlled
- frequency=weekly
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | cream | silpo_novus | promo_controlled |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | cream | silpo_novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | cream | silpo_novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo_novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo_novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo_novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cream | silpo_novus | promo_controlled | weekly | none | none | n/a | n/a | 10 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-10-27 00:00:00 | 25.58083974115278 | 41.790000000000006 | 54.24 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-03 00:00:00 | 25.51995504055111 | 42.239999999999995 | 53.945 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-10 00:00:00 | 25.55925747159386 | 40.05 | 54.99 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-17 00:00:00 | 25.48605909640304 | 37.480000000000004 | 59.99 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-24 00:00:00 | 25.3633859069219 | 41.4 | 58.94 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-01 00:00:00 | 22.48178988858204 | 38.879999999999995 | 59.99 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-08 00:00:00 | 20.68922595011787 | 40.019999999999996 | 73.24125000000001 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-15 00:00:00 | 20.62585615656168 | 38.400000000000006 | 64.085 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-22 00:00:00 | 20.17784663700449 | 34.8 | 109.995 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-29 00:00:00 | 20.07140987312907 | 38.9 | 129.0 | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

_No rows_

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | any_i2 | eligibility_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cream | silpo_novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cream/silpo_novus/time_series_promo_controlled.png
