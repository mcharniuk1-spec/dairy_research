# RW4 Audit And Status

## Scope

This nested repository now runs the RW4 dairy transmission workflow centered on:

- `common.py`
- `rw4_data.py`
- `rw2_extended_mapping_pipeline.py`
- `vpt_primary_chain.py`
- `model_worker.py`
- `sheet_worker.py`
- `run_all_rw4.py`
- `run_total_run.py`

## Inputs

The active RW4 pipeline uses:

- `full_uah.xlsx`
- `farm_gate_daily.xlsx`
- `farm_gate_all_missing_filled_daily.xlsx`

## Current RW4 Design

- The domestic chain is modeled as `FarmGateUA -> ProducerUA -> ProZorro -> Retail`.
- Reverse-flow estimation is included for `Retail -> ProZorro -> ProducerUA -> FarmGateUA`.
- Farm-gate is carried with both `initial` and `all_missing_filled` sources.
- Producer and farm-gate reconstruction are carried with both `linear` and `pchip` variants.
- Retail uses observed and baseline price definitions, with promo-state metadata preserved.
- Benchmark series `ConsumerUA`, `EU`, and `CME` are used as external checks rather than endogenous chain stages.

## Verified Outputs

The latest validated RW4 outputs are:

- `outputs/primary_chain_summary/primary_chain_consolidated.xlsx`
- `outputs/run_all_summary/run_all_rw4_summary.xlsx`
- `outputs/total_run/Total_Run.xlsx`

The consolidated primary-chain workbook now includes:

- `Consolidated_ModelCoefficients`
- `ReverseFlow_ModelCoefficients`
- `RawMilk_To_Product_Transmission`
- `AveragePrice_Chain_Transmission`
- `Retailer_Brand_Transmission`
- `Variant_Robustness`
- `FarmGate_Source_Comparison`
- `Benchmark_Comparison`
- `Coverage_Validation`
- `Reconstruction_Diagnostics`
- `Mapping_Audit`
- `Unit_Admissibility`

## Remaining Interpretation Caveats

- Brand-level Silpo transmission is estimable and included; Novus brand support is much thinner, so many brand results remain weak or non-core.
- Promo-state model sheets are populated, but for this data the incidence/type/depth equations are currently recorded as unavailable when the underlying state variation or convergence is not strong enough.
- Core findings should still be interpreted only when robustness flags support stability across interpolation variants and farm-gate sources.

## RW4 Entry Points

Run the modular RW4 pipeline:

```bash
python3 run_all_rw4.py
```

Run the modular pipeline and rebuild the combined Total Run:

```bash
python3 run_total_run.py
```
