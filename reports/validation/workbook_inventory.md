# Workbook Inventory & Data Quality Report

## Executive Summary
- **FY 2025 GAA Source**: `raw/2025/GAA-2025.xlsx` (68.5 MB)
- **FY 2026 GAA Source**: `raw/2026/FY2026-GAA-Byobject.xlsx` (61.6 MB)
- **Engine**: DuckDB (`data/budget.duckdb`)

---

## 📊 Summary Inventory

| Fiscal Year | Raw Sheet | Total Raw Rows | Normalized Leaf Rows | Total Pesos (Normalized) | Official DBM Total | Variance (%) | Provenance Coverage |
|---|---|---|---|---|---|---|---|
| **FY 2025** | Sheet 1 | 723,106 | 539,379 | ₱6,326,685,586,000.00 | ₱6,326,324,300,000.00 | 0.0057% | 100.0% |
| **FY 2026** | Sheet 1 | 736,849 | 522,214 | ₱6,793,162,000,000.00 | ₱6,793,162,000,000.00 | 0.0000% | 100.0% |

---

## 🔍 Structure & Schema Differences

1. **Expense Object Field Names**:
   - FY 2025 uses `UACS_SOBJ_CD` and `UACS_SOBJ_DSC` (Sub-Object Code/Description).
   - FY 2026 uses `UACS_OBJ_CD` and `UACS_OBJ_DSC` (Object Code/Description).
2. **Hierarchy Levels**:
   - Both datasets use `PREXC_LEVEL` values 1 to 7.
   - `PREXC_LEVEL 7` contains detailed operational line items.
   - `PREXC_LEVEL 3` contains Automatic Appropriations (e.g., National Tax Allotment).
3. **Currency Scaling**:
   - Amounts in raw Excel sheets are recorded in **Thousand Pesos**.
   - Normalization multiplies raw values by 1,000.0 to produce exact Peso amounts (`amount_pesos`).
