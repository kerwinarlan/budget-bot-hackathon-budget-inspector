import json
import os
from typing import List, Dict, Any

def save_research_receipts(leads: List[Dict[str, Any]], output_dir: str = "queries/investigations") -> List[str]:
    os.makedirs(output_dir, exist_ok=True)
    receipt_paths = []
    
    for lead in leads:
        lead_id = lead.get("lead_id", "LEAD-000")
        filename = f"receipt_{lead_id.lower().replace('-', '_')}.json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, "w") as f:
            json.dump(lead, f, indent=2)
            
        receipt_paths.append(filepath)
        
    print(f"[Reporting] Saved {len(receipt_paths)} research receipts to {output_dir}/")
    return receipt_paths

def format_lead_markdown(lead: Dict[str, Any]) -> str:
    md_lines = [
        f"### {lead.get('title', 'Investigative Lead')}",
        f"**Lead ID**: `{lead.get('lead_id')}` | **Category**: `{lead.get('category')}` | **Confidence**: `{lead.get('confidence')}`",
        "",
        f"**Observation**: {lead.get('observation')}",
        "",
        "#### Numerical Evidence:",
        "```json",
        json.dumps(lead.get("numerical_evidence", {}), indent=2),
        "```",
        "",
        "#### Source Provenance:",
    ]
    
    p25 = lead.get("provenance_2025", [])
    if p25:
        p = p25[0]
        md_lines.append(f"- **FY 2025**: File `{p['source_file']}`, Sheet `{p['source_sheet']}`, Row `{p['source_row']}` (₱{p['amount_pesos']:,.2f})")
    else:
        md_lines.append("- **FY 2025**: No exact baseline match (`NEW_IN_2026`)")
        
    p26 = lead.get("provenance_2026", [])
    if p26:
        p = p26[0]
        md_lines.append(f"- **FY 2026**: File `{p['source_file']}`, Sheet `{p['source_sheet']}`, Row `{p['source_row']}` (₱{p['amount_pesos']:,.2f})")
    else:
        md_lines.append("- **FY 2026**: No match (`DISAPPEARED`)")
        
    md_lines.extend([
        "",
        "#### Caveats & Analytical Context:",
    ])
    for c in lead.get("caveats", []):
        md_lines.append(f"- ⚠️ {c}")
        
    md_lines.extend([
        "",
        "#### Recommended Next Questions:",
    ])
    for n in lead.get("next_steps", []):
        md_lines.append(f"- 🔍 {n}")
        
    md_lines.append("\n---\n")
    return "\n".join(md_lines)
