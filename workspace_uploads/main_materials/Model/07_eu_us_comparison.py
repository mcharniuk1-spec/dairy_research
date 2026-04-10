# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# Part 7: EU vs US Milk Price Comparison
# Compare European trend (EJgxfgP) with US (Class III Milk Futures)
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller, grangercausalitytests
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')

BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# =============================================================================
# LOAD EU MILK PRICE DATA
# =============================================================================

def load_eu_milk_data():
    """
    Load EU milk historical price series
    Multiple sheets may exist - extract relevant price series
    """
    print("="*80)
    print("LOADING EU MILK PRICE DATA")
    print("="*80)
    
    # Load Excel file
    excel_file = pd.ExcelFile(BASE_PATH + 'eu-milk-historical-price-series_en07012026.xlsx')
    print(f"Available sheets: {excel_file.sheet_names}")
    
    # Load first sheet (adjust based on actual structure)
    # Common structure: Date column + price columns by country
    df = pd.read_excel(excel_file, sheet_name=0)
    
    print(f"\nShape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    # Identify date column (flexible matching)
    date_cols = [col for col in df.columns if any(x in str(col).lower() 
                for x in ['date', 'month', 'year', 'period', 'time'])]
    
    if date_cols:
        date_col = date_cols[0]
        df['Date'] = pd.to_datetime(df[date_col])
    else:
        print("\n⚠ Warning: No date column found. Using index.")
        df['Date'] = pd.date_range(start='2016-01-01', periods=len(df), freq='M')
    
    # Identify price columns
    price_cols = [col for col in df.columns if col not in ['Date'] and 
                 df[col].dtype in [np.float64, np.int64]]
    
    print(f"\nDate column: {date_col if date_cols else 'Index'}")
    print(f"Price columns: {price_cols}")
    
    # Calculate EU average if multiple countries
    if len(price_cols) > 1:
        df['EU_avg_price'] = df[price_cols].mean(axis=1)
        df['EU_median_price'] = df[price_cols].median(axis=1)
        print(f"\nCalculated EU average and median prices")
    else:
        df['EU_avg_price'] = df[price_cols[0]]
    
    # Create monthly series
    df = df.set_index('Date')
    df['YearMonth'] = df.index.to_period('M')
    
    # Resample to monthly if daily/weekly
    if len(df) > 500:  # Likely daily data
        print("\nResampling to monthly frequency...")
        df_monthly = df[['EU_avg_price']].resample('M').mean()
    else:
        df_monthly = df[['EU_avg_price']].copy()
    
    df_monthly['ln_EU_price'] = np.log(df_monthly['EU_avg_price'])
    
    print(f"\nFinal monthly EU data shape: {df_monthly.shape}")
    print(f"Date range: {df_monthly.index.min()} to {df_monthly.index.max()}")
    
    return df_monthly


def load_ejgxfgp_interpolated():
    """
    Load EJgxfgP daily interpolated data
    Contains both real and interpolated EU price series
    """
    print("\n" + "="*80)
    print("LOADING EJgxfgP INTERPOLATED DATA")
    print("="*80)
    
    df = pd.read_excel(BASE_PATH + 'EJgxfgP_daily_interpolated.xlsx')
    
    print(f"\nShape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    # Identify date column
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    if date_cols:
        df['Date'] = pd.to_datetime(df[date_cols[0]])
    else:
        # Try first column
        df['Date'] = pd.to_datetime(df.iloc[:, 0])
    
    df = df.set_index('Date')
    
    # Identify real vs interpolated price columns
    real_cols = [col for col in df.columns if 'real' in col.lower() or 'actual' in col.lower()]
    interp_cols = [col for col in df.columns if 'interp' in col.lower()]
    
    print(f"\nReal price columns: {real_cols}")
    print(f"Interpolated price columns: {interp_cols}")
    
    # Resample to monthly
    if len(real_cols) > 0:
        df_monthly = df[[real_cols[0]]].resample('M').mean()
        df_monthly.columns = ['EU_real_price']
    
    if len(interp_cols) > 0:
        interp_monthly = df[[interp_cols[0]]].resample('M').mean()
        df_monthly['EU_interp_price'] = interp_monthly.iloc[:, 0]
    
    df_monthly['ln_EU_real'] = np.log(df_monthly['EU_real_price'])
    if 'EU_interp_price' in df_monthly.columns:
        df_monthly['ln_EU_interp'] = np.log(df_monthly['EU_interp_price'])
    
    print(f"\nMonthly aggregated shape: {df_monthly.shape}")
    print(f"Date range: {df_monthly.index.min()} to {df_monthly.index.max()}")
    
    return df_monthly


# =============================================================================
# COMPARE EU vs US TRENDS
# =============================================================================

def compare_eu_us_trends():
    """
    Compare EU and US milk price trends
    Test for correlation, cointegration, and lead-lag relationships
    """
    print("\n" + "="*80)
    print("EU vs US MILK PRICE COMPARISON")
    print("="*80)
    
    # Load US Class III data
    class3_df = pd.read_csv(BASE_PATH + 'processed/class3_monthly.csv')
    class3_df['Date'] = pd.to_datetime(class3_df['Date'])
    class3_df = class3_df.set_index('Date')
    
    # Load EU data
    eu_df = load_eu_milk_data()
    
    # Merge on date
    merged = pd.merge(class3_df[['Price', 'ln_Price']], 
                     eu_df[['EU_avg_price', 'ln_EU_price']], 
                     left_index=True, right_index=True, how='inner')
    
    merged.columns = ['US_Price', 'ln_US', 'EU_Price', 'ln_EU']
    
    print(f"\nMerged dataset:")
    print(f"Shape: {merged.shape}")
    print(f"Date range: {merged.index.min()} to {merged.index.max()}")
    print(f"\nFirst 5 observations:")
    print(merged.head())
    
    # =========================================================================
    # DESCRIPTIVE COMPARISON
    # =========================================================================
    
    print(f"\n{'='*80}")
    print("DESCRIPTIVE STATISTICS COMPARISON")
    print(f"{'='*80}")
    
    stats_df = pd.DataFrame({
        'US_Mean': merged['US_Price'].mean(),
        'US_Std': merged['US_Price'].std(),
        'US_CV': (merged['US_Price'].std() / merged['US_Price'].mean()) * 100,
        'EU_Mean': merged['EU_Price'].mean(),
        'EU_Std': merged['EU_Price'].std(),
        'EU_CV': (merged['EU_Price'].std() / merged['EU_Price'].mean()) * 100
    }, index=[0])
    
    print(stats_df.T)
    
    # Correlation
    corr = merged[['US_Price', 'EU_Price']].corr()
    print(f"\n{'='*80}")
    print("CORRELATION MATRIX")
    print(f"{'='*80}")
    print(corr)
    
    # =========================================================================
    # VISUALIZATION
    # =========================================================================
    
    # Plot 1: Price levels over time
    fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
    
    ax1 = axes[0]
    ax1_twin = ax1.twinx()
    
    l1 = ax1.plot(merged.index, merged['US_Price'], linewidth=2.5, 
                 color='#2E86AB', label='US Class III')
    l2 = ax1_twin.plot(merged.index, merged['EU_Price'], linewidth=2.5,
                      color='#C73E1D', label='EU Average', linestyle='--')
    
    ax1.set_ylabel('US Price (USD/cwt)', fontsize=12, color='#2E86AB')
    ax1_twin.set_ylabel('EU Price (EUR/100kg)', fontsize=12, color='#C73E1D')
    ax1.tick_params(axis='y', labelcolor='#2E86AB')
    ax1_twin.tick_params(axis='y', labelcolor='#C73E1D')
    
    lns = l1 + l2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc='upper left')
    ax1.set_title('EU vs US Milk Prices (Levels)', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Normalized to 100 (index)
    ax2 = axes[1]
    
    us_index = (merged['US_Price'] / merged['US_Price'].iloc[0]) * 100
    eu_index = (merged['EU_Price'] / merged['EU_Price'].iloc[0]) * 100
    
    ax2.plot(merged.index, us_index, linewidth=2.5, color='#2E86AB', 
            label='US Class III (Indexed)')
    ax2.plot(merged.index, eu_index, linewidth=2.5, color='#C73E1D', 
            label='EU Average (Indexed)', linestyle='--')
    
    ax2.axhline(100, color='black', linestyle=':', linewidth=1, alpha=0.5)
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Index (First observation = 100)', fontsize=12)
    ax2.legend(loc='best')
    ax2.set_title('EU vs US Milk Prices (Indexed)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/eu_vs_us_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nPlot saved: eu_vs_us_comparison.png")
    
    # =========================================================================
    # COINTEGRATION TEST
    # =========================================================================
    
    print(f"\n{'='*80}")
    print("COINTEGRATION TEST (EU vs US)")
    print(f"{'='*80}")
    
    # Engle-Granger two-step
    # Step 1: Regress ln_EU on ln_US
    y = merged['ln_EU']
    X = sm.add_constant(merged['ln_US'])
    
    ols_model = OLS(y, X)
    ols_results = ols_model.fit()
    
    print("\nStep 1: Cointegrating regression")
    print(ols_results.summary())
    
    # Step 2: Test residuals for stationarity
    residuals = ols_results.resid
    adf_result = adfuller(residuals, regression='nc')  # No constant in residual test
    
    print(f"\nStep 2: ADF test on residuals")
    print(f"ADF Statistic: {adf_result[0]:.6f}")
    print(f"p-value: {adf_result[1]:.6f}")
    print(f"Critical values: {adf_result[4]}")
    
    if adf_result[1] < 0.05:
        print("\n✓ Residuals are stationary → EU and US prices are COINTEGRATED")
        coint_conclusion = "Cointegrated"
    else:
        print("\n✗ Residuals non-stationary → NO cointegration")
        coint_conclusion = "Not cointegrated"
    
    # =========================================================================
    # GRANGER CAUSALITY
    # =========================================================================
    
    print(f"\n{'='*80}")
    print("GRANGER CAUSALITY TEST")
    print(f"{'='*80}")
    
    # Test if US Granger-causes EU
    gc_data = merged[['ln_EU', 'ln_US']].dropna()
    
    print("\nTest: Does US Class III Granger-cause EU prices?")
    gc_us_to_eu = grangercausalitytests(gc_data[['ln_EU', 'ln_US']], maxlag=6, verbose=True)
    
    print("\nTest: Does EU Granger-cause US Class III prices?")
    gc_eu_to_us = grangercausalitytests(gc_data[['ln_US', 'ln_EU']], maxlag=6, verbose=True)
    
    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    
    merged.to_csv(BASE_PATH + 'processed/eu_us_comparison.csv')
    
    summary_results = pd.DataFrame({
        'Metric': ['Correlation', 'Cointegration', 'US_Mean', 'EU_Mean', 
                  'US_Volatility', 'EU_Volatility'],
        'Value': [corr.iloc[0, 1], coint_conclusion, merged['US_Price'].mean(),
                 merged['EU_Price'].mean(), merged['US_Price'].std(), 
                 merged['EU_Price'].std()]
    })
    
    summary_results.to_csv(BASE_PATH + 'results/eu_us_comparison_summary.csv', index=False)
    
    print(f"\n{'='*80}")
    print("EU vs US COMPARISON COMPLETE")
    print(f"{'='*80}")
    
    return merged


# =============================================================================
# COMPARE REAL vs INTERPOLATED EU PRICES
# =============================================================================

def compare_real_vs_interpolated():
    """
    Compare real EU prices with interpolated series
    Assess interpolation quality
    """
    print("\n" + "="*80)
    print("REAL vs INTERPOLATED EU PRICES COMPARISON")
    print("="*80)
    
    ejg_df = load_ejgxfgp_interpolated()
    
    if 'EU_interp_price' not in ejg_df.columns:
        print("⚠ No interpolated series found")
        return
    
    # Drop missing
    comparison = ejg_df[['EU_real_price', 'EU_interp_price']].dropna()
    
    print(f"\nComparison sample size: {len(comparison)}")
    
    # Calculate errors
    comparison['error'] = comparison['EU_real_price'] - comparison['EU_interp_price']
    comparison['error_pct'] = (comparison['error'] / comparison['EU_real_price']) * 100
    comparison['abs_error'] = np.abs(comparison['error'])
    
    # Statistics
    print(f"\n{'='*80}")
    print("INTERPOLATION ERROR STATISTICS")
    print(f"{'='*80}")
    print(f"Mean error: {comparison['error'].mean():.4f}")
    print(f"Mean absolute error: {comparison['abs_error'].mean():.4f}")
    print(f"RMSE: {np.sqrt((comparison['error']**2).mean()):.4f}")
    print(f"Mean % error: {comparison['error_pct'].mean():.2f}%")
    print(f"MAPE: {comparison['abs_error'].mean() / comparison['EU_real_price'].mean() * 100:.2f}%")
    
    # Correlation
    corr = comparison[['EU_real_price', 'EU_interp_price']].corr()
    print(f"\nCorrelation: {corr.iloc[0, 1]:.6f}")
    
    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))
    
    # Plot 1: Real vs Interpolated
    ax1 = axes[0]
    ax1.plot(comparison.index, comparison['EU_real_price'], linewidth=2,
            color='#2E86AB', label='Real Prices')
    ax1.plot(comparison.index, comparison['EU_interp_price'], linewidth=2,
            color='#C73E1D', linestyle='--', label='Interpolated Prices')
    ax1.set_title('EU Milk Prices: Real vs Interpolated', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Price', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Error over time
    ax2 = axes[1]
    ax2.plot(comparison.index, comparison['error_pct'], linewidth=2, color='#6A994E')
    ax2.axhline(0, color='black', linestyle='--', linewidth=1)
    ax2.set_title('Interpolation Error Over Time', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Error (%)', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/eu_real_vs_interpolated.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nPlot saved: eu_real_vs_interpolated.png")
    
    return comparison


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def run_eu_us_comparison():
    """
    Main pipeline for EU vs US comparison
    """
    # Compare EU and US trends
    eu_us_merged = compare_eu_us_trends()
    
    # Compare real vs interpolated
    real_interp_comparison = compare_real_vs_interpolated()
    
    print(f"\n{'='*80}")
    print("EU-US COMPARISON ANALYSIS COMPLETE")
    print(f"{'='*80}")


if __name__ == "__main__":
    run_eu_us_comparison()
