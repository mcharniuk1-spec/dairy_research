# RW4 Primary Chain Consolidated Summary

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- RW4 domestic vertical chain is FarmGateUA -> ProducerUA -> ProZorro -> Retail, estimated with both forward and reverse-flow pairs. Farm-gate enters from two alternative reconstruction workbooks and both linear/pchip interpolation variants are carried end-to-end. Retail_combined is the anchored downstream index built from Silpo effective prices, Novus observed prices, and a level-aligned ConsumerUA anchor, while Retail_combined_core keeps the strict retailer-only overlap for robustness.
- panel_count=688
- model_rows=10141
- reverse_rows=4548
- benchmark_rows=1992

## Tables

### Consolidated_ModelCoefficients

| panel_level | panel_name | segment_name | product | standardized_type | retailer_panel | brand | price_variant | reconstruction_variant | farm_gate_source | frequency | intersection_rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |

### Variant_Robustness

| panel_level | segment_name | standardized_type | retailer_panel | brand | price_variant | intersection_rule | farm_gate_source | chain_direction | stage_from | stage_to | model_family |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | FarmGateUA | ProZorro | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | FarmGateUA | ProZorro | VECM |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | FarmGateUA | ProducerUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | FarmGateUA | ProducerUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | FarmGateUA | Retail | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | FarmGateUA | Retail | VECM |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | ProZorro | Retail | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | ProducerUA | ProZorro | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | ProducerUA | Retail | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | forward | ProducerUA | Retail | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | ProZorro | FarmGateUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | ProZorro | ProducerUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | ProducerUA | FarmGateUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | ProducerUA | FarmGateUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | Retail | FarmGateUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | Retail | FarmGateUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | Retail | ProZorro | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | Retail | ProducerUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | all_missing_filled | reverse | Retail | ProducerUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | initial | forward | FarmGateUA | ProZorro | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | initial | forward | FarmGateUA | ProZorro | VECM |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | initial | forward | FarmGateUA | ProducerUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | initial | forward | FarmGateUA | ProducerUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | initial | forward | FarmGateUA | Retail | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | initial | forward | FarmGateUA | Retail | VECM |

### FarmGate_Source_Comparison

| panel_level | segment_name | standardized_type | retailer_panel | brand | price_variant | intersection_rule | reconstruction_variant | chain_direction | stage_from | stage_to | model_family |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | FarmGateUA | ProZorro | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | FarmGateUA | ProZorro | VECM |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | FarmGateUA | ProducerUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | FarmGateUA | ProducerUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | FarmGateUA | Retail | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | FarmGateUA | Retail | VECM |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | ProZorro | Retail | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | ProducerUA | ProZorro | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | ProducerUA | Retail | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | forward | ProducerUA | Retail | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | ProZorro | FarmGateUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | ProZorro | ProducerUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | ProducerUA | FarmGateUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | ProducerUA | FarmGateUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | Retail | FarmGateUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | Retail | FarmGateUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | Retail | ProZorro | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | Retail | ProducerUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | linear | reverse | Retail | ProducerUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | pchip | forward | FarmGateUA | ProZorro | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | pchip | forward | FarmGateUA | ProZorro | VECM |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | pchip | forward | FarmGateUA | ProducerUA | ARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | pchip | forward | FarmGateUA | ProducerUA | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | pchip | forward | FarmGateUA | Retail | NARDL |
| average | all_products_average | all_products_average | Retail_combined |  | baseline | chain_common_support | pchip | forward | FarmGateUA | Retail | VECM |

### FarmGate_Direct_Summary

