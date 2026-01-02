import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data-reporting.db"
DATA_PATH = BASE_DIR / "data" / "processed" / "transactions_clean.csv"
SQL_PATH = BASE_DIR / "sql" / "create_tables.sql"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open(SQL_PATH, "r") as f:
    cursor.executescript(f.read())

df = pd.read_csv(DATA_PATH)
df.to_sql("transactions", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ Data successfully loaded into database")
