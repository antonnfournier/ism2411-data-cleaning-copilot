"""
This script loads a messy sales dataset, applies a series of data-cleaning steps,
and outputs a cleaned CSV file. The goal is to standardize column names,
remove whitespace, handle missing values, and remove clearly invalid rows.
The cleaned dataset is saved to data/processed/sales_data_clean.csv.
"""

import pandas as pd


# Function: load_data
# This was generated from GitHub Copilot
# What it does: Loads the raw CSV file into a pandas DataFrame.
# Why: All cleaning steps require working with the data in memory.

def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

# Function: clean_column_names
# Generated using Copilot suggestion
# What: Standardizes column names to lowercase_with_underscores.
# Why: Makes column names consistent and easier to work with in Python.

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

# Function: strip_text_fields
# What: Removes leading/trailing whitespace from product/category fields.
# Why: Whitespace causes duplicates and inconsistent grouping.
# -------------------------------------------------------------
def strip_text_fields(df: pd.DataFrame) -> pd.DataFrame:
    if "prodname" in df.columns:
        df["prodname"] = df["prodname"].astype(str).str.strip()
    if "category" in df.columns:
        df["category"] = df["category"].astype(str).str.strip()
    return df

# Function: handle_missing_values
# Copilot generated 
# What: Drops rows where price or qty is missing.
# Why: Missing values make calculations unreliable and inconsistent.

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["price", "qty"])
    return df

# Function: remove_invalid_rows
# What: Removes rows with negative price or negative quantity.
# Why: Negative values indicate data-entry errors.

def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["price"] >= 0]
    df = df[df["qty"] >= 0]
    return df

# Script Entry Point
# This allows the entire cleaning pipeline to run automatically.

    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    print("Loading raw data...")
    df_raw = load_data(raw_path)

    print("Cleaning column names...")
    df_clean = clean_column_names(df_raw)

    print("Stripping whitespace from text fields...")
    df_clean = strip_text_fields(df_clean)

    print("Handling missing values...")
    df_clean = handle_missing_values(df_clean)

    print("Removing invalid rows...")
    df_clean = remove_invalid_rows(df_clean)

    print("Saving cleaned data...")
    df_clean.to_csv(cleaned_path, index=False)

    print("\nCleaning complete. First few rows:")
    print(df_clean.head())

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

#From canvas assignment told to add this block to the bottom of this project

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())