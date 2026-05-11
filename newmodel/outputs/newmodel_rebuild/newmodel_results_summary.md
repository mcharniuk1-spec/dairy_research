# New Model Results Summary

## Evidence Hierarchy

1. Main evidence: observed monthly SSSU farm-gate, processor-level, and official consumer prices.
2. Mechanism evidence: ProZorro procurement and Silpo/Novus retail prices.
3. Extension evidence: regional dispersion and old-model validation.
4. Appendix-only evidence: weak old reconstructed or short-overlap models.

## Reliable Models

| model_id | hypothesis | method | n | period_start | period_end | long_run_beta | ect | ect_p | reliability | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H2_processor_to_consumer_drinking_milk_asymmetry | H2 | NARDL-lite | 111 | 2017-01-01 | 2026-03-01 |  | -0.1131 | 0.0106 | reliable | Asymmetry is statistically meaningful: positive shocks 0.29, negative shocks -0.08. |

## Probable / Needs Validation Models

| model_id | hypothesis | method | n | period_start | period_end | long_run_beta | ect | ect_p | reliability | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H1_farmgate_to_processor_sour_cream | H1 | ECM | 131 | 2015-01-01 | 2026-03-01 | 1.02 | -0.03585 | 0.1221 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.02, ECT -0.04. |
| H1_farmgate_to_prozorro_butter | H1 | ECM | 36 | 2023-01-01 | 2026-03-01 | 1.37 | -0.5013 | 0.001104 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.37, ECT -0.50. |
| H1_farmgate_to_prozorro_condensed_milk | H1 | ECM | 34 | 2023-02-01 | 2026-03-01 | 0.3678 | -0.8208 | 4.222e-06 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.37, ECT -0.82. |
| H1_farmgate_to_prozorro_cottage_cheese | H1 | ECM | 36 | 2023-01-01 | 2026-03-01 | 0.2953 | -0.6929 | 2.779e-07 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.30, ECT -0.69. |
| H1_farmgate_to_prozorro_drinking_milk | H1 | ECM | 36 | 2023-01-01 | 2026-03-01 | 0.8184 | -0.421 | 0.01763 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.82, ECT -0.42. |
| H1_farmgate_to_prozorro_hard_cheese | H1 | ECM | 36 | 2023-01-01 | 2026-03-01 | 0.8656 | -0.7169 | 0.001442 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.87, ECT -0.72. |
| H2_processor_to_consumer_drinking_milk | H2 | ECM | 111 | 2017-01-01 | 2026-03-01 | 0.8888 | -0.06642 | 0.01931 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.89, ECT -0.07. |
| H2_processor_to_consumer_soft_cheese | H2 | ECM | 111 | 2017-01-01 | 2026-03-01 | 1.146 | -0.0821 | 0.08636 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.15, ECT -0.08. |
| H2_processor_to_prozorro_butter | H2 | ECM | 39 | 2023-01-01 | 2026-03-01 | 1.163 | -1.028 | 3.973e-07 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.16, ECT -1.03. |
| H2_processor_to_prozorro_drinking_milk | H2 | ECM | 39 | 2023-01-01 | 2026-03-01 | 1.085 | -0.4624 | 0.007761 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.08, ECT -0.46. |
| H2_processor_to_prozorro_hard_cheese | H2 | ECM | 39 | 2023-01-01 | 2026-03-01 | 1.379 | -0.8694 | 9.315e-10 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.38, ECT -0.87. |
| H2_processor_to_consumer_soft_cheese_asymmetry | H2 | NARDL-lite | 111 | 2017-01-01 | 2026-03-01 |  | -0.1058 | 0.01574 | probable / needs validation | Asymmetry is suggestive but should not be a headline claim. |
| H2_processor_to_consumer_sour_cream_asymmetry | H2 | NARDL-lite | 111 | 2017-01-01 | 2026-03-01 |  | -0.09262 | 0.07846 | probable / needs validation | Asymmetry is suggestive but should not be a headline claim. |
| H2_prozorro_to_pooled_retail_observed_daily_asof | H2 | Short panel OLS-HAC | 104 | 2025-11-02 | 2026-01-08 |  |  |  | probable / needs validation | Short-window retail mechanism evidence; use for H2 timing and promotion discussion, not as a long-run market-power proof. |

## VECM Systems

| system | product | n | rank | alpha_farmgate | alpha_processor | alpha_consumer | status | reliability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| farmgate_processor_consumer_drinking_milk | drinking_milk | 107 | 0 |  |  |  | no_cointegration_rank | unreliable / appendix only |
| farmgate_processor_consumer_sour_cream | sour_cream | 107 | 1 | -0.02541 | 0.01963 | 0.01913 | estimated | probable / needs validation |

## Interpretation Rules

- A negative and significant error-correction term supports a long-run price relation and shows how quickly deviations are corrected.
- In this thesis, slow or incomplete correction is interpreted as evidence consistent with bargaining power, not as automatic legal proof of abuse.
- Nonlinear Autoregressive Distributed Lag (NARDL) asymmetry is treated as a mechanism under H1 or H2, not as a separate hypothesis.
- ProZorro and retail results are interpreted as institutional and promotional mechanisms because the overlap is short.
