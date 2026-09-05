# Budget Inspector Deployment Guide

**Budget Inspector** is an evidence-first, agentic analytical web application and CLI toolkit.

---

## 🛠️ Local Development & Running

### 1. One-Command Setup & Ingestion

```bash
# Set up virtual environment and install dependencies
make setup

# Run data ingestion pipeline and build DuckDB analytical database
make ingest

# Run reconciliation and data quality checks
make validate
```

### 2. Launch the Web Application

```bash
# Launch FastAPI web app locally on http://localhost:8000
budget-inspector serve
# or
make serve
```

---

## 🚀 Cloud Deployment Options

### Primary Production Target: Render

The interactive Budget Inspector backend uses **FastAPI, Python 3.11, and DuckDB**. Render is the recommended cloud platform for single-service deployment.

#### Deployment Steps on Render:
1. Connect your GitHub repository (`kerwinarlan/budget-bot-hackathon-budget-inspector`) on [Render Dashboard](https://dashboard.render.com).
2. Render will automatically detect `render.yaml`.
3. Build Command: `pip install -e .`
4. Start Command: `uvicorn budget_inspector.web:app --host 0.0.0.0 --port $PORT`
5. Health Check Path: `/health`

#### Data Deployment Strategy:
- **DuckDB Database (`data/budget.duckdb`)**: ~8.5 MB, containing normalized line items, agency comparison matrix, and PAP crosswalks.
- Bundling `data/budget.duckdb` directly in the deployment package provides instant <10ms query execution without external database dependencies or cold start latency.

---

## 📄 Static Fallback: GitHub Pages & Static Export

For static previews without a live Python backend:
- Precomputed static showcase HTML: `docs/index.html` or `reports/hackathon/preview.html`.
- Diagnostic report on private repository Pages limitations: `reports/deployment/GITHUB_PAGES_DIAGNOSIS.md`.
