# Dairy Research Repository

## Current Final Model Stack

The current thesis-facing model package is in [`newmodel/`](newmodel/). It contains the final V10 market-power thesis draft, the raw `Newmodel_data` workbooks, cleaned model data, final tables/figures, reports, and portable Python runners.

Use this first for the latest draft:

- Final draft: `newmodel/doc/Maksym_Charniuk_MSc_thesis_market_power_rewritten_v10.docx`
- Full setup and model description: `newmodel/README.md`
- Final V10 outputs: `newmodel/outputs/market_power_final_v10/`
- Main model-stack outputs: `newmodel/outputs/newmodel_deep_rebuild_v2/`

The older root-level package below is retained as the earlier `FINAL_RESEARCH` rerun and validation archive.

# FINAL_RESEARCH

This folder contains the corrected, reproducible rerun of the dairy price-transmission thesis pipeline built on `full_uah_final.xlsx`.

The project is designed as one self-contained empirical system: source materials, processed data, econometric outputs, figures, run logs, and thesis-style writing are stored here so the analysis can be reopened without relying on scattered external files.

## Research scope
- Topic: vertical price transmission in Ukraine's dairy chain.
- Core chain: FarmGate Ukraine average -> Producer Ukraine average -> ProZorro procurement price -> downstream retail endpoint.
- Downstream mechanisms: Silpo discount behavior, Novus comparison, retail spread behavior, and consumer-benchmark comparison.
- System extensions: aggregate chain indices and widened VECM robustness blocks.

## Folder structure
```text
FINAL_RESEARCH/
├── code/                     Reproducible Python scripts for the pipeline and companion documents
├── data/                     Final processed datasets used by the modelling system
├── documents/                Thesis-ready chapter text and workflow/result companions
├── figures/                  Full graph system, split into chapter, sequence, and model-specific folders
├── logs/                     Run summary and execution notes
├── materials/                Inputs, references, and instruction documents used by the project
├── outputs/                  Model outputs, summaries, chapter tables, and per-model exports
└── README.md                 This guide
```

## Key entry points
- `code/final_research_pipeline.py`: main end-to-end pipeline and output writer.
- `code/generate_stepbystep_doc.py`: generates the workflow explanation document.
- `code/generate_stepbystep_results.py`: generates the result-by-result companion and refreshes the chapter package.
- `materials/inputs/full_uah_final.xlsx`: corrected governmental source workbook.
- `materials/inputs/full_uah_final_whatadded_matched_smoothed.xlsx`: final matched/smoothed modelling workbook used by the pipeline.
- `outputs/final_research_outputs.xlsx`: master workbook with the main processed tables and model summaries.
- `outputs/integrated_summary_workbook.xlsx`: compact summary workbook for fast review.
- `documents/Chapter5_6_analysis.docx`: thesis-style Chapter 5 and Chapter 6 document for the dissertation.
- `documents/stepbystep.docx`: workflow explanation of transformations, datasets, and models.
- `documents/stepbystep_results.docx`: result-by-result companion with figures and short interpretations.
- `logs/run_summary.md`: compact run note with the main counts and retained model families.

## Materials
### `materials/inputs/`
- `full_uah_final.xlsx`: corrected FarmGateUA, ProducerUA, and ConsumerUA source workbook used as the base truth.
- `full_uah_final_whatadded_matched_smoothed.xlsx`: final modelling workbook with matched and smoothed panels used in the rerun.
- `full_uah_final_whatadded_matched_smoothed.xlsx 2.xlsx`: duplicate save kept for traceability because it was part of the working project history.

### `materials/references/`
- `Charniuk_Maksym_MScThesis_Draft_correctedformat.docx`: thesis-format and writing reference for Chapters 5 and 6.
- `data_estiamtion_updated_conclusion_fullversion.md`: earlier integrated chapter text used as a comparison and transition reference.

### `materials/instructions/`
- Correction and methodology notes used during the rebuild, including formatting guidance and data-method summaries.

## Processed data (`data/`)
- `product_dictionary_standardized.csv`: standardized product taxonomy across governmental, procurement, and retail layers.
- `product_audit_long.csv`: long-form product-definition audit across sources.
- `final_daily_panel.csv`: final modelling panel at daily frequency.
- `final_weekly_panel.csv`: weekly median modelling panel used for long-run specifications.
- `intersection_admissibility.csv`: strong / acceptable / weak / unusable overlap classification.
- `final_panel_coverage.csv`: source coverage and overlap audit.
- `aggregate_chain_index_daily.csv`, `aggregate_chain_index_weekly.csv`, `aggregate_chain_index_weights.csv`: aggregate dairy-chain index series and weights.
- `retail_items_full_harmonized.csv`: cleaned SKU-level retail archive used to build category-level retail prices.
- `retail_item_catalog.csv`, `retail_match_audit.csv`, `retail_name_reconciliation_examples.csv`: retail matching and harmonization audit outputs.
- `retail_brand_daily.csv`, `retail_brand_support.csv`: brand-level retail panels and support measures.
- `retail_level_scores.csv`, `retail_level_selection.csv`, `retail_optimal_daily.csv`: downstream endpoint selection and chosen retail layer.
- `consumerua_clean_daily.csv`, `cme_class3_daily.csv`, `europe_benchmark_daily.csv`: benchmark and cleaned supporting series.

