# Final V10 Build Report

## What changed

- Built from `draft/Maksym_Charniuk_MSc_thesis_draft_2.docx` to preserve Draft 2 styles.
- Preserved the Draft 2 literature-review chapter structure and content, with one framing sentence.
- Rewrote Introduction, Market Analysis, Methodology, Data, Results, Conclusion, Works Cited, and Appendix around market power and two hypotheses.
- Used `newmodel.xlsx` as the main dataset and explicitly named raw SSSU source variables in Ukrainian.
- Added mandatory audit coverage for farm-gate tonne magnitudes, processor tonne units, ProZorro non-breaking-space numbers, and retail product reclassification.
- Demoted old reconstructed and retail short-window evidence unless validation and overlap justify supporting use.
- Cleaned the Works Cited list into a curated Chicago author-date bibliography and repaired preserved literature-review citation punctuation.
- Added a Loy-style descriptive-statistics table for the cleaned Chapter 5 data and clearer β/λ result-table notation.
- Added a short OLS/IV/Lerner Index identification boundary, rather than estimating an unreliable direct markup model from unavailable margin and cost data.
- Added concise 2024 sector facts from AgroTimes, MilkUA.info, and Opendatabot to strengthen the market-structure motivation.
- Avoided LibreOffice/soffice validation because the local application crashes; used DOCX package QA instead.

## QA

```json
{
  "docx": "/Users/getapple/Documents/KSE/Master Thesis/output/doc/Maksym_Charniuk_MSc_thesis_market_power_rewritten_v10.docx",
  "exists": true,
  "size_bytes": 11408754,
  "zip_test": null,
  "embedded_images": 35,
  "has_styles": true,
  "has_settings": true,
  "has_update_fields": true,
  "paragraphs": 416,
  "tables": 21,
  "word_count": 14733,
  "visible_toc_placeholder": false,
  "contains_main_oldmodel_warning": true,
  "contains_data_audit": true,
  "contains_source_names_ua": true,
  "figure_files_checked": [
    {
      "file": "fig_06_reliability_screen_large.png",
      "size": [
        1989,
        1019
      ]
    },
    {
      "file": "fig_10_livestock_cost_index.png",
      "size": [
        1980,
        937
      ]
    },
    {
      "file": "fig_08_regional_farmgate_dispersion.png",
      "size": [
        2180,
        937
      ]
    },
    {
      "file": "fig_04_prozorro_weekly_large.png",
      "size": [
        2275,
        1106
      ]
    },
    {
      "file": "fig_05_retail_discounts_large.png",
      "size": [
        2275,
        1106
      ]
    },
    {
      "file": "fig_07_selected_coefficients_large.png",
      "size": [
        2794,
        1514
      ]
    },
    {
      "file": "fig_03_h2_processor_consumer_large.png",
      "size": [
        2275,
        1106
      ]
    },
    {
      "file": "fig_01_value_chain_market_power.png",
      "size": [
        2274,
        954
      ]
    },
    {
      "file": "fig_09_dairy_trade_hs0401_0406.png",
      "size": [
        3012,
        1773
      ]
    },
    {
      "file": "fig_02_h1_monthly_prices_large.png",
      "size": [
        2275,
        1106
      ]
    }
  ]
}
```