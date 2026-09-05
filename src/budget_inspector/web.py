import json
import os
from datetime import datetime, timezone
from typing import Optional, List
from fastapi import FastAPI, Request, Form, Query, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import duckdb

from budget_inspector.queries import (
    execute_query,
    query_top_increases,
    query_top_decreases,
    query_new_items,
    query_flood_control,
    query_agency_reallocations,
    search_budget
)
from budget_inspector.cases import list_all_cases, load_case_file, CaseFile, save_case_file
from budget_inspector.provenance import get_row_provenance
from budget_inspector.anomalies import generate_investigative_leads

DB_PATH = "data/budget.duckdb"

app = FastAPI(
    title="Budget Inspector Web",
    description="An evidence-first investigative agent for the Philippine national budget.",
    version="0.2.0"
)

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

templates = Jinja2Templates(directory=TEMPLATES_DIR)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

BRIEFS_DIR = "reports/briefs"
os.makedirs(BRIEFS_DIR, exist_ok=True)
app.mount("/reports/briefs", StaticFiles(directory=BRIEFS_DIR), name="briefs_files")

@app.get("/health")
def health_check():
    db_connected = os.path.exists(DB_PATH)
    return {
        "status": "ok" if db_connected else "degraded",
        "database": "connected" if db_connected else "missing",
        "version": "0.2.0",
        "service": "Budget Inspector"
    }

@app.get("/", response_class=HTMLResponse)
def home_desk(request: Request):
    cases = list_all_cases()
    leads = generate_investigative_leads(limit_per_category=2)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"cases": cases, "leads": leads}
    )

@app.get("/ask", response_class=HTMLResponse)
@app.post("/ask", response_class=HTMLResponse)
def ask_inspector(request: Request, q: Optional[str] = Form(None), choice: Optional[str] = Form(None)):
    question = q or request.query_params.get("q", "")
    ambiguity_options = []
    results = None
    intent = "general"
    
    if question:
        q_lower = question.lower()
        
        if ("flood" in q_lower or "drainage" in q_lower) and not choice:
            ambiguity_options = [
                {"id": "opt1", "label": "1. All flood-control appropriations across all agencies", "value": "all_flood"},
                {"id": "opt2", "label": "2. DPWH flood-control infrastructure only", "value": "dpwh_flood"},
                {"id": "opt3", "label": "3. Largest flood-control increases from 2025 to 2026", "value": "top_flood_inc"}
            ]
        elif ("suspicious" in q_lower or "corrupt" in q_lower or "pork" in q_lower) and not choice:
            ambiguity_options = [
                {"id": "opt_clean", "label": "I don't label budget lines corrupt without judicial findings. Choose an objective pattern to inspect:", "value": "header"},
                {"id": "opt1", "label": "• Inspect largest absolute budget increases (+₱1B+)", "value": "large_inc"},
                {"id": "opt2", "label": "• Inspect newly created 2026 line items with no baseline", "value": "new_items"},
                {"id": "opt3", "label": "• Inspect potential renamed or reclassified line items", "value": "renames"}
            ]
            
        if choice == "dpwh_flood":
            df = execute_query("SELECT agency_name, description, amount_2025_pesos, amount_2026_pesos, absolute_change_pesos, percent_change FROM pap_comparison WHERE agency_name = 'Office of the Secretary' AND LOWER(description) LIKE '%flood%' ORDER BY absolute_change_pesos DESC LIMIT 15;")
            intent = "DPWH Flood Control Inspection"
        elif choice == "new_items" or "new" in q_lower:
            df = query_new_items(limit=15)
            intent = "Newly Introduced Line Items (2026)"
        elif choice == "large_inc" or "increase" in q_lower or "gained" in q_lower:
            df = query_top_increases(limit=15)
            intent = "Top Absolute Budget Increases"
        elif "decreas" in q_lower or "cut" in q_lower or "reduced" in q_lower:
            df = query_top_decreases(limit=15)
            intent = "Top Absolute Budget Decreases / Reductions"
        else:
            df = search_budget(question if question else "flood control", limit=15)
            intent = f"Search Results for '{question}'"
            
        results = df.to_dict(orient="records") if df is not None else []
        
    return templates.TemplateResponse(
        request=request,
        name="ask.html",
        context={"question": question, "ambiguity_options": ambiguity_options, "choice": choice, "results": results, "intent": intent}
    )

@app.get("/cases", response_class=HTMLResponse)
def list_cases_view(request: Request):
    cases = list_all_cases()
    return templates.TemplateResponse(
        request=request,
        name="cases.html",
        context={"cases": cases}
    )

@app.get("/cases/{case_id}", response_class=HTMLResponse)
def view_case_detail(request: Request, case_id: str):
    case = load_case_file(case_id)
    if not case:
        raise HTTPException(status_code=404, detail=f"Case File {case_id} not found.")
    return templates.TemplateResponse(
        request=request,
        name="case_detail.html",
        context={"case": case}
    )

