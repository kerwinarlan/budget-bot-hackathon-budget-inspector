---
name: budget-inspector
description: Use when answering Philippine national budget questions, comparing 2025 vs 2026 GAA appropriations, investigating line items, flood control, or generating evidence-backed leads.
---

# Budget Inspector Skill

This skill teaches coding agents how to interrogate Philippine General Appropriations Act (GAA) datasets (FY 2025 R.A. 12116 vs FY 2026 R.A. 12314) reproducibly and deterministically using DuckDB and Python.

---

## 🛠️ CORE WORKFLOW

When asked a budget question, follow these exact 10 steps:

1. **Classify Intent**:
   - `top_increases`: Largest absolute or percentage budget gains.
   - `new_items`: Line items appearing in 2026 with no 2025 match.
   - `disappeared`: Line items present in 2025 missing in 2026.
   - `reallocation`: Agencies with flat headline growth but internal reshuffling.
   - `flood_control`: Infrastructure mitigation keyword search across DPWH engineering districts.
   - `lookup`: Agency or keyword search.

2. **Inspect Schema & Tables**:
   - Primary database: `data/budget.duckdb`
   - Key tables: `pap_comparison`, `agency_comparison`, `department_comparison`, `budget_2025`, `budget_2026`.

3. **Formulate & Execute SQL**:
   - Use `src/budget_inspector/queries.py` or run SQL against `data/budget.duckdb`.
   - Never estimate or summarize numbers in prose prior to SQL execution.

4. **Validate Arithmetic**:
   - Ensure numbers match DuckDB outputs exactly.

5. **Entity Resolution**:
   - Distinguish exact matches, PAP matches, and candidate renames.

6. **Retrieve Provenance**:
   - Extract `source_file`, `source_sheet`, and `source_row` for every cited finding.

7. **Generate Research Receipt**:
   - Produce a machine-readable JSON research receipt under `queries/investigations/`.

8. **Apply Journalistic Ethics**:
   - Use approved neutral terms (*unusual change*, *large variance*, *investigative lead*, *reclassification candidate*).
   - NEVER label entries *corrupt*, *fraudulent*, *pork barrel*, or *ghost project*.

9. **Preserve Fiscal Distinction**:
   - Explicitly note that *appropriation* ≠ *expenditure* or *contract award*.

10. **Return Final Evidence**:
    - Output answer, exact PHP amounts, delta, percentage change, SQL query, source file/row citation, and caveats.

---

## 💻 CLI CHEAT SHEET

```bash
# Check system status
budget-inspector status

# Discover top increases
budget-inspector top-increases --limit 15

# Discover new 2026 line items
budget-inspector new-items --limit 15

# Search flood control allocations
budget-inspector search "flood control"

# Generate automated investigative leads
budget-inspector leads

# Natural language query
budget-inspector ask "Which agencies had the largest budget increases?"
```
