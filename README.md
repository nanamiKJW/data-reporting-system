# Scalable Data Reporting and Analytics System

## Project Overview

This project is a **mini version of a real-world reporting system** that handles high-volume transactional or sensor data.

**Key features:**

- Generates synthetic transactional data
- Cleans and transforms data through an ETL pipeline
- Stores data in a SQLite database
- Performs analytics queries
- Streamlit dashboard for visualization

## Motivation

Large organizations generate massive volumes of data every day.

Without an efficient data pipeline, it is difficult to:

- Monitor system performance
- Detect anomalies
- Support data-driven decision making

This project demonstrates "scalable data handling" and "monitoring", applicable to:

- Banking transactions
- Sensor systems
- Scientific experiments

---

## System Architecture

Raw Data --> ETL Pipeline --> SQLite Database --> Analytics Queries --> Streamlit Dashboard

**Components:**

| Component | Description |
| --- | --- |
| Data Generator (`generate_data.py`) | Simulates high-volume transaction data |
| ETL Pipeline (`etl_pipeline.py`) | Cleans, normalizes, and transforms data |
| Database (`SQLite`) | Stores structured transaction data |
| Analytics Queries (`analytics_queries.sql`) | Provides insights and monitoring metrics |
| Dashboard (`dashboard/app.py`) | Visualizes key metrics and trends |

---

## Tech Stack

| Layer | Tool |
| --- | --- |
| Language | Python |
| Database | SQLite |
| Data Processing | Pandas |
| Queries | SQL |
| Visualization | Streamlit |
|  |  |

---

## How to Run

```bash
1. Set up Python environment

python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\\Scripts\\activate      # Windows
pip install -r requirements.txt

2. Run scripts in order

python scripts/generate_data.py
python scripts/etl_pipeline.py
python scripts/load_to_db.py

3. Run Streamlit Dashboard

cd dashboard
streamlit run app.py
Open browser at: <http://localhost:8501>

Sample Outputs:

Total transactions: 10,000

Success/Failed transactions counts

Transactions by system type

Failure rates per system

Hourly transaction trends

**What I Learned**

Real-world ETL pipeline creation

Database integration with Python

Data cleaning, normalization, and validation

SQL analytics queries for monitoring

Streamlit dashboard visualization

Debugging and handling schema mismatches

**Future Improvements**

Add filters for system type and date ranges in the dashboard

Real-time streaming data simulation

Deploy dashboard online (Streamlit Cloud / Heroku)

Add advanced analytics and anomaly detection

Use PostgreSQL for more scalable database support


**Contact / Author**
Name: Phonephet Vilaysack
Location: Spain

```