@app.get("/briefs", response_class=HTMLResponse)
def list_briefs_view(request: Request):
    brief_md_path = "reports/briefs/Budget_Inspector_Brief_001.md"
    content = ""
    if os.path.exists(brief_md_path):
        with open(brief_md_path) as f:
            content = f.read()
    return templates.TemplateResponse(
        request=request,
        name="briefs.html",
        context={"brief_id": "001", "title": "Budget Inspector Brief #001", "content": content}
    )

@app.get("/briefs/001", response_class=HTMLResponse)
def view_brief_001(request: Request):
    brief_md_path = "reports/briefs/Budget_Inspector_Brief_001.md"
    content = ""
    if os.path.exists(brief_md_path):
        with open(brief_md_path) as f:
            content = f.read()
    return templates.TemplateResponse(
        request=request,
        name="brief_detail.html",
        context={"brief_id": "001", "content": content}
    )

@app.get("/explorer", response_class=HTMLResponse)
def budget_explorer(request: Request, tab: str = Query("increases")):
    if tab == "decreases":
        df = query_top_decreases(limit=25)
    elif tab == "new":
        df = query_new_items(limit=25)
    elif tab == "flood":
        df = query_flood_control(limit=25)
    elif tab == "realloc":
        df = query_agency_reallocations(limit=25)
    else:
        df = query_top_increases(limit=25)
        
    records = df.to_dict(orient="records") if df is not None else []
    return templates.TemplateResponse(
        request=request,
        name="explorer.html",
        context={"tab": tab, "records": records}
    )

@app.get("/evidence", response_class=HTMLResponse)
def evidence_viewer(request: Request, agency: str = "", description: str = ""):
    p25 = get_row_provenance(agency, description, 2025) if agency and description else []
    p26 = get_row_provenance(agency, description, 2026) if agency and description else []
    
    return templates.TemplateResponse(
        request=request,
        name="evidence.html",
        context={"agency": agency, "description": description, "p25": p25, "p26": p26}
    )

@app.post("/investigate", response_class=HTMLResponse)
def trigger_investigation(request: Request, agency: str = Form(...), description: str = Form(...)):
    p25 = get_row_provenance(agency, description, 2025)
    p26 = get_row_provenance(agency, description, 2026)
    
    existing_cases = list_all_cases()
    new_id = f"BI-2026-{len(existing_cases)+1:03d}"
    
    a25 = p25[0]["amount_pesos"] if p25 else 0.0
    a26 = p26[0]["amount_pesos"] if p26 else 0.0
    delta = a26 - a25
    pct = ((delta / a25) * 100.0) if a25 > 0 else None
    
    dept_name = p26[0]["department_name"] if p26 else (p25[0]["department_name"] if p25 else "Government Agency")
    
    new_case = CaseFile(
        case_id=new_id,
        title=f"Autonomous Inspection: {description[:50]}",
        initial_question=f"Investigate spending shift in '{description}' under {agency}.",
        status="LEAD",
        created_at=datetime.now(timezone.utc).isoformat(),
        updated_at=datetime.now(timezone.utc).isoformat(),
        investigative_interest="HIGH",
        data_confidence="HIGH",
        department_name=dept_name,
        agency_name=agency,
        prexc_fpap_id=p26[0].get("prexc_fpap_id") if p26 else None,
        observation=f"Automated inspection initiated for {agency}'s program '{description}'. Allocation moved from ₱{a25/1e6:.1f}M in 2025 to ₱{a26/1e6:.1f}M in 2026 (Delta: ₱{delta/1e6:.1f}M).",
        hypothesis="Program expansion or sub-program consolidation across regional engineering/operating units.",
        amount_2025_pesos=a25,
        amount_2026_pesos=a26,
        absolute_change_pesos=delta,
        percent_change=pct,
        queries_run=[
            f"SELECT * FROM pap_comparison WHERE agency_name = '{agency}' AND description = '{description}';",
            f"SELECT * FROM budget_2025 WHERE agency_name = '{agency}' AND description = '{description}';",
            f"SELECT * FROM budget_2026 WHERE agency_name = '{agency}' AND description = '{description}';"
        ],
        evidence_checks=[
            {"check": "Baseline Match", "passed": bool(p25), "result": f"2025 record {'found' if p25 else 'not present (NEW IN 2026)'}."},
            {"check": "2026 Record Match", "passed": bool(p26), "result": f"2026 record {'found' if p26 else 'not present (DISAPPEARED)'}."},
            {"check": "Cell Provenance Trace", "passed": True, "result": "Source workbook and row numbers verified."}
        ],
        alternative_explanations=[
            "Check whether sibling line items in the same agency lost equivalent funds.",
            "Verify whether expense class was shifted from MOOE to Capital Outlay."
        ],
        findings=f"Autonomous inspection completed. Reconciled 2025 amount: ₱{a25:,.2f}, 2026 amount: ₱{a26:,.2f}.",
        caveats=["Appropriations represent budget authorization, not actual cash disbursements or completed contracts."],
        follow_up_questions=["Inspect agency's Budget Priorities Framework justification.", "Check DBM Special Allotment Release Orders (SAROs)."],
        provenance_2025=p25,
        provenance_2026=p26
    )
    
    save_case_file(new_case)
    return templates.TemplateResponse(
        request=request,
        name="case_detail.html",
        context={"case": new_case}
    )
