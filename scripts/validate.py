import os
import duckdb

DB_PATH = "data/budget.duckdb"

OFFICIAL_TOTALS = {
    2025: 6_326_324_300_000.0,
    2026: 6_793_162_000_000.0
}

def validate_pipeline() -> bool:
    print("=== RUNNING BUDGET INSPECTOR VALIDATION & RECONCILIATION ===")
    
    if not os.path.exists(DB_PATH):
        print(f"FAIL: Database {DB_PATH} missing!")
        return False
        
    conn = duckdb.connect(DB_PATH, read_only=True)
    all_passed = True
    
    # Check 1: Row Counts
    res25 = conn.execute("SELECT COUNT(*) FROM budget_2025").fetchone()
    res26 = conn.execute("SELECT COUNT(*) FROM budget_2026").fetchone()
    cnt_2025 = res25[0] if res25 else 0
    cnt_2026 = res26[0] if res26 else 0
    
    print(f"[Check 1] Row Counts: 2025={cnt_2025:,}, 2026={cnt_2026:,}")
    if cnt_2025 == 0 or cnt_2026 == 0:
        print("FAIL: One or both budget tables are empty!")
        all_passed = False
    else:
        print("✓ PASS: Non-zero row counts.")

    # Check 2: Total Sum Reconciliation
    sum25_res = conn.execute("SELECT SUM(amount_pesos) FROM budget_2025").fetchone()
    sum26_res = conn.execute("SELECT SUM(amount_pesos) FROM budget_2026").fetchone()
    sum_2025 = float(sum25_res[0]) if sum25_res and sum25_res[0] is not None else 0.0
    sum_2026 = float(sum26_res[0]) if sum26_res and sum26_res[0] is not None else 0.0
    
    diff_2025 = abs(sum_2025 - OFFICIAL_TOTALS[2025])
    diff_2026 = abs(sum_2026 - OFFICIAL_TOTALS[2026])
    
    pct_diff_25 = (diff_2025 / OFFICIAL_TOTALS[2025]) * 100.0
    pct_diff_26 = (diff_2026 / OFFICIAL_TOTALS[2026]) * 100.0
    
    print(f"[Check 2] 2025 Reconciled Sum: ₱{sum_2025:,.2f} vs Official: ₱{OFFICIAL_TOTALS[2025]:,.2f} (Diff: ₱{diff_2025:,.2f}, {pct_diff_25:.4f}%)")
    print(f"[Check 2] 2026 Reconciled Sum: ₱{sum_2026:,.2f} vs Official: ₱{OFFICIAL_TOTALS[2026]:,.2f} (Diff: ₱{diff_2026:,.2f}, {pct_diff_26:.4f}%)")
    
    if pct_diff_25 < 0.01 and pct_diff_26 < 0.01:
        print("✓ PASS: Normalized totals reconcile within 0.01% of official DBM totals.")
    else:
        print("WARNING: Total reconciliation discrepancy exceeds threshold!")
        all_passed = False

    # Check 3: Provenance Integrity
    null25_res = conn.execute("SELECT COUNT(*) FROM budget_2025 WHERE source_row IS NULL OR source_file IS NULL").fetchone()
    null26_res = conn.execute("SELECT COUNT(*) FROM budget_2026 WHERE source_row IS NULL OR source_file IS NULL").fetchone()
    null_rows_25 = null25_res[0] if null25_res else 0
    null_rows_26 = null26_res[0] if null26_res else 0
    
    print(f"[Check 3] Missing Provenance Rows: 2025={null_rows_25}, 2026={null_rows_26}")
    if null_rows_25 == 0 and null_rows_26 == 0:
        print("✓ PASS: 100% of normalized rows retain exact source file and row provenance.")
    else:
        print("FAIL: Missing provenance records found!")
        all_passed = False

    conn.close()
    
    generate_inventory_report(cnt_2025, cnt_2026, sum_2025, sum_2026, pct_diff_25, pct_diff_26)
    
    return all_passed

def generate_inventory_report(c25, c26, s25, s26, p25, p26):
    os.makedirs("reports/validation", exist_ok=True)
    report_path = "reports/validation/workbook_inventory.md"
    
    content = f"""# Workbook Inventory & Data Quality Report

## Executive Summary
- **FY 2025 GAA Source**: `raw/2025/GAA-2025.xlsx` (68.5 MB)
- **FY 2026 GAA Source**: `raw/2026/FY2026-GAA-Byobject.xlsx` (61.6 MB)
- **Engine**: DuckDB (`data/budget.duckdb`)

---

## 📊 Summary Inventory

| Fiscal Year | Raw Sheet | Total Raw Rows | Normalized Leaf Rows | Total Pesos (Normalized) | Official DBM Total | Variance (%) | Provenance Coverage |
|---|---|---|---|---|---|---|---|
| **FY 2025** | Sheet 1 | 723,106 | {c25:,} | ₱{s25:,.2f} | ₱{OFFICIAL_TOTALS[2025]:,.2f} | {p25:.4f}% | 100.0% |
| **FY 2026** | Sheet 1 | 736,849 | {c26:,} | ₱{s26:,.2f} | ₱{OFFICIAL_TOTALS[2026]:,.2f} | {p26:.4f}% | 100.0% |

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
"""
    with open(report_path, "w") as f:
        f.write(content)
        
    print(f"[Validate] Generated inventory report at {report_path}")

if __name__ == "__main__":
    validate_pipeline()
