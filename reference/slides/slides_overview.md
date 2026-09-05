# Presentation Slides Overview — Budget Bot Hackathon

**Presentation URL**: `https://www.canva.com/design/DAHNla4KhI0/mfK6VEGsKWHJ2ZeChURRxw/view`

---

## 🖼️ Slide Inventory & Extracted Insights

1. **Title Slide**: *Budget Bot Hackathon — 27 June 2026* (Sponsors: PLDT Smart, Economic Journalists Association of the Philippines - EJAP).
2. **Context**: Open Budget Survey results highlighting Philippine budget transparency lead in Southeast Asia (Score: 76/100).
3. **Background Article**: *"I created an AI chatbot to speak to my country's budget. Here's how I did it"* by Jaemark Tordecilla.
4. **Data Visualization Example**: Scatter plot of *DPWH Covered Court Projects: Amount vs. Number of Projects (2023-2025)* highlighting extreme outliers (e.g., Sorsogon 2nd District Engineering Office in 2025 with over 100 projects worth >₱1 Billion).
5. **Coding Agent Concept**: Transitioning from basic chat prompts to local coding agents that run Python/SQL directly against raw data files.
6. **Meta Ad Library Example**: Case study showing spend concentration among Facebook ad advertisers in the Philippines.
7. **Excel Source Preview**: Showing raw spreadsheet rows used as ingestion targets.
8. **Codex / Claude Code CLI**: CLI environments executing automated skill commands.
9. **Why a Skill?**:
   - Lives locally on the computer.
   - Combines instructions, helper scripts, and lookup tables.
   - Operates directly on local files.
   - Guarantees analysis reproducibility with exact SQL/Python code behind every answer.
   - Standardizes line-item search, agency matching, and cross-year comparison.
10. **Architecture Flowcharts**:
    - `Excel Files -> Python -> Searchable DB -> Agency Lookup JSON`
    - `User -> Agent + Skill -> SQL Execution -> Query Results + Audit Trail`
11. **Plugin Installation Instructions**:
    - Claude Code: `claude plugin marketplace add tordecilla/budget-bot-skill` & `claude plugin install budget-bot@budget-bot`
    - Codex: `/plugin marketplace add tordecilla/budget-bot-skill` & `/plugin add budget-bot@budget-bot`
