# Clean New Model Data Dictionary

| dataset | source | frequency | layer | unit | role | limitation |
| --- | --- | --- | --- | --- | --- | --- |
| Farm-gate monthly | SSSU agricultural sales; Farm_milk_2015.xlsx | Monthly | Farm-gate | Converted to UAH/kg | Main H1 upstream price | Farm price label is abbreviated; conversion must be documented. |
| Processor monthly | SSSU producer prices; Processor_2013_2026.xlsx | Monthly | Processor | UAH/tonne converted to UAH/kg | Main H1 downstream and H2 upstream price | Ukraine-only; no regional processor series. |
| Consumer monthly | SSSU consumer prices; Consumer_2017_2026.xlsx | Monthly | Official consumer | UAH/kg | Main H2 official benchmark | Only selected products: milk, sour cream, soft cheese. |
| ProZorro lot-level | ProzorroM(full) | Event / lot | Institutional procurement | UAH/kg after parsing | H1/H2 institutional mechanism | Irregular events; piece units need package parsing. |
| Silpo/Novus SKU-day | Retail sheets in newmodel workbook | Daily observed online prices | Retail | UAH/kg where package parsing is reliable | H2 retail mechanism and discount analysis | Short period; classification and package parsing required. |

# Product Dictionary

| product | label | role | main_use |
| --- | --- | --- | --- |
| raw_milk | Raw milk | Farm-gate raw material | H1 upstream |
| drinking_milk | Drinking milk | Comparable dairy product group | H1/H2 where matching is available |
| sour_cream | Sour cream | Comparable dairy product group | H1/H2 where matching is available |
| kefir | Kefir | Comparable dairy product group | H1/H2 where matching is available |
| butter | Butter | Comparable dairy product group | H1/H2 where matching is available |
| hard_cheese | Hard cheese | Comparable dairy product group | H1/H2 where matching is available |
| soft_cheese | Soft cheese | Comparable dairy product group | Audit or exclusion |
| cottage_cheese | Cottage cheese | Comparable dairy product group | H2 / retail-ProZorro mechanism if support is sufficient |
| skim_milk_powder | Skim milk powder | Comparable dairy product group | H1/H2 where matching is available |
| cream | Cream | Comparable dairy product group | H2 / retail-ProZorro mechanism if support is sufficient |
| condensed_milk | Condensed milk | Comparable dairy product group | H2 / retail-ProZorro mechanism if support is sufficient |
| yogurt | Yogurt | Comparable dairy product group | H2 / retail-ProZorro mechanism if support is sufficient |
| other_dairy | Other dairy | Dairy but weakly comparable | Audit or exclusion |
| exclude_non_dairy | Excluded non-dairy | Excluded | Audit or exclusion |