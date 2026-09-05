from typing import Dict, Any, List
import pandas as pd
from budget_inspector.queries import execute_query

def get_row_provenance(agency_name: str, description: str, year: int) -> List[Dict[str, Any]]:
    """
    Retrieves exact source spreadsheet rows, file, sheet, and UACS details for a given item and year.
    """
    table_name = f"budget_{year}"
    sql = f"""
    SELECT 
        fiscal_year,
        department_name,
        agency_name,
        prexc_fpap_id,
        raw_description,
        expense_class,
        object_code,
        object_description,
        amount_thousands,
        amount_pesos,
        source_file,
        source_sheet,
        source_row
    FROM {table_name}
    WHERE agency_name = ? AND description = ?
    ORDER BY source_row ASC
    LIMIT 20
    """
    df = execute_query(sql, [agency_name, description])
    
    provenance_list = []
    for _, row in df.iterrows():
        provenance_list.append({
            "fiscal_year": int(row["fiscal_year"]),  # type: ignore
            "department_name": str(row["department_name"]),
            "agency_name": str(row["agency_name"]),
            "prexc_fpap_id": str(row["prexc_fpap_id"]),
            "raw_description": str(row["raw_description"]),
            "expense_class": str(row["expense_class"]),
            "object_code": str(row["object_code"]),
            "object_description": str(row["object_description"]),
            "amount_pesos": float(row["amount_pesos"]),  # type: ignore
            "source_file": str(row["source_file"]),
            "source_sheet": str(row["source_sheet"]),
            "source_row": int(row["source_row"])  # type: ignore
        })
    return provenance_list

def build_provenance_citation(finding: Dict[str, Any]) -> str:
    """Formats a human-readable citation block for a finding."""
    citation_lines = []
    if "provenance_2025" in finding and finding["provenance_2025"]:
        p25 = finding["provenance_2025"][0]
        citation_lines.append(f"**2025 Source**: File `{p25['source_file']}`, Sheet `{p25['source_sheet']}`, Row `{p25['source_row']}` (₱{p25['amount_pesos']:,.2f})")
    if "provenance_2026" in finding and finding["provenance_2026"]:
        p26 = finding["provenance_2026"][0]
        citation_lines.append(f"**2026 Source**: File `{p26['source_file']}`, Sheet `{p26['source_sheet']}`, Row `{p26['source_row']}` (₱{p26['amount_pesos']:,.2f})")
    return "\n".join(citation_lines)
