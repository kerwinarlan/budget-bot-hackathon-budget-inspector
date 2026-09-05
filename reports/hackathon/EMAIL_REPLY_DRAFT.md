Subject: Post-Hackathon Deliverables & Collaborative Suite — Team Vibe Coders PH

Hi Jaemark and the Budget Bot Hackathon Team,

Thank you for hosting the Philippine Budget Bot AI Hackathon last June 27. It was an extraordinary workshop exploring how AI coding agents can transform public fiscal data inspection.

On behalf of the entire **Vibe Coders PH** team, **Aljhone Agnas** and I (**Kerwin Arlan**) are proud to submit our team's post-hackathon deliverables, findings, and agentic workflows for your workshop documentation and international AI-in-media writeups.

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

### 2. Our Team's Two Complementary Repositories

To give newsrooms, watchdogs, and policy researchers both longitudinal depth and cell-level precision, **Team Vibe Coders PH** built a unified 2-part open-source investigative suite:

#### Part A. Longitudinal 7-Year Anomaly Terminal (By Aljhone Agnas & Vibe Coders PH)
- **Repository**: [`github.com/Aljeu/ph-budget-investigator`](https://github.com/Aljeu/ph-budget-investigator)
- **Live Portal**: [`aljeu.github.io/ph-budget-investigator/`](https://aljeu.github.io/ph-budget-investigator/)
- **Core Focus**: Longitudinal 7-year trend analysis across two presidential administrations (FY 2020–2026), 8 pre-analyzed anomaly sectors (CIF, MAIP, FMR, Ayuda volatility), SQLite FTS5 full-text search, and multi-year sparkline visualizations.

#### Part B. Cell Provenance, Case Files & Newsroom Brief Desk (By Kerwin Arlan & Vibe Coders PH)
- **Repository**: [`github.com/kerwinarlan/budget-bot-hackathon-budget-inspector`](https://github.com/kerwinarlan/budget-bot-hackathon-budget-inspector)
- **Live Portal**: [`kerwinarlan.github.io/budget-bot-hackathon-budget-inspector`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/)
- **Core Focus**: High-precision DuckDB cross-year reconciliation engine (100.0% exact match against official DBM totals), natural language Ambiguity Clarification Engine, cell-level row provenance, automated Case File generator (`BI-2026-001`), and multi-format Brief Report exporter (Markdown, Standalone HTML, and Print-Ready PDF).

#### How Our Repositories Complement Each Other:
Aljhone's engine provides the **macro 7-year historical trajectory (2020–2026)** across two administrations, while Kerwin's engine provides the **deep 2025↔2026 cell-level forensic breakdown**, exact DuckDB row reconciliation, and automated newsroom brief generation.

---

### 3. Our Agentic Workflow Architecture

Our team's agentic workflow operates on a strict separation of concerns:
1. **Ambiguity Clarification**: The agent identifies query ambiguity and prompts reporters to confirm inspection criteria (e.g. distinguishing DPWH flood control vs. nationwide infrastructure).
2. **Deterministic Calculations**: DuckDB and Python compute exact sums, deltas, and ratios against normalized Parquet tables derived from DBM spreadsheets—preventing LLM calculation errors.
3. **Multi-Check Autonomous Investigation**: Executes 7 audit checks (`OBSERVE -> QUESTION -> HYPOTHESIS -> QUERY -> VERIFY -> CHECK ALTERNATIVE EXPLANATIONS -> ASSESS -> FOLLOW-UP`).
4. **Machine-Readable Case Files & Brief Exporter**: Saves structured JSON/MD Case Files and generates print-ready PDF and Standalone HTML Brief Reports (`Budget_Inspector_Brief_001.pdf` & `.html`).

---

### 📁 Attached Team Deliverables (PDF & HTML Formats)
- **PDF Brief Report**: [`reports/briefs/Budget_Inspector_Brief_001.pdf`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/reports/briefs/Budget_Inspector_Brief_001.pdf)
- **Standalone HTML Brief Report**: [`reports/briefs/Budget_Inspector_Brief_001.html`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/reports/briefs/Budget_Inspector_Brief_001.html)
- **Official Agency Audit Memorandum (PDF)**: [`reports/interrogative/Memorandum_bucor.pdf`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/reports/interrogative/Memorandum_bucor.pdf)
- **Official Agency Audit Memorandum (HTML)**: [`reports/interrogative/Memorandum_bucor.html`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/reports/interrogative/Memorandum_bucor.html)
- **Interactive Newsroom Desk Preview**: [`reports/hackathon/preview.html`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/reports/hackathon/preview.html)

We look forward to collaborating with EJAP, DBM, and the civic tech community to advance open-budget transparency in the Philippines.

Best regards,

**Kerwin Arlan & Aljhone Agnas**  
Team Vibe Coders PH  
kaarlan@up.edu.ph
