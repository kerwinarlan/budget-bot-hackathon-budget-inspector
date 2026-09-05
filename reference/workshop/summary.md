# Workshop Summary — Philippine Budget Bot AI Hackathon

**Date**: June 27, 2026  
**Organizers**: Economic Journalists Association of the Philippines (EJAP) & PLDT Smart  
**Lead Facilitator**: Jaemark Tordecilla (Filipino Journalist & Creator of Budget Bot)  
**Team**: Vibe Coders  

---

## 💡 Workshop Goals & Background

The Philippine Budget Bot AI Hackathon brought together journalists, civic tech developers, data analysts, and researchers to explore how LLM-driven coding agents (e.g., Claude Code, OpenAI Codex, Hermes Agent) can interrogate complex government financial datasets.

Specifically, participants were tasked with comparing the **FY 2025 General Appropriations Act (GAA, R.A. 12116)** against the **FY 2026 General Appropriations Act (GAA, R.A. 12314)** spreadsheets published by the Department of Budget and Management (DBM).

---

## 🛠️ Demonstrated Workflow & Agent Architecture

The workshop emphasized a two-step agentic workflow:

1. **Data Ingestion & Indexing**:
   - DBM Excel spreadsheets (GAA/NEP) are ingested, cleaned, and normalized.
   - Structured relational storage (SQLite/DuckDB) is created.
   - An `agency_lookup.json` file is generated for agency/department alias mapping.

2. **Agentic Investigation via Skill**:
   - The user asks natural language investigation questions.
   - The coding agent uses the `budget-bot-skill` to look up agency codes, inspect table schemas, and formulate exact SQL queries.
   - The relational database executes the query and returns CSV/dataframes.
   - The agent interprets findings, formats evidence, and produces audit trails.

---

## 🎯 Organizer Requirements for Deliverables

Organizers requested three post-hackathon outputs:
1. **Favorite Lead / Discovery**: The most compelling, verified budget change or anomaly discovered during analysis.
2. **Agentic Workflows Developed**: Documentation on how coding agents were directed to produce reproducible audit trails.
3. **International Media Writeup Potential**: A polished, evidence-first project summary suitable for submission to AI-in-media outlets.
