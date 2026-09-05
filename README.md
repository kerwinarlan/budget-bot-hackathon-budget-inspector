# Budget Inspector (Philippine Budget Bot Hackathon Output)

> **Vibe Coders Team Deliverable**  
> Post-Hackathon Output for the Philippine **Budget Bot AI Hackathon** (June 27, 2026).  
> Built by Kerwin Arlan & Team Vibe Coders.

---

## 📌 Overview

**Budget Inspector** is an evidence-first agentic analytical toolkit for inspecting Philippine national budget data published by the Department of Budget and Management (DBM).

It provides a reproducible, audit-trailed workflow that enables journalists, researchers, policy analysts, civic tech workers, and citizens to interrogate the **FY 2025 General Appropriations Act (GAA, R.A. 12116)** and **FY 2026 General Appropriations Act (GAA, R.A. 12314)** using natural language or structured CLI commands.

---

## 🎯 Key Objectives

1. **Deterministic Integrity**: AI agents guide query formulation and explanation, but **DuckDB and Python** execute all calculations, aggregations, and entity matching.
2. **Mandatory Provenance**: Every output number maps directly back to the exact source Excel file, sheet, row, and UACS code.
3. **Journalistic Objectivity**: Strictly avoids sensationalism. Flags statistical anomalies, reallocations, and renames as investigative *leads*, not claims of wrongdoing.
4. **Agentic Reproducibility**: Generates machine-readable **Research Receipts (JSON)** and SQL audit logs for every query and lead.

---

## 🏗️ Repository Architecture

```text
budget-bot-hackathon-budget-inspector/
│
├── AGENTS.md                   # Agent guidelines & evidence rules
├── README.md                   # Project overview & quickstart
├── pyproject.toml              # Build & dependency metadata
├── Makefile                    # Target shortcuts (ingest, validate, report)
├── .gitignore
│
├── raw/                        # Untouched DBM Excel files
│   ├── 2025/GAA-2025.xlsx
│   └── 2026/FY2026-GAA-Byobject.xlsx
│
├── reference/                  # Hackathon slides & presentation notes
│   ├── workshop/
│   └── slides/
│
├── data/
│   ├── manifests/manifest.json # SHA-256 hashes & retrieval metadata
│   ├── normalized/             # Cleaned Parquet tables
│   └── budget.duckdb           # Embedded analytical SQL database
│
├── src/budget_inspector/
│   ├── acquire.py              # Download & manifest generation
│   ├── inspect_workbooks.py    # Sheet & schema discovery
│   ├── schema.py               # Canonical Pydantic schema
│   ├── normalize.py            # Data cleaning & currency conversion
│   ├── entity_resolution.py    # Cross-year PAP & fuzzy matching
│   ├── compare.py              # 2025 vs 2026 comparison engine
│   ├── anomalies.py            # Heuristic lead generator
│   ├── queries.py              # DuckDB query executor
│   ├── provenance.py           # Cell/row provenance extractor
│   ├── reporting.py            # Research receipt & report generator
│   └── cli.py                  # Typer CLI application
│
├── skills/
│   └── budget-inspector/
│       └── SKILL.md            # Reusable skill for AI coding agents
│
├── agents/
│   └── budget-inspector.md     # Agent context definition
│
├── queries/
│   └── investigations/         # Saved SQL queries & research receipts
│
├── reports/
│   ├── hackathon/              # Final hackathon deliverables & email draft
│   └── validation/             # Reconciliations & inventory reports
│
├── tests/                      # Unit & integration tests (pytest)
└── scripts/                    # Workflow execution scripts
    ├── download_data.py
    ├── ingest.py
    ├── validate.py
    └── run_demo.py
```

---

## 🚀 Quickstart

### 1. Environment Setup

```bash
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e .
```

### 2. One-Command Data Pipeline

```bash
# Acquire official DBM spreadsheets, normalize, and build DuckDB engine
python scripts/ingest.py

# Run reconciliation and data quality checks
python scripts/validate.py
```

### 3. Run the CLI / Agent Tools

```bash
# View database status & row counts
budget-inspector status

# Discover top absolute increases from 2025 to 2026
budget-inspector top-increases --limit 10

# Search for flood control appropriations
budget-inspector search "flood control"

# Generate automated investigative leads
budget-inspector leads

# Ask natural language questions
budget-inspector ask "Which agencies experienced the largest internal reallocations?"
```

---

## 📊 Key Findings Highlight

1. **Exact Reconciliation**: Reconciled normalized row totals directly against official DBM Grand Totals:
   - **FY 2025 GAA**: ₱6,326,324,300,000 (100.00% exact match)
   - **FY 2026 GAA**: ₱6,793,162,000,000 (100.00% exact match)
2. **Headline Growth**: Total budget increased by **₱466.84 Billion (+7.38%)**.
3. **DPWH Flood Control**: Specialized flood control analysis isolated key regional and capital outlay shifts across DPWH engineering districts.

---

## 📄 Hackathon Deliverables

- `reports/hackathon/HACKATHON_DELIVERABLE.md`: Full event deliverable.
- `reports/hackathon/DEMO_FINDINGS.md`: Key verified leads and evidence.
- `reports/hackathon/EMAIL_REPLY_DRAFT.md`: Draft email response to hackathon organizers.
- `reports/hackathon/PROJECT_SUMMARY.md`: Public-facing summary (300–500 words).
