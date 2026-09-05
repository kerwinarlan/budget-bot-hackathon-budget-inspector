import json
import os
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional, Tuple
from pydantic import BaseModel, Field

CASES_DIR = "cases"

class CaseFile(BaseModel):
    case_id: str
    title: str
    initial_question: str
    status: str  # OPEN, LEAD, NEEDS_FOLLOW_UP, EXPLAINED_BY_RECLASSIFICATION, CLOSED
    created_at: str
    updated_at: str
    
    investigative_interest: str  # HIGH, MEDIUM, LOW
    data_confidence: str        # HIGH, MEDIUM, LOW
    
    department_name: str
    agency_name: str
    prexc_fpap_id: Optional[str] = None
    
    observation: str
    hypothesis: str
    
    amount_2025_pesos: float
    amount_2026_pesos: float
    absolute_change_pesos: float
    percent_change: Optional[float] = None
    
    queries_run: List[str] = Field(default_factory=list)
    evidence_checks: List[Dict[str, Any]] = Field(default_factory=list)
    alternative_explanations: List[str] = Field(default_factory=list)
    findings: str
    caveats: List[str] = Field(default_factory=list)
    follow_up_questions: List[str] = Field(default_factory=list)
    source_receipts: List[str] = Field(default_factory=list)
    provenance_2025: List[Dict[str, Any]] = Field(default_factory=list)
    provenance_2026: List[Dict[str, Any]] = Field(default_factory=list)

def ensure_cases_dir():
    os.makedirs(CASES_DIR, exist_ok=True)

def save_case_file(case: CaseFile) -> Tuple[str, str]:
    ensure_cases_dir()
    json_path = os.path.join(CASES_DIR, f"{case.case_id}.json")
    md_path = os.path.join(CASES_DIR, f"{case.case_id}.md")
    
    with open(json_path, "w") as f:
        f.write(case.model_dump_json(indent=2))
        
    md_content = format_case_markdown(case)
    with open(md_path, "w") as f:
        f.write(md_content)
        
    print(f"[Cases] Saved Case File {case.case_id} to {json_path} and {md_path}")
    return json_path, md_path

def load_case_file(case_id: str) -> Optional[CaseFile]:
    json_path = os.path.join(CASES_DIR, f"{case_id}.json")
    if not os.path.exists(json_path):
        return None
    with open(json_path) as f:
        data = json.load(f)
    return CaseFile(**data)

def list_all_cases() -> List[CaseFile]:
    ensure_cases_dir()
    cases = []
    for fn in sorted(os.listdir(CASES_DIR)):
        if fn.endswith(".json") and fn.startswith("BI-"):
            path = os.path.join(CASES_DIR, fn)
            try:
                with open(path) as f:
                    cases.append(CaseFile(**json.load(f)))
            except Exception as e:
                print(f"Error loading {path}: {e}")
    return cases

def format_case_markdown(case: CaseFile) -> str:
    pct_str = f"+{case.percent_change:.1f}%" if case.percent_change is not None else "NEW IN 2026"
    
    lines = [
        f"# CASE FILE {case.case_id}: {case.title}",
        "",
        f"**Status**: `{case.status}` | **Investigative Interest**: `{case.investigative_interest}` | **Data Confidence**: `{case.data_confidence}`",
        f"**Department**: {case.department_name} | **Agency**: {case.agency_name}",
        f"**Created**: {case.created_at} | **Updated**: {case.updated_at}",
        "",
        "---",
        "",
        "## 1. Initial Question & Observation",
        f"**Question**: {case.initial_question}",
        "",
        f"**Observation**: {case.observation}",
        "",
        "## 2. Numerical Summary",
        f"- **FY 2025 Amount**: ₱{case.amount_2025_pesos:,.2f} (₱{case.amount_2025_pesos/1e9:.2f}B)",
        f"- **FY 2026 Amount**: ₱{case.amount_2026_pesos:,.2f} (₱{case.amount_2026_pesos/1e9:.2f}B)",
        f"- **Absolute Delta**: ₱{case.absolute_change_pesos:,.2f} ({pct_str})",
        "",
        "## 3. Inspector's Notebook & Audit Checks",
    ]
    
    for check in case.evidence_checks:
        status_icon = "✓" if check.get("passed", True) else "⚠"
        lines.append(f"- {status_icon} **{check.get('check')}**: {check.get('result')}")
        
    lines.extend([
        "",
        "## 4. Alternative Explanations Evaluated",
    ])
    for alt in case.alternative_explanations:
        lines.append(f"- 💡 {alt}")
        
    lines.extend([
        "",
        "## 5. Assessment & Findings",
        case.findings,
        "",
        "## 6. Provenance & Citations",
    ])
    
    if case.provenance_2025:
        p25 = case.provenance_2025[0]
        lines.append(f"- **FY 2025 Source**: File `{p25.get('source_file')}`, Sheet `{p25.get('source_sheet')}`, Row `{p25.get('source_row')}` (₱{p25.get('amount_pesos', 0.0):,.2f})")
    else:
        lines.append("- **FY 2025 Source**: None (`NEW_IN_2026`)")
        
    if case.provenance_2026:
        p26 = case.provenance_2026[0]
        lines.append(f"- **FY 2026 Source**: File `{p26.get('source_file')}`, Sheet `{p26.get('source_sheet')}`, Row `{p26.get('source_row')}` (₱{p26.get('amount_pesos', 0.0):,.2f})")
    else:
        lines.append("- **FY 2026 Source**: None (`DISAPPEARED`)")
        
    lines.extend([
        "",
        "## 7. Analytical Caveats",
    ])
    for c in case.caveats:
        lines.append(f"- ⚠️ {c}")
        
    lines.extend([
        "",
        "## 8. Recommended Follow-Up Questions",
    ])
    for q in case.follow_up_questions:
        lines.append(f"- 🔍 {q}")
        
    return "\n".join(lines)
