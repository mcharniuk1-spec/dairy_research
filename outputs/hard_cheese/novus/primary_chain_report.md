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
- standardized_type=hard_cheese
- retailer=novus
- promo_variant=promo_controlled
- frequency=weekly
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | hard_cheese | novus | promo_controlled |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | hard_cheese | novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | hard_cheese | novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | hard_cheese | novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | hard_cheese | novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | hard_cheese | novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hard_cheese | novus | promo_controlled | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-11-10 00:00:00 | 59.31606880691795 | 272.225 | 189.0 | hard_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-17 00:00:00 | 59.45520000587967 | 294.0 | 330.9975 | hard_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-11-24 00:00:00 | 59.2850858876422 | 287.99 | 49.99 | hard_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-01 00:00:00 | 51.70489886750449 | 279.6 | 68.495 | hard_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-08 00:00:00 | 46.22716106084129 | 315.25 | 89.99 | hard_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-15 00:00:00 | 46.34016153275736 | 241.5 | 117.0 | hard_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-22 00:00:00 | 47.37634906317265 | 235.0 | 404.495 | hard_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-12-29 00:00:00 | 47.37749768939897 | 320.88 | 216.495 | hard_cheese | novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

_No rows_

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | any_i2 | eligibility_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hard_cheese | novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/hard_cheese/novus/time_series_promo_controlled.png
