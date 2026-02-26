# Primary Chain Consolidated Summary

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.
- model_rows=48
- pretest_rows=144
- diagnostic_rows=48
- eligibility_rows=48

## Tables

### Consolidated_ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | silpo | observed | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| butter | silpo | promo_controlled | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| butter | novus | observed | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| butter | novus | promo_controlled | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| butter | silpo_novus | observed | weekly | none | none | n/a | n/a | 10 | nan | nan | nan |
| butter | silpo_novus | promo_controlled | weekly | none | none | n/a | n/a | 10 | nan | nan | nan |
| cottage_cheese | silpo | observed | weekly | none | none | n/a | n/a | 0 | nan | nan | nan |
| cottage_cheese | silpo | promo_controlled | weekly | none | none | n/a | n/a | 0 | nan | nan | nan |
| cottage_cheese | novus | observed | weekly | none | none | n/a | n/a | 0 | nan | nan | nan |
| cottage_cheese | novus | promo_controlled | weekly | none | none | n/a | n/a | 0 | nan | nan | nan |
| cottage_cheese | silpo_novus | observed | weekly | none | none | n/a | n/a | 0 | nan | nan | nan |
| cottage_cheese | silpo_novus | promo_controlled | weekly | none | none | n/a | n/a | 0 | nan | nan | nan |
| cream | silpo | observed | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| cream | silpo | promo_controlled | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| cream | novus | observed | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| cream | novus | promo_controlled | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| cream | silpo_novus | observed | weekly | none | none | n/a | n/a | 10 | nan | nan | nan |
| cream | silpo_novus | promo_controlled | weekly | none | none | n/a | n/a | 10 | nan | nan | nan |
| hard_cheese | silpo | observed | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| hard_cheese | silpo | promo_controlled | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| hard_cheese | novus | observed | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| hard_cheese | novus | promo_controlled | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |
| hard_cheese | silpo_novus | observed | weekly | none | none | n/a | n/a | 10 | nan | nan | nan |
| hard_cheese | silpo_novus | promo_controlled | weekly | none | none | n/a | n/a | 10 | nan | nan | nan |
| milk | silpo | observed | weekly | none | none | n/a | n/a | 8 | nan | nan | nan |

### Consolidated_PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo | observed |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo | observed |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo | observed |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo | promo_controlled |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo | promo_controlled |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | novus | observed |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | novus | observed |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | novus | observed |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | novus | promo_controlled |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | novus | promo_controlled |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo_novus | observed |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo_novus | observed |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo_novus | observed |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo_novus | promo_controlled |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo_novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | silpo_novus | promo_controlled |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | silpo | observed |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | silpo | observed |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | silpo | observed |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | silpo | promo_controlled |
| prozorro | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | silpo | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | silpo | promo_controlled |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | novus | observed |

### Consolidated_ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 | butter | silpo | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | butter | silpo | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | butter | novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | butter | novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | butter | silpo_novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | butter | silpo_novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | silpo | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | silpo | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | silpo_novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | silpo_novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | cream | silpo | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | cream | silpo | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | cream | novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | cream | novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | cream | silpo_novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | cream | silpo_novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | hard_cheese | silpo | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | hard_cheese | silpo | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | hard_cheese | novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | hard_cheese | novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | hard_cheese | silpo_novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | hard_cheese | silpo_novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | milk | silpo | observed |

### Consolidated_Eligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | any_i2 | eligibility_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | silpo | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| butter | silpo | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| butter | novus | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| butter | novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| butter | silpo_novus | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| butter | silpo_novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cottage_cheese | silpo | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cottage_cheese | silpo | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cottage_cheese | novus | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cottage_cheese | novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cottage_cheese | silpo_novus | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cottage_cheese | silpo_novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cream | silpo | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cream | silpo | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cream | novus | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cream | novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cream | silpo_novus | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| cream | silpo_novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| hard_cheese | silpo | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| hard_cheese | silpo | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| hard_cheese | novus | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| hard_cheese | novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| hard_cheese | silpo_novus | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| hard_cheese | silpo_novus | promo_controlled | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
| milk | silpo | observed | weekly | ambiguous | ambiguous | ambiguous | 0 | Insufficient common sample after alignment; model outputs are placeholders. |
