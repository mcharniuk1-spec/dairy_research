# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# Part 2: Descriptive Statistics and Visualization
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# =============================================================================
# DESCRIPTIVE STATISTICS FUNCTIONS
# =============================================================================

def calculate_descriptive_stats(df, price_col, name):
    """
    Calculate comprehensive descriptive statistics for price series
    """
    print(f"\n{'='*80}")
    print(f"DESCRIPTIVE STATISTICS: {name}")
    print(f"{'='*80}")
    
    stats_dict = {
        'N': len(df),
        'Mean': df[price_col].mean(),
        'Median': df[price_col].median(),
        'Std Dev': df[price_col].std(),
        'Min': df[price_col].min(),
        'Max': df[price_col].max(),
        'Range': df[price_col].max() - df[price_col].min(),
        'CV (%)': (df[price_col].std() / df[price_col].mean()) * 100,
        'Skewness': stats.skew(df[price_col].dropna()),
        'Kurtosis': stats.kurtosis(df[price_col].dropna()),
        'Q1': df[price_col].quantile(0.25),
        'Q3': df[price_col].quantile(0.75),
        'IQR': df[price_col].quantile(0.75) - df[price_col].quantile(0.25)
    }
    
    stats_df = pd.DataFrame([stats_dict]).T
    stats_df.columns = ['Value']
    print(stats_df)
    
    # Test for normality
    _, p_value = stats.shapiro(df[price_col].dropna()[:5000])  # Shapiro-Wilk test (max 5000 obs)
    print(f"\nShapiro-Wilk normality test p-value: {p_value:.6f}")
    if p_value < 0.05:
        print("→ Reject H0: Data is NOT normally distributed")
    else:
        print("→ Fail to reject H0: Data appears normally distributed")
    
    return stats_df


