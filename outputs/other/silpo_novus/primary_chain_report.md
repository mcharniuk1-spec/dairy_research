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
- retailer=silpo_novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | other | silpo_novus | promo_controlled |
| prozorro | 0.9029715543675233 | 0.01 | 1.3734510184088137e-14 | 0.1 | 1.2601733598025704e-10 | 0.1 | I(1) | 1.0 | other | silpo_novus | promo_controlled |
| retail | 0.13774846220222936 | 0.1 | 0.02230468906736146 | 0.1 | 1.0563874553359726e-08 | 0.1 | I(1) | 0.0 | other | silpo_novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo_novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo_novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | other | silpo_novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 52 | 3.191807377212628 | -12.70081452552557 | nan |
| other | silpo_novus | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 50 | 0.7522139284224749 | 6.209165049284259 | -0.4291476640555165 |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ARDL | prozorro_to_retail | retail | prozorro | 0.389263947975609 | 0.10283762781865896 | 0.8943003210984833 | 0 |
| NARDL | prozorro_to_retail | retail | prozorro | 0.2397663534427088 | 0.0059467560072590945 | 6.260837456607158e-56 | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-04-14 00:00:00 | nan | 5.0 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-15 00:00:00 | nan | 5.295 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-16 00:00:00 | nan | 4.985 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-17 00:00:00 | nan | 5.43 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-18 00:00:00 | nan | 5.100000000000001 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-19 00:00:00 | nan | 5.175000000000001 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-21 00:00:00 | nan | 5.4 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-22 00:00:00 | nan | 5.25 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-23 00:00:00 | nan | 5.0600000000000005 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-24 00:00:00 | nan | 5.235 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-25 00:00:00 | nan | 5.46 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-28 00:00:00 | nan | 5.2 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-29 00:00:00 | nan | 4.72 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-30 00:00:00 | nan | 4.775 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-01 00:00:00 | nan | 5.08 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-02 00:00:00 | nan | 5.05 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-05 00:00:00 | nan | 5.100000000000001 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-06 00:00:00 | nan | 4.995 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-07 00:00:00 | nan | 5.22 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-08 00:00:00 | nan | 5.04 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-09 00:00:00 | nan | 4.675000000000001 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-12 00:00:00 | nan | 4.78 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-13 00:00:00 | nan | 4.890000000000001 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-14 00:00:00 | nan | 5.2 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-15 00:00:00 | nan | 4.95 | nan | other | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| prozorro_to_retail | 1 | 0.021801623475124304 |
| prozorro_to_retail | 2 | -0.1677317854495336 |
| prozorro_to_retail | 3 | -0.18614997912727976 |
| prozorro_to_retail | 4 | -0.11954773824154614 |
| prozorro_to_retail | 5 | -0.3024125191964572 |
| prozorro_to_retail | 6 | -0.3584160123905419 |
| prozorro_to_retail | 7 | -0.256406254168928 |
| prozorro_to_retail | 8 | -0.15845877042218173 |
| prozorro_to_retail | 9 | -0.3378266814360856 |
| prozorro_to_retail | 10 | -0.15596459462221665 |
| prozorro_to_retail | 11 | -0.15873386433990713 |
| prozorro_to_retail | 12 | -0.244078537874973 |
| prozorro_to_retail | 13 | -0.2191276584924703 |
| prozorro_to_retail | 14 | -0.09053412649840303 |
| prozorro_to_retail | 15 | -0.019377145758522434 |
| prozorro_to_retail | 16 | -0.028522233066124413 |
| prozorro_to_retail | 17 | -0.011156583097595032 |
| prozorro_to_retail | 18 | -0.05490922876379749 |
| prozorro_to_retail | 19 | -0.20245354984748348 |
| prozorro_to_retail | 20 | -0.13694972856526602 |
| prozorro_to_retail | 21 | -0.09355059469842485 |
| prozorro_to_retail | 22 | 0.024867173761834425 |
| prozorro_to_retail | 23 | 0.039988247700322485 |
| prozorro_to_retail | 24 | 0.02962642392675777 |
| prozorro_to_retail | 25 | -0.022052301936377822 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| other | silpo_novus | promo_controlled | daily | ambiguous | I(1) | I(1) | 0 | 232 | 56 | 0 | 52 |

### NARDL_Multipliers

| horizon | mult_pos | mult_neg | link |
| --- | --- | --- | --- |
| 0 | -1.2056182554944732 | -1.9578321839169481 | prozorro_to_retail |
| 1 | -1.362521157383359 | -2.2126305412477545 | prozorro_to_retail |
| 2 | -1.3829409880461392 | -2.245790790339477 | prozorro_to_retail |
| 3 | -1.3855984881897114 | -2.2501063680823803 | prozorro_to_retail |
| 4 | -1.3859443435070113 | -2.2506680107649646 | prozorro_to_retail |
| 5 | -1.3859893541915052 | -2.250741104686959 | prozorro_to_retail |
| 6 | -1.3859952120216938 | -2.2507506173568435 | prozorro_to_retail |
| 7 | -1.3859959743778967 | -2.2507518553652286 | prozorro_to_retail |
| 8 | -1.3859960735932992 | -2.2507520164834824 | prozorro_to_retail |
| 9 | -1.3859960865054997 | -2.250752037451912 | prozorro_to_retail |
| 10 | -1.3859960881859335 | -2.2507520401808088 | prozorro_to_retail |
| 11 | -1.3859960884046303 | -2.250752040535956 | prozorro_to_retail |
| 12 | -1.3859960884330922 | -2.2507520405821757 | prozorro_to_retail |
| 13 | -1.3859960884367963 | -2.250752040588191 | prozorro_to_retail |
| 14 | -1.3859960884372784 | -2.250752040588974 | prozorro_to_retail |
| 15 | -1.3859960884373412 | -2.2507520405890755 | prozorro_to_retail |
| 16 | -1.3859960884373494 | -2.250752040589089 | prozorro_to_retail |
| 17 | -1.3859960884373503 | -2.2507520405890906 | prozorro_to_retail |
| 18 | -1.3859960884373506 | -2.250752040589091 | prozorro_to_retail |
| 19 | -1.3859960884373506 | -2.250752040589091 | prozorro_to_retail |
| 20 | -1.3859960884373506 | -2.250752040589091 | prozorro_to_retail |

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/other/silpo_novus/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/other/silpo_novus/lag_profile_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/other/silpo_novus/nardl_multipliers_promo_controlled.png
