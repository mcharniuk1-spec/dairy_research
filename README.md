# RW4 Dairy Price Transmission Pipeline

This repository now runs the RW4 vertical price transmission workflow directly from the nested project root:

- `/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research`

RW4 extends the earlier modular workflow with:

- two alternative farm-gate reconstruction workbooks,
- explicit `linear` and `pchip` upstream variants,
- stricter unit admissibility for level/cointegration models,
- a four-stage domestic chain `FarmGateUA -> ProducerUA -> ProZorro -> Retail`,
- reverse-flow estimation `Retail -> ProZorro -> ProducerUA -> FarmGateUA`,
- promo-state outputs for Silpo,
- robustness tables across interpolation and farm-gate sources,
- RW4 run-all and Total Run outputs.

## Inputs

Core workbooks in this repo root:

- `full_uah.xlsx`
- `farm_gate_daily.xlsx`
- `farm_gate_all_missing_filled_daily.xlsx`

Supporting workbooks remain available for legacy and auxiliary modules:

- `Silpo.xlsx`
- `Novus_newest.xlsx`
- `EJgxfgP_daily_interpolated.xlsx`

## Main Files

- `common.py`: shared loading, writing, plotting, and repo-root path setup.
- `rw4_data.py`: RW4 data contracts, auditable product mapping, farm-gate loading, unit admissibility, promo-state enrichment.
- `rw2_extended_mapping_pipeline.py`: shared descriptive/test utilities and daily-panel helpers used by RW4 modules.
- `vpt_primary_chain.py`: RW4 core transmission engine and consolidated summary builder.
- `model_worker.py`: family reports, promo-state models, intersection checks, forecasts, and synthetic consumer module.
- `graph_worker.py`: graph outputs.
- `sheet_worker.py`: source-level diagnostics for every sheet/workbook source.
- `run_all_rw4.py`: full RW4 execution.
- `run_total_run.py`: RW4 execution plus combined Total Run workbook/PDF/markdown.

## Primary Outputs

RW4 consolidated chain outputs are written to:

- `outputs/primary_chain_summary/primary_chain_consolidated.xlsx`
- `outputs/primary_chain_summary/primary_chain_consolidated.pdf`

Key required sheets include:

- `Consolidated_ModelCoefficients`
- `ReverseFlow_ModelCoefficients`
- `RawMilk_To_Product_Transmission`
- `AveragePrice_Chain_Transmission`
- `Retailer_Brand_Transmission`
- `Variant_Robustness`
- `FarmGate_Source_Comparison`
- `Benchmark_Comparison`
- `Reconstruction_Diagnostics`
- `Mapping_Audit`
- `Unit_Admissibility`

Promo-state outputs are written to:

- `outputs/model_discounts/model_discounts_output.xlsx`

Run-all outputs are written to:

- `outputs/run_all_summary/run_all_rw4_summary.xlsx`
- `outputs/run_all_summary/run_all_rw4_summary.pdf`
- `outputs/run_all_summary/run_all_rw4_summary.md`

Combined Total Run outputs are written to:

- `outputs/total_run/Total_Run.xlsx`
- `outputs/total_run/Total_Run.pdf`
- `outputs/total_run/Total_Run.md`

## Running

Run the full RW4 pipeline:

```bash
python3 run_all_rw4.py
```

Run the full pipeline plus rebuild Total Run:

```bash
python3 run_total_run.py
```

Rebuild Total Run only from existing outputs:

```bash
python3 run_total_run.py --skip-run-all
```

## Current Modeling Rules

- Farm-gate enters from both `farm_gate_daily.xlsx` and `farm_gate_all_missing_filled_daily.xlsx`.
- Upstream producer/farm-gate runs are carried with both `linear` and `pchip` reconstructions.
- `ConsumerUA`, `EU`, and `CME III` are benchmark/check series, not endogenous chain stages.
- Silpo uses both observed and baseline price states; Novus stays observed-only.
- Findings should be treated as core only when they are stable across interpolation variants and farm-gate sources.
