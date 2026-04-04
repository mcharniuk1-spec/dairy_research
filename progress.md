# RW4 Upgrade Progress

Latest implementation pass:

- moved active pipeline orchestration to `run_all_rw4.py`,
- updated `run_total_run.py` to use RW4,
- fixed repo-root data loading so the nested repo uses its own workbooks,
- added auditable product mapping in `product_dictionary.csv`,
- added `rw4_data.py` for:
  - farm-gate workbook loading,
  - unit admissibility,
  - retail baseline reconstruction,
  - promo-state enrichment,
  - mapping audit,
  - reconstruction diagnostics,
- upgraded `vpt_primary_chain.py` to:
  - include `FarmGateUA_initial` and `FarmGateUA_filled`,
  - run both `linear` and `pchip` upstream variants,
  - estimate forward and reverse-flow links,
  - produce RW4 robustness and benchmark tables,
- upgraded `model_worker.py` discount module to output promo-state incidence/type/depth plus synthesis tables,
- updated `README.md` for RW4.

Remaining validation task:

- run `python3 run_total_run.py` end to end in the local virtualenv and inspect any runtime/model admissibility issues that still need tuning.