def plot_time_series(df, date_col, price_col, title, save_name):
    """
    Plot price time series with trend
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    ax.plot(df[date_col], df[price_col], linewidth=1.5, label='Price', color='#2E86AB')
    
    # Add moving average
    df['MA_30'] = df[price_col].rolling(window=30, min_periods=1).mean()
    ax.plot(df[date_col], df['MA_30'], linewidth=2, label='30-period MA', 
            color='#A23B72', linestyle='--', alpha=0.7)
    
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price', fontsize=12)
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + f'plots/{save_name}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Plot saved: {save_name}.png")


def plot_distribution(df, price_col, title, save_name):
    """
    Plot price distribution histogram with normal curve
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histogram with KDE
    axes[0].hist(df[price_col].dropna(), bins=50, density=True, 
                 alpha=0.7, color='#2E86AB', edgecolor='black')
    
    # Fit normal distribution
    mu, sigma = df[price_col].mean(), df[price_col].std()
    x = np.linspace(df[price_col].min(), df[price_col].max(), 100)
    axes[0].plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2, 
                label=f'Normal(μ={mu:.2f}, σ={sigma:.2f})')
    
    axes[0].set_title(f'{title} - Histogram', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Price', fontsize=11)
    axes[0].set_ylabel('Density', fontsize=11)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Q-Q plot
    stats.probplot(df[price_col].dropna(), dist="norm", plot=axes[1])
    axes[1].set_title(f'{title} - Q-Q Plot', fontsize=14, fontweight='bold')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + f'plots/{save_name}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Plot saved: {save_name}.png")


def plot_correlation_matrix(df, cols, title, save_name):
    """
    Plot correlation matrix heatmap
    """
    corr = df[cols].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt='.3f', cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + f'plots/{save_name}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Plot saved: {save_name}.png")


def compare_price_series(df, date_col, price_cols, labels, title, save_name):
    """
    Compare multiple price series on same plot (normalized to 100)
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E']
    
    for i, (col, label) in enumerate(zip(price_cols, labels)):
        # Normalize to 100 at first observation
        normalized = (df[col] / df[col].iloc[0]) * 100
        ax.plot(df[date_col], normalized, linewidth=2, label=label, color=colors[i % len(colors)])
    
    ax.axhline(y=100, color='black', linestyle='--', linewidth=1, alpha=0.5)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Index (First observation = 100)', fontsize=12)
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + f'plots/{save_name}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Plot saved: {save_name}.png")


# =============================================================================
# MAIN DESCRIPTIVE ANALYSIS
# =============================================================================

def run_descriptive_analysis():
    """
    Run comprehensive descriptive analysis on all datasets
    """
    
    # Load processed data
    print("Loading processed datasets...")
    
    class3_monthly = pd.read_csv(BASE_PATH + 'processed/class3_monthly.csv')
    class3_monthly['Date'] = pd.to_datetime(class3_monthly['Date'])
    
    novus_monthly = pd.read_csv(BASE_PATH + 'processed/novus_monthly.csv')
    novus_monthly['Date'] = pd.to_datetime(novus_monthly['Date'])
    
    try:
        silpo_monthly = pd.read_csv(BASE_PATH + 'processed/silpo_monthly.csv')
        silpo_monthly['Date'] = pd.to_datetime(silpo_monthly['Date'])
        has_silpo = True
    except:
        print("Silpo data not available")
        has_silpo = False
    
    # =========================================================================
    # 1. CLASS III MILK FUTURES DESCRIPTIVE STATS
    # =========================================================================
    
    stats_class3 = calculate_descriptive_stats(class3_monthly, 'Price', 
                                               'CME Class III Milk Futures (Monthly)')
    
    plot_time_series(class3_monthly, 'Date', 'Price', 
                    'CME Class III Milk Futures - Monthly Average Price',
                    'class3_timeseries')
    
    plot_distribution(class3_monthly, 'Price',
                     'CME Class III Milk Futures',
                     'class3_distribution')
    
    # =========================================================================
    # 2. NOVUS RETAIL DESCRIPTIVE STATS
    # =========================================================================
    
    stats_novus = calculate_descriptive_stats(novus_monthly, 'median_unit_price',
                                             'Novus Retail Milk Prices (Monthly)')
    
    plot_time_series(novus_monthly, 'Date', 'median_unit_price',
                    'Novus - Median Milk Unit Price (UAH/L)',
                    'novus_timeseries')
    
    plot_distribution(novus_monthly, 'median_unit_price',
                     'Novus Retail Prices',
                     'novus_distribution')
    
    # =========================================================================
    # 3. SILPO RETAIL DESCRIPTIVE STATS (if available)
    # =========================================================================
    
    if has_silpo:
        stats_silpo = calculate_descriptive_stats(silpo_monthly, 'median_unit_price',
                                                  'Silpo Retail Milk Prices (Monthly)')
        
        plot_time_series(silpo_monthly, 'Date', 'median_unit_price',
                        'Silpo - Median Milk Unit Price (UAH/L)',
                        'silpo_timeseries')
        
        plot_distribution(silpo_monthly, 'median_unit_price',
                         'Silpo Retail Prices',
                         'silpo_distribution')
        
        # Discount analysis
        print(f"\n{'='*80}")
        print("SILPO DISCOUNT PATTERN ANALYSIS")
        print(f"{'='*80}")
        print(f"\nMean discount share: {silpo_monthly['discount_share'].mean():.2%}")
        print(f"Max discount share: {silpo_monthly['discount_share'].max():.2%}")
        print(f"Min discount share: {silpo_monthly['discount_share'].min():.2%}")
        
        # Plot discount trends
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(silpo_monthly['Date'], silpo_monthly['discount_share'] * 100,
               linewidth=2, color='#C73E1D', label='Discount Share (%)')
        ax.set_title('Silpo - Share of Milk Products on Discount Over Time',
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Discount Share (%)', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        plt.tight_layout()
        plt.savefig(BASE_PATH + 'plots/silpo_discount_trends.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    # =========================================================================
    # 4. COMPARE NOVUS vs SILPO (if both available)
    # =========================================================================
    
    if has_silpo:
        # Merge datasets
        comparison = pd.merge(novus_monthly[['Date', 'median_unit_price']], 
                            silpo_monthly[['Date', 'median_unit_price']], 
                            on='Date', suffixes=('_novus', '_silpo'))
        
        # Correlation
        corr = comparison[['median_unit_price_novus', 'median_unit_price_silpo']].corr()
        print(f"\n{'='*80}")
        print("NOVUS vs SILPO PRICE CORRELATION")
        print(f"{'='*80}")
        print(corr)
        
        # Plot comparison
        compare_price_series(comparison, 'Date',
                           ['median_unit_price_novus', 'median_unit_price_silpo'],
                           ['Novus', 'Silpo'],
                           'Retail Milk Prices: Novus vs Silpo (Indexed to 100)',
                           'novus_vs_silpo_comparison')
    
    # =========================================================================
    # 5. SUMMARY TABLE
    # =========================================================================
    
    summary_data = {
        'Dataset': ['CME Class III', 'Novus Retail', 'Silpo Retail'],
        'N_Months': [len(class3_monthly), len(novus_monthly), 
                    len(silpo_monthly) if has_silpo else 0],
        'Mean_Price': [class3_monthly['Price'].mean(), 
                      novus_monthly['median_unit_price'].mean(),
                      silpo_monthly['median_unit_price'].mean() if has_silpo else np.nan],
        'Std_Dev': [class3_monthly['Price'].std(),
                   novus_monthly['median_unit_price'].std(),
                   silpo_monthly['median_unit_price'].std() if has_silpo else np.nan],
        'CV_%': [(class3_monthly['Price'].std() / class3_monthly['Price'].mean()) * 100,
                (novus_monthly['median_unit_price'].std() / novus_monthly['median_unit_price'].mean()) * 100,
                (silpo_monthly['median_unit_price'].std() / silpo_monthly['median_unit_price'].mean()) * 100 if has_silpo else np.nan]
    }
    
    summary_df = pd.DataFrame(summary_data)
    print(f"\n{'='*80}")
    print("SUMMARY COMPARISON TABLE")
    print(f"{'='*80}")
    print(summary_df.to_string(index=False))
    
    summary_df.to_csv(BASE_PATH + 'results/descriptive_summary.csv', index=False)
    
    print(f"\n{'='*80}")
    print("DESCRIPTIVE ANALYSIS COMPLETE")
    print(f"{'='*80}")


if __name__ == "__main__":
    run_descriptive_analysis()
