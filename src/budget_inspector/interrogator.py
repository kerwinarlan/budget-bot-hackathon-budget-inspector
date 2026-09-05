import os
import subprocess
from typing import Dict, Any, List, Optional
from budget_inspector.queries import execute_query
from budget_inspector.writer import write_agency_memorandum

OUTPUT_DIR = "reports/interrogative"

def interrogate_agency(agency_keyword: str) -> Dict[str, Any]:
    """
    Interrogates line items for a specific target agency (e.g. 'BuCor', 'DepEd', 'PhilHealth', 'DPWH')
    and produces an official Agency Audit Memorandum + FOI Request Draft in Kerwin's style.
    """
    print(f"[Interrogator] Initiating targeted interrogation for agency keyword: '{agency_keyword}'...")
    
    sql = """
    SELECT department_name, agency_name, prexc_fpap_id, description, expense_class, amount_2025_pesos, amount_2026_pesos, absolute_change_pesos, percent_change
    FROM pap_comparison
    WHERE LOWER(agency_name) LIKE ? OR LOWER(department_name) LIKE ?
    ORDER BY absolute_change_pesos DESC
    LIMIT 25
    """
    pattern = f"%{agency_keyword.lower()}%"
    df = execute_query(sql, [pattern, pattern])
    
    if df.empty:
        df = execute_query("SELECT department_name, agency_name, prexc_fpap_id, description, expense_class, amount_2025_pesos, amount_2026_pesos, absolute_change_pesos, percent_change FROM pap_comparison ORDER BY absolute_change_pesos DESC LIMIT 15;")
        
    records = df.to_dict(orient="records")
    agency_name = records[0]["agency_name"] if records else "Government Agency"
    dept_name = records[0]["department_name"] if records else "Department"
    
    memo_md = write_agency_memorandum(agency_name, dept_name, records)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clean_agency_id = agency_keyword.lower().replace(" ", "_").replace("/", "_")
    
    md_path = os.path.join(OUTPUT_DIR, f"Memorandum_{clean_agency_id}.md")
    html_path = os.path.join(OUTPUT_DIR, f"Memorandum_{clean_agency_id}.html")
    pdf_path = os.path.join(OUTPUT_DIR, f"Memorandum_{clean_agency_id}.pdf")
    
    with open(md_path, "w") as f:
        f.write(memo_md)
        
    body_html = memo_md.replace("# ", "<h1>").replace("## ", "<h2>").replace("### ", "<h3>").replace("\n", "<br>")
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Agency Audit Memorandum — {agency_name}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; max-width: 850px; margin: 2rem auto; padding: 0 1.5rem; color: #0f172a; background: #ffffff; }}
    .memo-header {{ background: #0f172a; color: #ffffff; padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem; }}
    .memo-header h1 {{ font-size: 1.5rem; color: #ffffff; margin: 0; }}
    .memo-header p {{ font-size: 0.85rem; color: #94a3b8; margin-top: 0.25rem; }}
    h2 {{ color: #1e40af; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.3rem; margin-top: 1.75rem; font-size: 1.2rem; }}
    h3 {{ color: #0f172a; margin-top: 1.25rem; font-size: 1.05rem; }}
    code {{ background: #f1f5f9; padding: 0.15rem 0.35rem; border-radius: 4px; font-family: monospace; font-size: 0.85rem; }}
  </style>
</head>
<body>
  <div class="memo-header">
    <h1>OFFICIAL AGENCY AUDIT MEMORANDUM</h1>
    <p>Target: {agency_name} ({dept_name}) | Prepared by Budget Inspector Desk (Team Vibe Coders PH)</p>
  </div>
  <div>
    {body_html}
  </div>
</body>
</html>
"""
    with open(html_path, "w") as f:
        f.write(html_content)
        
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists(chrome_path):
        cmd = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            f"--print-to-pdf={pdf_path}",
            html_path
        ]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[Interrogator] Generated PDF Audit Memo at {pdf_path}")
        except Exception as e:
            print(f"Warning: Chrome PDF generation error ({e})")
            
    print(f"[Interrogator] Completed interrogation for {agency_name}: MD ({md_path}), HTML ({html_path}), PDF ({pdf_path})")
    
    return {
        "agency_name": agency_name,
        "department_name": dept_name,
        "record_count": len(records),
        "records": records,
        "md_path": md_path,
        "html_path": html_path,
        "pdf_path": pdf_path,
        "memo_content": memo_md
    }

if __name__ == "__main__":
    interrogate_agency("bucor")
