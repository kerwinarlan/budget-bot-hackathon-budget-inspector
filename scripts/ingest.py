import sys
from budget_inspector.acquire import acquire_data
from budget_inspector.normalize import run_normalization
from budget_inspector.compare import build_duckdb_database

def main():
    print("=== BUDGET INSPECTOR PIPELINE INGESTION ===")
    
    # Step 1: Acquire source files & write manifest
    manifest_path = acquire_data(force=False)
    print(f"✓ Data Manifest verified at {manifest_path}")
    
    # Step 2: Normalize Excel spreadsheets to Parquet
    p25, p26 = run_normalization()
    print(f"✓ Data Normalized to Parquet: {p25}, {p26}")
    
    # Step 3: Build DuckDB analytical engine
    db_path = build_duckdb_database(p25, p26)
    print(f"✓ DuckDB Database constructed at {db_path}")
    
    print("\n🎉 INGESTION COMPLETE AND VALIDATED!")

if __name__ == "__main__":
    main()
