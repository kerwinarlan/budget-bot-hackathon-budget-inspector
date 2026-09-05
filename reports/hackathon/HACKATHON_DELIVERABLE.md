# Budget Inspector — Post-Hackathon Product Deliverable

**Team Name**: Vibe Coders  
**Event**: Philippine Budget Bot AI Hackathon (June 27, 2026)  
**Authors**: Kerwin Arlan & Team Vibe Coders  
**Team Skill Fork**: [`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill) *(forked from [`tordecilla/budget-bot-skill`](https://github.com/tordecilla/budget-bot-skill) by Jaemark Tordecilla)*  
**Primary Repository**: [`kerwinarlan/budget-bot-hackathon-budget-inspector`](https://github.com/kerwinarlan/budget-bot-hackathon-budget-inspector)  

---

## 1. Executive Summary & Evolution

We started with a hackathon skill that could query DBM GAA spreadsheets. We extended it into **Budget Inspector**: an evidence-first investigative agent and newsroom desk application for the Philippine national budget.

Budget Inspector does not merely output numbers—it guides users through an **Ask → Investigate → Case File → Evidence → Brief** workflow:
- **Ask Inspector**: Natural language interface with ambiguity resolution.
- **Ambiguity Engine**: Prompts users to refine scope when questions are ambiguous or framed with unverified assumptions.
- **Autonomous Multi-Check Investigation**: Executes 7 audit checks (`OBSERVE -> QUESTION -> HYPOTHESIS -> QUERY -> VERIFY -> CHECK ALTERNATIVE EXPLANATIONS -> ASSESS -> FOLLOW-UP`).
- **Case Files System**: Generates structured, reproducible Case Files (`cases/BI-2026-001.json` & `.md`).
- **Inspector Briefs**: Compiles verified case files into newsroom evidence reports (*Budget Inspector Brief #001*).

---

## 2. Reconciled Data Engine & Provenance

| Fiscal Year | Document | Raw Rows | Normalized Leaf Rows | Total Pesos (Normalized) | Official DBM Total | Variance |
|---|---|---|---|---|---|---|
| **FY 2025** | GAA R.A. 12116 | 723,106 | 539,379 | ₱6,326,685,586,000.00 | ₱6,326,324,300,000.00 | **0.0057%** |
| **FY 2026** | GAA R.A. 12314 | 736,849 | 522,214 | ₱6,793,162,000,000.00 | ₱6,793,162,000,000.00 | **0.0000%** |

- **Headline Growth**: Total national budget expanded by **+₱466.84 Billion (+7.38%)**.
- **Provenance**: 100% of rows trace back to exact DBM spreadsheet row numbers (`GAA-2025.xlsx` & `FY2026-GAA-Byobject.xlsx`).

---

## 3. Verified Case Files Produced

1. **`BI-2026-001` — DepEd Basic Education Facilities (+215.3%)**:
   - Allocation expanded from **₱25.44B** in 2025 to **₱80.21B** in 2026 (+₱54.77 Billion).
   - Provenance: FY2025 Row 121894 vs FY2026 Row 124510.
2. **`BI-2026-002` — PhilHealth Supreme Court Mandate Subsidies**:
   - Newly introduced **₱60.00 Billion** appropriation in FY 2026 following legal fund transfers.
   - Provenance: FY2026 Row 720102.
3. **`BI-2026-003` — DPWH Infrastructure Maintenance & Flood Control**:
   - Flood mitigation facilities maintenance allocation grew by **+₱1.10 Billion (+157.1%)**, from ₱700M in 2025 to ₱1.80B in 2026.
   - Provenance: FY2025 Row 215410 vs FY2026 Row 218902.

---

## 4. Editorial Deliverable: Budget Inspector Brief #001

Verified cases were compiled into **Budget Inspector Brief #001**: *"What Changed Between the 2025 and 2026 Philippine GAA?"* saved at:
- `reports/briefs/Budget_Inspector_Brief_001.md`
- `reports/briefs/Budget_Inspector_Brief_001.html`

---

## 5. Web App & Local Run Instructions

```bash
# Set up environment and ingest DuckDB engine
make setup && make ingest

# Launch web desk locally
make serve
# Open http://localhost:8000
```
