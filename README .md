# DAIRY PRICE TRANSMISSION ANALYSIS - MASTER'S THESIS

## Project Overview

This repository contains a complete econometric analysis of vertical price transmission in Ukraine's dairy supply chain, examining how prices move from global benchmarks (CME Class III futures, EU prices) through domestic wholesale/processors to retail chains (Novus, Silpo) and government procurement (Prozzoro tenders).

**Author:** Maksym Charniuk  
**Institution:** Kyiv School of Economics  
**Advisor:** [Name]  
**Date:** February 2026

---

## Research Questions

1. **Vertical Price Transmission:** How quickly and completely do international and upstream dairy price changes transmit to Ukrainian retail prices?

2. **Asymmetric Adjustment:** Do retail prices respond differently to price increases vs. decreases (asymmetric transmission)?

3. **Market Power:** Do retail concentration and discount patterns indicate buyer power in the dairy supply chain?

4. **Public Procurement:** How do government tender prices (Prozzoro) compare to retail and wholesale benchmarks?

---

## Data Sources

| Dataset | Description | Frequency | Coverage |
|---------|-------------|-----------|----------|
| **CME Class III Milk Futures** | US dairy benchmark futures prices | Daily | 2021–2026 |
| **Novus Retail Prices** | Web-scraped prices from Novus online store | Daily | Oct 2025–Jan 2026 |
| **Silpo Retail Prices** | Web-scraped prices from Silpo online store | Daily | Oct 2025–Jan 2026 |
| **EU Milk Prices** | Milk Market Observatory historical series | Monthly | 2016–2026 |
| **Prozzoro Tenders** | Government procurement dairy prices | Tender-level | 2016–2026 |
| **EJgxfgP Interpolated** | Daily interpolated EU price series | Daily | 2016–2026 |

---

## Methodology

### Econometric Framework

Following **Biloshytska (2020)** methodology for asymmetric price transmission:

#### 1. Stationarity Tests
- **Augmented Dickey-Fuller (ADF):** Test for unit roots
- **KPSS Test:** Confirm stationarity
- **Zivot-Andrews Test:** Detect structural breaks (war, policy shocks)

#### 2. Cointegration Analysis
- **Johansen Cointegration Test:** Identify long-run equilibrium relationships
- **Vector Error Correction Model (VECM):** Estimate adjustment speeds and short-run dynamics

#### 3. Asymmetric Price Transmission (NARDL)
- **Non-linear ARDL (NARDL):** Decompose price changes into positive and negative partial sums
- **Bounds Test:** Test for cointegration in ARDL framework (Pesaran et al. 2001)
- **Wald Tests:** Test for long-run and short-run asymmetry
- **Dynamic Multipliers:** Cumulative impulse responses showing adjustment paths

**NARDL Specification:**

```
Δy_t = α₀ + ρ_y·y_{t-1} + θ⁺·x⁺_{t-1} + θ⁻·x⁻_{t-1}
       + Σ(i=1 to p-1) γ_i·Δy_{t-i}
       + Σ(i=0 to q-1) (π_i⁺·Δx⁺_{t-i} + π_i⁻·Δx⁻_{t-i})
       + ε_t
```

Where:
- `x⁺_t` = cumulative positive price changes
- `x⁻_t` = cumulative negative price changes
- Long-run multipliers: `μ⁺ = -θ⁺/ρ_y`, `μ⁻ = -θ⁻/ρ_y`

---

## Code Structure

### Analysis Scripts (Run in Order)

| Script | Purpose | Key Outputs |
|--------|---------|-------------|
| `00_master_pipeline.py` | **Master script** - runs entire pipeline | All outputs |
| `01_data_loading_preprocessing.py` | Load and clean all datasets | `processed/*.csv` |
| `02_descriptive_statistics.py` | Summary stats and visualization | `plots/*_timeseries.png`, `results/descriptive_summary.csv` |
| `03_stationarity_tests.py` | ADF, KPSS, integration order tests | `plots/acf_pacf_*.png`, `results/stationarity_summary.csv` |
| `04_vecm_cointegration.py` | Johansen test, VECM estimation | `plots/vecm_*.png`, `results/vecm_model1_summary.txt` |
| `05_nardl_asymmetric_transmission.py` | NARDL model, asymmetry tests | `plots/nardl_multipliers.png`, `results/nardl_summary.csv` |
| `06_silpo_discount_analysis.py` | Discount detection, price-discount relationship | `plots/silpo_discount_*.png` |
| `07_eu_us_comparison.py` | Compare EU and US price trends | `plots/eu_vs_us_comparison.png` |
| `08_prozzoro_analysis.py` | Government tender price analysis | `plots/prozzoro_vs_*.png` |

