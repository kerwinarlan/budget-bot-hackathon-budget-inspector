import json
import os
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import duckdb

from budget_inspector.queries import (
    query_top_increases,
    query_new_items,
    query_flood_control,
    query_agency_reallocations,
    search_budget
)
from budget_inspector.anomalies import generate_investigative_leads
from budget_inspector.reporting import save_research_receipts, format_lead_markdown

app = typer.Typer(help="Budget Inspector — Evidence-first Philippine budget analysis CLI.")
console = Console()

DB_PATH = "data/budget.duckdb"

@app.command("status")
def status():
    """Displays database status, ingested row counts, and dataset manifest."""
    console.print(Panel("[bold blue]Budget Inspector System Status[/bold blue]", expand=False))
    
    if not os.path.exists(DB_PATH):
        console.print("[red]Database not found! Run 'python scripts/ingest.py' first.[/red]")
        return
        
    conn = duckdb.connect(DB_PATH, read_only=True)
    tables = conn.execute("SHOW TABLES").fetchall()
    
    table = Table(title="DuckDB Database Inventory")
    table.add_column("Table Name", style="cyan")
    table.add_column("Row Count", style="magenta", justify="right")
    
    for t in tables:
        tname = t[0]
        res = conn.execute(f"SELECT COUNT(*) FROM {tname}").fetchone()
        cnt = res[0] if res else 0
        table.add_row(tname, f"{cnt:,}")
        
    conn.close()
    console.print(table)
    
    manifest_path = "data/manifests/manifest.json"
    if os.path.exists(manifest_path):
        with open(manifest_path) as f:
            m = json.load(f)
        console.print("\n[bold green]Ingested Source Manifests:[/bold green]")
        for src in m.get("sources", []):
            console.print(f"  • FY {src['fiscal_year']}: {src['filename']} ({src['file_size_bytes']/(1024*1024):.1f} MB) | SHA-256: {src['sha256'][:12]}...")

@app.command("top-increases")
def top_increases(limit: int = typer.Option(10, help="Number of items to return")):
    """Displays line items with the largest absolute peso increase from 2025 to 2026."""
    df = query_top_increases(limit=limit)
    
    table = Table(title=f"Top {limit} Budget Increases (2025 → 2026)")
    table.add_column("Agency", style="cyan")
    table.add_column("Description", style="white")
    table.add_column("2025 (PHP)", style="yellow", justify="right")
    table.add_column("2026 (PHP)", style="green", justify="right")
    table.add_column("Delta (PHP)", style="bold magenta", justify="right")
    table.add_column("Growth", style="bold blue", justify="right")
    
    for _, row in df.iterrows():
        a25 = float(row["amount_2025_pesos"])  # type: ignore
        a26 = float(row["amount_2026_pesos"])  # type: ignore
        delta = float(row["absolute_change_pesos"])  # type: ignore
        pct_val = row["percent_change"]
        pct = float(pct_val) if pct_val is not None else 0.0  # type: ignore
        
        table.add_row(
            str(row["agency_name"])[:25],
            str(row["description"])[:45],
            f"₱{a25/1e6:,.1f}M",
            f"₱{a26/1e6:,.1f}M",
            f"+₱{delta/1e6:,.1f}M",
            f"+{pct:.1f}%"
        )
    console.print(table)

@app.command("new-items")
def new_items(limit: int = typer.Option(10, help="Number of items to return")):
    """Displays largest newly introduced line items in FY 2026."""
    df = query_new_items(limit=limit)
    
    table = Table(title=f"Top {limit} New Line Items in 2026")
    table.add_column("Agency", style="cyan")
    table.add_column("Description", style="white")
    table.add_column("Class", style="yellow")
    table.add_column("2026 Amount (PHP)", style="bold green", justify="right")
    
    for _, row in df.iterrows():
        a26 = float(row["amount_2026_pesos"])  # type: ignore
        table.add_row(
            str(row["agency_name"])[:25],
            str(row["description"])[:50],
            str(row["expense_class"])[:20],
            f"₱{a26/1e6:,.1f}M"
        )
    console.print(table)

@app.command("search")
def search(query_text: str = typer.Argument(..., help="Keyword or phrase to search")):
    """Searches budget line items across 2025 and 2026."""
    df = search_budget(query_text, limit=15)
    
    table = Table(title=f"Budget Search Results for '{query_text}'")
    table.add_column("Agency", style="cyan")
    table.add_column("Description", style="white")
    table.add_column("2025 (PHP)", style="yellow", justify="right")
    table.add_column("2026 (PHP)", style="green", justify="right")
    table.add_column("Delta (PHP)", style="bold magenta", justify="right")
    
    for _, row in df.iterrows():
        a25 = float(row["amount_2025_pesos"])  # type: ignore
        a26 = float(row["amount_2026_pesos"])  # type: ignore
        delta = float(row["absolute_change_pesos"])  # type: ignore
        table.add_row(
            str(row["agency_name"])[:25],
            str(row["description"])[:45],
            f"₱{a25/1e6:,.1f}M",
            f"₱{a26/1e6:,.1f}M",
            f"{'+' if delta >=0 else ''}₱{delta/1e6:,.1f}M"
        )
    console.print(table)

@app.command("leads")
def leads():
    """Generates automated heuristic investigative leads and outputs research receipts."""
    lead_list = generate_investigative_leads(limit_per_category=3)
    save_research_receipts(lead_list)
    
    console.print(f"\n[bold green]Generated {len(lead_list)} High-Signal Investigative Leads:[/bold green]\n")
    for lead in lead_list:
        console.print(format_lead_markdown(lead))

@app.command("ask")
def ask(question: str = typer.Argument(..., help="Natural language question")):
    """Translates a natural language query into deterministic SQL inspection."""
    console.print(f"[bold blue]Question:[/bold blue] {question}")
    q_lower = question.lower()
    
    if "flood" in q_lower or "drainage" in q_lower:
        console.print("[yellow]Routing intent -> Flood Control Analysis[/yellow]\n")
        df = query_flood_control(limit=10)
    elif "new" in q_lower:
        console.print("[yellow]Routing intent -> New Items Analysis[/yellow]\n")
        df = query_new_items(limit=10)
    elif "reallocat" in q_lower or "shift" in q_lower:
        console.print("[yellow]Routing intent -> Agency Reallocation Analysis[/yellow]\n")
        df = query_agency_reallocations(limit=10)
    else:
        console.print("[yellow]Routing intent -> Top Budget Increases[/yellow]\n")
        df = query_top_increases(limit=10)
        
    console.print(df.head(10))

if __name__ == "__main__":
    app()
