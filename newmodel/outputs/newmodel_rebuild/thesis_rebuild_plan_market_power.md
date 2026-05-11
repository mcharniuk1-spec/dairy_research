# Thesis Rebuild Plan: Market Power in the Dairy Value Chain in Ukraine

## Core Reframing

The thesis must no longer be framed as retail-to-farm price transmission. The research object is market power in the Ukrainian dairy value chain. Price transmission is the empirical method.

## Hypotheses

- H1: Market power exists between farm-gate raw milk producers and processors.
- H2: Market power exists between processors/procurement and downstream retail actors.

## Main Evidence Now Built

| dataset | rows | date_min | date_max | products | quality_ok_share |
| --- | --- | --- | --- | --- | --- |
| clean_farmgate_monthly | 3645 | 2015-01-01 | 2026-03-01 | raw_milk | 0.832 |
| clean_processor_monthly | 954 | 2013-01-01 | 2026-03-01 | butter, drinking_milk, hard_cheese, kefir, skim_milk_powder, sour_cream | 1 |
| clean_consumer_monthly | 8658 | 2017-01-01 | 2026-03-01 | drinking_milk, soft_cheese, sour_cream | 0.964 |
| clean_prozorro_lot_level | 16573 | 2023-01-02 | 2026-04-29 | butter, condensed_milk, cottage_cheese, cream, drinking_milk, hard_cheese, kefir, other_dairy, skim_milk_powder, soft_cheese | 1 |
| clean_retail_sku_day | 88295 | 2025-10-21 | 2026-01-08 | butter, condensed_milk, cottage_cheese, cream, drinking_milk, exclude_non_dairy, hard_cheese, kefir, other_dairy, skim_milk_powder, sour_cream, yogurt | 0.914 |
| clean_farm_volumes | 19110 | 2025-01-01 | 2026-03-01 | butter, condensed_milk, cream, drinking_milk, kefir, other_dairy, raw_milk, skim_milk_powder | 1 |
| clean_cost_index | 171 | 2015-01-01 | 2025-10-01 | livestock_products | 1 |

## Main Model Result Inventory

