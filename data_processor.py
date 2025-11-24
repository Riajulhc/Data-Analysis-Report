import pandas as pd
from pathlib import Path

EXPECTED_COLUMNS = {
    'OrderID': 'int64', 
    'Region': 'object',
    'Product': 'object', 
    'UnitsSold': 'int64',
    'Revenue': 'float64', 
    'Date': 'object'
}

def load_data(file_path: Path) -> pd.DataFrame | None:
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Data loaded successfully from: {file_path.name}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("❌ Error: The CSV file is empty.")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred during data loading: {e}")
        return None

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    for col, dtype in EXPECTED_COLUMNS.items():
        if col in df.columns:
            try:
                if col == 'Date':
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                elif df[col].dtype != dtype:
                    df[col] = df[col].astype(dtype)
            except Exception:
                df[col] = df[col].replace('', pd.NA).replace('NA', pd.NA)
                print(f"⚠️ Warning: Could not fully convert column '{col}' to {dtype}. Unconvertible values set to missing.")
    
    initial_rows = len(df)
    df.dropna(inplace=True)
    rows_dropped = initial_rows - len(df)
    if rows_dropped > 0:
        print(f"🧹 Cleaned data: Dropped {rows_dropped} rows with missing values.")
        
    return df

def analyze_sales(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            'total_revenue': 0.0,
            'total_units': 0,
            'average_order_value': 0.0,
            'top_region': 'N/A'
        }

    total_revenue = df['Revenue'].sum()
    total_units = df['UnitsSold'].sum()
    
    unique_orders_count = df['OrderID'].nunique()
    average_order_value = total_revenue / unique_orders_count if unique_orders_count > 0 else 0.0
    
    regional_sales = df.groupby('Region')['Revenue'].sum()
    top_region = regional_sales.idxmax() if not regional_sales.empty else 'N/A'
    
    return {
        'total_revenue': total_revenue,
        'total_units': total_units,
        'average_order_value': average_order_value,
        'top_region': top_region
    }