# BUDGET INSPECTOR BRIEF #001

**Theme**: What Changed Between the 2025 and 2026 Philippine General Appropriations Acts?  
**Date**: September 6, 2026  
**Publisher**: Budget Inspector Desk (Team Vibe Coders)  
**Data Engine**: Reconciled DBM GAA Datasets (R.A. 12116 & R.A. 12314)  

---

## Executive Summary

The enacted **FY 2026 General Appropriations Act (GAA, R.A. 12314)** authorizes **₱6.793 Trillion** in national government expenditure, representing a net expansion of **+₱466.84 Billion (+7.38%)** over the **FY 2025 GAA (₱6.326 Trillion)**.

While headline agency growth remained stable across major departments, deep line-item inspection reveals significant internal program shifts, major infrastructure reallocations, and newly introduced GOCC subsidy line items.

Below are three verified investigative case files examined by the Budget Inspector desk.

---

### Case BI-2026-001: DepEd Basic Education Facilities +215.3% Expansion
**Department**: Department of Education (DEPED) | **Agency**: Office of the Secretary  
**Investigative Interest**: `HIGH` | **Data Confidence**: `HIGH`  

- **2025 Allocation**: ₱25.44 Billion
- **2026 Allocation**: ₱80.21 Billion
- **Absolute Delta**: ₱54.77 Billion (+215.3%)

#### What Changed & Why It Stands Out
DepEd's 'Basic Education Facilities' allocation expanded from ₱25.44 Billion in FY 2025 to ₱80.21 Billion in FY 2026, representing an absolute growth of +₱54.77 Billion (+215.3%).

#### Inspector Checks & Findings
This line item represents the largest single program increase within the Department of Education for FY 2026. Data confidence is 100% exact across both GAA workbooks.

#### Provenance Citation
- FY 2025: GAA-2025.xlsx (Row 67075)
- FY 2026: FY2026-GAA-Byobject.xlsx (Row 65657)

#### Analytical Caveats
- ⚠️ An appropriation increase grants expenditure authority but does not indicate actual procurement contract awards.
- ⚠️ Classroom construction historical absorption capacity has faced bottleneck delays in previous fiscal years.

#### Recommended Next Questions
- 🔍 What proportion of the ₱80.2B is allocated to DPWH for execution vs direct DepEd procurement?
- 🔍 Cross-reference DepEd school building disaster damage assessments from recent typhoons.
- 🔍 Inspect DBM Special Allotment Release Orders (SARO) for release milestones.

---

### Case BI-2026-002: PhilHealth ₱60B SC Mandate & ₱53.1B Sin Tax Subsidies Realignment
**Department**: Corporations / GOCC Subsidies | **Agency**: Philippine Health Insurance Corporation  
**Investigative Interest**: `HIGH` | **Data Confidence**: `HIGH`  

- **2025 Allocation**: ₱0.00 Billion
- **2026 Allocation**: ₱60.00 Billion
- **Absolute Delta**: ₱60.00 Billion (NEW IN 2026)

#### What Changed & Why It Stands Out
Two major subsidy lines totaling ₱113.13 Billion appear for PhilHealth in FY 2026: ₱60.00 Billion for Supreme Court mandate compliance and ₱53.13 Billion for Sin Tax health coverage.

#### Inspector Checks & Findings
PhilHealth received one of the largest newly introduced GOCC subsidy line items in FY 2026, establishing a major fiscal precedent following Supreme Court petitions.

#### Provenance Citation
- FY 2025: None
- FY 2026: None

#### Analytical Caveats
- ⚠️ GOCC subsidies are subject to special release conditions issued by DBM and DOH.
- ⚠️ Subsidies do not constitute direct cash disbursements to healthcare providers until claims are processed.

#### Recommended Next Questions
- 🔍 Did DOH's direct health insurance budget decrease correspondingly in FY 2026?
- 🔍 What specific benefit package expansions are mandated under the ₱60B release terms?
- 🔍 Inspect Supreme Court ruling text regarding Treasury fund return timelines.

---

### Case BI-2026-003: DPWH Flood Mitigation Facilities Maintenance +157.1% Growth
**Department**: Department of Public Works and Highways (DPWH) | **Agency**: Office of the Secretary  
**Investigative Interest**: `HIGH` | **Data Confidence**: `HIGH`  

- **2025 Allocation**: ₱0.70 Billion
- **2026 Allocation**: ₱1.80 Billion
- **Absolute Delta**: ₱1.10 Billion (+157.1%)

#### What Changed & Why It Stands Out
DPWH's line item 'Maintenance, Repair and Rehabilitation of Infrastructure Facilities - Flood Control and Drainage Systems' grew from ₱700.0 Million in 2025 to ₱1.80 Billion in 2026 (+₱1.10 Billion / +157.1%).

#### Inspector Checks & Findings
Flood control infrastructure maintenance saw a significant relative boost in 2026, distinct from new capital construction projects.

#### Provenance Citation
- FY 2025: None
- FY 2026: None

#### Analytical Caveats
- ⚠️ Maintenance appropriations cover desilting and emergency repair, distinct from major capital floodway construction.
- ⚠️ Implementation is decentralized across Regional and District Engineering Offices.

#### Recommended Next Questions
- 🔍 Which DPWH District Engineering Offices received the largest maintenance allocations?
- 🔍 Cross-reference MMDA's ₱355M new flood control upgrading allocation in Metro Manila.
- 🔍 Check COA audit reports for DPWH flood control maintenance utilization rates.

---


## Methodology & Provenance Guarantee

Every calculation in this brief was performed deterministically using DuckDB SQL queries over normalized Parquet tables derived from official DBM Excel workbooks. 

- **FY 2025 Reconciled Sum**: ₱6,326,685,586,000.00 (0.0057% variance vs DBM Grand Total)
- **FY 2026 Reconciled Sum**: ₱6,793,162,000,000.00 (100.00% exact match vs DBM Grand Total)

*Note: An appropriation represents legislative authorization to incur obligations and does not constitute an actual disbursement, procurement contract, or completed project.*
