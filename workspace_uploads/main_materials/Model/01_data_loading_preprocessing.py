# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# Part 1: Data Loading and Preprocessing
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set paths
BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.max_rows', 100)

# =============================================================================
# 1. CLASS III MILK FUTURES DATA (CME - US Benchmark)
# =============================================================================

def load_class3_data():
    """
    Load and preprocess CME Class III Milk Futures data
    - Convert American date format (MM/DD/YYYY) to datetime
    - Clean volume and percentage change columns
    - Create monthly aggregates
    """
    print("="*80)
    print("LOADING CLASS III MILK FUTURES DATA")
    print("="*80)
    
    df = pd.read_csv(BASE_PATH + 'Class-III-Milk-Futures-Historical-Data-2.csv')
    
    # Convert Date column (American format: MM/DD/YYYY)
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    
    # Clean Volume column (remove 'K' and convert to numeric)
    df['Vol.'] = df['Vol.'].str.replace('K', '').astype(float) * 1000
    
    # Clean Change % (remove '%' and convert to numeric)
    df['Change %'] = df['Change %'].str.replace('%', '').astype(float) / 100
    
    # Sort by date ascending
    df = df.sort_values('Date').reset_index(drop=True)
    
    # Create year-month column for aggregation
    df['YearMonth'] = df['Date'].dt.to_period('M')
    
    # Print summary
    print(f"\nShape: {df.shape}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"\nDescriptive Statistics:")
    print(df[['Price', 'Open', 'High', 'Low', 'Vol.']].describe())
    
    # Create monthly aggregates
    monthly_class3 = df.groupby('YearMonth').agg({
        'Price': 'mean',
        'Open': 'mean',
        'High': 'max',
        'Low': 'min',
        'Vol.': 'sum',
        'Change %': 'mean'
    }).reset_index()
    
    monthly_class3['Date'] = monthly_class3['YearMonth'].dt.to_timestamp()
    monthly_class3['ln_Price'] = np.log(monthly_class3['Price'])
    
    print(f"\nMonthly aggregates shape: {monthly_class3.shape}")
    print(f"\nFirst 5 monthly observations:")
    print(monthly_class3.head())
    
    return df, monthly_class3


# =============================================================================
# 2. NOVUS RETAIL DATA
# =============================================================================

def load_novus_data():
    """
    Load and preprocess Novus retail dairy prices
    - Parse scraped_at timestamp
    - Extract product characteristics from title
    - Calculate unit prices (UAH per liter/kg)
    - Identify discount patterns
    """
    print("\n" + "="*80)
    print("LOADING NOVUS RETAIL DATA")
    print("="*80)
    
    df = pd.read_excel(BASE_PATH + 'Novus_newest.xlsx')
    
    # Parse timestamp
    df['scraped_at'] = pd.to_datetime(df['scraped_at'])
    df['Date'] = df['scraped_at'].dt.date
    df['YearMonth'] = df['scraped_at'].dt.to_period('M')
    
    # Extract volume from title (using regex)
    import re
    def extract_volume(title):
        """Extract volume in grams or liters"""
        match = re.search(r'(\d+(?:\.\d+)?)\s*(г|мл|л|kg)', str(title))
        if match:
            vol = float(match.group(1))
            unit = match.group(2)
            # Convert to liters/kg
            if unit in ['г', 'мл']:
                vol = vol / 1000
            return vol
        return np.nan
    
    df['volume'] = df['title'].apply(extract_volume)
    
    # Calculate unit price (UAH per liter or kg)
    df['unit_price'] = df['price'] / df['volume']
    
    # Product categorization
    df['product_type'] = 'Other'
    df.loc[df['title'].str.contains('Молоко|молоко', na=False, case=False), 'product_type'] = 'Milk'
    df.loc[df['title'].str.contains('Йогурт|йогурт', na=False, case=False), 'product_type'] = 'Yogurt'
    df.loc[df['title'].str.contains('Сир|сир', na=False, case=False), 'product_type'] = 'Cheese'
    df.loc[df['title'].str.contains('Кефір|кефір', na=False, case=False), 'product_type'] = 'Kefir'
    df.loc[df['title'].str.contains('Ряжанка|ряжанка', na=False, case=False), 'product_type'] = 'Ryazhenka'
    df.loc[df['title'].str.contains('Масло|масло', na=False, case=False), 'product_type'] = 'Butter'
    df.loc[df['title'].str.contains('Вершки|вершки', na=False, case=False), 'product_type'] = 'Cream'
    
    # Extract fat content
    def extract_fat(title):
        match = re.search(r'(\d+(?:\.\d+)?)\s*%', str(title))
        if match:
            return float(match.group(1))
        return np.nan
    
    df['fat_content'] = df['title'].apply(extract_fat)
    
    print(f"\nShape: {df.shape}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"\nProduct type distribution:")
    print(df['product_type'].value_counts())
    
    print(f"\nPrice statistics:")
    print(df[['price', 'unit_price']].describe())
    
    # Filter milk products for main analysis
    milk_df = df[df['product_type'] == 'Milk'].copy()
    
    # Monthly aggregates
    monthly_novus = milk_df.groupby('YearMonth').agg({
        'price': 'median',
        'unit_price': 'median',
        'id': 'count'  # Number of observations
    }).reset_index()
    
    monthly_novus.columns = ['YearMonth', 'median_price', 'median_unit_price', 'n_obs']
    monthly_novus['Date'] = monthly_novus['YearMonth'].dt.to_timestamp()
    monthly_novus['ln_price'] = np.log(monthly_novus['median_price'])
    monthly_novus['ln_unit_price'] = np.log(monthly_novus['median_unit_price'])
    
    print(f"\nMonthly milk price aggregates:")
    print(monthly_novus)
    
    return df, milk_df, monthly_novus


# =============================================================================
# 3. SILPO RETAIL DATA
# =============================================================================

def load_silpo_data():
    """
    Load and preprocess Silpo retail dairy prices
    - Similar processing as Novus
    - Add discount indicator (binary variable)
    - Check for promotional pricing patterns
    """
    print("\n" + "="*80)
    print("LOADING SILPO RETAIL DATA")
    print("="*80)
    
    # For large file, use chunking or specific columns
    try:
        df = pd.read_excel(BASE_PATH + 'Silpo.xlsx',
                          usecols=['id', 'title', 'price', 'scraped_at', 'category'])
        
        # Parse timestamp
        df['scraped_at'] = pd.to_datetime(df['scraped_at'])
        df['Date'] = df['scraped_at'].dt.date
        df['YearMonth'] = df['scraped_at'].dt.to_period('M')
        
        # Extract volume (same function as Novus)
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
        
        # **DISCOUNT INDICATOR**
        # Method 1: Identify price drops within same product over time
        df = df.sort_values(['id', 'Date']).reset_index(drop=True)
        df['prev_price'] = df.groupby('id')['price'].shift(1)
        df['price_change'] = df['price'] - df['prev_price']
        df['discount_binary'] = (df['price_change'] < -1).astype(int)  # Discount if price drops >1 UAH
        
        # Method 2: Flag if price is below product's median (promotional pricing)
        df['product_median_price'] = df.groupby('id')['price'].transform('median')
        df['below_median'] = (df['price'] < df['product_median_price'] * 0.95).astype(int)
        
        print(f"\nShape: {df.shape}")
        print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
        print(f"\nProduct type distribution:")
        print(df['product_type'].value_counts())
        
        print(f"\nDiscount statistics:")
        print(f"Products with discount (method 1): {df['discount_binary'].sum()}")
        print(f"Products below median (method 2): {df['below_median'].sum()}")
        
        # Filter milk products
        milk_df = df[df['product_type'] == 'Milk'].copy()
        
        # Monthly aggregates with discount share
        monthly_silpo = milk_df.groupby('YearMonth').agg({
            'price': 'median',
            'unit_price': 'median',
            'discount_binary': 'mean',  # Share of products on discount
            'below_median': 'mean',
            'id': 'count'
        }).reset_index()
        
        monthly_silpo.columns = ['YearMonth', 'median_price', 'median_unit_price', 
                                'discount_share', 'below_median_share', 'n_obs']
        monthly_silpo['Date'] = monthly_silpo['YearMonth'].dt.to_timestamp()
        monthly_silpo['ln_price'] = np.log(monthly_silpo['median_price'])
        monthly_silpo['ln_unit_price'] = np.log(monthly_silpo['median_unit_price'])
        
        print(f"\nMonthly milk price aggregates with discount indicators:")
        print(monthly_silpo)
        
        return df, milk_df, monthly_silpo
        
    except Exception as e:
        print(f"Error loading Silpo data: {e}")
        print("File may be too large. Consider using csv conversion or chunking.")
        return None, None, None


# =============================================================================
# 4. EU MILK PRICE DATA
# =============================================================================

def load_eu_milk_data():
    """
    Load EU milk historical price series
    - Multiple sheets may exist (by product, by country)
    - Harmonize to monthly frequency
    - Calculate EU average benchmark
    """
    print("\n" + "="*80)
    print("LOADING EU MILK PRICE DATA")
    print("="*80)
    
    # Load all sheets
    excel_file = pd.ExcelFile(BASE_PATH + 'eu-milk-historical-price-series_en07012026.xlsx')
    print(f"Available sheets: {excel_file.sheet_names}")
    
    # Load main price sheet (adjust sheet name based on actual file)
    # Common sheet names: 'Milk', 'Raw milk', 'Prices', 'Data'
    
    df_dict = {}
    for sheet in excel_file.sheet_names[:3]:  # Load first 3 sheets
        df_dict[sheet] = pd.read_excel(excel_file, sheet_name=sheet)
        print(f"\nSheet '{sheet}' shape: {df_dict[sheet].shape}")
        print(f"Columns: {df_dict[sheet].columns.tolist()}")
        print(f"First 3 rows:")
        print(df_dict[sheet].head(3))
    
    # Assuming main sheet has date column and price columns by country
    # Adjust based on actual structure
    
    return df_dict


# =============================================================================
# 5. DAIRY ENRICHED FILTERED DATA (PROZZORO)
# =============================================================================

def load_prozzoro_data():
    """
    Load Prozzoro public procurement tender data for dairy products
    - Contains government purchase prices
    - May have multiple product categories
    - Extract date, price, quantity, product description
    """
    print("\n" + "="*80)
    print("LOADING PROZZORO DAIRY TENDER DATA")
    print("="*80)
    
    df = pd.read_excel(BASE_PATH + 'dairy_enriched_filtered.xlsx')
    
    print(f"\nShape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    print(f"\nData types:")
    print(df.dtypes)
    
    print(f"\nMissing values:")
    print(df.isnull().sum())
    
    # Identify date columns
    date_cols = [col for col in df.columns if 'date' in col.lower() or 'дата' in col.lower()]
    print(f"\nPotential date columns: {date_cols}")
    
    # Identify price columns
    price_cols = [col for col in df.columns if 'price' in col.lower() or 'ціна' in col.lower() or 'вартість' in col.lower()]
    print(f"Potential price columns: {price_cols}")
    
    return df


# =============================================================================
# 6. EJgxfgP INTERPOLATED DATA
# =============================================================================

def load_ejgxfgp_data():
    """
    Load EJgxfgP daily interpolated data
    - May contain interpolated EU prices at daily frequency
    - Compare real vs interpolated values
    """
    print("\n" + "="*80)
    print("LOADING EJgxfgP INTERPOLATED DATA")
    print("="*80)
    
    df = pd.read_excel(BASE_PATH + 'EJgxfgP_daily_interpolated.xlsx')
    
    print(f"\nShape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    # Check for date column
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    print(f"\nDate columns: {date_cols}")
    
    return df


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    
    # Load all datasets
    class3_daily, class3_monthly = load_class3_data()
    novus_daily, novus_milk, novus_monthly = load_novus_data()
    silpo_daily, silpo_milk, silpo_monthly = load_silpo_data()
    eu_data = load_eu_milk_data()
    prozzoro_data = load_prozzoro_data()
    ejgxfgp_data = load_ejgxfgp_data()
    
    # Save processed monthly data
    class3_monthly.to_csv(BASE_PATH + 'processed/class3_monthly.csv', index=False)
    novus_monthly.to_csv(BASE_PATH + 'processed/novus_monthly.csv', index=False)
    if silpo_monthly is not None:
        silpo_monthly.to_csv(BASE_PATH + 'processed/silpo_monthly.csv', index=False)
    
    print("\n" + "="*80)
    print("DATA LOADING COMPLETE")
    print("="*80)
