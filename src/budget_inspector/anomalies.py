from typing import List, Dict, Any
from budget_inspector.queries import (
    query_top_increases,
    query_new_items,
    query_flood_control,
)
from budget_inspector.provenance import get_row_provenance

def generate_investigative_leads(limit_per_category: int = 3) -> List[Dict[str, Any]]:
    print("[Anomalies] Running heuristic lead generator across 2025↔2026 budget matrix...")
    leads: List[Dict[str, Any]] = []
    
    # 1. Category: LARGE_INCREASE
    df_inc = query_top_increases(limit=limit_per_category, min_2025_pesos=100_000_000.0)
    for _, row in df_inc.iterrows():
        a25 = float(row["amount_2025_pesos"]) if row["amount_2025_pesos"] is not None else 0.0  # type: ignore
        a26 = float(row["amount_2026_pesos"]) if row["amount_2026_pesos"] is not None else 0.0  # type: ignore
        delta = float(row["absolute_change_pesos"]) if row["absolute_change_pesos"] is not None else 0.0  # type: ignore
        pct_val = row["percent_change"]
        pct = float(pct_val) if pct_val is not None else 0.0  # type: ignore
        
        agency = str(row["agency_name"])
        desc = str(row["description"])
        
        p25 = get_row_provenance(agency, desc, 2025)
        p26 = get_row_provenance(agency, desc, 2026)
        
        leads.append({
            "lead_id": f"LEAD-INC-{len(leads)+1:03d}",
            "title": f"Substantial Budget Expansion: {desc[:60]}...",
            "category": "LARGE_INCREASE",
            "confidence": "HIGH",
            "observation": f"{agency}'s program '{desc}' increased by ₱{delta/1e9:.2f} Billion (+{pct:.1f}%), expanding from ₱{a25/1e9:.2f}B in 2025 to ₱{a26/1e9:.2f}B in 2026.",
            "numerical_evidence": {
                "department": str(row["department_name"]),
                "agency": agency,
                "prexc_fpap_id": str(row["prexc_fpap_id"]),
                "expense_class": str(row["expense_class"]),
                "amount_2025_pesos": a25,
                "amount_2026_pesos": a26,
                "absolute_change_pesos": delta,
                "percent_change": round(pct, 2)
            },
            "source_years": [2025, 2026],
            "query_used": "pap_comparison ORDER BY absolute_change_pesos DESC",
            "provenance_2025": p25,
            "provenance_2026": p26,
            "caveats": [
                "An appropriation increase reflects legislative authorization, not actual obligation or disbursement.",
                "Verify whether scope expansion or sub-item consolidation accounts for the growth."
            ],
            "next_steps": [
                "Inspect agency budget justification documents for scope changes.",
                "Cross-reference with DBM Special Allotment Release Orders (SARO) when available."
            ]
        })

    # 2. Category: NEW_ITEM
    df_new = query_new_items(limit=limit_per_category, min_2026_pesos=500_000_000.0)
    for _, row in df_new.iterrows():
        a26 = float(row["amount_2026_pesos"]) if row["amount_2026_pesos"] is not None else 0.0  # type: ignore
        agency = str(row["agency_name"])
        desc = str(row["description"])
        p26 = get_row_provenance(agency, desc, 2026)
        
        leads.append({
            "lead_id": f"LEAD-NEW-{len(leads)+1:03d}",
            "title": f"Newly Created Line Item: {desc[:60]}...",
            "category": "NEW_ITEM",
            "confidence": "HIGH",
            "observation": f"A new appropriation line item titled '{desc}' under {agency} appears in FY 2026 with ₱{a26/1e9:.2f} Billion, having no exact match in FY 2025.",
            "numerical_evidence": {
                "department": str(row["department_name"]),
                "agency": agency,
                "prexc_fpap_id": str(row["prexc_fpap_id"]),
                "expense_class": str(row["expense_class"]),
                "amount_2025_pesos": 0.0,
                "amount_2026_pesos": a26,
                "absolute_change_pesos": a26,
                "percent_change": "NEW_IN_2026"
            },
            "source_years": [2026],
            "query_used": "pap_comparison WHERE change_status = 'NEW_IN_2026' ORDER BY amount_2026_pesos DESC",
            "provenance_2025": [],
            "provenance_2026": p26,
            "caveats": [
                "The line item may be a genuinely new national program or a restructured/renamed legacy item.",
                "Check for semantic equivalents under different wording in FY 2025."
            ],
            "next_steps": [
                "Perform fuzzy search across 2025 agency line items for potential renames.",
                "Review DBM Budget Priorities Framework for policy mandate changes."
            ]
        })

    # 3. Category: FLOOD_CONTROL_CHANGE
    df_fc = query_flood_control(limit=limit_per_category)
    for _, row in df_fc.iterrows():
        a25 = float(row["amount_2025_pesos"]) if row["amount_2025_pesos"] is not None else 0.0  # type: ignore
        a26 = float(row["amount_2026_pesos"]) if row["amount_2026_pesos"] is not None else 0.0  # type: ignore
        delta = float(row["absolute_change_pesos"]) if row["absolute_change_pesos"] is not None else 0.0  # type: ignore
        pct_val = row["percent_change"]
        pct = float(pct_val) if pct_val is not None else 0.0  # type: ignore
        
        agency = str(row["agency_name"])
        desc = str(row["description"])
        
        p25 = get_row_provenance(agency, desc, 2025)
        p26 = get_row_provenance(agency, desc, 2026)
        
        leads.append({
            "lead_id": f"LEAD-FC-{len(leads)+1:03d}",
            "title": f"Flood Mitigation Allocation Shift: {desc[:60]}...",
            "category": "FLOOD_CONTROL_CHANGE",
            "confidence": "HIGH",
            "observation": f"Flood control / drainage entry '{desc}' under {agency} changed by ₱{delta/1e9:.2f} Billion (from ₱{a25/1e9:.2f}B in 2025 to ₱{a26/1e9:.2f}B in 2026).",
            "numerical_evidence": {
                "department": str(row["department_name"]),
                "agency": agency,
                "expense_class": str(row["expense_class"]),
                "amount_2025_pesos": a25,
                "amount_2026_pesos": a26,
                "absolute_change_pesos": delta,
                "percent_change": round(pct, 2)
            },
            "source_years": [2025, 2026],
            "query_used": "pap_comparison WHERE description SIMILAR TO flood/drainage terms",
            "provenance_2025": p25,
            "provenance_2026": p26,
            "caveats": [
                "Flood control appropriations include river basin dredging, seawalls, pumping stations, and local drainage.",
                "Appropriation does not guarantee project completion or contractor award."
            ],
            "next_steps": [
                "Map geographical distribution across DPWH Engineering District Offices.",
                "Check regional allocations against typhoon risk vulnerability data."
            ]
        })

    print(f"[Anomalies] Generated {len(leads)} high-signal investigative leads.")
    return leads
