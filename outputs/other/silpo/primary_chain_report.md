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
- frequency=weekly
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | other | silpo | promo_controlled |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | other | silpo | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | other | silpo | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other | silpo | promo_controlled | weekly | none | none | n/a | n/a | 0 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

_No rows_

### LagProfile

_No rows_

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | any_i2 | eligibility_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other | silpo | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/other/silpo/time_series_promo_controlled.png
