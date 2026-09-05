import os
import pytest
import pandas as pd
import duckdb
from budget_inspector.queries import query_top_increases, query_new_items
from budget_inspector.anomalies import generate_investigative_leads
from budget_inspector.reporting import save_research_receipts

DB_PATH = "data/budget.duckdb"

def test_duckdb_exists():
    assert os.path.exists(DB_PATH), "Database data/budget.duckdb should exist."

def test_query_top_increases():
    df = query_top_increases(limit=5)
    assert not df.empty, "query_top_increases should return non-empty DataFrame."
    assert "amount_2025_pesos" in df.columns
    assert "amount_2026_pesos" in df.columns
    assert "absolute_change_pesos" in df.columns
    assert df.iloc[0]["absolute_change_pesos"] >= df.iloc[1]["absolute_change_pesos"]

def test_query_new_items():
    df = query_new_items(limit=5)
    assert not df.empty, "query_new_items should return non-empty DataFrame."
    assert (df["change_status"] == "NEW_IN_2026").all()

def test_generate_leads_and_receipts():
    leads = generate_investigative_leads(limit_per_category=1)
    assert len(leads) > 0, "Lead generator should produce at least 1 lead."
    
    paths = save_research_receipts(leads, output_dir="data/staging/test_receipts")
    assert len(paths) == len(leads)
    for p in paths:
        assert os.path.exists(p)
        os.remove(p)
