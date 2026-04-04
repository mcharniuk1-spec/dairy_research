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
- standardized_type=butter
- retailer=novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | 0.08225840900720094 | 0.01 | 2.6818026212664985e-12 | 0.1 | 1.3006957963949979e-20 | 0.1 | I(1) | 1.0 | butter | novus | promo_controlled |
| prozorro | 0.05640422694264767 | 0.01 | 3.518946761497874e-22 | 0.1 | 1.9269184182015793e-13 | 0.1 | I(1) | 1.0 | butter | novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | butter | novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | butter | novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | butter | novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | butter | novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.2127764229425364 | 0.27405320585302084 | -0.8083252331134949 |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NARDL | producer_to_prozorro | prozorro | producer | 0.30437404399912776 | 0.5287391650637225 | 4.2203813853019655e-84 | 0 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-02-01 00:00:00 | 31.78268739915295 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-02 00:00:00 | 31.74153855497394 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-03 00:00:00 | 31.71205395008976 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-04 00:00:00 | 31.69228954461795 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-05 00:00:00 | 31.68030129867603 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-06 00:00:00 | 31.67414517238153 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-07 00:00:00 | 31.67187712585198 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-08 00:00:00 | 31.6715531192049 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-09 00:00:00 | 31.71501589339797 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-10 00:00:00 | 31.82710410052748 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-11 00:00:00 | 31.98036756741884 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-12 00:00:00 | 32.14735612089748 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-13 00:00:00 | 32.30061958778885 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-14 00:00:00 | 32.41270779491835 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-15 00:00:00 | 32.45617056911143 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-16 00:00:00 | 32.45341900628176 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-17 00:00:00 | 32.44522030312711 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-18 00:00:00 | 32.43165843764893 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-19 00:00:00 | 32.41281738784873 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-20 00:00:00 | 32.38878113172797 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-21 00:00:00 | 32.35963364728814 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-22 00:00:00 | 32.32545891253073 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-23 00:00:00 | 31.91148084818262 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-24 00:00:00 | 30.90284056637734 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-25 00:00:00 | 29.53949783222626 | nan | nan | butter | novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| producer_to_prozorro | 1 | 0.07873337531291687 |
| producer_to_prozorro | 2 | 0.08283043430904553 |
| producer_to_prozorro | 3 | 0.08251800718380085 |
| producer_to_prozorro | 4 | 0.08422490303011267 |
| producer_to_prozorro | 5 | 0.0907848031216401 |
| producer_to_prozorro | 6 | 0.08185920607839353 |
| producer_to_prozorro | 7 | 0.08099913022176998 |
| producer_to_prozorro | 8 | 0.08418185337829556 |
| producer_to_prozorro | 9 | 0.08011971167494186 |
| producer_to_prozorro | 10 | 0.08071177659888301 |
| producer_to_prozorro | 11 | 0.0855520813606708 |
| producer_to_prozorro | 12 | 0.08891786146062777 |
| producer_to_prozorro | 13 | 0.0906935444584109 |
| producer_to_prozorro | 14 | 0.09336004953876562 |
| producer_to_prozorro | 15 | 0.09806722582073225 |
| producer_to_prozorro | 16 | 0.10411102969445078 |
| producer_to_prozorro | 17 | 0.11083781027515911 |
| producer_to_prozorro | 18 | 0.11554030327110705 |
| producer_to_prozorro | 19 | 0.11683243707057434 |
| producer_to_prozorro | 20 | 0.11514579002515733 |
| producer_to_prozorro | 21 | 0.11293989092313386 |
| producer_to_prozorro | 22 | 0.11348584116046659 |
| producer_to_prozorro | 23 | 0.11614446866624657 |
| producer_to_prozorro | 24 | 0.1193793796780393 |
| producer_to_prozorro | 25 | 0.12118388938915296 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | novus | promo_controlled | daily | I(1) | I(1) | ambiguous | 1793 | 230 | 19 | 220 | 17 |

### NARDL_Multipliers

| horizon | mult_pos | mult_neg | link |
| --- | --- | --- | --- |
| 0 | -0.5437076425441754 | -0.33093121960163896 | producer_to_prozorro |
| 1 | -0.48043463639437756 | -0.2924196897746266 | producer_to_prozorro |
| 2 | -0.48779791951561324 | -0.29690140029865086 | producer_to_prozorro |
| 3 | -0.4869410305889971 | -0.2963798492381926 | producer_to_prozorro |
| 4 | -0.4870407495079179 | -0.29644054381166113 | producer_to_prozorro |
| 5 | -0.4870291448967695 | -0.29643348058903957 | producer_to_prozorro |
| 6 | -0.48703049536267273 | -0.2964343025589613 | producer_to_prozorro |
| 7 | -0.4870303382046144 | -0.2964342069036792 | producer_to_prozorro |
| 8 | -0.4870303564936028 | -0.2964342180353919 | producer_to_prozorro |
| 9 | -0.48703035436525444 | -0.2964342167399587 | producer_to_prozorro |
| 10 | -0.4870303546129372 | -0.2964342168907124 | producer_to_prozorro |
| 11 | -0.4870303545841136 | -0.29643421687316873 | producer_to_prozorro |
| 12 | -0.48703035458746785 | -0.2964342168752103 | producer_to_prozorro |
| 13 | -0.4870303545870775 | -0.29643421687497273 | producer_to_prozorro |
| 14 | -0.48703035458712296 | -0.2964342168750004 | producer_to_prozorro |
| 15 | -0.48703035458711763 | -0.29643421687499716 | producer_to_prozorro |
| 16 | -0.4870303545871183 | -0.29643421687499755 | producer_to_prozorro |
| 17 | -0.4870303545871182 | -0.2964342168749975 | producer_to_prozorro |
| 18 | -0.4870303545871182 | -0.2964342168749975 | producer_to_prozorro |
| 19 | -0.4870303545871182 | -0.2964342168749975 | producer_to_prozorro |
| 20 | -0.4870303545871182 | -0.2964342168749975 | producer_to_prozorro |

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/butter/novus/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/butter/novus/lag_profile_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/butter/novus/nardl_multipliers_promo_controlled.png
