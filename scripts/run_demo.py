from budget_inspector.queries import query_top_increases, query_new_items, query_flood_control
from budget_inspector.anomalies import generate_investigative_leads
from budget_inspector.reporting import save_research_receipts, format_lead_markdown

def run_demo():
    print("==========================================================")
    print("       BUDGET INSPECTOR — DEMO INVESTIGATION RUN        ")
    print("==========================================================")
    
    # 1. Top Increases Demo
    print("\n--- 1. TOP ABSOLUTE BUDGET INCREASES (2025 → 2026) ---")
    df_inc = query_top_increases(limit=5)
    for idx, row in df_inc.iterrows():
        a25 = float(row["amount_2025_pesos"])  # type: ignore
        a26 = float(row["amount_2026_pesos"])  # type: ignore
        delta = float(row["absolute_change_pesos"])  # type: ignore
        pct_val = row["percent_change"]
        pct = float(pct_val) if pct_val is not None else 0.0  # type: ignore
        print(f"[{int(idx)+1}] {row['agency_name']} | {str(row['description'])[:50]}")  # type: ignore
        print(f"    2025: ₱{a25/1e9:.2f}B -> 2026: ₱{a26/1e9:.2f}B | Delta: +₱{delta/1e9:.2f}B (+{pct:.1f}%)\n")

    # 2. New Items Demo
    print("--- 2. TOP NEW APPROPRIATIONS INTRODUCED IN FY 2026 ---")
    df_new = query_new_items(limit=5)
    for idx, row in df_new.iterrows():
        a26 = float(row["amount_2026_pesos"])  # type: ignore
        print(f"[{int(idx)+1}] {row['agency_name']} | {str(row['description'])[:50]}")  # type: ignore
        print(f"    2026 Amount: ₱{a26/1e9:.2f} Billion (NEW IN 2026)\n")

    # 3. Flood Control Demo
    print("--- 3. FLOOD CONTROL & DRAINAGE ALLOCATION SHIFTS ---")
    df_fc = query_flood_control(limit=5)
    for idx, row in df_fc.iterrows():
        a25 = float(row["amount_2025_pesos"])  # type: ignore
        a26 = float(row["amount_2026_pesos"])  # type: ignore
        delta = float(row["absolute_change_pesos"])  # type: ignore
        print(f"[{int(idx)+1}] {row['agency_name']} | {str(row['description'])[:50]}")  # type: ignore
        print(f"    2025: ₱{a25/1e9:.2f}B -> 2026: ₱{a26/1e9:.2f}B | Delta: {'+' if delta>=0 else ''}₱{delta/1e9:.2f}B\n")

    # 4. Generate Leads and Research Receipts
    print("--- 4. GENERATING INVESTIGATIVE LEADS & RESEARCH RECEIPTS ---")
    leads = generate_investigative_leads(limit_per_category=2)
    receipts = save_research_receipts(leads)
    
    print(f"\nSaved {len(receipts)} machine-readable research receipts under queries/investigations/")
    print("\nSample Lead Markdown Output:\n")
    print(format_lead_markdown(leads[0]))

if __name__ == "__main__":
    run_demo()
