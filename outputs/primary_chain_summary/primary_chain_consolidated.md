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
- RW4 domestic vertical chain is FarmGateUA -> ProducerUA -> ProZorro -> Retail, estimated with both forward and reverse-flow pairs. Farm-gate enters from two alternative reconstruction workbooks and both linear/pchip interpolation variants are carried end-to-end.
- panel_count=104
- model_rows=2574
- reverse_rows=1137
- benchmark_rows=224

## Tables

### Consolidated_ModelCoefficients

| panel_level | panel_name | segment_name | product | standardized_type | retailer_panel | brand | price_variant | reconstruction_variant | farm_gate_source | frequency | chain_direction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | reverse |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | forward |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | forward |

### Variant_Robustness

| panel_level | segment_name | standardized_type | retailer_panel | brand | price_variant | farm_gate_source | chain_direction | stage_from | stage_to | model_family | same_sr_sign |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | FarmGateUA | ProZorro | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | FarmGateUA | ProZorro | VECM | False |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | FarmGateUA | ProducerUA | ARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | FarmGateUA | ProducerUA | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | FarmGateUA | Retail | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | FarmGateUA | Retail | VECM | False |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | ProZorro | Retail | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | ProducerUA | ProZorro | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | ProducerUA | Retail | ARDL | nan |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | ProducerUA | Retail | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | forward | ProducerUA | Retail | VECM | False |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | ProZorro | FarmGateUA | NARDL | False |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | ProZorro | ProducerUA | NARDL | False |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | ProducerUA | FarmGateUA | ARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | ProducerUA | FarmGateUA | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | Retail | FarmGateUA | ARDL | False |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | Retail | FarmGateUA | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | Retail | ProZorro | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | Retail | ProducerUA | ARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | all_missing_filled | reverse | Retail | ProducerUA | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | initial | forward | FarmGateUA | ProZorro | NARDL | True |
| average | all_products_average | all_products_average | Silpo |  | baseline | initial | forward | FarmGateUA | ProZorro | VECM | False |
| average | all_products_average | all_products_average | Silpo |  | baseline | initial | forward | FarmGateUA | ProducerUA | ARDL | nan |
| average | all_products_average | all_products_average | Silpo |  | baseline | initial | forward | FarmGateUA | ProducerUA | NARDL | False |
| average | all_products_average | all_products_average | Silpo |  | baseline | initial | forward | FarmGateUA | Retail | NARDL | True |

### FarmGate_Source_Comparison

| panel_level | segment_name | standardized_type | retailer_panel | brand | price_variant | reconstruction_variant | chain_direction | stage_from | stage_to | model_family | robust_across_reconstruction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | FarmGateUA | ProZorro | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | FarmGateUA | ProZorro | VECM | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | FarmGateUA | ProducerUA | ARDL | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | FarmGateUA | ProducerUA | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | FarmGateUA | Retail | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | FarmGateUA | Retail | VECM | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | ProZorro | Retail | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | ProducerUA | ProZorro | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | ProducerUA | Retail | ARDL | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | ProducerUA | Retail | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | forward | ProducerUA | Retail | VECM | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | ProZorro | FarmGateUA | ARDL | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | ProZorro | FarmGateUA | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | ProZorro | ProducerUA | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | ProducerUA | FarmGateUA | ARDL | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | ProducerUA | FarmGateUA | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | Retail | FarmGateUA | ARDL | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | Retail | FarmGateUA | NARDL | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | Retail | ProZorro | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | Retail | ProducerUA | ARDL | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | linear | reverse | Retail | ProducerUA | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | pchip | forward | FarmGateUA | ProZorro | NARDL | 1 |
| average | all_products_average | all_products_average | Silpo |  | baseline | pchip | forward | FarmGateUA | ProZorro | VECM | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | pchip | forward | FarmGateUA | ProducerUA | ARDL | 0 |
| average | all_products_average | all_products_average | Silpo |  | baseline | pchip | forward | FarmGateUA | ProducerUA | NARDL | 0 |

### Benchmark_Comparison

| panel_level | panel_name | segment_name | product | standardized_type | retailer_panel | brand | price_variant | reconstruction_variant | farm_gate_source | frequency | benchmark_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo |  | observed | linear | initial | daily | EU |
| product | product::Сметана::Silpo::observed::initial::linear | Сметана | Сметана | sour_cream | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Сметана::Silpo::observed::initial::linear | Сметана | Сметана | sour_cream | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Сметана::Silpo::observed::initial::linear | Сметана | Сметана | sour_cream | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Сметана::Silpo::observed::initial::linear | Сметана | Сметана | sour_cream | Silpo |  | observed | linear | initial | daily | ConsumerUA |
| product | product::Вершки::Silpo::baseline::initial::linear | Вершки | Вершки | cream | Silpo |  | baseline | linear | initial | daily | EU |
