Subject: Post-Hackathon Submission — Team Vibe Coders (Budget Inspector)

Hi Jaemark and the Budget Bot Hackathon Team,

Thank you for organizing the Philippine Budget Bot AI Hackathon! It was an incredible experience exploring how coding agents can help interrogate government budget spreadsheets.

On behalf of team **Vibe Coders**, here is our post-hackathon deliverable and summary:

---

### 1. What We Built
We extended our initial hackathon skill into **Budget Inspector**: an evidence-first, agentic analytical web application and newsroom desk for the Philippine budget.

Unlike conversational chatbots that risk hallucinating numbers, Budget Inspector strictly separates reasoning from calculation:
- **FastAPI / Python Web App**: Serves an interactive desk (`http://localhost:8000` / Render-ready).
- **Ask → Investigate → Case File → Evidence → Brief Workflow**: Handles ambiguity resolution, autonomous multi-check investigations, cell-level row provenance, and case file creation.
- **DuckDB Analytical Engine**: Reconciles normalized row sums directly against official DBM Grand Totals (100.0% exact match for FY 2026 GAA).

---

### 2. Our Favorite Discoveries & Case Files
1. **DepEd Facilities Expansion (`BI-2026-001`)**: DepEd’s *Basic Education Facilities* line item surged by **+215.3% (+₱54.77 Billion)**, expanding from ₱25.44B in 2025 (`GAA-2025.xlsx`, Row 121894) to ₱80.21B in 2026 (`FY2026-GAA-Byobject.xlsx`, Row 124510).
2. **PhilHealth SC Mandate Realignment (`BI-2026-002`)**: Isolated **₱113.13 Billion** in newly introduced PhilHealth subsidies in 2026, including ₱60B allocated in compliance with Supreme Court mandates regarding unutilized fund transfers.
3. **DPWH Infrastructure Maintenance (`BI-2026-003`)**: Isolated a **+₱1.10 Billion (+157.1%)** expansion in flood mitigation infrastructure maintenance.

---

### 3. Editorial Deliverable: Budget Inspector Brief #001
We compiled our verified case files into an editorial evidence report titled **Budget Inspector Brief #001** (*"What Changed Between the 2025 and 2026 Philippine GAA?"*), available at `reports/briefs/Budget_Inspector_Brief_001.md` and viewable in the web app under `/briefs/001`.

---

### Repositories & Deliverables
- **Main Analytical Repo**: [`kerwinarlan/budget-bot-hackathon-budget-inspector`](https://github.com/kerwinarlan/budget-bot-hackathon-budget-inspector)
- **Team Skill Repo**: [`kerwinarlan/budget-bot-skill`](https://github.com/kerwinarlan/budget-bot-skill) *(forked from [`tordecilla/budget-bot-skill`](https://github.com/tordecilla/budget-bot-skill))*

Key deliverable paths in the repository:
- `reports/hackathon/HACKATHON_DELIVERABLE.md`
- `reports/briefs/Budget_Inspector_Brief_001.md`
- `DEPLOYMENT.md` & `render.yaml`

We look forward to future collaborations and staying connected with EJAP and the civic tech community!

Best regards,

**Kerwin Arlan & Team Vibe Coders**  
kaarlan@up.edu.ph
