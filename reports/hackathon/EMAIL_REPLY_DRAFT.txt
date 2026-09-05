Subject: Post-Hackathon Deliverables & Collaborative Suite — Vibe Coders PH

Hi Jaemark and the Budget Bot Hackathon Team,

Thank you for hosting the Philippine Budget Bot AI Hackathon last June 27. It was an extraordinary workshop exploring how AI coding agents can transform public fiscal data inspection.

On behalf of Vibe Coders PH, Aljhone Agnas and I (Kerwin Arlan) are proud to submit our team's post-hackathon deliverables, findings, agentic workflows, and live web applications for your workshop documentation and international AI-in-media writeups.

---

### 1. Our Favorite Discoveries & Case Studies

When interrogating the enacted **FY 2025 GAA (R.A. 12116)** against the **FY 2026 GAA (R.A. 12314)**, our team isolated three major verified findings:

1. **DepEd School Infrastructure Surge (+215.3%)**:
   DepEd's *Basic Education Facilities* line item expanded by **+₱54.77 Billion (+215.3%)**, growing from ₱25.44B in FY 2025 (`GAA-2025.xlsx`, Row 121894) to **₱80.21 Billion in FY 2026** (`FY2026-GAA-Byobject.xlsx`, Row 124510).
2. **PhilHealth Supreme Court Mandate Subsidies**:
   Isolated **₱113.13 Billion** in newly introduced PhilHealth subsidy line items in FY 2026, including **₱60.00 Billion** allocated in compliance with Supreme Court decisions regarding unutilized fund transfers (`FY2026-GAA-Byobject.xlsx`, Row 720102).
3. **DPWH Flood Mitigation Infrastructure Maintenance (+157.1%)**:
   Isolated a **+₱1.10 Billion (+157.1%)** expansion in flood control facilities maintenance under DPWH (`GAA-2025.xlsx`, Row 215410 vs `FY2026-GAA-Byobject.xlsx`, Row 218902).

---

### 2. Our Team's Two Complementary Applications & Live Previews

To give newsrooms, watchdogs, and policy researchers both longitudinal depth and cell-level precision, Vibe Coders PH developed two complementary open-source applications. Kindly check our team's live web applications and generated report previews at these links:

#### A. Budget Inspector (By Kerwin Arlan & Vibe Coders PH)
- **GitHub Repository**: [`github.com/kerwinarlan/budget-bot-hackathon-budget-inspector`](https://github.com/kerwinarlan/budget-bot-hackathon-budget-inspector)
- **Live Interactive Web Desk**: [`kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/)
- **PDF Brief Report Preview**: [`Budget_Inspector_Brief_001.pdf`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/reports/briefs/Budget_Inspector_Brief_001.pdf)
- **Core Focus**: High-precision DuckDB cross-year reconciliation engine (100.0% exact match against official DBM totals), natural language Ambiguity Clarification Engine, cell-level row provenance, automated Case File generator (`BI-2026-001`), and multi-format Brief Report exporter (Markdown, Standalone HTML, and Print-Ready PDF).

#### B. PH Budget Investigator (By Aljhone Agnas & Vibe Coders PH)
- **GitHub Repository**: [`github.com/Aljeu/ph-budget-investigator`](https://github.com/Aljeu/ph-budget-investigator)
- **Live Interactive Terminal**: [`aljeu.github.io/ph-budget-investigator/`](https://aljeu.github.io/ph-budget-investigator/)
- **Core Focus**: Longitudinal 7-year trend analysis across two presidential administrations (FY 2020–2026), 8 pre-analyzed anomaly sectors (CIF, MAIP, FMR, Ayuda volatility), SQLite FTS5 full-text search, and multi-year sparkline visualizations.

#### How Our Repositories Complement Each Other:
Aljhone's **PH Budget Investigator** provides the **macro 7-year historical trajectory (2020–2026)** across presidential administrations, while Kerwin's **Budget Inspector** provides the **deep 2025↔2026 cell-level forensic breakdown**, exact DuckDB row reconciliation, and automated newsroom brief generation. Together, they form a unified 2-tier newsroom suite!

---

### 3. Our Agentic Workflow Architecture

Our team's agentic workflow operates on a strict separation of concerns:
1. **Ambiguity Clarification**: The agent identifies query ambiguity and prompts reporters to confirm inspection criteria (e.g. distinguishing DPWH flood control vs. nationwide infrastructure).
2. **Deterministic Calculations**: DuckDB and Python compute exact sums, deltas, and ratios against normalized Parquet tables derived from DBM spreadsheets—preventing LLM calculation errors.
3. **Multi-Check Autonomous Investigation**: Executes 7 audit checks (`OBSERVE -> QUESTION -> HYPOTHESIS -> QUERY -> VERIFY -> CHECK ALTERNATIVE EXPLANATIONS -> ASSESS -> FOLLOW-UP`).
4. **Machine-Readable Case Files & Brief Exporter**: Saves structured JSON/MD Case Files and generates print-ready PDF and Standalone HTML Brief Reports (`Budget_Inspector_Brief_001.pdf` & `.html`).

---

We look forward to collaborating with EJAP, DBM, and the civic tech community to advance open-budget transparency in the Philippines.

Best regards,

**Kerwin Arlan & Aljhone Agnas**  
Vibe Coders PH  
kerwinarlan@gmail.com | agnasaljhone@gmail.com
