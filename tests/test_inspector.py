import os
import pytest
from fastapi.testclient import TestClient
from budget_inspector.web import app
from budget_inspector.queries import query_top_increases, query_new_items
from budget_inspector.anomalies import generate_investigative_leads
from budget_inspector.reporting import save_research_receipts
from budget_inspector.cases import list_all_cases

DB_PATH = "data/budget.duckdb"
client = TestClient(app)

def test_duckdb_exists():
    assert os.path.exists(DB_PATH), "Database data/budget.duckdb should exist."

def test_health_check_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["database"] == "connected"

def test_home_desk_route():
    response = client.get("/")
    assert response.status_code == 200
    assert "Budget Inspector Desk" in response.text

def test_query_top_increases():
    df = query_top_increases(limit=5)
    assert not df.empty, "query_top_increases should return non-empty DataFrame."
    assert "amount_2025_pesos" in df.columns
    assert "amount_2026_pesos" in df.columns

def test_query_new_items():
    df = query_new_items(limit=5)
    assert not df.empty, "query_new_items should return non-empty DataFrame."

def test_cases_listing():
    cases = list_all_cases()
    assert len(cases) >= 3, "At least 3 initial Case Files should exist."

def test_case_detail_route():
    response = client.get("/cases/BI-2026-001")
    assert response.status_code == 200
    assert "BI-2026-001" in response.text
