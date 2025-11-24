 Sales Data Reporter

A simple, structured Python project designed to analyze raw sales data from a CSV file, calculate key business metrics, and generate a concise report. This project demonstrates modular programming, data manipulation using pandas, and robust file path handling.

 Features

Data Loading: Safely loads sales data from the ./data directory.

Data Cleaning: Handles potential missing values or incorrect data types.

Key Metric Calculation: Calculates total sales, average order value, and the top-selling region.

Reporting: Outputs a clean, formatted analysis report to the console.

 Setup and Installation

Prerequisites

You need Python 3.8+ installed. This project relies on the pandas library.

Clone the repository:

git clone [your-repo-link]
cd sales-data-reporter


Create and activate a virtual environment (Recommended):

python -m venv .venv
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate  # On Windows


Install dependencies:

pip install pandas


 Usage

To run the report generation, execute the main script located in the src directory:

python src/report_generator.py


Input Data

The raw data is expected in the ./data/sales_data.csv file. You can replace this file with your own dataset, provided it maintains the required columns: OrderID, Region, Product, UnitsSold, and Revenue.

 Project Structure

.
├── data/
│   └── sales_data.csv        # Input data file
├── src/
│   ├── __init__.py           # Makes 'src' a Python package
│   ├── data_processor.py     # Module for data loading and analysis
│   └── report_generator.py   # Main execution script
└── README.md
