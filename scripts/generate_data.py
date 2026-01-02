import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os


def generate_transaction_data(
    num_records: int = 10000,
    start_date: str = "2025-01-01",
    output_path: str = "data/raw/transactions.csv"
):
    """
    Generate synthetic transaction/sensor-like data to simulate
    high-volume systems (banking, monitoring, scientific infrastructure).

    Parameters:
        num_records (int): Number of records to generate
        start_date (str): Start date for timestamps (YYYY-MM-DD)
        output_path (str): Output CSV file path
    """

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Convert start date to datetime
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")

    # Possible system sources
    system_types = ["ATM", "Mobile", "Web", "Sensor"]

    # Possible transaction statuses
    statuses = ["SUCCESS", "FAILED"]

    data = {
        "transaction_id": range(1, num_records + 1),
        "timestamp": [
            start_datetime + timedelta(seconds=random.randint(0, 60 * 60 * 24 * 30))
            for _ in range(num_records)
        ],
        "system_type": np.random.choice(system_types, num_records),
        "amount": np.round(np.random.uniform(1.0, 5000.0, num_records), 2),
        "status": np.random.choice(statuses, num_records, p=[0.95, 0.05])
    }

    df = pd.DataFrame(data)

    # Introduce some missing values (to test ETL robustness)
    missing_indices = np.random.choice(df.index, size=int(num_records * 0.01), replace=False)
    df.loc[missing_indices, "amount"] = None

    # Save to CSV
    df.to_csv(output_path, index=False)

    print(f"Generated {num_records} records.")
    print(f"Data saved to: {output_path}")


if __name__ == "__main__":
    generate_transaction_data()
