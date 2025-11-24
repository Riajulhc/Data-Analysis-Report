import sys
import os
from pathlib import Path
from src.data_processor import load_data, clean_data, analyze_sales

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def generate_report(metrics: dict):
    
    def format_currency(value):
        return f"${value:,.2f}"

    print("\n" + "="*50)
    print("       MONTHLY SALES ANALYSIS REPORT       ")
    print("="*50)

    print("\n--- 1. OVERALL PERFORMANCE ---")
    print(f"Total Revenue Generated:  {format_currency(metrics['total_revenue'])}")
    print(f"Total Units Sold:         {metrics['total_units']:,}")
    print(f"Average Order Value:      {format_currency(metrics['average_order_value'])}")

    print("\n--- 2. KEY INSIGHTS ---")
    print(f"Highest Performing Region: {metrics['top_region']}")
    
    print("\n" + "="*50)
    print("         Report Generation Complete          ")
    print("="*50)


def main():
    base_dir = Path(__file__).resolve().parent.parent 
    data_file_path = base_dir / "data" / "sales_data.csv"
    
    print("Starting Sales Data Analysis...")
    
    df_raw = load_data(data_file_path)
    if df_raw is None:
        print("Aborting report generation due to data loading failure.")
        return

    df_cleaned = clean_data(df_raw)
    
    if df_cleaned.empty:
        print("Aborting report generation: Cleaned dataset is empty.")
        return
        
    metrics = analyze_sales(df_cleaned)
    
    generate_report(metrics)


if __name__ == "__main__":
    init_file = Path(__file__).resolve().parent / "__init__.py"
    if not init_file.exists():
        with open(init_file, 'w') as f:
            f.write("# This makes 'src' a Python package.")
            
    main()