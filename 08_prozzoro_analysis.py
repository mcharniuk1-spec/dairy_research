# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# Part 8: Prozzoro Public Procurement Price Analysis
# Compare government tender prices with retail (Novus/Silpo) and wholesale (Class III/EU)
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# =============================================================================
# LOAD PROZZORO DATA
# =============================================================================

def load_prozzoro_data():
    """
    Load Prozzoro dairy tender data
    Extract relevant price, date, and product information
    """
    print("="*80)
    print("LOADING PROZZORO PUBLIC PROCUREMENT DATA")
    print("="*80)
    
    df = pd.read_excel(BASE_PATH + 'dairy_enriched_filtered.xlsx')
    
    print(f"\nShape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    # Identify key columns (adjust based on actual structure)
    # Common columns: date, price, product_name, quantity, unit, tender_id
    
    # Find date columns
    date_cols = [col for col in df.columns if any(x in str(col).lower() 
                for x in ['date', 'дата', 'publish', 'award'])]
    print(f"\nDate columns found: {date_cols}")
    
    # Find price columns
    price_cols = [col for col in df.columns if any(x in str(col).lower() 
                 for x in ['price', 'ціна', 'вартість', 'amount', 'value'])]
    print(f"Price columns found: {price_cols}")
    
    # Find product description columns
    product_cols = [col for col in df.columns if any(x in str(col).lower() 
                   for x in ['title', 'назва', 'description', 'опис', 'product', 'товар'])]
    print(f"Product columns found: {product_cols}")
    
    # Find quantity/unit columns
    quantity_cols = [col for col in df.columns if any(x in str(col).lower() 
                    for x in ['quantity', 'кількість', 'unit', 'одиниця', 'volume'])]
    print(f"Quantity columns found: {quantity_cols}")
    
    # Parse main date column (use first date column)
    if date_cols:
        df['Date'] = pd.to_datetime(df[date_cols[0]], errors='coerce')
    else:
        print("\n⚠ Warning: No date column found")
        return None
    
    # Extract main price (use first price column or unit price if available)
    unit_price_cols = [col for col in price_cols if 'unit' in col.lower() or 'одиниц' in col.lower()]
    
    if unit_price_cols:
        df['price'] = pd.to_numeric(df[unit_price_cols[0]], errors='coerce')
        print(f"\nUsing unit price column: {unit_price_cols[0]}")
    elif price_cols:
        df['price'] = pd.to_numeric(df[price_cols[0]], errors='coerce')
        print(f"\nUsing price column: {price_cols[0]}")
    else:
        print("\n⚠ Warning: No price column found")
        return None
    
    # Product name
    if product_cols:
        df['product'] = df[product_cols[0]]
    
    # Filter to valid observations
    df = df[df['Date'].notna() & df['price'].notna()].copy()
    
    print(f"\nFiltered dataset shape: {df.shape}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    
    # Create month column
    df['YearMonth'] = df['Date'].dt.to_period('M')
    
    # Product categorization
    df['product_category'] = 'Other'
    
    if 'product' in df.columns:
        df.loc[df['product'].str.contains('молоко|Молоко|milk', na=False, case=False), 'product_category'] = 'Milk'
        df.loc[df['product'].str.contains('кефір|Кефір|kefir', na=False, case=False), 'product_category'] = 'Kefir'
        df.loc[df['product'].str.contains('сир|Сир|cheese', na=False, case=False), 'product_category'] = 'Cheese'
        df.loc[df['product'].str.contains('йогурт|Йогурт|yogurt', na=False, case=False), 'product_category'] = 'Yogurt'
        df.loc[df['product'].str.contains('масло|Масло|butter', na=False, case=False), 'product_category'] = 'Butter'
        df.loc[df['product'].str.contains('сметан|Сметан|sour cream', na=False, case=False), 'product_category'] = 'Sour Cream'
    
        print(f"\nProduct category distribution:")
        print(df['product_category'].value_counts())
    
    # Descriptive statistics
    print(f"\n{'='*80}")
    print("PROZZORO PRICE STATISTICS")
    print(f"{'='*80}")
    print(df['price'].describe())
    
    return df


# =============================================================================
# MONTHLY AGGREGATION
# =============================================================================

def create_monthly_prozzoro(df, product_category='Milk'):
    """
    Aggregate Prozzoro data to monthly level for specific product
    """
    print(f"\n{'='*80}")
    print(f"MONTHLY AGGREGATION: {product_category}")
    print(f"{'='*80}")
    
    # Filter to specific product
    product_df = df[df['product_category'] == product_category].copy()
    
    print(f"\n{product_category} observations: {len(product_df)}")
    
    if len(product_df) == 0:
        print(f"⚠ No {product_category} observations found")
        return None
    
    # Monthly aggregates
    monthly = product_df.groupby('YearMonth').agg({
        'price': ['median', 'mean', 'std', 'count'],
        'Date': 'min'  # First day of month
    }).reset_index()
    
    # Flatten column names
    monthly.columns = ['YearMonth', 'median_price', 'mean_price', 
                      'std_price', 'n_tenders', 'Date']
    
    monthly['ln_price'] = np.log(monthly['median_price'])
    monthly['price_cv'] = monthly['std_price'] / monthly['mean_price']  # Coefficient of variation
    
    print(f"\nMonthly aggregation complete: {len(monthly)} months")
    print(f"\nSummary:")
    print(monthly[['median_price', 'mean_price', 'n_tenders']].describe())
    
    return monthly


# =============================================================================
# COMPARE PROZZORO WITH RETAIL PRICES
# =============================================================================

def compare_prozzoro_retail():
    """
    Compare Prozzoro government procurement prices with retail (Novus/Silpo)
    Research question: Are government tenders priced below/above retail?
    """
    print(f"\n{'='*80}")
    print("PROZZORO vs RETAIL PRICE COMPARISON")
    print(f"{'='*80}")
    
    # Load Prozzoro data
    prozzoro_df = load_prozzoro_data()
    if prozzoro_df is None:
        return
    
    prozzoro_monthly = create_monthly_prozzoro(prozzoro_df, product_category='Milk')
    if prozzoro_monthly is None:
        return
    
    # Load Novus retail data
    try:
        novus_monthly = pd.read_csv(BASE_PATH + 'processed/novus_monthly.csv')
        novus_monthly['Date'] = pd.to_datetime(novus_monthly['Date'])
        has_novus = True
    except:
        print("⚠ Novus data not available")
        has_novus = False
    
    # Load Silpo retail data
    try:
        silpo_monthly = pd.read_csv(BASE_PATH + 'processed/silpo_monthly_with_discounts.csv')
        silpo_monthly['Date'] = pd.to_datetime(silpo_monthly['Date'])
        has_silpo = True
    except:
        print("⚠ Silpo data not available")
        has_silpo = False
    
    if not has_novus and not has_silpo:
        print("⚠ No retail data available for comparison")
        return
    
    # Merge datasets
    comparison = prozzoro_monthly[['Date', 'median_price']].copy()
    comparison.columns = ['Date', 'Prozzoro_price']
    
    if has_novus:
        comparison = pd.merge(comparison, 
                            novus_monthly[['Date', 'median_unit_price']],
                            on='Date', how='outer', suffixes=('', '_novus'))
        comparison.columns = list(comparison.columns[:-1]) + ['Novus_price']
    
    if has_silpo:
        comparison = pd.merge(comparison,
                            silpo_monthly[['Date', 'median_unit_price']],
                            on='Date', how='outer', suffixes=('', '_silpo'))
        comparison.columns = list(comparison.columns[:-1]) + ['Silpo_price']
    
    comparison = comparison.sort_values('Date').reset_index(drop=True)
    
    print(f"\nComparison dataset shape: {comparison.shape}")
    print(f"Date range: {comparison['Date'].min()} to {comparison['Date'].max()}")
    
    # Calculate price differences
    if has_novus:
        comparison['diff_novus'] = comparison['Prozzoro_price'] - comparison['Novus_price']
        comparison['diff_novus_pct'] = (comparison['diff_novus'] / comparison['Novus_price']) * 100
    
    if has_silpo:
        comparison['diff_silpo'] = comparison['Prozzoro_price'] - comparison['Silpo_price']
        comparison['diff_silpo_pct'] = (comparison['diff_silpo'] / comparison['Silpo_price']) * 100
    
    # Statistics
    print(f"\n{'='*80}")
    print("PRICE DIFFERENTIAL STATISTICS")
    print(f"{'='*80}")
    
    if has_novus:
        print(f"\nProzzoro vs Novus:")
        print(f"Mean difference: {comparison['diff_novus'].mean():.2f} UAH ({comparison['diff_novus_pct'].mean():.1f}%)")
        print(f"Median difference: {comparison['diff_novus'].median():.2f} UAH ({comparison['diff_novus_pct'].median():.1f}%)")
        
        if comparison['diff_novus_pct'].mean() < 0:
            print("→ Prozzoro prices are LOWER than Novus retail (on average)")
        else:
            print("→ Prozzoro prices are HIGHER than Novus retail (on average)")
    
    if has_silpo:
        print(f"\nProzzoro vs Silpo:")
        print(f"Mean difference: {comparison['diff_silpo'].mean():.2f} UAH ({comparison['diff_silpo_pct'].mean():.1f}%)")
        print(f"Median difference: {comparison['diff_silpo'].median():.2f} UAH ({comparison['diff_silpo_pct'].median():.1f}%)")
        
        if comparison['diff_silpo_pct'].mean() < 0:
            print("→ Prozzoro prices are LOWER than Silpo retail (on average)")
        else:
            print("→ Prozzoro prices are HIGHER than Silpo retail (on average)")
    
    # Visualization
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))
    
    # Plot 1: Price levels
    ax1 = axes[0]
    ax1.plot(comparison['Date'], comparison['Prozzoro_price'], 
            linewidth=2.5, marker='o', label='Prozzoro (Gov Tenders)', color='#6A994E')
    
    if has_novus:
        ax1.plot(comparison['Date'], comparison['Novus_price'],
                linewidth=2, marker='s', label='Novus (Retail)', color='#2E86AB', alpha=0.7)
    
    if has_silpo:
        ax1.plot(comparison['Date'], comparison['Silpo_price'],
                linewidth=2, marker='^', label='Silpo (Retail)', color='#C73E1D', alpha=0.7)
    
    ax1.set_title('Milk Prices: Prozzoro vs Retail', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Price (UAH)', fontsize=12)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Price differentials
    ax2 = axes[1]
    
    if has_novus:
        ax2.plot(comparison['Date'], comparison['diff_novus_pct'],
                linewidth=2, marker='o', label='Prozzoro vs Novus (%)', color='#2E86AB')
    
    if has_silpo:
        ax2.plot(comparison['Date'], comparison['diff_silpo_pct'],
                linewidth=2, marker='s', label='Prozzoro vs Silpo (%)', color='#C73E1D')
    
    ax2.axhline(0, color='black', linestyle='--', linewidth=1)
    ax2.set_title('Price Differential: Prozzoro vs Retail (%)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Difference (%)', fontsize=12)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/prozzoro_vs_retail_comparison.png', 
               dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nPlot saved: prozzoro_vs_retail_comparison.png")
    
    # Save comparison data
    comparison.to_csv(BASE_PATH + 'processed/prozzoro_retail_comparison.csv', index=False)
    
    return comparison


# =============================================================================
# COMPARE PROZZORO WITH CLASS III AND EU PRICES
# =============================================================================

def compare_prozzoro_wholesale():
    """
    Compare Prozzoro prices with Class III (US) and EU wholesale benchmarks
    """
    print(f"\n{'='*80}")
    print("PROZZORO vs WHOLESALE BENCHMARK COMPARISON")
    print(f"{'='*80}")
    
    # Load Prozzoro data
    prozzoro_df = load_prozzoro_data()
    if prozzoro_df is None:
        return
    
    prozzoro_monthly = create_monthly_prozzoro(prozzoro_df, product_category='Milk')
    if prozzoro_monthly is None:
        return
    
    # Load Class III data
    try:
        class3_monthly = pd.read_csv(BASE_PATH + 'processed/class3_monthly.csv')
        class3_monthly['Date'] = pd.to_datetime(class3_monthly['Date'])
        has_class3 = True
    except:
        print("⚠ Class III data not available")
        has_class3 = False
    
    # Load EU data
    try:
        eu_us_data = pd.read_csv(BASE_PATH + 'processed/eu_us_comparison.csv')
        eu_us_data['Date'] = pd.to_datetime(eu_us_data.iloc[:, 0])  # First column is date
        has_eu = True
    except:
        print("⚠ EU data not available")
        has_eu = False
    
    if not has_class3 and not has_eu:
        print("⚠ No wholesale benchmark data available")
        return
    
    # Merge
    comparison = prozzoro_monthly[['Date', 'median_price']].copy()
    comparison.columns = ['Date', 'Prozzoro_UAH']
    
    if has_class3:
        comparison = pd.merge(comparison,
                            class3_monthly[['Date', 'Price']],
                            on='Date', how='outer')
        comparison.columns = list(comparison.columns[:-1]) + ['Class3_USD']
    
    if has_eu:
        comparison = pd.merge(comparison,
                            eu_us_data[['Date', 'EU_Price']],
                            on='Date', how='outer')
        comparison.columns = list(comparison.columns[:-1]) + ['EU_EUR']
    
    comparison = comparison.sort_values('Date').reset_index(drop=True)
    
    print(f"\nComparison dataset shape: {comparison.shape}")
    print(f"Observations: {len(comparison)}")
    
    # Note: Direct price comparison requires currency conversion
    # For now, compare trends using index
    
    # Normalize to 100 at first common observation
    first_valid_idx = comparison[['Prozzoro_UAH', 'Class3_USD' if has_class3 else 'EU_EUR']].dropna().index[0]
    
    comparison['Prozzoro_index'] = (comparison['Prozzoro_UAH'] / 
                                   comparison.loc[first_valid_idx, 'Prozzoro_UAH']) * 100
    
    if has_class3:
        comparison['Class3_index'] = (comparison['Class3_USD'] / 
                                     comparison.loc[first_valid_idx, 'Class3_USD']) * 100
    
    if has_eu:
        comparison['EU_index'] = (comparison['EU_EUR'] / 
                                comparison.loc[first_valid_idx, 'EU_EUR']) * 100
    
    # Plot indexed comparison
    fig, ax = plt.subplots(figsize=(14, 7))
    
    ax.plot(comparison['Date'], comparison['Prozzoro_index'],
           linewidth=2.5, marker='o', label='Prozzoro (Ukraine)', color='#6A994E')
    
    if has_class3:
        ax.plot(comparison['Date'], comparison['Class3_index'],
               linewidth=2, marker='s', label='Class III (US)', color='#2E86AB', alpha=0.7)
    
    if has_eu:
        ax.plot(comparison['Date'], comparison['EU_index'],
               linewidth=2, marker='^', label='EU Average', color='#C73E1D', alpha=0.7)
    
    ax.axhline(100, color='black', linestyle=':', linewidth=1, alpha=0.5)
    ax.set_title('Milk Price Trends: Prozzoro vs Global Benchmarks (Indexed)',
                fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Index (First observation = 100)', fontsize=12)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/prozzoro_vs_wholesale_comparison.png',
               dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nPlot saved: prozzoro_vs_wholesale_comparison.png")
    
    # Correlation analysis
    print(f"\n{'='*80}")
    print("CORRELATION WITH GLOBAL BENCHMARKS")
    print(f"{'='*80}")
    
    if has_class3:
        valid_data = comparison[['Prozzoro_UAH', 'Class3_USD']].dropna()
        if len(valid_data) > 5:
            corr_class3 = valid_data.corr().iloc[0, 1]
            print(f"Prozzoro vs Class III correlation: {corr_class3:.4f}")
    
    if has_eu:
        valid_data = comparison[['Prozzoro_UAH', 'EU_EUR']].dropna()
        if len(valid_data) > 5:
            corr_eu = valid_data.corr().iloc[0, 1]
            print(f"Prozzoro vs EU correlation: {corr_eu:.4f}")
    
    # Save results
    comparison.to_csv(BASE_PATH + 'processed/prozzoro_wholesale_comparison.csv', index=False)
    
    return comparison


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def run_prozzoro_analysis():
    """
    Main pipeline for Prozzoro analysis
    """
    # Compare with retail
    prozzoro_retail = compare_prozzoro_retail()
    
    # Compare with wholesale benchmarks
    prozzoro_wholesale = compare_prozzoro_wholesale()
    
    print(f"\n{'='*80}")
    print("PROZZORO ANALYSIS COMPLETE")
    print(f"{'='*80}")


if __name__ == "__main__":
    run_prozzoro_analysis()
