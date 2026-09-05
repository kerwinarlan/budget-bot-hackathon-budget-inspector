# Budget Inspector: Reproducible Agentic Budget Reporting

**Team Vibe Coders** | Philippine Budget Bot AI Hackathon Deliverable

---

## Overview

In public-interest journalism and policy research, accuracy is paramount. When inspecting multi-trillion peso national budget spreadsheets, AI language models can offer unprecedented query flexibility—but relying on LLMs to perform mental math risks hallucinating financial facts.

To bridge this gap, **Team Vibe Coders** developed **Budget Inspector**: an open-source, evidence-first analytical toolkit built during and after the Philippine **Budget Bot AI Hackathon** (June 27, 2026).

Budget Inspector extends our team's hackathon skill repo ([`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill), forked from [`tordecilla/budget-bot-skill`](https://github.com/tordecilla/budget-bot-skill)). It enables journalists, researchers, and citizens to interrogate the **FY 2025 General Appropriations Act (GAA, R.A. 12116)** and **FY 2026 General Appropriations Act (GAA, R.A. 12314)** spreadsheets published by the Department of Budget and Management (DBM).

---

## How It Works: The Evidence-First Agentic Architecture

Rather than using AI to generate numbers, Budget Inspector uses coding agents to control a deterministic SQL and Python analytical engine:

1. **Raw Spreadsheet Ingestion**: Ingests over 700,000 spreadsheet rows per fiscal year from official DBM Excel workbooks, building a local DuckDB analytical database.
2. **Reconciliation**: Reconciles normalized row sums against official DBM headline totals:
   - **FY 2025**: Reconciled to ₱6,326,685,586,000.00 (0.0057% variance).
   - **FY 2026**: Reconciled to ₱6,793,162,000,000.00 (100.00% exact match).
3. **Agentic Skill Orchestration**: An AI agent uses custom skills to map user questions to exact SQL queries, calculate deltas, and retrieve cell-level provenance (file, sheet, row).
4. **Machine-Readable Research Receipts**: Generates JSON receipts and Markdown audit trails for every query, detailing exact formulas, source rows, and analytical caveats.

---

## Key Discoveries

- **DepEd Facilities Expansion**: DepEd's *Basic Education Facilities* line item surged by **+215.3% (+₱54.77 Billion)**, expanding from ₱25.44B in 2025 to ₱80.21B in 2026.
- **PhilHealth Realignment**: Identified **₱113.13 Billion** in newly introduced PhilHealth subsidies in 2026, including ₱60B allocated in compliance with Supreme Court mandates regarding unutilized fund transfers.
- **Local Government Revenue Share**: National Tax Allotments (NTA) increased by **+15.1% (+₱155.90 Billion)**, reaching ₱1.191 Trillion in FY 2026.

---

## Journalistic Ethics & Safeguards

Budget Inspector enforces strict ethical boundaries. It classifies statistical outliers as *investigative leads* rather than accusations of wrongdoing, explicitly reminding users that an *appropriation* represents legislative authorization, not an obligation, expenditure, or contract award.

> *"We used AI not to make claims about the budget, but to build a reproducible investigative workflow around public fiscal data."*
