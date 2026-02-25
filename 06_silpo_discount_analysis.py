# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# Part 6: Silpo-Specific Analysis with Discount Indicators
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')

BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# =============================================================================
# SILPO DATA LOADING WITH DISCOUNT DETECTION
# =============================================================================

def load_silpo_with_discounts():
    """
    Load Silpo data and create comprehensive discount indicators
    """
    print("="*80)
    print("LOADING SILPO DATA WITH DISCOUNT ANALYSIS")
    print("="*80)
    
    # Load data (adjust columns as needed based on actual file structure)
    df = pd.read_excel(BASE_PATH + 'Silpo.xlsx')
    
    # Parse dates
    df['scraped_at'] = pd.to_datetime(df['scraped_at'])
    df['Date'] = df['scraped_at'].dt.date
    df['YearMonth'] = df['scraped_at'].dt.to_period('M')
    
    # Extract volume from title
    import re
    def extract_volume(title):
        match = re.search(r'(\d+(?:\.\d+)?)\s*(г|мл|л|kg)', str(title))
        if match:
            vol = float(match.group(1))
            unit = match.group(2)
            if unit in ['г', 'мл']:
                vol = vol / 1000
            return vol
        return np.nan
    
    df['volume'] = df['title'].apply(extract_volume)
    df['unit_price'] = df['price'] / df['volume']
    
    # Product categorization
    df['product_type'] = 'Other'
    df.loc[df['title'].str.contains('Молоко|молоко', na=False, case=False), 'product_type'] = 'Milk'
    df.loc[df['title'].str.contains('Йогурт|йогурт', na=False, case=False), 'product_type'] = 'Yogurt'
    df.loc[df['title'].str.contains('Сир|сир', na=False, case=False), 'product_type'] = 'Cheese'
    
    print(f"\nTotal observations: {len(df)}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"\nProduct distribution:")
    print(df['product_type'].value_counts())
    
    # ==========================================================================
    # DISCOUNT INDICATOR 1: Price Drop Detection
    # ==========================================================================
    
    df = df.sort_values(['id', 'Date']).reset_index(drop=True)
    df['prev_price'] = df.groupby('id')['price'].shift(1)
    df['price_change'] = df['price'] - df['prev_price']
    df['price_change_pct'] = (df['price_change'] / df['prev_price']) * 100
    
    # Binary: 1 if price dropped by >5%
    df['discount_drop_5pct'] = ((df['price_change_pct'] < -5) & 
                                (df['price_change_pct'].notna())).astype(int)
    
    # Binary: 1 if price dropped by >10%
    df['discount_drop_10pct'] = ((df['price_change_pct'] < -10) & 
                                 (df['price_change_pct'].notna())).astype(int)
    
    # ==========================================================================
    # DISCOUNT INDICATOR 2: Below Historical Median
    # ==========================================================================
    
    # Calculate product-level median price
    df['product_median_price'] = df.groupby('id')['price'].transform('median')
    df['product_q25_price'] = df.groupby('id')['price'].transform(lambda x: x.quantile(0.25))
    
    # Binary: 1 if price < 95% of product median (promotional pricing)
    df['discount_below_median'] = (df['price'] < df['product_median_price'] * 0.95).astype(int)
    
    # Binary: 1 if price < Q1 (bottom 25% of price distribution)
    df['discount_below_q25'] = (df['price'] < df['product_q25_price']).astype(int)
    
    # ==========================================================================
    # DISCOUNT INDICATOR 3: Keyword Detection
    # ==========================================================================
    
    # Check if title contains discount keywords
    discount_keywords = ['акція', 'акция', 'знижка', 'скидка', 'промо', 'promo', 
                        'спеціальна', 'специальная', '2+1', '1+1']
    
    pattern = '|'.join(discount_keywords)
    df['discount_keyword'] = df['title'].str.contains(pattern, case=False, na=False).astype(int)
    
    # ==========================================================================
    # COMPOSITE DISCOUNT INDICATOR
    # ==========================================================================
    
    # Create composite: at least 2 out of 3 signals
    df['discount_composite'] = (
        (df['discount_drop_10pct'] + 
         df['discount_below_median'] + 
         df['discount_keyword']) >= 2
    ).astype(int)
    
    print(f"\n{'='*80}")
    print("DISCOUNT DETECTION SUMMARY")
    print(f"{'='*80}")
    print(f"Price drop >5%: {df['discount_drop_5pct'].sum()} ({df['discount_drop_5pct'].mean():.2%})")
    print(f"Price drop >10%: {df['discount_drop_10pct'].sum()} ({df['discount_drop_10pct'].mean():.2%})")
    print(f"Below median: {df['discount_below_median'].sum()} ({df['discount_below_median'].mean():.2%})")
    print(f"Below Q25: {df['discount_below_q25'].sum()} ({df['discount_below_q25'].mean():.2%})")
    print(f"Keyword match: {df['discount_keyword'].sum()} ({df['discount_keyword'].mean():.2%})")
    print(f"Composite (≥2 signals): {df['discount_composite'].sum()} ({df['discount_composite'].mean():.2%})")
    
    return df


# =============================================================================
# MONTHLY AGGREGATION WITH DISCOUNT METRICS
# =============================================================================

def create_monthly_silpo_with_discounts(df):
    """
    Aggregate Silpo data to monthly level with discount metrics
    """
    print(f"\n{'='*80}")
    print("MONTHLY AGGREGATION WITH DISCOUNT METRICS")
    print(f"{'='*80}")
    
    # Filter to milk products for main analysis
    milk_df = df[df['product_type'] == 'Milk'].copy()
    
    # Monthly aggregates
    monthly = milk_df.groupby('YearMonth').agg({
        'price': ['median', 'mean', 'std', 'count'],
        'unit_price': ['median', 'mean', 'std'],
        'discount_drop_5pct': 'mean',
        'discount_drop_10pct': 'mean',
        'discount_below_median': 'mean',
        'discount_below_q25': 'mean',
        'discount_keyword': 'mean',
        'discount_composite': 'mean',
        'id': 'nunique'  # Number of unique products
    }).reset_index()
    
    # Flatten column names
    monthly.columns = ['_'.join(col).strip('_') if col[1] else col[0] 
                      for col in monthly.columns.values]
    
    monthly.columns = ['YearMonth', 'median_price', 'mean_price', 'std_price', 'n_obs',
                      'median_unit_price', 'mean_unit_price', 'std_unit_price',
                      'discount_share_5pct', 'discount_share_10pct',
                      'discount_share_below_median', 'discount_share_below_q25',
                      'discount_share_keyword', 'discount_share_composite',
                      'n_unique_products']
    
    monthly['Date'] = monthly['YearMonth'].dt.to_timestamp()
    monthly['ln_price'] = np.log(monthly['median_price'])
    monthly['ln_unit_price'] = np.log(monthly['median_unit_price'])
    
    # Calculate price volatility (coefficient of variation)
    monthly['price_cv'] = monthly['std_price'] / monthly['mean_price']
    
    print(f"\nMonthly aggregation complete: {len(monthly)} months")
    print(f"\nDiscount metrics summary:")
    print(monthly[['discount_share_5pct', 'discount_share_10pct', 
                  'discount_share_below_median', 'discount_share_composite']].describe())
    
    return monthly


# =============================================================================
# REGRESSION: PRICE vs DISCOUNT INTENSITY
# =============================================================================

def analyze_discount_price_relationship(monthly_df):
    """
    Regression analysis: Does higher discount intensity predict lower average prices?
    """
    print(f"\n{'='*80}")
    print("REGRESSION: DISCOUNT INTENSITY → PRICE LEVEL")
    print(f"{'='*80}")
    
    # Model: ln(price) = α + β₁·discount_share + β₂·time_trend + ε
    
    monthly_df['time_trend'] = range(len(monthly_df))
    
    y = monthly_df['ln_price']
    X = monthly_df[['discount_share_composite', 'time_trend']]
    X = sm.add_constant(X)
    
    model = OLS(y, X)
    results = model.fit()
    
    print(results.summary())
    
    print(f"\n{'='*80}")
    print("INTERPRETATION")
    print(f"{'='*80}")
    print(f"Coefficient on discount_share: {results.params['discount_share_composite']:.4f}")
    print(f"p-value: {results.pvalues['discount_share_composite']:.4f}")
    
    if results.pvalues['discount_share_composite'] < 0.05:
        if results.params['discount_share_composite'] < 0:
            print("✓ Higher discount share → LOWER average prices (significant)")
        else:
            print("✓ Higher discount share → HIGHER average prices (significant)")
    else:
        print("✗ No significant relationship between discount share and price level")
    
    # Plot relationship
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.scatter(monthly_df['discount_share_composite'] * 100, 
              monthly_df['median_price'],
              s=100, alpha=0.6, color='#2E86AB', edgecolors='black')
    
    # Add fitted line
    from scipy.stats import linregress
    slope, intercept, r_val, p_val, std_err = linregress(
        monthly_df['discount_share_composite'], monthly_df['median_price']
    )
    x_fit = np.linspace(monthly_df['discount_share_composite'].min(),
                       monthly_df['discount_share_composite'].max(), 100)
    y_fit = intercept + slope * x_fit
    ax.plot(x_fit * 100, y_fit, 'r--', linewidth=2, 
           label=f'Fitted line (R²={r_val**2:.3f})')
    
    ax.set_title('Discount Intensity vs Average Price', fontsize=16, fontweight='bold')
    ax.set_xlabel('Discount Share (%)', fontsize=12)
    ax.set_ylabel('Median Price (UAH)', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/silpo_discount_vs_price.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return results


# =============================================================================
# TIME SERIES PLOTS: PRICE AND DISCOUNT EVOLUTION
# =============================================================================

def plot_price_discount_trends(monthly_df):
    """
    Plot price and discount share evolution over time
    """
    fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
    
    # Plot 1: Price evolution
    ax1 = axes[0]
    ax1.plot(monthly_df['Date'], monthly_df['median_price'], 
            linewidth=2.5, color='#2E86AB', marker='o', label='Median Price')
    ax1.fill_between(monthly_df['Date'],
                     monthly_df['mean_price'] - monthly_df['std_price'],
                     monthly_df['mean_price'] + monthly_df['std_price'],
                     alpha=0.2, color='#2E86AB', label='±1 Std Dev')
    
    ax1.set_title('Silpo Milk Prices Over Time', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Price (UAH)', fontsize=12)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Discount shares
    ax2 = axes[1]
    ax2.plot(monthly_df['Date'], monthly_df['discount_share_composite'] * 100,
            linewidth=2.5, color='#C73E1D', marker='s', label='Composite Discount Share')
    ax2.plot(monthly_df['Date'], monthly_df['discount_share_10pct'] * 100,
            linewidth=2, color='#F18F01', marker='^', alpha=0.7, label='Price Drop >10%')
    ax2.plot(monthly_df['Date'], monthly_df['discount_share_keyword'] * 100,
            linewidth=2, color='#6A994E', marker='D', alpha=0.7, label='Keyword Match')
    
    ax2.set_title('Discount Intensity Over Time', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Share of Products on Discount (%)', fontsize=12)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/silpo_price_discount_evolution.png', 
               dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nTime series plots saved")


# =============================================================================
# NARDL WITH DISCOUNT CONTROL
# =============================================================================

def nardl_with_discount_control(silpo_monthly, class3_monthly):
    """
    Estimate NARDL model with discount share as control variable
    
    Model: Price transmission may differ in periods of high vs low discounting
    """
    print(f"\n{'='*80}")
    print("NARDL MODEL WITH DISCOUNT CONTROL")
    print(f"{'='*80}")
    
    # Merge Silpo and Class III data
    merged = pd.merge(silpo_monthly[['Date', 'ln_unit_price', 'discount_share_composite']],
                     class3_monthly[['Date', 'ln_Price']],
                     on='Date', how='inner')
    
    merged.columns = ['Date', 'ln_Silpo', 'discount_share', 'ln_Class3']
    merged = merged.set_index('Date')
    
    print(f"\nMerged sample size: {len(merged)}")
    
    if len(merged) < 30:
        print("⚠ Sample too small for reliable NARDL estimation")
        return
    
    # Create NARDL data with discount as exogenous control
    from part05_nardl_asymmetric_transmission import create_nardl_data
    
    nardl_df = create_nardl_data(merged['ln_Silpo'], merged['ln_Class3'], 
                                p_lags=4, q_lags=4)
    
    # Add discount share (lagged)
    nardl_df['discount_lag1'] = merged['discount_share'].shift(1).loc[nardl_df.index]
    nardl_df = nardl_df.dropna()
    
    # Estimate with discount control
    exog_vars = ['y_lag1', 'x_pos_lag1', 'x_neg_lag1', 'discount_lag1']
    exog_vars += [f'delta_y_lag{i}' for i in range(1, 4)]
    exog_vars += [f'delta_x_pos_lag{i}' for i in range(4)]
    exog_vars += [f'delta_x_neg_lag{i}' for i in range(4)]
    
    y = nardl_df['delta_y']
    X = nardl_df[exog_vars]
    X = sm.add_constant(X)
    
    model = OLS(y, X)
    results = model.fit()
    
    print(results.summary())
    
    print(f"\n{'='*80}")
    print("DISCOUNT CONTROL VARIABLE INTERPRETATION")
    print(f"{'='*80}")
    print(f"Coefficient on discount_lag1: {results.params['discount_lag1']:.4f}")
    print(f"p-value: {results.pvalues['discount_lag1']:.4f}")
    
    if results.pvalues['discount_lag1'] < 0.05:
        print("✓ Discount intensity significantly affects price transmission dynamics")
    else:
        print("✗ Discount intensity does not significantly affect transmission")
    
    return results


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def run_silpo_discount_analysis():
    """
    Main pipeline for Silpo analysis with discount indicators
    """
    # Step 1: Load and process Silpo data
    silpo_df = load_silpo_with_discounts()
    
    # Step 2: Create monthly aggregates
    silpo_monthly = create_monthly_silpo_with_discounts(silpo_df)
    
    # Save processed monthly data
    silpo_monthly.to_csv(BASE_PATH + 'processed/silpo_monthly_with_discounts.csv', index=False)
    
    # Step 3: Regression analysis
    reg_results = analyze_discount_price_relationship(silpo_monthly)
    
    # Step 4: Time series visualization
    plot_price_discount_trends(silpo_monthly)
    
    # Step 5: NARDL with discount control (if Class III data available)
    try:
        class3_monthly = pd.read_csv(BASE_PATH + 'processed/class3_monthly.csv')
        class3_monthly['Date'] = pd.to_datetime(class3_monthly['Date'])
        
        nardl_results = nardl_with_discount_control(silpo_monthly, class3_monthly)
    except:
        print("\n⚠ Class III data not available for NARDL with discount control")
    
    print(f"\n{'='*80}")
    print("SILPO DISCOUNT ANALYSIS COMPLETE")
    print(f"{'='*80}")


if __name__ == "__main__":
    run_silpo_discount_analysis()
