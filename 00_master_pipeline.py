# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# MASTER SCRIPT - Run Complete Analysis Pipeline
# =============================================================================

"""
This master script orchestrates the complete analysis pipeline for the dairy
price transmission thesis. It runs all components in sequence.

USAGE:
    python 00_master_pipeline.py

DIRECTORY STRUCTURE REQUIRED:
    /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/
    ├── Class-III-Milk-Futures-Historical-Data-2.csv
    ├── Novus_newest.xlsx
    ├── Silpo.xlsx
    ├── dairy_enriched_filtered.xlsx
    ├── eu-milk-historical-price-series_en07012026.xlsx
    ├── EJgxfgP_daily_interpolated.xlsx
    ├── processed/      (will be created)
    ├── plots/          (will be created)
    └── results/        (will be created)

OUTPUTS:
    - Processed monthly datasets (CSV)
    - Descriptive statistics tables
    - Stationarity test results
    - VECM and NARDL model outputs
    - Comparison tables and visualizations
    - Publication-ready plots (PNG, 300 DPI)
"""

import os
import sys
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Add current directory to path
sys.path.append(os.getcwd())

BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# =============================================================================
# SETUP
# =============================================================================

def create_directories():
    """
    Create necessary subdirectories for outputs
    """
    print("="*80)
    print("SETTING UP DIRECTORY STRUCTURE")
    print("="*80)
    
    dirs = ['processed', 'plots', 'results']
    
    for dir_name in dirs:
        dir_path = os.path.join(BASE_PATH, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"✓ Created directory: {dir_name}/")
        else:
            print(f"✓ Directory exists: {dir_name}/")
    
    print("\n")


def check_data_files():
    """
    Verify that all required data files are present
    """
    print("="*80)
    print("CHECKING DATA FILES")
    print("="*80)
    
    required_files = [
        'Class-III-Milk-Futures-Historical-Data-2.csv',
        'Novus_newest.xlsx',
        'Silpo.xlsx',
        'dairy_enriched_filtered.xlsx',
        'eu-milk-historical-price-series_en07012026.xlsx',
        'EJgxfgP_daily_interpolated.xlsx'
    ]
    
    missing_files = []
    
    for filename in required_files:
        filepath = os.path.join(BASE_PATH, filename)
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath) / (1024 * 1024)  # MB
            print(f"✓ {filename} ({file_size:.2f} MB)")
        else:
            print(f"✗ {filename} - NOT FOUND")
            missing_files.append(filename)
    
    if missing_files:
        print(f"\n⚠ WARNING: {len(missing_files)} file(s) missing")
        print("Some analyses may fail. Continue anyway? (y/n)")
        response = input().lower()
        if response != 'y':
            print("Exiting...")
            sys.exit(1)
    
    print("\n")


# =============================================================================
# PIPELINE COMPONENTS
# =============================================================================

def run_data_loading():
    """
    Step 1: Load and preprocess all datasets
    """
    print("="*80)
    print("STEP 1: DATA LOADING AND PREPROCESSING")
    print("="*80)
    
    try:
        from part01_data_loading_preprocessing import (
            load_class3_data,
            load_novus_data,
            load_silpo_data,
            load_eu_milk_data,
            load_prozzoro_data,
            load_ejgxfgp_data
        )
        
        # Load each dataset
        class3_daily, class3_monthly = load_class3_data()
        novus_daily, novus_milk, novus_monthly = load_novus_data()
        
        # Silpo may timeout - handle gracefully
        try:
            silpo_daily, silpo_milk, silpo_monthly = load_silpo_data()
        except Exception as e:
            print(f"\n⚠ Silpo loading failed: {e}")
            print("Continuing without Silpo data...")
        
        # EU and Prozzoro data
        try:
            eu_data = load_eu_milk_data()
        except Exception as e:
            print(f"\n⚠ EU data loading failed: {e}")
        
        try:
            prozzoro_data = load_prozzoro_data()
        except Exception as e:
            print(f"\n⚠ Prozzoro data loading failed: {e}")
        
        try:
            ejgxfgp_data = load_ejgxfgp_data()
        except Exception as e:
            print(f"\n⚠ EJgxfgP data loading failed: {e}")
        
        print("\n✓ Data loading complete\n")
        
    except Exception as e:
        print(f"\n✗ Data loading failed: {e}")
        raise


def run_descriptive_analysis():
    """
    Step 2: Descriptive statistics and visualization
    """
    print("="*80)
    print("STEP 2: DESCRIPTIVE STATISTICS")
    print("="*80)
    
    try:
        from part02_descriptive_statistics import run_descriptive_analysis
        run_descriptive_analysis()
        print("\n✓ Descriptive analysis complete\n")
    except Exception as e:
        print(f"\n✗ Descriptive analysis failed: {e}")
        raise


def run_stationarity_tests():
    """
    Step 3: Stationarity tests (ADF, KPSS, integration order)
    """
    print("="*80)
    print("STEP 3: STATIONARITY TESTS")
    print("="*80)
    
    try:
        from part03_stationarity_tests import run_stationarity_tests
        run_stationarity_tests()
        print("\n✓ Stationarity tests complete\n")
    except Exception as e:
        print(f"\n✗ Stationarity tests failed: {e}")
        raise


