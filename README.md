# Budget Inspector

> **An evidence-first investigative agent for the Philippine national budget.**  
> *"I don't tell you what's corrupt. I show you what changed, why it stands out, and where to look next."*

[![Vibe Coders PH](https://img.shields.io/badge/Vibe_Coders_PH-Official_Deliverable-purple?style=flat-square)](https://github.com/kerwinarlan/budget-bot-skill)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![DuckDB](https://img.shields.io/badge/DuckDB-1.0+-FFF000?style=flat-square&logo=duckdb&logoColor=black)](https://duckdb.org)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Live-22C55E?style=flat-square&logo=github)](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

---

## 🌐 Live Web Desk & Static Showcases

- 🌐 **Live GitHub Pages Portal**: [https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/)
- 🐙 **Public GitHub Repository**: [https://github.com/kerwinarlan/budget-bot-hackathon-budget-inspector](https://github.com/kerwinarlan/budget-bot-hackathon-budget-inspector)
- 🛠️ **Team Skill Repository**: [`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill) *(forked from [`tordecilla/budget-bot-skill`](https://github.com/tordecilla/budget-bot-skill) by Jaemark Tordecilla)*

---

## 📋 Table of Contents
1. [Overview & Product Identity](#-overview--product-identity)
2. [📰 Non-Technical Guide for Journalists & Policy Analysts](#-non-technical-guide-for-journalists--policy-analysts)
3. [🔄 Agentic Product Flow](#-agentic-product-flow)
4. [🎯 Core Capabilities](#-core-capabilities)
5. [📊 Verified Case Studies](#-verified-case-studies)
6. [🚀 Technical Quickstart & API Reference](#-technical-quickstart--api-reference)
7. [☁️ Deployment Options](#%EF%B8%8F-deployment-options)
8. [⚖️ Journalistic Ethics & Anti-Slop Safeguards](#%EF%B8%8F-journalistic-ethics--anti-slop-safeguards)

---

## 📌 Overview & Product Identity

In public-interest journalism and fiscal research, accuracy is non-negotiable. When inspecting multi-trillion peso government spreadsheets containing over **700,000 rows**, relying on AI language models to do mental math risks hallucinating financial figures.

**Budget Inspector** solves this by separating reasoning from calculation:
- **LLMs & Coding Agents**: Handle schema discovery, intent classification, ambiguity resolution, and journalistic explanation.
- **DuckDB SQL Engine**: Executes all sums, deltas, ratios, entity resolution, and cell-level provenance tracing with 100.0% mathematical precision.

---

## 📰 Non-Technical Guide for Journalists & Policy Analysts

*This section is specifically written for reporters, researchers, editors, and civic workers who want to investigate the Philippine budget without writing code.*

### 1. How to Open and Use the Web Desk
You do not need to install complex database software. You can access Budget Inspector in two easy ways:
- **Option A (Online)**: Visit the live web desk at [https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/).
- **Option B (Local Desk)**: If running on your newsroom computer, open your terminal and type `budget-inspector serve` (or `make serve`), then open `http://localhost:8000` in your web browser.

### 2. Asking Plain-English Questions
Navigate to **🔎 Ask Inspector** (`/ask`) or use the search bar on the front page. Type natural questions like:
- *"Which programs increased the most from 2025 to 2026?"*
- *"What happened to flood-control appropriations?"*
- *"Which line items are completely new in 2026?"*
- *"Where did money move inside agencies whose total budget stayed flat?"*

### 3. Understanding the Ambiguity Resolution Prompt
When you ask a broad question (e.g. *"What happened to flood control?"*), the Inspector won't guess what you meant. It will present clear choices:
1. *All flood control across all government agencies*
2. *DPWH infrastructure flood control only*
3. *Largest 2025→2026 flood control increases*

Click your preferred option to confirm the inspection scope.

### 4. How to Interpret Budget Terms (Fiscal Primer for Reporters)

| Term | Plain-English Meaning | Is it in this tool? |
|---|---|---|
| **Appropriation** | The maximum budget authority approved by Congress in the General Appropriations Act (GAA). | **YES** — This tool inspects enacted GAA spreadsheets. |
| **Allotment** | The release authorization issued by DBM allowing agencies to incur obligations. | *Future integration* |
| **Obligation** | A legal commitment made by an agency (e.g., signed procurement contract). | *Future integration* |
| **Disbursement** | The actual cash paid out by the Treasury to contractors/suppliers. | *Future integration* |

> ⚠️ **Key Rule for Newsrooms**: An increase in an *appropriation* means Congress authorized more budget. It does **NOT** mean the money was already spent, stolen, or awarded to a contractor.

### 5. Exporting Newsroom Evidence for Your Story
- **📄 Download PDF Brief**: Click **"📄 Download PDF Brief"** at the top of any brief page to download a high-resolution, print-ready PDF newsroom report (`Budget_Inspector_Brief_001.pdf`).
- **🌐 Download HTML Brief**: Click **"🌐 Download HTML Brief"** to save a standalone, formatted web article.
- **🧾 Inspect Cell Provenance**: Click **"Cell Info"** on any item to open the slide-over drawer showing the exact Excel file (`GAA-2025.xlsx`), sheet name, and **1-indexed Excel row number** for factual citation in your news article.
- **📋 Copy Citations**: Click **"Copy Citation"** or **"Copy Case File"** to copy formatted text directly into your draft.

---

## 🔄 Agentic Product Flow

```text
User Asks Natural Question
            ↓
Inspector Checks Ambiguity (Clarification Prompt)
            ↓
Deterministic DuckDB SQL Execution
            ↓
Total Reconciliation & Provenance Tracing
            ↓
Multi-Check Autonomous Investigation
            ↓
Case File Created (cases/BI-2026-xxx.json)
            ↓
Follow-Up Questions & Caveats Formulated
            ↓
Published in Budget Inspector Brief #001 (MD, HTML, PDF)
```

---

## 🎯 Core Capabilities

1. **Ask Inspector (`/ask`)**: Guided natural language query routing paired with an ambiguity resolution engine.
2. **Autonomous Multi-Check Investigation (`/investigate`)**: Executes a 7-step audit check (`OBSERVE -> QUESTION -> HYPOTHESIS -> QUERY -> VERIFY -> CHECK ALTERNATIVE EXPLANATIONS -> ASSESS -> FOLLOW-UP`).
3. **Case Files System (`/cases`)**: Stores machine-readable JSON (`cases/BI-2026-001.json`) and Markdown (`cases/BI-2026-001.md`) case files with **Investigative Interest** and **Data Confidence** scores.
4. **Inspector Briefs (`/briefs`)**: Automatically compiles verified case files into newsroom evidence reports (*Budget Inspector Brief #001*).
5. **Cell & Row Provenance (`/evidence`)**: Traces every number down to the exact DBM Excel workbook, sheet, and 1-indexed row number.
6. **Journalistic Ethics Safeguards**: Rejects unsupported "suspicion/corruption" framing, offering objective investigative criteria instead.

---

## 📊 Verified Case Studies

Our analytical engine reconciled **539,379 leaf rows in FY 2025** and **522,214 leaf rows in FY 2026** directly against official DBM Grand Totals (**100.0% exact match** for 2026, **0.0057% variance** for 2025).

| Case ID | Title | Agency | 2025 (PHP) | 2026 (PHP) | Delta (PHP) | Provenance Pointer |
|---|---|---|---|---|---|---|
| **`BI-2026-001`** | DepEd Basic Education Facilities | Office of the Secretary | ₱25.44B | ₱80.21B | **+₱54.77B (+215.3%)** | `GAA-2025.xlsx#121894` vs `FY2026-GAA-Byobject.xlsx#124510` |
| **`BI-2026-002`** | PhilHealth SC Mandate Subsidies | PhilHealth | ₱0.00 | ₱60.00B | **+₱60.00B (NEW)** | `FY2026-GAA-Byobject.xlsx#720102` |
| **`BI-2026-003`** | DPWH Flood Mitigation Facilities | Office of the Secretary | ₱700.0M | ₱1.80B | **+₱1.10B (+157.1%)** | `GAA-2025.xlsx#215410` vs `FY2026-GAA-Byobject.xlsx#218902` |

---

## 🚀 Technical Quickstart & API Reference

### 1. Environment Setup

```bash
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### 2. Ingest Data & Validate Reconciliations

```bash
# Acquire official DBM spreadsheets and build DuckDB engine
make ingest

# Verify 100% total reconciliation and provenance coverage
make validate

# Run unit test suite (7 tests)
make test
```

### 3. Launch Local Web Application

```bash
# Launch interactive Budget Inspector Desk
budget-inspector serve
# or
make serve
```
Open **`http://localhost:8000`** in your browser.

---

## ☁️ Deployment Options

- **Primary Web App Target (Render)**: FastAPI + Jinja2 + DuckDB database bundled in standard Python web service (`render.yaml`).
- **Health Check Endpoint**: `/health` (`{"status": "ok", "database": "connected", "version": "0.2.0"}`)
- **GitHub Pages Fallback**: `reports/deployment/GITHUB_PAGES_DIAGNOSIS.md` details private vs public deployment options.

---

## ⚖️ Journalistic Ethics & Anti-Slop Safeguards

Budget Inspector strictly enforces newsroom evidence standards:
1. **Allowed Terminology**: *unusual change*, *large variance*, *investigative lead*, *item worth reviewing*, *reclassification candidate*, *possible rename*.
2. **Forbidden Labels**: Never labels entries *corrupt*, *fraudulent*, *pork barrel*, or *ghost project* without separate external judicial or official COA audit findings.
3. **Anti-Slop Visual Standards**: Clean dark canvas (`#090d16`), tabular numerics (`tabular-nums font-mono`), no glowing purple gradients or AI clichés, WCAG AA contrast.
