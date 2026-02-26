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
- retailer=silpo_novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | cottage_cheese | silpo_novus | promo_controlled |
| prozorro | 1.1483227108295172e-10 | 0.01 | 4.589982408975803e-17 | 0.1 | 4.813752592554151e-10 | 0.1 | I(1) | 0.0 | cottage_cheese | silpo_novus | promo_controlled |
| retail | 7.053635234015645e-08 | 0.055181023671470035 | 0.0008960877939895775 | 0.1 | 4.783037514608705e-06 | 0.1 | I(0) | 0.0 | cottage_cheese | silpo_novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | silpo_novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | silpo_novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cottage_cheese | silpo_novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cottage_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 42 | -0.4066263125016476 | -1.685428485355531 | nan |
| cottage_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 40 | -0.04779905990700553 | -0.5494671968185126 | -0.9346201147084174 |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ARDL | prozorro_to_retail | retail | prozorro | 0.1007447696043067 | 0.45591024880877795 | 0.7986167356499732 | 0 |
| NARDL | prozorro_to_retail | retail | prozorro | 0.13802457343734706 | 0.7478438770300309 | 2.6950380978724114e-06 | 0 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-04-14 00:00:00 | nan | 138.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-16 00:00:00 | nan | 118.8 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-18 00:00:00 | nan | 108.9 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-21 00:00:00 | nan | 120.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-22 00:00:00 | nan | 99.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-23 00:00:00 | nan | 107.08 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-24 00:00:00 | nan | 160.2 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-29 00:00:00 | nan | 156.06 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-04-30 00:00:00 | nan | 226.25 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-01 00:00:00 | nan | 82.5 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-02 00:00:00 | nan | 118.08000000000001 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-05 00:00:00 | nan | 101.29499999999999 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-06 00:00:00 | nan | 115.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-07 00:00:00 | nan | 258.2 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-08 00:00:00 | nan | 145.4 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-09 00:00:00 | nan | 101.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-11 00:00:00 | nan | 89.4 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-12 00:00:00 | nan | 168.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-13 00:00:00 | nan | 131.34 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-14 00:00:00 | nan | 75.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-15 00:00:00 | nan | 152.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-16 00:00:00 | nan | 145.2 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-19 00:00:00 | nan | 98.75 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-20 00:00:00 | nan | 159.0 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2025-05-21 00:00:00 | nan | 134.04 | nan | cottage_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| prozorro_to_retail | 1 | -0.08078408601258956 |
| prozorro_to_retail | 2 | -0.06454950488841439 |
| prozorro_to_retail | 3 | -0.1933334718038668 |
| prozorro_to_retail | 4 | 0.18827209925822697 |
| prozorro_to_retail | 5 | 0.14536351827047989 |
| prozorro_to_retail | 6 | -0.2545432657888236 |
| prozorro_to_retail | 7 | -0.12508455517529882 |
| prozorro_to_retail | 8 | 0.08631606508396195 |
| prozorro_to_retail | 9 | 0.1355966845634848 |
| prozorro_to_retail | 10 | 0.2139347251618982 |
| prozorro_to_retail | 11 | -0.009468860585183389 |
| prozorro_to_retail | 12 | 0.2419733955614274 |
| prozorro_to_retail | 13 | 0.043158430923380946 |
| prozorro_to_retail | 14 | -0.1931909836115445 |
| prozorro_to_retail | 15 | -0.28301809398285815 |
| prozorro_to_retail | 16 | -0.07939066612951604 |
| prozorro_to_retail | 17 | -0.08985615650558762 |
| prozorro_to_retail | 18 | 0.018032174074130422 |
| prozorro_to_retail | 19 | 0.23940024361697732 |
| prozorro_to_retail | 20 | 0.23013991101982256 |
| prozorro_to_retail | 21 | -0.1517583037018874 |
| prozorro_to_retail | 22 | -0.19380051895183734 |
| prozorro_to_retail | 23 | -0.09515676503663541 |
| prozorro_to_retail | 24 | 0.07460101451181338 |
| prozorro_to_retail | 25 | 0.20413401238475085 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cottage_cheese | silpo_novus | promo_controlled | daily | ambiguous | I(1) | I(0) | 0 | 190 | 55 | 0 | 42 |

### NARDL_Multipliers

| horizon | mult_pos | mult_neg | link |
| --- | --- | --- | --- |
| 0 | -0.25026320175044364 | -0.2024641418434381 | prozorro_to_retail |
| 1 | -0.23767528150629347 | -0.1922804534226094 | prozorro_to_retail |
| 2 | -0.2383084378591443 | -0.19279267997743665 | prozorro_to_retail |
| 3 | -0.2382765909011576 | -0.19276691563424117 | prozorro_to_retail |
| 4 | -0.2382781927625753 | -0.19276821154788337 | prozorro_to_retail |
| 5 | -0.23827811219098657 | -0.192768146365078 | prozorro_to_retail |
| 6 | -0.23827811624363485 | -0.19276814964369007 | prozorro_to_retail |
| 7 | -0.2382781160397918 | -0.19276814947878007 | prozorro_to_retail |
| 8 | -0.23827811605004484 | -0.19276814948707482 | prozorro_to_retail |
| 9 | -0.23827811604952912 | -0.1927681494866576 | prozorro_to_retail |
| 10 | -0.23827811604955507 | -0.19276814948667859 | prozorro_to_retail |
| 11 | -0.23827811604955376 | -0.19276814948667753 | prozorro_to_retail |
| 12 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |
| 13 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |
| 14 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |
| 15 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |
| 16 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |
| 17 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |
| 18 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |
| 19 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |
| 20 | -0.23827811604955382 | -0.1927681494866776 | prozorro_to_retail |

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cottage_cheese/silpo_novus/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cottage_cheese/silpo_novus/lag_profile_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cottage_cheese/silpo_novus/nardl_multipliers_promo_controlled.png