def run_vecm_analysis():
    """
    Step 4: VECM cointegration analysis
    """
    print("="*80)
    print("STEP 4: VECM COINTEGRATION ANALYSIS")
    print("="*80)
    
    try:
        from part04_vecm_cointegration import run_vecm_analysis
        run_vecm_analysis()
        print("\n✓ VECM analysis complete\n")
    except Exception as e:
        print(f"\n✗ VECM analysis failed: {e}")
        print("This may be due to insufficient overlapping data. Continuing...")


def run_nardl_analysis():
    """
    Step 5: NARDL asymmetric transmission analysis
    """
    print("="*80)
    print("STEP 5: NARDL ASYMMETRIC PRICE TRANSMISSION")
    print("="*80)
    
    try:
        from part05_nardl_asymmetric_transmission import run_nardl_analysis
        run_nardl_analysis()
        print("\n✓ NARDL analysis complete\n")
    except Exception as e:
        print(f"\n✗ NARDL analysis failed: {e}")
        print("This may be due to insufficient data. Continuing...")


def run_silpo_discount_analysis():
    """
    Step 6: Silpo-specific analysis with discount indicators
    """
    print("="*80)
    print("STEP 6: SILPO DISCOUNT ANALYSIS")
    print("="*80)
    
    try:
        from part06_silpo_discount_analysis import run_silpo_discount_analysis
        run_silpo_discount_analysis()
        print("\n✓ Silpo discount analysis complete\n")
    except Exception as e:
        print(f"\n✗ Silpo analysis failed: {e}")
        print("This may be due to file size issues. Continuing...")


def run_eu_us_comparison():
    """
    Step 7: EU vs US milk price comparison
    """
    print("="*80)
    print("STEP 7: EU vs US COMPARISON")
    print("="*80)
    
    try:
        from part07_eu_us_comparison import run_eu_us_comparison
        run_eu_us_comparison()
        print("\n✓ EU vs US comparison complete\n")
    except Exception as e:
        print(f"\n✗ EU vs US comparison failed: {e}")
        print("Continuing...")


def run_prozzoro_analysis():
    """
    Step 8: Prozzoro public procurement analysis
    """
    print("="*80)
    print("STEP 8: PROZZORO ANALYSIS")
    print("="*80)
    
    try:
        from part08_prozzoro_analysis import run_prozzoro_analysis
        run_prozzoro_analysis()
        print("\n✓ Prozzoro analysis complete\n")
    except Exception as e:
        print(f"\n✗ Prozzoro analysis failed: {e}")
        print("Continuing...")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """
    Execute complete analysis pipeline
    """
    start_time = datetime.now()
    
    print("\n" + "="*80)
    print("DAIRY PRICE TRANSMISSION ANALYSIS - MASTER PIPELINE")
    print("="*80)
    print(f"Start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")
    
    # Setup
    create_directories()
    check_data_files()
    
    # Analysis pipeline
    steps = [
        ("Data Loading", run_data_loading),
        ("Descriptive Statistics", run_descriptive_analysis),
        ("Stationarity Tests", run_stationarity_tests),
        ("VECM Analysis", run_vecm_analysis),
        ("NARDL Analysis", run_nardl_analysis),
        ("Silpo Discount Analysis", run_silpo_discount_analysis),
        ("EU vs US Comparison", run_eu_us_comparison),
        ("Prozzoro Analysis", run_prozzoro_analysis)
    ]
    
    completed_steps = []
    failed_steps = []
    
    for step_name, step_function in steps:
        try:
            print(f"\n{'='*80}")
            print(f"RUNNING: {step_name}")
            print(f"{'='*80}\n")
            
            step_function()
            completed_steps.append(step_name)
            
        except Exception as e:
            print(f"\n✗ {step_name} FAILED: {e}")
            failed_steps.append((step_name, str(e)))
            
            print("\nContinue to next step? (y/n)")
            response = input().lower()
            if response != 'y':
                print("Pipeline interrupted by user.")
                break
    
    # Summary
    end_time = datetime.now()
    duration = end_time - start_time
    
    print("\n" + "="*80)
    print("PIPELINE EXECUTION SUMMARY")
    print("="*80)
    print(f"Start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"End time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Duration: {duration}")
    print(f"\nCompleted steps: {len(completed_steps)}/{len(steps)}")
    
    if completed_steps:
        print("\n✓ Completed:")
        for step in completed_steps:
            print(f"  - {step}")
    
    if failed_steps:
        print("\n✗ Failed:")
        for step, error in failed_steps:
            print(f"  - {step}: {error}")
    
    print("\n" + "="*80)
    print("OUTPUTS SAVED TO:")
    print("="*80)
    print(f"  - Processed data: {BASE_PATH}processed/")
    print(f"  - Plots: {BASE_PATH}plots/")
    print(f"  - Results: {BASE_PATH}results/")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
