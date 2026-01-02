import sqlite3
import pandas as pd
import streamlit as st
from pathlib import Path

# -------------------------------
# Database path
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data-reporting.db"

# -------------------------------
# Connect to SQLite
# -------------------------------
conn = sqlite3.connect(DB_PATH)

# -------------------------------
# Load data into DataFrame
# -------------------------------
df = pd.read_sql_query("SELECT * FROM transactions", conn)

# -------------------------------
# Normalize columns for robustness
# -------------------------------
# Status: lowercase and remove spaces
df['status'] = df['status'].astype(str).str.strip().str.lower()

# System type: title case and remove spaces
df['system_type'] = df['system_type'].astype(str).str.strip().str.title()

# Timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Transaction Dashboard", layout="wide")
st.title("📊 Transaction Monitoring Dashboard")

# Metrics
total_transactions = len(df)
total_success = df[df['status'] == 'success'].shape[0]
total_failed = df[df['status'] == 'failed'].shape[0]

st.metric("Total Transactions", total_transactions)
st.metric("Successful Transactions", total_success)
st.metric("Failed Transactions", total_failed)

# Transactions by system type
st.subheader("Transactions by System Type")
transactions_by_system = df.groupby("system_type").size().reset_index(name='count')
st.bar_chart(transactions_by_system.set_index("system_type")["count"])

# Failure rate by system type
st.subheader("Failure Rate by System Type (%)")
failure_rate = df.groupby("system_type")["status"].apply(lambda x: (x == "failed").mean()).reset_index(name="failure_rate")
failure_rate["failure_rate_percent"] = (failure_rate["failure_rate"] * 100).round(2)
st.bar_chart(failure_rate.set_index("system_type")["failure_rate_percent"])

# Transactions over time (hourly)
st.subheader("Transactions Over Time (Hourly)")
df['hour'] = df['timestamp'].dt.floor('H')
transactions_over_time = df.groupby("hour").size().reset_index(name="count")
st.line_chart(transactions_over_time.set_index("hour")["count"])
