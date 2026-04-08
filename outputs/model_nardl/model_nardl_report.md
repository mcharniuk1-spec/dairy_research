# NARDL Summary from RW4 Primary Chain

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
- family=NARDL
- rows=3028
- source=/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/primary_chain_consolidated.xlsx

## Tables

### NARDL_Summary

| panel_level | panel_name | segment_name | product | standardized_type | retailer_panel | brand | price_variant | reconstruction_variant | farm_gate_source | frequency | intersection_rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сметана::initial::linear | Сметана | Сметана | sour_cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сметана::initial::linear | Сметана | Сметана | sour_cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сир кисломолочний::initial::linear | Сир кисломолочний | Сир кисломолочний | cottage_cheese | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сир кисломолочний::initial::linear | Сир кисломолочний | Сир кисломолочний | cottage_cheese | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сметана::initial::linear | Сметана | Сметана | sour_cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_prozorro::Сметана::initial::linear | Сметана | Сметана | sour_cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::producer_prozorro::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::producer_prozorro::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::producer_prozorro::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::producer_prozorro::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::producer_prozorro::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