| stage_from | stage_to | retailer_panel | price_variant | panel_level | intersection_rule | model_family | rows_total | median_n_obs | core_finding_share | robust_linear_vs_pchip_share | robust_across_reconstruction_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FarmGateUA | ProZorro |  |  | pairwise_product | pairwise_overlap | ARDL | 8 | 190.0 | 0.0 | 0.5 | 0.0 |
| FarmGateUA | ProZorro |  |  | pairwise_product | pairwise_overlap | NARDL | 36 | 189.0 | 0.3888888888888889 | 1.0 | 0.7777777777777778 |
| FarmGateUA | ProZorro |  |  | pairwise_product | pairwise_overlap | VECM | 16 | 202.5 | 0.0 | 0.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | baseline | product | chain_common_support | ARDL | 4 | 189.0 | 0.0 | 0.5 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | observed | product | chain_common_support | ARDL | 4 | 189.0 | 0.0 | 0.5 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | baseline | average | chain_common_support | NARDL | 4 | 36.0 | 0.0 | 1.0 | 1.0 |
| FarmGateUA | ProZorro | Retail_combined | baseline | product | chain_common_support | NARDL | 16 | 181.5 | 0.25 | 1.0 | 0.75 |
| FarmGateUA | ProZorro | Retail_combined | observed | average | chain_common_support | NARDL | 4 | 36.0 | 0.0 | 1.0 | 1.0 |
| FarmGateUA | ProZorro | Retail_combined | observed | product | chain_common_support | NARDL | 16 | 181.5 | 0.25 | 1.0 | 0.75 |
| FarmGateUA | ProZorro | Retail_combined | baseline | average | chain_common_support | VECM | 4 | 38.0 | 0.0 | 0.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | baseline | product | chain_common_support | VECM | 16 | 183.5 | 0.0 | 0.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | observed | average | chain_common_support | VECM | 4 | 38.0 | 0.0 | 0.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | observed | product | chain_common_support | VECM | 16 | 183.5 | 0.0 | 0.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | dual_variant_output | comparison | comparison_panel | NARDL | 4 | 629.0 | 0.0 | 1.0 | 1.0 |
| FarmGateUA | ProZorro | Retail_combined | dual_variant_output | comparison | comparison_panel | VECM | 4 | 631.0 | 0.0 | 0.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | baseline | pairwise_product | pairwise_overlap | ARDL | 4 | 191.0 | 0.0 | 0.5 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | observed | pairwise_product | pairwise_overlap | ARDL | 4 | 191.0 | 0.0 | 0.5 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined | baseline | pairwise_product | pairwise_overlap | NARDL | 18 | 178.0 | 0.2222222222222222 | 0.8888888888888888 | 0.7777777777777778 |
| FarmGateUA | ProZorro | Retail_combined | observed | pairwise_product | pairwise_overlap | NARDL | 18 | 178.0 | 0.2222222222222222 | 0.8888888888888888 | 0.7777777777777778 |
| FarmGateUA | ProZorro | Retail_combined_core | baseline | product | chain_common_support | ARDL | 4 | 46.0 | 0.0 | 1.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined_core | observed | product | chain_common_support | ARDL | 4 | 46.0 | 0.0 | 1.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined_core | baseline | product | chain_common_support | NARDL | 13 | 46.0 | 0.15384615384615385 | 0.7692307692307693 | 0.7692307692307693 |
| FarmGateUA | ProZorro | Retail_combined_core | observed | product | chain_common_support | NARDL | 13 | 46.0 | 0.15384615384615385 | 0.7692307692307693 | 0.7692307692307693 |
| FarmGateUA | ProZorro | Retail_combined_core | baseline | average | chain_common_support | VECM | 4 | 61.0 | 0.0 | 0.0 | 0.0 |
| FarmGateUA | ProZorro | Retail_combined_core | baseline | product | chain_common_support | VECM | 16 | 47.0 | 0.0 | 0.0 | 0.0 |

### FarmGate_Reverse_Summary

| stage_from | stage_to | retailer_panel | price_variant | panel_level | intersection_rule | model_family | rows_total | median_n_obs | core_finding_share | robust_linear_vs_pchip_share | robust_across_reconstruction_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ProZorro | FarmGateUA |  |  | pairwise_product | pairwise_overlap | ARDL | 4 | 216.0 | 0.0 | 0.5 | 0.0 |
| ProZorro | FarmGateUA |  |  | pairwise_product | pairwise_overlap | ECM | 2 | 178.0 | 0.0 | 0.0 | 0.0 |
| ProZorro | FarmGateUA |  |  | pairwise_product | pairwise_overlap | NARDL | 36 | 189.0 | 0.1111111111111111 | 0.8888888888888888 | 0.8888888888888888 |
| ProZorro | FarmGateUA | Retail_combined | baseline | product | chain_common_support | ARDL | 6 | 132.0 | 0.0 | 0.6666666666666666 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | observed | product | chain_common_support | ARDL | 6 | 132.0 | 0.0 | 0.6666666666666666 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | baseline | average | chain_common_support | NARDL | 4 | 36.0 | 0.0 | 1.0 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | baseline | product | chain_common_support | NARDL | 16 | 181.5 | 0.25 | 0.875 | 0.875 |
| ProZorro | FarmGateUA | Retail_combined | observed | average | chain_common_support | NARDL | 4 | 36.0 | 0.0 | 1.0 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | observed | product | chain_common_support | NARDL | 16 | 181.5 | 0.25 | 0.875 | 0.875 |
| ProZorro | FarmGateUA | Retail_combined | dual_variant_output | comparison | comparison_panel | ECM | 2 | 626.5 | 0.0 | 1.0 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | dual_variant_output | comparison | comparison_panel | NARDL | 4 | 629.0 | 0.0 | 0.5 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | baseline | pairwise_product | pairwise_overlap | ARDL | 4 | 48.0 | 0.0 | 0.5 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | observed | pairwise_product | pairwise_overlap | ARDL | 4 | 48.0 | 0.0 | 0.5 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | baseline | pairwise_product | pairwise_overlap | ECM | 2 | 178.0 | 0.0 | 0.0 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | observed | pairwise_product | pairwise_overlap | ECM | 2 | 178.0 | 0.0 | 0.0 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined | baseline | pairwise_product | pairwise_overlap | NARDL | 18 | 178.0 | 0.16666666666666666 | 0.7777777777777778 | 0.8888888888888888 |
| ProZorro | FarmGateUA | Retail_combined | observed | pairwise_product | pairwise_overlap | NARDL | 18 | 178.0 | 0.16666666666666666 | 0.7777777777777778 | 0.8888888888888888 |
| ProZorro | FarmGateUA | Retail_combined_core | baseline | product | chain_common_support | ARDL | 8 | 46.0 | 0.0 | 0.75 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined_core | observed | product | chain_common_support | ARDL | 8 | 46.0 | 0.0 | 0.75 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined_core | baseline | product | chain_common_support | NARDL | 13 | 46.0 | 0.46153846153846156 | 0.7692307692307693 | 0.7692307692307693 |
| ProZorro | FarmGateUA | Retail_combined_core | observed | product | chain_common_support | NARDL | 13 | 46.0 | 0.46153846153846156 | 0.7692307692307693 | 0.7692307692307693 |
| ProZorro | FarmGateUA | Retail_combined_core | dual_variant_output | comparison | comparison_panel | NARDL | 1 | 184.0 | 0.0 | 0.0 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined_core | baseline | pairwise_product | pairwise_overlap | ARDL | 8 | 46.0 | 0.0 | 0.75 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined_core | observed | pairwise_product | pairwise_overlap | ARDL | 8 | 46.0 | 0.0 | 0.75 | 0.0 |
| ProZorro | FarmGateUA | Retail_combined_core | baseline | pairwise_product | pairwise_overlap | NARDL | 15 | 44.0 | 0.4 | 0.6666666666666666 | 0.8 |

