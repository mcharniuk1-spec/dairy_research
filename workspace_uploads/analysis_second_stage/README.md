# Analysis Second Stage

This folder contains a non-destructive second-stage robustness redesign for the master thesis dairy price-transmission analysis.

## Main Files
- `run_second_stage_analysis.py`: reproducible runner for the second-stage daily panel, local-projection models, margin/market-power proxy models, discount models, figures, and documents.
- `outputs/second_stage_model_outputs.xlsx`: consolidated workbook of model outputs.
- `data/second_stage_daily_panel.csv`: cleaned model panel.
- `documents/second_stage_estimation_summary.md`: thesis-style estimation summary with figure references.
- `documents/second_stage_data_estiamtion_updated_conclusion.docx`: thesis-style second-stage chapter document aligned to the main draft structure.
- `documents/corrected_format_additions_bold.md`: separate bolded correction/addition notes for the corrected-format draft.

## Method Note
The second-stage design intentionally differs from RW4. It uses local projections and spread/discount proxy equations instead of repeating the same ARDL, ECM, NARDL, and VECM model ladder.

The current version also adds deeper retail preparation: harmonized Silpo-Novus item keys, dairy-only literal product typing, brand/item reconciliation outputs, tested downstream retail levels, an optimal retail endpoint, and a ConsumerUA-linked retail endpoint.