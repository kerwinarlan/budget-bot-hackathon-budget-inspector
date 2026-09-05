# Data Sources & Official Provenance

## Primary Authoritative Sources

### 1. FY 2025 General Appropriations Act (GAA, R.A. 12116)
- **Publisher**: Department of Budget and Management (DBM), Republic of the Philippines
- **Source Page**: `https://www.dbm.gov.ph/index.php/2025/general-appropriations-act-gaa-fy-2025`
- **Spreadsheet File**: `https://www.dbm.gov.ph/wp-content/uploads/GAA/GAA2025/GAA-2025.xlsx`
- **Local Location**: `raw/2025/GAA-2025.xlsx`
- **Enacted Total**: ₱6,326,324,300,000 (₱6.326 Trillion)

### 2. FY 2026 General Appropriations Act (GAA, R.A. 12314)
- **Publisher**: Department of Budget and Management (DBM), Republic of the Philippines
- **Source Page**: `https://www.dbm.gov.ph/index.php/2026/general-appropriations-act-gaa-fy-2026`
- **Spreadsheet File**: `https://www.dbm.gov.ph/wp-content/uploads/GAA/GAA2026/FY2026-GAA-Byobject.xlsx`
- **Local Location**: `raw/2026/FY2026-GAA-Byobject.xlsx`
- **Enacted Total**: ₱6,793,162,000,000 (₱6.793 Trillion)

---

## Technical Data Notes
- **Unit of Measurement in Spreadsheets**: Amounts (`AMT`) are represented in **Thousand Pesos (PHP 1,000)**.
  - Example: `597196.0` in cell = `597,196,000 Pesos`.
  - The normalization engine converts all values to exact Pesos or explicit Thousands with documented scale.
- **Hierarchy Representation**:
  - `PREXC_LEVEL 1 to 6`: Organizational, Department, Agency, Program, Sub-program headers.
  - `PREXC_LEVEL 7`: Detailed line items carrying `AMT`.
  - `PREXC_LEVEL 3` (Special): Automatic Appropriations lines carrying `AMT`.
