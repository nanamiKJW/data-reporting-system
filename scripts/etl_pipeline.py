import pandas as pd
import os


def extract_data(input_path: str) -> pd.DataFrame:
    """
    Extract raw data from CSV file.

    Parameters:
        input_path (str): Path to raw CSV file

    Returns:
        pd.DataFrame: Raw data
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw data:
    - Remove duplicates
    - Handle missing values
    - Convert timestamp to datetime
    - Standardize text fields

    Parameters:
        df (pd.DataFrame): Raw data

    Returns:
        pd.DataFrame: Cleaned data
    """

    # Remove duplicate records
    df = df.drop_duplicates(subset="transaction_id")

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Drop rows with invalid timestamps
    df = df.dropna(subset=["timestamp"])

    # Handle missing amounts (replace with median)
    if df["amount"].isnull().any():
        median_amount = df["amount"].median()
        df["amount"] = df["amount"].fillna(median_amount)

    # Standardize text fields
    df["system_type"] = df["system_type"].str.upper().str.strip()
    df["status"] = df["status"].str.upper().str.strip()

    return df


def load_data(df: pd.DataFrame, output_path: str):
    """
    Load processed data to CSV file.

    Parameters:
        df (pd.DataFrame): Processed data
        output_path (str): Path to save cleaned CSV
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


def run_etl(
    input_path: str = "data/raw/transactions.csv",
    output_path: str = "data/processed/transactions_clean.csv"
):
    """
    Run full ETL pipeline.
    """

    print("Starting ETL pipeline...")

    # Extract
    raw_df = extract_data(input_path)
    print(f"Extracted {len(raw_df)} records.")

    # Transform
    clean_df = transform_data(raw_df)
    print(f"Transformed to {len(clean_df)} clean records.")

    # Load
    load_data(clean_df, output_path)
    print(f"Clean data saved to: {output_path}")


if __name__ == "__main__":
    run_etl()
