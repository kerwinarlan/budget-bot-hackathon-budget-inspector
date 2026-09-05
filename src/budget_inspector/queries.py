import os
import duckdb
import pandas as pd
from typing import Dict, Any, List, Optional

DB_PATH = "data/budget.duckdb"

def get_db_connection():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"DuckDB database not found at {DB_PATH}. Run pipeline ingestion first.")
    return duckdb.connect(DB_PATH, read_only=True)

def execute_query(sql_query: str, params: Optional[List[Any]] = None) -> pd.DataFrame:
    """Executes a SQL query against DuckDB and returns a pandas DataFrame."""
    conn = get_db_connection()
    try:
        if params:
            df = conn.execute(sql_query, params).df()
        else:
            df = conn.execute(sql_query).df()
        return df
    finally:
        conn.close()

def query_top_increases(limit: int = 25, min_2025_pesos: float = 10_000_000.0) -> pd.DataFrame:
    sql = """
    SELECT 
        department_name,
        agency_name,
        prexc_fpap_id,
        description,
        expense_class,
        amount_2025_pesos,
        amount_2026_pesos,
        absolute_change_pesos,
        percent_change,
        change_status
    FROM pap_comparison
    WHERE amount_2025_pesos >= ? AND absolute_change_pesos > 0
    ORDER BY absolute_change_pesos DESC
    LIMIT ?
    """
    return execute_query(sql, [min_2025_pesos, limit])

def query_top_decreases(limit: int = 25, min_2025_pesos: float = 10_000_000.0) -> pd.DataFrame:
    sql = """
    SELECT 
        department_name,
        agency_name,
        prexc_fpap_id,
        description,
        expense_class,
        amount_2025_pesos,
        amount_2026_pesos,
        absolute_change_pesos,
        percent_change,
        change_status
    FROM pap_comparison
    WHERE amount_2025_pesos >= ? AND absolute_change_pesos < 0
    ORDER BY absolute_change_pesos ASC
    LIMIT ?
    """
    return execute_query(sql, [min_2025_pesos, limit])

def query_top_percent_increases(limit: int = 15, min_2025_pesos: float = 50_000_000.0) -> pd.DataFrame:
    sql = """
    SELECT 
        department_name,
        agency_name,
        prexc_fpap_id,
        description,
        expense_class,
        amount_2025_pesos,
        amount_2026_pesos,
        absolute_change_pesos,
        percent_change
    FROM pap_comparison
    WHERE amount_2025_pesos >= ? AND percent_change IS NOT NULL
    ORDER BY percent_change DESC
    LIMIT ?
    """
    return execute_query(sql, [min_2025_pesos, limit])

def query_new_items(limit: int = 25, min_2026_pesos: float = 100_000_000.0) -> pd.DataFrame:
    sql = """
    SELECT 
        department_name,
        agency_name,
        prexc_fpap_id,
        description,
        expense_class,
        amount_2026_pesos,
        change_status
    FROM pap_comparison
    WHERE change_status = 'NEW_IN_2026' AND amount_2026_pesos >= ?
    ORDER BY amount_2026_pesos DESC
    LIMIT ?
    """
    return execute_query(sql, [min_2026_pesos, limit])

def query_disappeared_items(limit: int = 25, min_2025_pesos: float = 100_000_000.0) -> pd.DataFrame:
    sql = """
    SELECT 
        department_name,
        agency_name,
        prexc_fpap_id,
        description,
        expense_class,
        amount_2025_pesos,
        change_status
    FROM pap_comparison
    WHERE change_status = 'DISAPPEARED' AND amount_2025_pesos >= ?
    ORDER BY amount_2025_pesos DESC
    LIMIT ?
    """
    return execute_query(sql, [min_2025_pesos, limit])

def query_flood_control(limit: int = 25) -> pd.DataFrame:
    sql = """
    SELECT 
        department_name,
        agency_name,
        description,
        expense_class,
        amount_2025_pesos,
        amount_2026_pesos,
        absolute_change_pesos,
        percent_change,
        change_status
    FROM pap_comparison
    WHERE LOWER(description) LIKE '%flood%' 
       OR LOWER(description) LIKE '%drainage%' 
       OR LOWER(description) LIKE '%seawall%' 
       OR LOWER(description) LIKE '%river control%' 
       OR LOWER(description) LIKE '%dike%'
    ORDER BY amount_2026_pesos DESC
    LIMIT ?
    """
    return execute_query(sql, [limit])

def query_agency_reallocations(limit: int = 15) -> pd.DataFrame:
    sql = """
    SELECT 
        department_name,
        agency_name,
        amount_2025_pesos,
        amount_2026_pesos,
        absolute_change_pesos,
        percent_change
    FROM agency_comparison
    WHERE amount_2025_pesos > 1000000000.0 AND ABS(percent_change) <= 10.0
    ORDER BY amount_2026_pesos DESC
    LIMIT ?
    """
    return execute_query(sql, [limit])

def search_budget(keyword: str, limit: int = 25) -> pd.DataFrame:
    sql = """
    SELECT 
        department_name,
        agency_name,
        description,
        expense_class,
        amount_2025_pesos,
        amount_2026_pesos,
        absolute_change_pesos,
        percent_change,
        change_status
    FROM pap_comparison
    WHERE LOWER(description) LIKE ? OR LOWER(agency_name) LIKE ? OR LOWER(department_name) LIKE ?
    ORDER BY absolute_change_pesos DESC
    LIMIT ?
    """
    pattern = f"%{keyword.lower()}%"
    return execute_query(sql, [pattern, pattern, pattern, limit])
