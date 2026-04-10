# Second-Stage Verification Log

Run date: 2026-04-07

Workspace: `/Users/getapple/Documents/KSE/Master Thesis`

## Execution

- Runner executed successfully with the project virtual environment:
  - `Main materials/Model/Charniuk_Dairy_Research/.venv/bin/python analysis second stage/run_second_stage_analysis.py`
- Output workbook created:
  - `analysis second stage/outputs/second_stage_model_outputs.xlsx`
- Main summary documents created:
  - `analysis second stage/documents/second_stage_estimation_summary.md`
  - `analysis second stage/documents/second_stage_estimation_summary.html`
  - `analysis second stage/documents/second_stage_estimation_summary.docx`
  - `analysis second stage/documents/corrected_format_additions_bold.md`
  - `analysis second stage/documents/corrected_format_additions_bold.html`
  - `analysis second stage/documents/corrected_format_additions_bold.docx`

## Output Checks

- `second_stage_model_outputs.xlsx` contains the expected sheets:
  - `README`
  - `Data_Inventory`
  - `Panel_Coverage`
  - `Local_Projections`
  - `LP_Summary`
  - `Margin_Models`
  - `Spread_Summary`
  - `Discount_Models`
  - `Robust_Findings`
- Key populated table sizes:
  - `Local_Projections`: 2,628 rows
  - `LP_Summary`: 66 rows
  - `Margin_Models`: 130 rows
  - `Discount_Models`: 4 rows
  - `Robust_Findings`: 125 rows
- Figure files validated as readable PNGs:
  - `01_panel_coverage.png`
  - `02_lp_pass_through_horizons.png`
  - `03_forward_reverse_core_share.png`
  - `04_vertical_spread_proxy.png`
  - `05_discount_incidence.png`
- DOCX companion files passed ZIP integrity checks:
  - `second_stage_estimation_summary.docx`
  - `corrected_format_additions_bold.docx`
- Script syntax was checked with Python AST parsing.

## Notes

- `python3 -m compileall` was not used as the final syntax check because the default macOS Python cache path is outside the sandbox. The AST syntax parse avoids writing cache files and completed successfully.
- The Casey thesis/reference was not found by filename or searchable DOCX text. The correction file records this limitation explicitly.