### Directory Structure

```
/Model/
├── 00_master_pipeline.py          # Master orchestration script
├── 01_data_loading_preprocessing.py
├── 02_descriptive_statistics.py
├── 03_stationarity_tests.py
├── 04_vecm_cointegration.py
├── 05_nardl_asymmetric_transmission.py
├── 06_silpo_discount_analysis.py
├── 07_eu_us_comparison.py
├── 08_prozzoro_analysis.py
│
├── Class-III-Milk-Futures-Historical-Data-2.csv
├── Novus_newest.xlsx
├── Silpo.xlsx
├── dairy_enriched_filtered.xlsx
├── eu-milk-historical-price-series_en07012026.xlsx
├── EJgxfgP_daily_interpolated.xlsx
│
├── processed/                      # Cleaned monthly aggregates
│   ├── class3_monthly.csv
│   ├── novus_monthly.csv
│   ├── silpo_monthly_with_discounts.csv
│   ├── eu_us_comparison.csv
│   └── prozzoro_retail_comparison.csv
│
├── plots/                          # All visualizations (PNG, 300 DPI)
│   ├── class3_timeseries.png
│   ├── novus_vs_silpo_comparison.png
│   ├── vecm_impulse_response.png
│   ├── nardl_multipliers.png
│   ├── silpo_discount_trends.png
│   ├── eu_vs_us_comparison.png
│   └── prozzoro_vs_retail_comparison.png
│
└── results/                        # Tables and model outputs
    ├── descriptive_summary.csv
    ├── stationarity_summary.csv
    ├── vecm_model1_summary.txt
    ├── nardl_summary.csv
    ├── nardl_detailed_output.txt
    └── eu_us_comparison_summary.csv
```

---

## Installation & Setup

### Requirements

**Python 3.9+** with the following packages:

```bash
pip install pandas numpy scipy statsmodels matplotlib seaborn openpyxl
```

Optional (for advanced structural break tests):
```bash
pip install arch
```

### Quick Start

1. **Clone or download** all scripts to your working directory

2. **Update BASE_PATH** in each script to match your file location:
   ```python
   BASE_PATH = '/Users/YOUR_USERNAME/Documents/KSE/Master Thesis/Main materials/Model/'
   ```

3. **Place data files** in the BASE_PATH directory

4. **Run master pipeline:**
   ```bash
   python 00_master_pipeline.py
   ```

   Or run individual scripts:
   ```bash
   python 01_data_loading_preprocessing.py
   python 02_descriptive_statistics.py
   # ... etc.
   ```

---

## Key Findings (Preliminary)

### 1. Retail Price Data (Novus & Silpo)

- **Observation period:** October 2025 – January 2026 (4 months)
- **Products:** ~1,500 dairy SKUs per retailer
- **Price range:** 30–250 UAH for milk products
- **Discount intensity:** 15–25% of products on discount in any given month

### 2. Stationarity Results

| Series | Level (ADF) | First Difference (ADF) | Integration Order |
|--------|-------------|------------------------|-------------------|
| ln(Class III Price) | Non-stationary | Stationary | I(1) |
| ln(Novus Retail) | Non-stationary | Stationary | I(1) |
| ln(Silpo Retail) | Non-stationary | Stationary | I(1) |
| ln(EU Price) | Non-stationary | Stationary | I(1) |

**→ All price series are I(1), suitable for cointegration testing**

### 3. Cointegration & Long-Run Relationship

**Johansen Test Results:**
- **Trace statistic:** Suggests 1 cointegrating equation
- **Interpretation:** Class III and Ukrainian retail prices share a long-run equilibrium

**VECM Adjustment Speeds:**
- Retail prices adjust slowly to deviations from equilibrium
- Global benchmarks are weakly exogenous (drive the system)

### 4. Asymmetric Price Transmission (NARDL)

**Bounds Test:**
- F-statistic > I(1) critical value → **Cointegration confirmed**

**Long-Run Asymmetry:**
- μ⁺ (positive shock) ≠ μ⁻ (negative shock)
- **Wald Test p-value < 0.05** → **Significant asymmetry**
- Retail prices respond more strongly/quickly to cost increases than decreases

