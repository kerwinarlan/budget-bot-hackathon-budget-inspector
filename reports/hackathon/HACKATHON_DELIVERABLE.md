# Budget Inspector — Hackathon Deliverable

**Team Name**: Vibe Coders  
**Event**: Philippine Budget Bot AI Hackathon (June 27, 2026)  
**Authors**: Kerwin Arlan & Team Vibe Coders  
**Team Skill Fork**: [`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill) *(forked from [`tordecilla/budget-bot-skill`](https://github.com/tordecilla/budget-bot-skill) by Jaemark Tordecilla)*  
**Target Audience**: Hackathon Organizers (EJAP / PLDT Smart), Media Researchers, Civic Tech Developers  

---

## 1. What We Built

**Budget Inspector** is an evidence-first, agentic analytical toolkit for inspecting Philippine national budget data. It provides an automated, reproducible workflow that allows journalists, policy analysts, and citizens to interrogate the **FY 2025 General Appropriations Act (GAA, R.A. 12116)** and **FY 2026 General Appropriations Act (GAA, R.A. 12314)** spreadsheets published by the Department of Budget and Management (DBM).

Our solution extends our team's hackathon skill ([`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill), forked from `tordecilla/budget-bot-skill`).

Unlike general conversational LLMs that risk hallucinating financial figures, Budget Inspector separates reasoning from calculation:
- **LLMs / Coding Agents**: Handle schema inspection, query planning, hypothesis generation, and journalistic explanation.
- **DuckDB & Python Engine**: Handle all arithmetic, aggregations, deltas, ratios, entity resolution, and cell-level provenance tracing.

---

## 2. Why We Built It

Public budget spreadsheets published by DBM contain over **700,000 rows** per fiscal year across 20 hierarchical columns. Comparing line items across fiscal years manually is slow, error-prone, and prone to losing line-item context when program names or UACS codes change.

We built Budget Inspector to solve three core challenges in public fiscal reporting:
1. **Reproducibility**: Guaranteeing that every reported number can be traced back to its exact source file, sheet, and row.
2. **Structural Discovery**: Uncovering internal agency reallocations and structural budget shifts that remain hidden behind flat headline agency growth numbers.
3. **Journalistic Safeguards**: Enforcing objective terminology (*unusual change*, *large variance*, *investigative lead*) while strictly prohibiting premature accusations (*corrupt*, *pork barrel*, *ghost project*) that lack external judicial or official audit corroboration.

---

## 3. Data Pipeline & Total Reconciliation

Our data acquisition and normalization engine ingested untouched DBM Excel spreadsheets and reconciled them directly against official DBM Grand Totals:

| Fiscal Year | Document | Raw Rows | Normalized Leaf Rows | Total Pesos (Normalized) | Official DBM Total | Variance |
|---|---|---|---|---|---|---|
| **FY 2025** | GAA R.A. 12116 | 723,106 | 539,379 | ₱6,326,685,586,000.00 | ₱6,326,324,300,000.00 | **0.0057%** |
| **FY 2026** | GAA R.A. 12314 | 736,849 | 522,214 | ₱6,793,162,000,000.00 | ₱6,793,162,000,000.00 | **0.0000%** |

- **Headline Growth**: Total national budget increased by **₱466.84 Billion (+7.38%)** between 2025 and 2026.
- **Provenance Coverage**: 100.0% of normalized rows retain exact source file and row index pointers.

---

## 4. Agentic Workflow Architecture

Our agentic workflow operates in 10 deterministic steps:

```text
1. User Natural Language Question
    ↓
2. Intent Classification & Schema Inspection
    ↓
3. Deterministic SQL Query Formulation
    ↓
4. DuckDB Analytical Engine Execution
    ↓
5. Total Reconciliation & Range Validation
    ↓
6. Layered Entity Resolution (Exact, PAP, Fuzzy)
    ↓
7. Cell & Row Provenance Extraction
    ↓
8. Machine-Readable Research Receipt (.json) Generation
    ↓
9. Conservative Explanation & Caveat Formatting
    ↓
10. Final Evidence-Backed Response
```

---

## 5. Summary of Top Verified Investigative Leads

### Lead 1: National Tax Allotment (NTA) Local Government Shift
- **Observation**: NTA allocation increased by **₱155.90 Billion (+15.07%)**, from **₱1,034.60B** in 2025 to **₱1,190.51B** in 2026.
- **Provenance**: FY 2025 (`GAA-2025.xlsx`, Row 723080) vs FY 2026 (`FY2026-GAA-Byobject.xlsx`, Row 736823).

### Lead 2: Basic Education Facilities Construction (DepEd)
- **Observation**: DepEd's Basic Education Facilities line item surged by **₱54.77 Billion (+215.3%)**, expanding from **₱25.44B** in 2025 to **₱80.21B** in 2026.
- **Provenance**: FY 2025 (`GAA-2025.xlsx`, Row 121894) vs FY 2026 (`FY2026-GAA-Byobject.xlsx`, Row 124510).

### Lead 3: Pantawid Pamilyang Pilipino Program (DSWD 4Ps)
- **Observation**: DSWD 4Ps implementation allocation grew by **₱44.04 Billion (+78.1%)**, from **₱56.40B** in 2025 to **₱100.44B** in 2026.
- **Provenance**: FY 2025 (`GAA-2025.xlsx`, Row 652101) vs FY 2026 (`FY2026-GAA-Byobject.xlsx`, Row 664120).

### Lead 4: New PhilHealth Subsidies Introduced in 2026
- **Observation**: Two new major PhilHealth line items appear in FY 2026 without exact 2025 matches:
  - Additional Appropriation in Compliance with Supreme Court Mandate: **₱60.00 Billion**
  - Health Insurance Coverage under Sin Tax Law: **₱53.13 Billion**
- **Provenance**: FY 2026 (`FY2026-GAA-Byobject.xlsx`, Rows 720102–720105).

---

## 6. What Surprised Us

1. **Precision Reconciliation**: Reconciling over 500,000 leaf rows against DBM's official multi-trillion peso headline figures yielded exact 100.0% alignment for 2026 and 99.9943% alignment for 2025.
2. **Sub-Program Volatility**: Behind modest headline growth in major departments, individual program lines frequently experience +200% to +300% shifts between fiscal years.

---

## 7. Limitations & Ethical Boundaries

- **Appropriation vs. Expenditure**: An appropriation represents legislative authorization to incur obligations, NOT actual disbursement or contract execution.
- **Renames & Restructuring**: Apparent "new" or "disappeared" items often reflect agency administrative reorganizations rather than program terminations.
- **No Accusations**: The system generates leads for journalistic investigation, not conclusions of wrongdoing.

---

## 8. What We Would Build Next

1. **NEP vs. GAA Comparison Engine**: Comparing the President's National Expenditure Program (NEP) proposal against the enacted GAA to highlight congressional insertions and realignments.
2. **COA Audit Cross-Reference**: Linking DBM budget lines with Commission on Audit (COA) annual audit report findings.
3. **Interactive Web Dashboard**: Deploying a lightweight Streamlit / React interface with interactive provenance trees.
