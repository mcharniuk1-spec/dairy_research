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
- retailer=silpo
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | cottage_cheese | silpo | promo_controlled |
| prozorro | 1.1483227108295005e-10 | 0.01 | 4.589982408975472e-17 | 0.1 | 4.813752592550519e-10 | 0.1 | I(1) | 0.0 | cottage_cheese | silpo | promo_controlled |
| retail | 5.9157706543378735e-08 | 0.1 | 7.517018918246667e-13 | 0.0865089553841217 | 0.0018569176848127478 | 0.041666666666666796 | I(0) | 0.0 | cottage_cheese | silpo | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | silpo | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | silpo | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | silpo | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cottage_cheese | silpo | promo_controlled | daily | none | none | n/a | n/a | 203 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-04-14 00:00:00 | nan | 138.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-16 00:00:00 | nan | 118.8 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-18 00:00:00 | nan | 108.9 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-21 00:00:00 | nan | 120.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-22 00:00:00 | nan | 99.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-23 00:00:00 | nan | 107.08 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-24 00:00:00 | nan | 160.2 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-29 00:00:00 | nan | 156.06 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-30 00:00:00 | nan | 226.25 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-01 00:00:00 | nan | 82.5 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-02 00:00:00 | nan | 118.08000000000001 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-05 00:00:00 | nan | 101.29499999999999 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-06 00:00:00 | nan | 115.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-07 00:00:00 | nan | 258.2 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-08 00:00:00 | nan | 145.4 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-09 00:00:00 | nan | 101.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-11 00:00:00 | nan | 89.4 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-12 00:00:00 | nan | 168.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-13 00:00:00 | nan | 131.34 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-14 00:00:00 | nan | 75.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-15 00:00:00 | nan | 152.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-16 00:00:00 | nan | 145.2 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-19 00:00:00 | nan | 98.75 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-20 00:00:00 | nan | 159.0 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-21 00:00:00 | nan | 134.04 | nan | cottage_cheese | silpo | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| prozorro_to_retail | 1 | -0.03042410853195715 |
| prozorro_to_retail | 2 | 0.09315059121833928 |
| prozorro_to_retail | 3 | -0.013554687740592215 |
| prozorro_to_retail | 4 | 0.2640036394817208 |
| prozorro_to_retail | 5 | -0.01665792884614875 |
| prozorro_to_retail | 6 | 0.12427459978543254 |
| prozorro_to_retail | 7 | -0.1940209713635291 |
| prozorro_to_retail | 8 | 0.030775604018925283 |
| prozorro_to_retail | 9 | -0.09372737565447635 |
| prozorro_to_retail | 10 | -0.07704229808546917 |
| prozorro_to_retail | 11 | -0.17919361937712847 |
| prozorro_to_retail | 12 | 0.18757301375096241 |
| prozorro_to_retail | 13 | 0.10991817659598781 |
| prozorro_to_retail | 14 | -0.34943263469401786 |
| prozorro_to_retail | 15 | 0.08988836742206224 |
| prozorro_to_retail | 16 | 0.24534854931006433 |
| prozorro_to_retail | 17 | 0.08079616663444002 |
| prozorro_to_retail | 18 | 0.1868750222264715 |
| prozorro_to_retail | 19 | 0.13127219217068242 |
| prozorro_to_retail | 20 | 0.004357040410090344 |
| prozorro_to_retail | 21 | 0.08986030260644852 |
| prozorro_to_retail | 22 | 0.1322365935271666 |
| prozorro_to_retail | 23 | -0.3991469531086648 |
| prozorro_to_retail | 24 | 0.16752752371267343 |
| prozorro_to_retail | 25 | 0.05655494006971566 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cottage_cheese | silpo | promo_controlled | daily | ambiguous | I(1) | I(0) | 0 | 190 | 48 | 0 | 35 |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cottage_cheese/silpo/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cottage_cheese/silpo/lag_profile_promo_controlled.png
