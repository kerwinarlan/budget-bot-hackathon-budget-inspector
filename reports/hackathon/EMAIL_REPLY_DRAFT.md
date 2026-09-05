Subject: Post-Hackathon Submission & Collaborative Deliverables — Team Vibe Coders PH

Hi Jaemark and the Budget Bot Hackathon Team,

Thank you for hosting the Philippine Budget Bot AI Hackathon last June 27. It was an invaluable session exploring how AI coding agents can transform government budget inspection.

On behalf of **Team Vibe Coders PH** (Kerwin Arlan & Aljhone Agnas), here is our post-hackathon deliverable and summary for your workshop documentation and international AI-in-media writeups.

---

### 1. Our Favorite Discoveries & Case Files

When analyzing the enacted **FY 2025 GAA (R.A. 12116)** against the **FY 2026 GAA (R.A. 12314)**, our engine isolated three major findings:

1. **DepEd School Infrastructure Surge (+215.3%)**:
   DepEd's *Basic Education Facilities* line item expanded by **+₱54.77 Billion (+215.3%)**, growing from ₱25.44B in FY 2025 (`GAA-2025.xlsx`, Row 121894) to **₱80.21 Billion in FY 2026** (`FY2026-GAA-Byobject.xlsx`, Row 124510).
2. **PhilHealth Supreme Court Mandate Subsidies**:
   Isolated **₱113.13 Billion** in newly introduced PhilHealth subsidy line items in FY 2026, including **₱60.00 Billion** allocated in compliance with Supreme Court decisions regarding unutilized fund transfers (`FY2026-GAA-Byobject.xlsx`, Row 720102).
3. **DPWH Flood Mitigation Facilities Maintenance (+157.1%)**:
   Isolated a **+₱1.10 Billion (+157.1%)** expansion in flood control facilities maintenance under DPWH (`GAA-2025.xlsx`, Row 215410 vs `FY2026-GAA-Byobject.xlsx`, Row 218902).

---

### 2. Our Team's Complementary Repositories

During and after the hackathon, our team built two complementary open-source repositories that form a 2-tier newsroom investigative suite:

#### A. `kerwinarlan/budget-bot-hackathon-budget-inspector` (By Kerwin Arlan)
- **Repository**: [`github.com/kerwinarlan/budget-bot-hackathon-budget-inspector`](https://github.com/kerwinarlan/budget-bot-hackathon-budget-inspector)
- **Live Portal**: [`kerwinarlan.github.io/budget-bot-hackathon-budget-inspector`](https://kerwinarlan.github.io/budget-bot-hackathon-budget-inspector/)
- **Core Focus**: High-precision DuckDB cross-year reconciliation engine (100.0% exact match against official DBM totals), natural language Ambiguity Clarification Engine, cell-level row provenance, automated Case File generator (`BI-2026-001`), and multi-format Brief Report exporter (Markdown, Standalone HTML, and Print-Ready PDF).

#### B. `Aljeu/ph-budget-investigator` (By Aljhone Agnas)
- **Repository**: [`github.com/Aljeu/ph-budget-investigator`](https://github.com/Aljeu/ph-budget-investigator)
- **Live Portal**: [`aljeu.github.io/ph-budget-investigator/`](https://aljeu.github.io/ph-budget-investigator/)
- **Core Focus**: Longitudinal 7-year trend analysis across two presidential administrations (FY 2020–2026), 8 pre-analyzed anomaly sectors (CIF, MAIP, FMR, Ayuda volatility), SQLite FTS5 full-text search, and multi-year sparkline visualizations.

**How They Complement Each Other**:  
Aljhone's engine provides the **macro 7-year historical trajectory** across administrations, while Kerwin's engine provides the **deep 2025↔2026 cell-level forensic breakdown**, exact DuckDB row reconciliation, and automated newsroom brief generation.

---

### 3. Our Agentic Workflow Architecture

Our agentic workflow operates on a strict separation of concerns:
1. **Ambiguity Clarification**: The agent identifies query ambiguity and prompts reporters to confirm inspection criteria (e.g. distinguishing DPWH flood control vs. nationwide infrastructure).
2. **Deterministic Calculations**: DuckDB and Python compute exact sums, deltas, and ratios against normalized Parquet tables derived from DBM spreadsheets—preventing LLM calculation errors.
3. **Multi-Check Autonomous Investigation**: Executes 7 audit checks (`OBSERVE -> QUESTION -> HYPOTHESIS -> QUERY -> VERIFY -> CHECK ALTERNATIVE EXPLANATIONS -> ASSESS -> FOLLOW-UP`).
4. **Machine-Readable Case Files & Brief Exporter**: Saves structured JSON/MD Case Files and generates print-ready PDF Brief Reports (`Budget_Inspector_Brief_001.pdf`).

---

### 📁 Attached Deliverables
- **PDF Brief Report**: `reports/briefs/Budget_Inspector_Brief_001.pdf`
- **Official Agency Audit Memorandum**: `reports/interrogative/Memorandum_bucor.pdf`
- **Methodology & Documentation**: `README.md` and `HACKATHON_DELIVERABLE.md`

We look forward to collaborating with EJAP, DBM, and the civic tech community to advance open-budget transparency in the Philippines.

Best regards,

**Kerwin Arlan & Aljhone Agnas**  
Team Vibe Coders PH  
kaarlan@up.edu.ph