### Unified_Retail_Comparison

| comparison_block | retailer_panel | price_variant | chain_direction | stage_from | stage_to | intersection_rule | model_family | rows_total | products_total | median_source_count | anchor_only_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| data | Retail_combined |  |  |  |  |  |  | 9 | 9.0 | 15.0 | nan |
| data | Retail_combined_core |  |  |  |  |  |  | 9 | 9.0 | 12.0 | nan |
| model | Retail_combined | baseline | forward | FarmGateUA | Retail | chain_common_support | NARDL | 20 | nan | nan | nan |
| model | Retail_combined | baseline | forward | FarmGateUA | Retail | chain_common_support | VECM | 4 | nan | nan | nan |
| model | Retail_combined | baseline | forward | FarmGateUA | Retail | pairwise_overlap | ARDL | 28 | nan | nan | nan |
| model | Retail_combined | baseline | forward | FarmGateUA | Retail | pairwise_overlap | ECM | 28 | nan | nan | nan |
| model | Retail_combined | baseline | forward | FarmGateUA | Retail | pairwise_overlap | NARDL | 60 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProZorro | Retail | chain_common_support | ARDL | 4 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProZorro | Retail | chain_common_support | NARDL | 20 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProZorro | Retail | pairwise_overlap | ARDL | 4 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProZorro | Retail | pairwise_overlap | NARDL | 20 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProducerUA | Retail | chain_common_support | ARDL | 18 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProducerUA | Retail | chain_common_support | NARDL | 18 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProducerUA | Retail | pairwise_overlap | ARDL | 14 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProducerUA | Retail | pairwise_overlap | ECM | 8 | nan | nan | nan |
| model | Retail_combined | baseline | forward | ProducerUA | Retail | pairwise_overlap | NARDL | 16 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | FarmGateUA | chain_common_support | ARDL | 8 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | FarmGateUA | chain_common_support | NARDL | 20 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | FarmGateUA | pairwise_overlap | ARDL | 25 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | FarmGateUA | pairwise_overlap | ECM | 26 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | FarmGateUA | pairwise_overlap | NARDL | 60 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | ProZorro | chain_common_support | ARDL | 8 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | ProZorro | chain_common_support | NARDL | 20 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | ProZorro | pairwise_overlap | ARDL | 8 | nan | nan | nan |
| model | Retail_combined | baseline | reverse | Retail | ProZorro | pairwise_overlap | NARDL | 20 | nan | nan | nan |

### Intersection_Stability

