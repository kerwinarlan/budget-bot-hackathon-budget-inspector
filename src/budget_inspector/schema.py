from typing import Optional, List, Any, Dict
from pydantic import BaseModel, Field

class NormalizedBudgetRow(BaseModel):
    fiscal_year: int
    department_code: Optional[str] = None
    department_name: str
    agency_code: Optional[str] = None
    agency_name: str
    prexc_fpap_id: Optional[str] = None
    prexc_level: Optional[float] = None
    description: str
    raw_description: str
    operating_unit_code: Optional[str] = None
    operating_unit_name: Optional[str] = None
    region_id: Optional[str] = None
    division_code: Optional[str] = None
    division_name: Optional[str] = None
    fund_code: Optional[str] = None
    fund_subcat_name: Optional[str] = None
    expense_code: Optional[str] = None
    expense_class: Optional[str] = None
    object_code: Optional[str] = None
    object_description: Optional[str] = None
    amount_thousands: float
    amount_pesos: float
    
    # Provenance
    source_file: str
    source_sheet: str
    source_row: int
    
class ComparisonRow(BaseModel):
    match_key: str
    match_type: str  # EXACT, STRUCTURED_PAP, FUZZY_RENAME, NEW_IN_2026, DISAPPEARED
    department_name: str
    agency_name: str
    prexc_fpap_id: Optional[str] = None
    description_2025: Optional[str] = None
    description_2026: Optional[str] = None
    expense_class: Optional[str] = None
    object_description: Optional[str] = None
    amount_2025_pesos: float = 0.0
    amount_2026_pesos: float = 0.0
    absolute_change_pesos: float = 0.0
    percent_change: Optional[float] = None
    change_status: str  # INCREASE, DECREASE, UNCHANGED, NEW_IN_2026, DISAPPEARED
    
    provenance_2025: Optional[Dict[str, Any]] = None
    provenance_2026: Optional[Dict[str, Any]] = None

class ResearchReceipt(BaseModel):
    lead_id: str
    title: str
    category: str
    confidence: str  # HIGH, MEDIUM, LOW
    observation: str
    numerical_evidence: Dict[str, Any]
    source_years: List[int]
    query_used: str
    provenance: List[Dict[str, Any]]
    caveats: List[str]
    next_steps: List[str]
