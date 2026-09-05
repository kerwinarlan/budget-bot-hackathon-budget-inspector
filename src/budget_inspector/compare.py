import os
import duckdb
import pandas as pd
from budget_inspector.entity_resolution import build_pap_aggregated_comparison

DB_PATH = "data/budget.duckdb"

def build_duckdb_database(parquet_2025: str = "data/normalized/budget_2025.parquet", parquet_2026: str = "data/normalized/budget_2026.parquet") -> str:
    print(f"[Compare] Building DuckDB database at {DB_PATH}...")
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = duckdb.connect(DB_PATH)
    
    # 1. Create raw normalized tables
    print("[Compare] Loading normalized Parquet files into DuckDB...")
    conn.execute(f"CREATE OR REPLACE TABLE budget_2025 AS SELECT * FROM read_parquet('{parquet_2025}')")
    conn.execute(f"CREATE OR REPLACE TABLE budget_2026 AS SELECT * FROM read_parquet('{parquet_2026}')")
    
    # 2. Build aggregated PAP comparison table in pandas and load to DuckDB
    df_2025 = pd.read_parquet(parquet_2025)
    df_2026 = pd.read_parquet(parquet_2026)
    
    df_pap_comp = build_pap_aggregated_comparison(df_2025, df_2026)
    conn.execute("CREATE OR REPLACE TABLE pap_comparison AS SELECT * FROM df_pap_comp")
    
    # 3. Create Agency Level Comparison view/table
    conn.execute("""
    CREATE OR REPLACE TABLE agency_comparison AS
    WITH a25 AS (
        SELECT department_name, agency_name, SUM(amount_pesos) AS amount_2025_pesos
        FROM budget_2025
        GROUP BY department_name, agency_name
    ),
    a26 AS (
        SELECT department_name, agency_name, SUM(amount_pesos) AS amount_2026_pesos
        FROM budget_2026
        GROUP BY department_name, agency_name
    )
    SELECT 
        COALESCE(a25.department_name, a26.department_name) AS department_name,
        COALESCE(a25.agency_name, a26.agency_name) AS agency_name,
        COALESCE(a25.amount_2025_pesos, 0.0) AS amount_2025_pesos,
        COALESCE(a26.amount_2026_pesos, 0.0) AS amount_2026_pesos,
        (COALESCE(a26.amount_2026_pesos, 0.0) - COALESCE(a25.amount_2025_pesos, 0.0)) AS absolute_change_pesos,
        CASE 
            WHEN COALESCE(a25.amount_2025_pesos, 0.0) = 0 THEN NULL
            ELSE ((COALESCE(a26.amount_2026_pesos, 0.0) - a25.amount_2025_pesos) / a25.amount_2025_pesos) * 100.0
        END AS percent_change
    FROM a25
    FULL OUTER JOIN a26 
      ON a25.department_name = a26.department_name 
     AND a25.agency_name = a26.agency_name
    """)
    
    # 4. Create Department Level Comparison view/table
    conn.execute("""
    CREATE OR REPLACE TABLE department_comparison AS
    WITH d25 AS (
        SELECT department_name, SUM(amount_pesos) AS amount_2025_pesos
        FROM budget_2025
        GROUP BY department_name
    ),
    d26 AS (
        SELECT department_name, SUM(amount_pesos) AS amount_2026_pesos
        FROM budget_2026
        GROUP BY department_name
    )
    SELECT 
        COALESCE(d25.department_name, d26.department_name) AS department_name,
        COALESCE(d25.amount_2025_pesos, 0.0) AS amount_2025_pesos,
        COALESCE(d26.amount_2026_pesos, 0.0) AS amount_2026_pesos,
        (COALESCE(d26.amount_2026_pesos, 0.0) - COALESCE(d25.amount_2025_pesos, 0.0)) AS absolute_change_pesos,
        CASE 
            WHEN COALESCE(d25.amount_2025_pesos, 0.0) = 0 THEN NULL
            ELSE ((COALESCE(d26.amount_2026_pesos, 0.0) - d25.amount_2025_pesos) / d25.amount_2025_pesos) * 100.0
        END AS percent_change
    FROM d25
    FULL OUTER JOIN d26 ON d25.department_name = d26.department_name
    """)
    
    print("[Compare] Tables created in DuckDB:")
    tables = conn.execute("SHOW TABLES").fetchall()
    for t in tables:
        res = conn.execute(f"SELECT COUNT(*) FROM {t[0]}").fetchone()
        count = res[0] if res else 0
        print(f"  - {t[0]}: {count:,} rows")
        
    conn.close()
    return DB_PATH

if __name__ == "__main__":
    build_duckdb_database()
