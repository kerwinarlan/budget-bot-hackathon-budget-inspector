# Demo Findings & Investigative Leads

This report presents our top verified investigative leads discovered during our cross-year analysis of the **FY 2025 GAA (R.A. 12116)** and **FY 2026 GAA (R.A. 12314)**.

Every lead includes exact calculations, source provenance (file, sheet, row), and analytical caveats.

---

## 📌 Lead 1: National Tax Allotment (NTA) Growth
- **Lead ID**: `LEAD-INC-001`
- **Category**: `LARGE_INCREASE`
- **Department**: Automatic Appropriations
- **Agency**: National Tax Allotment
- **Program**: Allocation to Local Government Units - National Tax Allotment
- **2025 Amount**: ₱1,034,604,869,000.00 (₱1,034.60B)
- **2026 Amount**: ₱1,190,509,672,000.00 (₱1,190.51B)
- **Absolute Change**: +₱155,904,803,000.00 (+₱155.90 Billion)
- **Percentage Change**: +15.07%
- **Source Provenance**:
  - FY 2025: `GAA-2025.xlsx`, Sheet `Sheet 1`, Row `723080`
  - FY 2026: `FY2026-GAA-Byobject.xlsx`, Sheet `Sheet 1`, Row `736823`
- **Query Used**:
  ```sql
  SELECT department_name, agency_name, description, amount_2025_pesos, amount_2026_pesos, absolute_change_pesos, percent_change
  FROM pap_comparison
  WHERE agency_name = 'National Tax Allotment'
  ORDER BY absolute_change_pesos DESC;
  ```
- **Caveat**: Mandatory automatic formula allocation driven by national internal revenue collections under the Mandanas-Garcia Supreme Court ruling.

---

## 📌 Lead 2: Basic Education Facilities (DepEd)
- **Lead ID**: `LEAD-INC-002`
- **Category**: `LARGE_INCREASE`
- **Department**: Department of Education (DEPED)
- **Agency**: Office of the Secretary
- **Program**: Basic Education Facilities
- **2025 Amount**: ₱25,441,852,000.00 (₱25.44B)
- **2026 Amount**: ₱80,212,410,000.00 (₱80.21B)
- **Absolute Change**: +₱54,770,558,000.00 (+₱54.77 Billion)
- **Percentage Change**: +215.28%
- **Source Provenance**:
  - FY 2025: `GAA-2025.xlsx`, Sheet `Sheet 1`, Row `121894`
  - FY 2026: `FY2026-GAA-Byobject.xlsx`, Sheet `Sheet 1`, Row `124510`
- **Query Used**:
  ```sql
  SELECT agency_name, description, amount_2025_pesos, amount_2026_pesos, absolute_change_pesos, percent_change
  FROM pap_comparison
  WHERE description LIKE '%Basic Education Facilities%'
  ORDER BY absolute_change_pesos DESC;
  ```
- **Caveat**: Reflects major classroom construction and furniture procurement drive; verify procurement implementation schedule.

---

## 📌 Lead 3: Pantawid Pamilyang Pilipino Program (DSWD 4Ps)
- **Lead ID**: `LEAD-INC-003`
- **Category**: `LARGE_INCREASE`
- **Department**: Department of Social Welfare and Development (DSWD)
- **Agency**: Office of the Secretary
- **Program**: Pantawid Pamilyang Pilipino Program (Implementation)
- **2025 Amount**: ₱56,400,000,000.00 (₱56.40B)
- **2026 Amount**: ₱100,440,000,000.00 (₱100.44B)
- **Absolute Change**: +₱44,040,000,000.00 (+₱44.04 Billion)
- **Percentage Change**: +78.09%
- **Source Provenance**:
  - FY 2025: `GAA-2025.xlsx`, Sheet `Sheet 1`, Row `652101`
  - FY 2026: `FY2026-GAA-Byobject.xlsx`, Sheet `Sheet 1`, Row `664120`
- **Caveat**: Expansion of cash grant coverage and inflation adjustments for beneficiary families.

---

## 📌 Lead 4: New PhilHealth Subsidies (FY 2026)
- **Lead ID**: `LEAD-NEW-001`
- **Category**: `NEW_ITEM`
- **Department**: Corporations / GOCC Subsidies
- **Agency**: Philippine Health Insurance Corporation (PhilHealth)
- **Program**: Additional Appropriation in Compliance with Supreme Court Mandate
- **2025 Amount**: ₱0.00 (`NEW_IN_2026`)
- **2026 Amount**: ₱60,000,000,000.00 (₱60.00B)
- **Source Provenance**:
  - FY 2026: `FY2026-GAA-Byobject.xlsx`, Sheet `Sheet 1`, Row `720102`
- **Caveat**: Statutory realignment following legal petitions on unutilized PhilHealth reserve fund transfers.
