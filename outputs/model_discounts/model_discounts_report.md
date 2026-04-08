# RW4 Promo-State and Discount Models

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- incidence_rows=1
- type_rows=1
- depth_rows=1
- asymmetry_rows=1322

## Tables

### Promo_State_Incidence

| standardized_type | model_scope | model | unreliable_flag | reason |
| --- | --- | --- | --- | --- |
| ALL | unavailable | binomial_attempt_failed | 1 | Promo-incidence binomial model had insufficient stable variation or failed to converge on current data. |

### Promo_State_Type

| standardized_type | model_scope | model | unreliable_flag | reason |
| --- | --- | --- | --- | --- |
| ALL | unavailable | multinomial_attempt_failed | 1 | Promo-state multinomial model had insufficient within-panel state variation or failed to converge on current data. |

### Promo_State_Depth

| standardized_type | model_scope | model | unreliable_flag | reason |
| --- | --- | --- | --- | --- |
| ALL | unavailable | depth_attempt_failed | 1 | Promo-depth conditional model had insufficient positive-markdown support or failed to converge on current data. |

### Asymmetry_Observed_vs_Baseline

| segment_name | standardized_type | farm_gate_source | reconstruction_variant | chain_direction | stage_from | stage_to | model_family | observed_sr_coef | baseline_sr_coef | delta_sr_coef | observed_lr_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Вершки | cream | initial | linear | forward | ProZorro | Retail | NARDL | 0.1855195387021934 | 0.1007392494158206 | -0.0847802892863728 | 0.2943590807532827 |
| Вершки | cream | initial | linear | forward | ProZorro | Retail | NARDL | 0.1855195387021934 | 0.1007392494158206 | -0.0847802892863728 | 0.2943590807532827 |
| Вершки | cream | initial | linear | forward | FarmGateUA | ProZorro | ARDL | 27.40581164655441 | 27.40581164655441 | 0.0 | -1.563367219701413 |
| Вершки | cream | initial | linear | forward | FarmGateUA | ProZorro | ARDL | 27.40581164655441 | 27.40581164655441 | 0.0 | -1.563367219701413 |
| Вершки | cream | initial | linear | forward | FarmGateUA | ProZorro | NARDL | -39.44395541420697 | -39.44395541420697 | 0.0 | -18.22659908428248 |
| Вершки | cream | initial | linear | forward | FarmGateUA | ProZorro | NARDL | -39.44395541420697 | -39.44395541420697 | 0.0 | -18.22659908428248 |
| Вершки | cream | initial | linear | forward | FarmGateUA | Retail | NARDL | -8.772023103981054 | -4.075323960016448 | 4.696699143964606 | -1.852043589957451 |
| Вершки | cream | initial | linear | forward | FarmGateUA | Retail | NARDL | -8.772023103981054 | -5.709143818937397 | 3.062879285043657 | -1.852043589957451 |
| Вершки | cream | initial | linear | forward | FarmGateUA | Retail | NARDL | -8.772023103981054 | -5.709143818937397 | 3.062879285043657 | -1.852043589957451 |
| Вершки | cream | initial | linear | forward | FarmGateUA | Retail | NARDL | -8.772023103981054 | -4.075323960016448 | 4.696699143964606 | -1.852043589957451 |
| Вершки | cream | initial | linear | reverse | Retail | ProZorro | NARDL | 1.562917141304475 | 2.310060540554998 | 0.7471433992505232 | -0.2420696049936481 |
| Вершки | cream | initial | linear | reverse | Retail | ProZorro | NARDL | 1.562917141304475 | 2.310060540554998 | 0.7471433992505232 | -0.2420696049936481 |
| Вершки | cream | initial | linear | reverse | ProZorro | FarmGateUA | NARDL | 0.001294370750072191 | 0.001294370750072191 | 0.0 | 0.02102571537973896 |
| Вершки | cream | initial | linear | reverse | ProZorro | FarmGateUA | NARDL | 0.001294370750072191 | 0.001294370750072191 | 0.0 | 0.02102571537973896 |
| Вершки | cream | initial | linear | reverse | Retail | FarmGateUA | NARDL | 0.006744790717442998 | -0.01054007989158433 | -0.01728487060902733 | 0.0979596312980813 |
| Вершки | cream | initial | linear | reverse | Retail | FarmGateUA | NARDL | 0.006744790717442998 | -0.0113459641210052 | -0.0180907548384482 | 0.0979596312980813 |
| Вершки | cream | initial | linear | reverse | Retail | FarmGateUA | NARDL | 0.006744790717442998 | -0.0113459641210052 | -0.0180907548384482 | 0.0979596312980813 |
| Вершки | cream | initial | linear | reverse | Retail | FarmGateUA | NARDL | 0.006744790717442998 | -0.01054007989158433 | -0.01728487060902733 | 0.0979596312980813 |
| Молоко питне | milk | initial | linear | forward | ProducerUA | ProZorro | NARDL | -39.35627563072685 | -39.35627563072685 | 0.0 | -1.428284989733576 |
| Молоко питне | milk | initial | linear | forward | ProZorro | Retail | NARDL | -0.05150967266593062 | -0.07759645603786203 | -0.026086783371931405 | -0.04955189374108957 |
| Молоко питне | milk | initial | linear | forward | ProZorro | Retail | NARDL | -0.05150967266593062 | -0.07759645603786203 | -0.026086783371931405 | -0.04955189374108957 |
| Молоко питне | milk | initial | linear | forward | ProducerUA | Retail | NARDL | -15.29852457315202 | 16.08250489949674 | 31.381029472648763 | 1.143785547528498 |
| Молоко питне | milk | initial | linear | reverse | Retail | ProZorro | NARDL | -3.377883072190306 | -4.3193244960139 | -0.9414414238235942 | -0.8065514462952509 |
| Молоко питне | milk | initial | linear | reverse | Retail | ProZorro | NARDL | -3.377883072190306 | -4.3193244960139 | -0.9414414238235942 | -0.8065514462952509 |
| Молоко питне | milk | initial | linear | reverse | ProZorro | ProducerUA | ARDL | -0.003981249234879858 | -0.003981249234879858 | 0.0 | 0.08556001807837454 |

### Discount_Strategy_Synthesis

| question | answer | evidence |
| --- | --- | --- |
| Do promotions behave like equilibrium correction? | yes | Baseline Silpo ECM-style coefficients are more often negative than observed-price ones. |
| Does pseudo-asymmetry weaken after promo control? | yes | Observed vs baseline coefficient gaps are summarized in Asymmetry_Observed_vs_Baseline. |
| Do effective prices adjust faster than baseline prices? | mixed | share_observed_ect_faster=0.26 |
| Does discount depth react to upstream shocks? | mixed | Promo_State_Depth stores HAC coefficients on FarmGate/Producer/ProZorro shocks. |
| Do retail shocks transmit materially to farm-gate prices? | yes | reverse_core_rows=119 |
| Is the retail-to-farmgate conclusion stable across farm-gate reconstructions? | yes | reverse_robust_share=1.00 |
| Is transmission stronger for product-specific panels than for all-products averages? | yes | product_core_rows=301; average_core_rows=84 |
| Do specific retailer brands show stronger or weaker transmission? | yes | brand_core_rows=55 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_discounts/discount_delta_short_run.png
