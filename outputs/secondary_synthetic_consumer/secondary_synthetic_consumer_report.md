# Secondary Module: Synthetic Ultimate Consumer (Silpo+Novus+ConsumerUA)

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- Built after primary chain models.
- Coverage is restricted to each standardized_type ProZorro period.
- frequency=daily
- series_rows=1890
- model_rows=10

## Tables

### SyntheticConsumer_Models

| standardized_type | frequency | model_family | link | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef | ect_pvalue | asymmetry_short_p |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cottage_cheese | daily | ARDL | prozorro_to_ultimate_consumer | ultimate_consumer_price | prozorro | 42 | -0.4066263125016476 | -1.685428485355531 | nan | nan | nan |
| cream | daily | ARDL | producer_to_prozorro | prozorro | producer | 199 | 3.349348015760423 | 0.266717232238544 | nan | nan | nan |
| cream | daily | ARDL | producer_to_ultimate_consumer | ultimate_consumer_price | producer | 46 | -10.082147233462337 | -7.788589449718949 | nan | nan | nan |
| cream | daily | ECM | producer_to_ultimate_consumer | ultimate_consumer_price | producer | 43 | -5.388499561865965 | -1.449855506085529 | -1.3992144686360841 | 0.00040790650958883097 | nan |
| hard_cheese | daily | ARDL | producer_to_ultimate_consumer | ultimate_consumer_price | producer | 189 | 1.602343683487597 | 2.538978832015522 | nan | nan | nan |
| milk | daily | ARDL | producer_to_prozorro | prozorro | producer | 201 | 0.6534485521618496 | -0.28996329386924236 | nan | nan | nan |
| milk | daily | ECM | producer_to_prozorro | prozorro | producer | 197 | -0.002155003969288638 | -0.3006834081052232 | -0.9538372381620318 | 3.2952288002155387e-21 | nan |
| milk | daily | ARDL | producer_to_ultimate_consumer | ultimate_consumer_price | producer | 201 | 1.0305554412349078 | 1.2107328897564298 | nan | nan | nan |
| sour_cream | daily | ARDL | producer_to_prozorro | prozorro | producer | 178 | 0.0982872243249222 | 0.36158068419167616 | nan | nan | nan |
| sour_cream | daily | ARDL | producer_to_ultimate_consumer | ultimate_consumer_price | producer | 178 | 1.005497411785936 | 1.0100286454509504 | nan | nan | nan |

### SyntheticConsumer_PreTests

