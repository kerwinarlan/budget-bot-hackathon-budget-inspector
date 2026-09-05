# Budget Inspector

> **An evidence-first investigative agent for the Philippine national budget.**  
> *"I don't tell you what's corrupt. I show you what changed, why it stands out, and where to look next."*

---

## 📌 Product Identity & Overview

**Budget Inspector** is an evidence-first, agentic analytical toolkit and web application for inspecting Philippine national budget data published by the Department of Budget and Management (DBM).

Built during and after the Philippine **Budget Bot AI Hackathon** (June 27, 2026) by team **Vibe Coders** (Kerwin Arlan & team), this system extends our hackathon skill repository [`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill) *(forked from [`tordecilla/budget-bot-skill`](https://github.com/tordecilla/budget-bot-skill) by Jaemark Tordecilla)*.

---

## 🔄 Agentic Product Flow

```text
Ask a Question
      ↓
Inspector Clarifies (Ambiguity Engine)
      ↓
Deterministic Analysis (DuckDB SQL)
      ↓
Evidence Verification (Source File & Row Provenance)
      ↓
Alternative Explanations Checked
      ↓
Case File Created (cases/BI-2026-xxx)
      ↓
Follow-Up Questions Generated
      ↓
Budget Inspector Brief Published
```

---

## 🎯 Key Capabilities

1. **Ask Inspector (`/ask`)**: Natural language question routing paired with an **Ambiguity/Clarification Engine** that prompts users when queries involve metric, scope, or framing ambiguity.
2. **Autonomous Multi-Check Investigation (`/investigate`)**: Runs a 7-step audit trail (`OBSERVE -> QUESTION -> HYPOTHESIS -> QUERY -> VERIFY -> CHECK ALTERNATIVE EXPLANATIONS -> ASSESS -> FOLLOW-UP`).
3. **Case Files System (`/cases`)**: Stores machine-readable JSON (`cases/BI-2026-001.json`) and Markdown (`cases/BI-2026-001.md`) case files with **Investigative Interest** and **Data Confidence** scores.
4. **Inspector Briefs (`/briefs`)**: Automatically compiles verified case files into newsroom evidence reports (e.g. *Budget Inspector Brief #001*).
5. **Cell & Row Provenance (`/evidence`)**: Traces every number down to the exact DBM Excel workbook, sheet, and 1-indexed row number.
6. **Journalistic Ethics Safeguards**: Rejects unsupported "suspicion/corruption" framing, offering objective investigative criteria instead.

---

## 🚀 Quickstart & Local Run

### 1. Environment Setup

```bash
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### 2. Ingest Data & Validate Reconciliations

```bash
# Ingest raw DBM spreadsheets and build local DuckDB database
make ingest

# Verify 100% total reconciliation and provenance coverage
make validate
```

### 3. Launch Web Application

```bash
# Launch interactive Budget Inspector Desk
budget-inspector serve
# or
make serve
```
Open **`http://localhost:8000`** in your browser.

---

## ☁️ Deployment Architecture

- **Primary Web App Target (Render)**: FastAPI + Jinja2 + DuckDB database bundled in standard Python web service (`render.yaml`).
- **Health Check**: `/health`
- **GitHub Pages Fallback**: `reports/deployment/GITHUB_PAGES_DIAGNOSIS.md` explains deployment constraints for private GitHub repositories.