| intersection_rule | stage_from | stage_to | retailer_panel | model_family | rows_total | median_n_obs | core_finding_share | robust_linear_vs_pchip_share | robust_across_reconstruction_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pairwise_overlap | FarmGateUA | ProZorro |  | ARDL | 8 | 190.0 | 0.0 | 0.5 | 0.0 |
| pairwise_overlap | FarmGateUA | ProZorro |  | NARDL | 36 | 189.0 | 0.3888888888888889 | 1.0 | 0.7777777777777778 |
| pairwise_overlap | FarmGateUA | ProZorro |  | VECM | 16 | 202.5 | 0.0 | 0.0 | 0.0 |
| chain_common_support | FarmGateUA | ProZorro | Retail_combined | ARDL | 8 | 189.0 | 0.0 | 0.5 | 0.0 |
| chain_common_support | FarmGateUA | ProZorro | Retail_combined | NARDL | 40 | 176.0 | 0.2 | 1.0 | 0.8 |
| chain_common_support | FarmGateUA | ProZorro | Retail_combined | VECM | 40 | 178.0 | 0.0 | 0.0 | 0.0 |
| comparison_panel | FarmGateUA | ProZorro | Retail_combined | NARDL | 4 | 629.0 | 0.0 | 1.0 | 1.0 |
| comparison_panel | FarmGateUA | ProZorro | Retail_combined | VECM | 4 | 631.0 | 0.0 | 0.0 | 0.0 |
| pairwise_overlap | FarmGateUA | ProZorro | Retail_combined | ARDL | 8 | 191.0 | 0.0 | 0.5 | 0.0 |
| pairwise_overlap | FarmGateUA | ProZorro | Retail_combined | NARDL | 36 | 178.0 | 0.2222222222222222 | 0.8888888888888888 | 0.7777777777777778 |
| chain_common_support | FarmGateUA | ProZorro | Retail_combined_core | ARDL | 8 | 46.0 | 0.0 | 1.0 | 0.0 |
| chain_common_support | FarmGateUA | ProZorro | Retail_combined_core | NARDL | 26 | 46.0 | 0.15384615384615385 | 0.7692307692307693 | 0.7692307692307693 |
| chain_common_support | FarmGateUA | ProZorro | Retail_combined_core | VECM | 40 | 48.0 | 0.0 | 0.0 | 0.0 |
| comparison_panel | FarmGateUA | ProZorro | Retail_combined_core | NARDL | 1 | 184.0 | 0.0 | 0.0 | 0.0 |
| comparison_panel | FarmGateUA | ProZorro | Retail_combined_core | VECM | 4 | 186.0 | 0.0 | 0.0 | 0.0 |
| pairwise_overlap | FarmGateUA | ProZorro | Retail_combined_core | ARDL | 8 | 46.0 | 0.0 | 1.0 | 0.0 |
| pairwise_overlap | FarmGateUA | ProZorro | Retail_combined_core | NARDL | 30 | 44.0 | 0.13333333333333333 | 0.6666666666666666 | 0.8 |
| brand_top_sku | FarmGateUA | ProZorro | Silpo | ARDL | 10 | 41.0 | 0.0 | 0.8 | 0.0 |
| brand_top_sku | FarmGateUA | ProZorro | Silpo | NARDL | 30 | 39.0 | 0.13333333333333333 | 0.8 | 0.8 |
| brand_top_sku | FarmGateUA | ProZorro | Silpo | VECM | 32 | 39.5 | 0.0 | 0.0 | 0.0 |
| chain_common_support | FarmGateUA | ProZorro | Silpo | ARDL | 10 | 41.0 | 0.0 | 0.8 | 0.0 |
| chain_common_support | FarmGateUA | ProZorro | Silpo | NARDL | 34 | 39.0 | 0.0 | 0.8235294117647058 | 0.7058823529411765 |
| chain_common_support | FarmGateUA | ProZorro | Silpo | VECM | 40 | 41.0 | 0.0 | 0.0 | 0.0 |
| pairwise_overlap | FarmGateUA | ProZorro | Silpo | ARDL | 10 | 41.0 | 0.0 | 0.8 | 0.0 |
| pairwise_overlap | FarmGateUA | ProZorro | Silpo | NARDL | 26 | 36.0 | 0.0 | 0.7692307692307693 | 0.6153846153846154 |

### Benchmark_Comparison

| panel_level | panel_name | segment_name | product | standardized_type | retailer_panel | brand | price_variant | reconstruction_variant | farm_gate_source | frequency | intersection_rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сметана::initial::linear | Сметана | Сметана | sour_cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сметана::initial::linear | Сметана | Сметана | sour_cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сметана::initial::linear | Сметана | Сметана | sour_cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сметана::initial::linear | Сметана | Сметана | sour_cream |  |  |  | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::producer_prozorro::Вершки::initial::linear | Вершки | Вершки | cream |  |  |  | linear | initial | daily | pairwise_overlap |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/farmgate_direct_heatmap.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/farmgate_reverse_corefinding.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/unified_retail_comparison.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/intersection_stability.png
