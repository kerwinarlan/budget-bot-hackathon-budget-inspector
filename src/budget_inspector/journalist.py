"""
Journalist Desk Companion Agent — Senior Investigative Reporter
Provides newsroom context, reporter feedback, FOI query sheets,
and explains how Budget Inspector transforms the newsroom workflow.
(Style grounded in Kerwin's writing guide github/kerwin-writing.md).
"""

from typing import Dict, Any, List

def generate_journalist_perspective(lead: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates reporter commentary, newsroom utility notes, headline options,
    and official spokesperson questions for a budget lead.
    """
    evidence = lead.get("numerical_evidence", {})
    title = lead.get("title", "Budget Shift").replace("Substantial Budget Expansion: ", "").replace("Newly Created Line Item: ", "")
    agency = evidence.get("agency", "Government Agency")
    dept = evidence.get("department", "Department")
    a25 = float(evidence.get("amount_2025_pesos", 0.0))
    a26 = float(evidence.get("amount_2026_pesos", 0.0))
    delta = float(evidence.get("absolute_change_pesos", 0.0))
    pct = evidence.get("percent_change", "N/A")
    pct_str = f"+{pct:.1f}%" if isinstance(pct, (int, float)) else str(pct)
    
    p25 = lead.get("provenance_2025", [])
    p26 = lead.get("provenance_2026", [])
    row25 = p25[0]["source_row"] if p25 else "N/A"
    row26 = p26[0]["source_row"] if p26 else "N/A"
    
    # Reporter Analysis
    utility_note = (
        f"How Budget Inspector helps me as an investigative reporter: "
        f"When covering {agency}, comparing a ₱{a26/1e9:.2f}B budget against last year's ₱{a25/1e9:.2f}B "
        f"manually across 700,000 Excel rows takes days. Budget Inspector isolated this +₱{delta/1e9:.2f}B ({pct_str}) variance in seconds "
        f"and gave me the exact cell coordinates (2025 Row {row25} vs 2026 Row {row26}). "
        f"That means I can file my FOI request and ask DBM for the exact Work and Financial Plan before deadline."
    )
    
    headline_policy = f"FY 2026 Budget Inspection: {agency}'s {title} Surges by +₱{delta/1e9:.2f} Billion ({pct_str})"
    headline_citizen = f"Where the Money Moves: Inside the ₱{a26/1e9:.2f}B Allocation for {title}"
    
    lede = (
        f"MANILA — Behind headline department totals, the enacted FY 2026 national budget authorizes a major "
        f"₱{a26/1e9:.2f} Billion allocation for {title} under {agency}, marking a +₱{delta/1e9:.2f} Billion ({pct_str}) "
        f"shift from FY 2025. Data reconciled by Budget Inspector shows the entire variance is concentrated in specific "
        f"operational line items."
    )
    
    reporter_questions = [
        f"To {agency} Budget Officer: What specific physical targets or expansion plans justify the +₱{delta/1e9:.2f}B increase in 2026?",
        f"To DBM Technical Service: Did this line item absorb previous sub-program allocations or off-budget accounts?",
        f"To Oversight Committee: What is the historical obligation rate for this line item in recent COA audit reports?"
    ]
    
    needs_next = [
        "Special Allotment Release Orders (SARO) for milestone releases",
        "Agency Quarterly Financial Accountability Reports (FAR No. 1)",
        "COA Annual Audit Report (AAR) historical absorption rate"
    ]
    
    return {
        "reporter_name": "Jaemark / Senior Fiscal Reporter",
        "newsroom_desk": "Budget Inspector Investigative Desk",
        "utility_note": utility_note,
        "headline_policy": headline_policy,
        "headline_citizen": headline_citizen,
        "newsroom_lede": lede,
        "reporter_questions": reporter_questions,
        "what_reporter_needs_next": needs_next
    }