| model_id | hypothesis | method | n | reliability | interpretation |
| --- | --- | --- | --- | --- | --- |
| H1_farmgate_to_processor_sour_cream | H1 | ECM | 131 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.02, ECT -0.04. |
| H1_farmgate_to_prozorro_butter | H1 | ECM | 36 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.37, ECT -0.50. |
| H1_farmgate_to_prozorro_condensed_milk | H1 | ECM | 34 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.37, ECT -0.82. |
| H1_farmgate_to_prozorro_cottage_cheese | H1 | ECM | 36 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.30, ECT -0.69. |
| H1_farmgate_to_prozorro_drinking_milk | H1 | ECM | 36 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.82, ECT -0.42. |
| H1_farmgate_to_prozorro_hard_cheese | H1 | ECM | 36 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.87, ECT -0.72. |
| H1_farmgate_to_processor_butter | H1 | ECM | 131 | unreliable / appendix only | The specification is retained only as a diagnostic or appendix result. |
| H1_farmgate_to_processor_drinking_milk | H1 | ECM | 131 | unreliable / appendix only | The specification is retained only as a diagnostic or appendix result. |
| H1_farmgate_to_processor_hard_cheese | H1 | ECM | 131 | unreliable / appendix only | The specification is retained only as a diagnostic or appendix result. |
| H1_farmgate_to_processor_kefir | H1 | ECM | 131 | unreliable / appendix only | The specification is retained only as a diagnostic or appendix result. |
| H1_farmgate_to_processor_skim_milk_powder | H1 | ECM | 131 | unreliable / appendix only | The specification is retained only as a diagnostic or appendix result. |
| H1_farmgate_to_prozorro_cream | H1 | ECM | 16 | unreliable / appendix only | Too few observations for a reliable equilibrium model. |
| H1_farmgate_to_prozorro_skim_milk_powder | H1 | ECM | 25 | unreliable / appendix only | The specification is retained only as a diagnostic or appendix result. |
| H1_farmgate_to_processor_butter_asymmetry | H1 | NARDL-lite | 131 | unreliable / appendix only | Asymmetry evidence is too weak for the main text. |
| H1_farmgate_to_processor_drinking_milk_asymmetry | H1 | NARDL-lite | 131 | unreliable / appendix only | Asymmetry evidence is too weak for the main text. |
| H1_farmgate_to_processor_hard_cheese_asymmetry | H1 | NARDL-lite | 131 | unreliable / appendix only | Asymmetry evidence is too weak for the main text. |
| H1_farmgate_to_processor_kefir_asymmetry | H1 | NARDL-lite | 131 | unreliable / appendix only | Asymmetry evidence is too weak for the main text. |
| H1_farmgate_to_processor_skim_milk_powder_asymmetry | H1 | NARDL-lite | 131 | unreliable / appendix only | Asymmetry evidence is too weak for the main text. |
| H1_farmgate_to_processor_sour_cream_asymmetry | H1 | NARDL-lite | 131 | unreliable / appendix only | Asymmetry evidence is too weak for the main text. |
| H2_processor_to_consumer_drinking_milk | H2 | ECM | 111 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 0.89, ECT -0.07. |
| H2_processor_to_consumer_soft_cheese | H2 | ECM | 111 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.15, ECT -0.08. |
| H2_processor_to_prozorro_butter | H2 | ECM | 39 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.16, ECT -1.03. |
| H2_processor_to_prozorro_drinking_milk | H2 | ECM | 39 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.08, ECT -0.46. |
| H2_processor_to_prozorro_hard_cheese | H2 | ECM | 39 | probable / needs validation | The coefficient pattern is economically usable but diagnostically weaker: beta 1.38, ECT -0.87. |
| H2_processor_to_consumer_soft_cheese_asymmetry | H2 | NARDL-lite | 111 | probable / needs validation | Asymmetry is suggestive but should not be a headline claim. |
| H2_processor_to_consumer_sour_cream_asymmetry | H2 | NARDL-lite | 111 | probable / needs validation | Asymmetry is suggestive but should not be a headline claim. |
| H2_prozorro_to_pooled_retail_observed_daily_asof | H2 | Short panel OLS-HAC | 104 | probable / needs validation | Short-window retail mechanism evidence; use for H2 timing and promotion discussion, not as a long-run market-power proof. |
| H2_processor_to_consumer_drinking_milk_asymmetry | H2 | NARDL-lite | 111 | reliable | Asymmetry is statistically meaningful: positive shocks 0.29, negative shocks -0.08. |
| H2_processor_to_consumer_sour_cream | H2 | ECM | 111 | unreliable / appendix only | The specification is retained only as a diagnostic or appendix result. |
| H2_processor_to_prozorro_skim_milk_powder | H2 | ECM | 28 | unreliable / appendix only | The specification is retained only as a diagnostic or appendix result. |
| H2_prozorro_to_pooled_retail_baseline_weekly | H2 | Short panel OLS-HAC | 39 | unreliable / appendix only | Short-window retail mechanism evidence; use for H2 timing and promotion discussion, not as a long-run market-power proof. |
| H2_prozorro_to_pooled_retail_observed_weekly | H2 | Short panel OLS-HAC | 39 | unreliable / appendix only | Short-window retail mechanism evidence; use for H2 timing and promotion discussion, not as a long-run market-power proof. |
| H2_prozorro_to_pooled_retail_package_daily_asof | H2 | Short panel OLS-HAC | 402 | unreliable / appendix only | Short-window retail mechanism evidence; use for H2 timing and promotion discussion, not as a long-run market-power proof. |
| H2_prozorro_to_pooled_retail_package_weekly | H2 | Short panel OLS-HAC | 53 | unreliable / appendix only | Short-window retail mechanism evidence; use for H2 timing and promotion discussion, not as a long-run market-power proof. |

## Writing Instruction

Chapters 5 and 6 must be written from the cleaned model evidence. Paragraphs should state the empirical result, interpret it economically, connect it to market power, and return to H1 or H2.