## Outputs (`outputs/`)
### Main workbooks and summaries
- `final_research_outputs.xlsx`: main results workbook used for integrated review.
- `integrated_summary_workbook.xlsx`: condensed cross-model summary workbook.
- `core_chain_models.csv`, `discount_strategy_models.csv`, `procurement_scale_models.csv`, `aggregate_index_models.csv`, `aggregate_index_vecm.csv`: model-family exports.
- `lag_correlation_scan.csv`, `link21_summary.csv`, `model_reliability_overview.csv`, `robust_findings.csv`: core screening and synthesis outputs.

### Chapter tables
- `outputs/chapter_tables/`: thesis-facing tables used by `Chapter5_6_analysis.docx`.

### Per-model exports
- `outputs/single_model_tables/`: one compact results file for each weekly specification and special model block.
- `outputs/single_model_diagnostics/`: diagnostics saved per retained model.
- `outputs/single_model_notes/`: plain-language notes and interpretation fragments per model.

### VECM detail
- `outputs/vecm_detail/`: table-by-table VECM exports, including stationarity, lag selection, Johansen tests, alpha/beta, speed of adjustment, IRF, and FEVD where feasible.

## Figures (`figures/`)
- Top-level numbered PNGs: integrated figure inventory covering the whole project.
- `chapter5_data/`: figures used or considered for the data chapter.
- `chapter6_results/`: figures used or considered for the results chapter.
- `sequence/`: figures ordered by execution logic, from raw data to final model interpretation.
- `model_specific/`: reserved for additional model-specific visuals.
- `reliability/`: reserved for reliability-oriented visuals.

## Documents (`documents/`)
- `Chapter5_6_analysis.docx/.md/.html`: final thesis chapter package.
- `stepbystep.docx/.md/.html`: methodological walkthrough of the final research sequence.
- `stepbystep_results.docx/.md/.html`: comprehensive results companion with figures and short interpretations.

## Logs (`logs/`)
- `run_summary.md/.txt/.html`: compact execution note with the current model counts and main retained result signal.

## Current run status
- Product dictionary rows: 28
- Strong intersections: 1
- Acceptable intersections: 4
- Weak-extension intersections: 10
- Reliable core models: 30
- Conditionally usable core models: 21
- Feasible VECM systems: 3
- Discount strategy signals: 2
- Procurement-scale signals: 5
- Strongest lag signal: Sour cream | FarmGate -> Producer | corr 0.932 | lag 0 weeks

## Execution order
1. Load the corrected governmental source workbook and validate the active sheets.
2. Run the product-definition audit across governmental, procurement, and retail sources.
3. Build cleaned retail product mappings, brand support tables, and the final daily panel.
4. Construct weekly medians and controlled smoothing variants for long-run modelling.
5. Score intersections and classify admissibility before estimation.
6. Run the first strict weekly screening pass.
7. Apply explicit post-test adaptation when strict overlap remains too thin.
8. Estimate weekly ECM and NARDL retained models, while keeping ARDL screening outputs for traceability.
9. Estimate daily local projections, vertical spread models, Silpo discount models, and procurement-scale models.
10. Estimate aggregate chain index models and widened system/VECM robustness blocks where feasible.
11. Export separate model tables, diagnostics, notes, chapter tables, and VECM detail tables.
12. Generate figures, summaries, and the thesis-style chapter and companion documents.

## How to use this folder
1. Open `documents/Chapter5_6_analysis.docx` if you want the thesis-ready narrative first.
2. Open `logs/run_summary.md` if you want the current high-level status in one page.
3. Open `outputs/final_research_outputs.xlsx` for the integrated numerical output.
4. Open `documents/stepbystep.docx` to understand the data-construction and modelling sequence.
5. Open `documents/stepbystep_results.docx` if you want all interpretable outputs and the full figure appendix.
6. Use `outputs/single_model_tables/`, `outputs/single_model_diagnostics/`, and `outputs/single_model_notes/` for model-by-model inspection.

## Reproducibility note
- The folder is organized so the core source materials used by the rerun are stored in `materials/` and the generated outputs are stored inside the project itself.
- The modelling outputs currently present in `outputs/` are the active final rerun outputs; this README documents that state rather than promising a fresh rerun on every open.
