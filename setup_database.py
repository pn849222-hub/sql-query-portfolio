# SQL Query Portfolio - Superstore Dataset
# Author: [BenDTA]
# Description: Load CSV data into SQLite and run business queries

import sqlite3
import pandas as pd
import os

# ── Config ───────────────────────────────────────────────
DB_PATH  = "superstore.db"
CSV_PATH = r"D:\GitHubProfilio\sales-data-analysis\data\superstore.csv"

# ── Load CSV into SQLite ──────────────────────────────────
df = pd.read_csv(CSV_PATH, encoding="latin-1")
df.columns = df.columns.str.strip().str.replace(" ", "_")

conn = sqlite3.connect(DB_PATH)
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Database created:", DB_PATH)
print("Table 'orders' loaded with", len(df), "rows")
print("\nColumns:")
for col in df.columns:
    print(f"  - {col}")

conn.close()