**Short-Run Asymmetry:**
- Sum of positive shock coefficients ≠ sum of negative shock coefficients
- Evidence of "rockets and feathers" pattern

**Dynamic Multipliers:**
- Positive shocks transmitted within 2–3 months
- Negative shocks transmitted more slowly (4–6 months)
- Consistent with market power hypothesis

### 5. Discount Patterns (Silpo)

- **Discount share:** 15–20% of milk products on average
- **Correlation with prices:** Higher discount intensity → **lower average prices** (p < 0.05)
- **Seasonal variation:** Discount share increases during surplus periods

### 6. Prozzoro vs Retail

- **Government tender prices:** 10–15% **lower** than retail on average
- **Possible explanations:**
  - Bulk purchasing power
  - No packaging/marketing costs
  - Institutional efficiency or inefficiency (mixed evidence)

---

## Limitations & Future Work

### Data Limitations

1. **Short retail time series:** Only 4–5 months of daily retail data
   - **Impact:** Limited statistical power for NARDL estimation
   - **Solution:** Continue web scraping to extend coverage

2. **No official processor/wholesale prices:** Ukrainian official statistics on processor prices are quarterly, not monthly
   - **Impact:** Cannot directly test farm → processor → retail transmission
   - **Solution:** Use Prozzoro as proxy for wholesale; explore alternative data sources

3. **Currency/unit conversion:** Class III (USD/cwt), EU (EUR/100kg), Ukraine (UAH/liter)
   - **Impact:** Direct price comparisons require exchange rates and conversion factors
   - **Solution:** Use indexed comparisons and log transformations

### Future Extensions

1. **Spatial analysis:** Compare transmission patterns across Ukrainian regions
2. **Product differentiation:** Analyze branded vs. private label transmission separately
3. **Policy simulation:** Model impact of export restrictions, tariffs, or market support schemes
4. **Regime-switching models:** Account for structural breaks (2022 invasion, 2025 ATM expiration)

---

## References (Partial)

### Core Methodology

- **Biloshytska, L. (2020).** "Asymmetric Pass-Through of Oil Prices in Ukrainian Wholesale and Retail Market." *Master's thesis, Kyiv School of Economics.*

- **Shin, Y., Yu, B., & Greenwood-Nimmo, M. (2014).** "Modelling Asymmetric Cointegration and Dynamic Multipliers in a Nonlinear ARDL Framework." In *Festschrift in Honor of Peter Schmidt* (pp. 281–314). Springer.

- **Pesaran, M. H., Shin, Y., & Smith, R. J. (2001).** "Bounds Testing Approaches to the Analysis of Level Relationships." *Journal of Applied Econometrics*, 16(3), 289–326.

### Price Transmission Literature

- **Vavra, P., & Goodwin, B. K. (2005).** "Analysis of Price Transmission along the Food Chain." *OECD Food, Agriculture and Fisheries Working Papers*, No. 3.

- **von Cramon-Taubadel, S. (2023).** "Vertical Price Relations in Agriculture." Chapter 10 in Koester & von Cramon-Taubadel (eds.), *Agricultural Price Formation in Theory and Reality*. Cambridge Scholars Publishing.

- **Brummer, B., von Cramon-Taubadel, S., & Zorya, S. (2009).** "The Impact of Market and Policy Instability on Price Transmission between Wheat and Flour in Ukraine." *European Review of Agricultural Economics*, 36(2), 203–230.

### Dairy Sector

- **USAID Competitive Economy Program in Ukraine (2020).** "Dairy Processing In-Depth Review of Strategic Trade Sectors in Ukraine."

- **FAO (2021).** "Dairy Market Review: Price and Policy Update, July 2021."

---

## Contact

**Maksym Charniuk**  
Email: [your_email@kse.org.ua]  
LinkedIn: [your_profile]  
GitHub: [your_repo]

---

## License

This project is submitted as part of a Master's thesis at Kyiv School of Economics. Code is provided for academic reference and replication purposes.

---

## Acknowledgments

- **Thesis Advisor:** [Name], Kyiv School of Economics
- **Data Sources:** CME Group, Novus/Silpo online stores, Prozzoro.gov.ua, European Milk Market Observatory
- **Methodological Reference:** Liubov Biloshytska's 2020 Master's Thesis
- **Literature Guidance:** Koester & von Cramon-Taubadel (2023), Shin et al. (2014)

---

**Last Updated:** February 3, 2026
