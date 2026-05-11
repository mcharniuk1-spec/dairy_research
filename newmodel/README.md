# Final Newmodel Stack: Ukrainian Dairy Market Power Thesis

This folder is the self-contained GitHub package for the final model stack used in `Maksym_Charniuk_MSc_thesis_market_power_rewritten_v10.docx`.

The final draft studies market power in Ukraine's dairy value chain. It narrows the thesis to two hypotheses:

1. **H1:** processor market power can appear between farm-gate raw milk suppliers and dairy processors when processor prices do not adjust fully, quickly, or symmetrically to farm-gate changes.
2. **H2:** retailer/downstream buyer power can appear between processors and consumer-facing or procurement channels when downstream prices, discounts, or procurement prices absorb shocks unevenly.

The V10 draft deliberately separates price-link evidence, adjustment evidence, and market-power interpretation. A significant coefficient is not treated as automatic proof of market power.

## Repository Layout

```text
newmodel/
├── data/Newmodel_data/                         Raw and component workbooks
├── doc/                                        Final V10 thesis DOCX
├── doc/source/                                 Draft 2 style shell and feedback/transcript inputs
├── outputs/newmodel_rebuild/                   First audited rebuild outputs
├── outputs/newmodel_deep_rebuild_v2/           Main model stack: clean data, figures, model tables, reports
├── outputs/market_power_final_v10/             Final draft tables, figures, QA, reliability audits
├── references/loy2016.pdf                      Reference paper used for the Loy-style mechanism check
├── scripts/newmodel_market_power_rebuild.py    First rebuild runner
├── scripts/deep_market_power_rebuild_v2.py     Main model-stack runner
├── scripts/build_market_power_thesis_final_v10.py  Final DOCX/table/figure builder
└── requirements.txt                            Python dependencies
```

## Current Final Draft

- `doc/Maksym_Charniuk_MSc_thesis_market_power_rewritten_v10.docx`
- Build report: `outputs/market_power_final_v10/reports/final_v10_build_report.md`
- QA JSON: `outputs/market_power_final_v10/reports/final_v10_docx_qa.json`
- Reliability audit: `outputs/market_power_final_v10/reports/final_v10_reliability_audit.md`

The V10 QA recorded 416 paragraphs, 21 tables, 35 embedded images, about 14,733 words, and successful DOCX package/style/image checks. LibreOffice rendering was not used because the local `soffice` binary crashed in earlier runs.

## Data Inputs

`data/Newmodel_data/newmodel.xlsx` is the integrated workbook used by the final model stack.

Component workbooks are retained under `data/Newmodel_data/parts of main dataset/`:

- `Farm_milk_2015.xlsx`
- `Processor_2013_2026.xlsx`
- `Consumer_2017_2026.xlsx`
- `Prozorro2023_2026.xlsx`
- `farm_volumes.xlsx`

Additional market/context inputs are retained under `data/Newmodel_data/additioanl materials/`, including trade workbooks and the livestock cost index workbook.

## Mandatory Data Corrections

The final model stack applies these audit corrections before interpretation:

- Processor prices are converted from UAH/tonne to UAH/kg.
- Farm-gate milk prices are treated as tonne-level magnitudes and converted to UAH/kg.
- ProZorro numeric strings with non-breaking spaces are repaired before unit-price construction.
- Retail products are reclassified from `product_title` and `product_name`; analytical outputs use a controlled `product` column.
- Retail baby food, desserts, plant-based drinks, and non-dairy products are excluded before dairy classification.

## Model Stack

Main outputs live in `outputs/newmodel_deep_rebuild_v2/`.

Key tables:

- `tables/integrated_evidence_register_v2.csv`: combined evidence register across new and previous model families.
- `tables/model_selection_H1_H2_v2.csv`: selected H1/H2 model evidence after reliability screening.
- `tables/additional_models_dols_lp_threshold_v2.csv`: DOLS, local-projection, and threshold-style alternatives.
- `tables/loy_style_first_stage_v2.csv` and `tables/loy_style_second_stage_v2.csv`: mechanism checks inspired by Loy et al.
- `tables/old_new_dataset_validation_v2.csv`: validation bridge between old reconstructed outputs and observed-data outputs.

Final V10 thesis-facing tables live in `outputs/market_power_final_v10/tables/`.

Final V10 thesis-facing figures live in `outputs/market_power_final_v10/figures/`.

## Reliability Hierarchy

The final thesis uses observed Ukrainian monthly SSSU data as the core empirical base. ProZorro procurement and Silpo/Novus retail observations are mechanism evidence. Earlier reconstructed daily/weekly outputs are retained only as validation or appendix support when overlap, mapping, coefficient size, direction, and diagnostics are acceptable.

Practical reading order:

1. Open the final thesis DOCX in `doc/`.
2. Read `outputs/market_power_final_v10/reports/final_v10_build_report.md`.
3. Inspect `outputs/market_power_final_v10/tables/main_h1_models_v10.csv` and `main_h2_models_v10.csv`.
4. Use `outputs/newmodel_deep_rebuild_v2/tables/integrated_evidence_register_v2.csv` for the full model inventory.
5. Use `outputs/newmodel_deep_rebuild_v2/clean_data/` to inspect cleaned data used by the model stack.

## Reproducible Setup

From the repository root:

```bash
cd newmodel
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/build_market_power_thesis_final_v10.py
```

To rerun the deeper model package:

```bash
cd newmodel
python scripts/deep_market_power_rebuild_v2.py
```

Both scripts default to the portable `newmodel/` folder. To rerun against the original local thesis workspace instead, set `THESIS_ROOT`:

```bash
THESIS_ROOT="/Users/getapple/Documents/KSE/Master Thesis" python scripts/build_market_power_thesis_final_v10.py
```

## Status

This GitHub package contains the final V10 draft, raw model workbooks, cleaned model outputs, final tables/figures, build reports, and the runners needed to reproduce the published model stack.