| standardized_type | series | frequency | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | producer | daily | 0.28733427647950704 | 0.1 | 3.939989249212331e-07 | 0.1 | 2.1006274517545675e-13 | 0.1 | I(1) | 0 |
| butter | prozorro | daily | 0.056404226942647726 | 0.01 | 3.518946761497874e-22 | 0.1 | 1.9269184182026386e-13 | 0.1 | I(1) | 1 |
| butter | ultimate_consumer_price | daily | 0.9948280909044506 | 0.01629787475740224 | 2.332614295314388e-05 | 0.1 | 0.0030906664317012153 | 0.1 | I(1) | 1 |
| cottage_cheese | producer | daily | nan | nan | nan | nan | nan | nan | ambiguous | 0 |
| cottage_cheese | prozorro | daily | 1.1483227108295172e-10 | 0.01 | 4.589982408975803e-17 | 0.1 | 4.813752592554151e-10 | 0.1 | I(1) | 0 |
| cottage_cheese | ultimate_consumer_price | daily | 0.8122416324953605 | 0.07937483460730256 | 3.111052445778247e-05 | 0.1 | 0.0004998917145070044 | 0.1 | I(1) | 0 |
| cream | producer | daily | 0.250564990586775 | 0.1 | 2.45386162864072e-07 | 0.1 | 5.803319568218489e-14 | 0.1 | I(1) | 0 |
| cream | prozorro | daily | 5.15934840442518e-22 | 0.1 | 3.6046356335359884e-13 | 0.1 | 1.1693001750830719e-11 | 0.09309066682789993 | I(0) | 0 |
| cream | ultimate_consumer_price | daily | 0.9898974984189568 | 0.04131706548274784 | 0.13281538679024207 | 0.1 | 1.8618636098860138e-07 | 0.1 | I(2) | 0 |
| hard_cheese | producer | daily | 0.07169849370926479 | 0.1 | 1.6796562524251144e-07 | 0.1 | 3.4022983690728456e-13 | 0.1 | I(1) | 0 |
| hard_cheese | prozorro | daily | 2.633366148124232e-10 | 0.08893253878307611 | 1.5324738060670524e-08 | 0.1 | 1.1965567303232429e-10 | 0.04166666666668085 | I(0) | 0 |
| hard_cheese | ultimate_consumer_price | daily | 0.0020093927286190185 | 0.1 | 1.0352889413033173e-06 | 0.1 | 3.4558512742049166e-06 | 0.1 | I(0) | 0 |
| milk | producer | daily | 0.11201722400789482 | 0.1 | 5.176893535234118e-05 | 0.1 | 2.027043992186184e-15 | 0.1 | I(1) | 0 |
| milk | prozorro | daily | 0.0014111002754477221 | 0.01 | 3.8189780115701814e-13 | 0.1 | 4.4125656034645e-11 | 0.1 | I(1) | 0 |
| milk | ultimate_consumer_price | daily | 0.03632042875304809 | 0.1 | 0.040537361406627226 | 0.1 | 2.2176533969954935e-05 | 0.1 | I(0) | 0 |
| other | producer | daily | nan | nan | nan | nan | nan | nan | ambiguous | 0 |
| other | prozorro | daily | 0.9029715543675231 | 0.01 | 1.3734510184087591e-14 | 0.1 | 1.260173359802745e-10 | 0.1 | I(1) | 1 |
| other | ultimate_consumer_price | daily | 0.5659999344514546 | 0.1 | 0.07783547487613032 | 0.1 | 0.001165657246792198 | 0.1 | I(2) | 0 |
| sour_cream | producer | daily | 0.1894666650765241 | 0.1 | 5.90273005994021e-14 | 0.1 | 4.493779268604255e-09 | 0.1 | I(1) | 0 |
| sour_cream | prozorro | daily | 0.21880956753864628 | 0.04947047925942609 | 2.411890357322739e-12 | 0.1 | 3.969186107838014e-13 | 0.1 | I(1) | 0 |
| sour_cream | ultimate_consumer_price | daily | 0.1170536345573358 | 0.1 | 5.055696436915593e-29 | 0.1 | 9.191766788720307e-17 | 0.1 | I(1) | 0 |

### Scaling_Factors

| standardized_type | silpo_scale_to_consumer | novus_scale_to_consumer | n_overlap_silpo_consumer | n_overlap_novus_consumer | period_start | period_end |
| --- | --- | --- | --- | --- | --- | --- |
| butter | 1.0 | 1.0 | 0 | 0 | 2025-04-14 00:00:00 | 2026-01-08 00:00:00 |
| cottage_cheese | 1.0 | 1.0 | 0 | 0 | 2025-04-14 00:00:00 | 2026-01-08 00:00:00 |
| cream | 1.0 | 1.0 | 0 | 0 | 2025-04-15 00:00:00 | 2026-01-08 00:00:00 |
| hard_cheese | 0.9882560209867999 | 0.3947101267414928 | 38 | 32 | 2025-04-14 00:00:00 | 2026-01-08 00:00:00 |
| milk | 0.20159688129728354 | 0.15769761187472736 | 37 | 20 | 2025-04-14 00:00:00 | 2026-01-08 00:00:00 |
| other | 1.0 | 1.0 | 0 | 0 | 2025-04-14 00:00:00 | 2026-01-09 00:00:00 |
| sour_cream | 0.619069086264577 | 0.5746730019074469 | 38 | 12 | 2025-04-14 00:00:00 | 2026-01-08 00:00:00 |
