Subject: Post-Hackathon Submission — Team Vibe Coders (Budget Inspector)

Hi Jaemark and the Budget Bot Hackathon Team,

Thank you for organizing the Philippine Budget Bot AI Hackathon! It was a fantastic experience exploring how coding agents can help interrogate government budget spreadsheets.

On behalf of team **Vibe Coders**, here is our post-hackathon deliverable and summary:

---

### 1. Our Favorite Discovery
When analyzing the **FY 2025 GAA (R.A. 12116)** versus the **FY 2026 GAA (R.A. 12314)**, we discovered a major **₱54.77 Billion (+215.3%) surge** in DepEd’s *Basic Education Facilities* line item (expanding from ₱25.44B in 2025 to ₱80.21B in 2026). 

We were able to verify this figure down to the exact spreadsheet row:
- **FY 2025**: File `GAA-2025.xlsx`, Row `121894`
- **FY 2026**: File `FY2026-GAA-Byobject.xlsx`, Row `124510`

We also isolated **₱113.13 Billion** in newly introduced PhilHealth subsidy line items in 2026 (including ₱60B allocated in compliance with Supreme Court mandates regarding unutilized fund transfers).

---

### 2. Our Agentic Workflow
Building upon our team skill repo ([`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill), forked from `tordecilla/budget-bot-skill`), we built **Budget Inspector** around a strict separation of concerns:
1. **Agents handle orchestration**: The AI agent classifies user intent, inspects UACS schemas, and formulates deterministic DuckDB SQL queries.
2. **DuckDB handles calculation**: DuckDB and Python compute exact sums, deltas, and ratios against normalized Parquet tables derived from DBM spreadsheets.
3. **Audit Trail & Receipts**: For every query, the system generates a machine-readable **Research Receipt (.json)** containing the SQL query, cell/row provenance, and analytical caveats (e.g., reminding users that appropriations do not equal actual disbursements).

---

### 3. International AI-in-Media Potential
We documented our methodology in a writeup titled **"Evidence-First Budget Reporting: Using Coding Agents as Reproducible Analytical Engines for Public Fiscal Data."** 

It highlights how AI tools can be deployed in investigative newsrooms to replace fragile manual spreadsheet checks with audit-trailed, cell-verifiable SQL workflows while enforcing strict journalistic standards (e.g., flagging anomalies as *investigative leads* rather than unsupported accusations).

---

### Repositories & Deliverables
- **Main Analytical Repo**: [`kerwinarlan/budget-bot-hackathon-budget-inspector`](https://github.com/kerwinarlan/budget-bot-hackathon-budget-inspector)
- **Team Skill Repo**: [`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill) *(forked from [`tordecilla/budget-bot-skill`](https://github.com/tordecilla/budget-bot-skill))*

Key report paths in main repo:
- `reports/hackathon/HACKATHON_DELIVERABLE.md`
- `reports/hackathon/DEMO_FINDINGS.md`
- `reports/hackathon/PROJECT_SUMMARY.md`

We look forward to future collaborations and staying connected with the EJAP and civic tech community!

Best regards,

**Kerwin Arlan & Team Vibe Coders**  
kaarlan@up.edu.ph
