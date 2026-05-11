# Newmodel Materials: Market Power in the Dairy Value Chain in Ukraine

This folder contains the model materials used for the rebuilt market-power thesis draft.

## Core files

- `data/Newmodel_data/`: raw and component workbooks for the integrated model dataset.
- `scripts/deep_market_power_rebuild_v2.py`: cleaning, audit, model-selection, and evidence-register pipeline.
- `scripts/build_market_power_thesis_final_v10.py`: thesis DOCX builder using Draft 2 formatting.
- `outputs/newmodel_deep_rebuild_v2/`: cleaned data, figures, tables, reports, and model outputs from the main rebuild.
- `outputs/newmodel_rebuild/`: earlier rebuild outputs retained for validation and comparison.
- `outputs/market_power_final_v10/`: final V10 tables, figures, reports, and reliability audits.
- `doc/Maksym_Charniuk_MSc_thesis_market_power_rewritten_v10.docx`: current rebuilt thesis draft.

## Reliability hierarchy

The final thesis uses observed Ukrainian monthly State Statistics Service of Ukraine (SSSU) data as the main empirical base. ProZorro and Silpo/Novus evidence is used as procurement and retail mechanism evidence. Old model and reconstruction outputs are retained for validation and appendix/supporting use only when they pass overlap, product-mapping, and diagnostic checks.

## Mandatory data-audit corrections

- Processor prices are converted from hryvnia per tonne to Ukrainian hryvnia per kilogram (UAH/kg).
- Farm-gate milk prices are treated as tonne-level magnitudes and converted to UAH/kg.
- ProZorro text numbers with non-breaking spaces are repaired before unit-price construction.
- Retail products are reclassified from `product_title` and `product_name`; every analytical table must contain a controlled `product` column.

## Current thesis draft

The latest draft is V10. It corrects the evidence hierarchy by separating:

1. price-link evidence,
2. adjustment evidence,
3. market-power interpretation.

This prevents significant long-run slopes from being overinterpreted as automatic proof of market power.
