import os
import pandas as pd
import numpy as np

def normalize_year_data(filepath: str, fiscal_year: int) -> pd.DataFrame:
    print(f"[Normalize] Normalizing FY {fiscal_year} data from {filepath}...")
    
    # Read excel file
    df_raw: pd.DataFrame = pd.read_excel(filepath)
    
    # Track Excel row numbers (1-indexed, header is row 1, data starts at row 2)
    excel_rows = np.arange(2, len(df_raw) + 2)
    df_raw["source_row"] = excel_rows
    df_raw["source_file"] = os.path.basename(filepath)
    df_raw["source_sheet"] = "Sheet 1"
    df_raw["fiscal_year"] = fiscal_year
    
    # Filter out null or zero AMT rows
    valid_amt = df_raw["AMT"].notna() & (df_raw["AMT"] > 0)
    df_valid = df_raw.loc[valid_amt].copy()
    
    # Filter out Grand Total row (where DEPARTMENT or PREXC_LEVEL is NaN and AMT > 1e9)
    is_grand_total = df_valid["DEPARTMENT"].isna() & df_valid["PREXC_LEVEL"].isna()
    df_leaf = df_valid.loc[~is_grand_total].copy()
    
    # Column mapping dictionary
    col_map = {
        "DEPARTMENT": "department_code",
        "UACS_DPT_DSC": "department_name",
        "AGENCY": "agency_code",
        "UACS_AGY_DSC": "agency_name",
        "PREXC_FPAP_ID": "prexc_fpap_id",
        "PREXC_LEVEL": "prexc_level",
        "DSC": "raw_description",
        "OPERUNIT": "operating_unit_code",
        "UACS_OPER_DSC": "operating_unit_name",
        "UACS_REG_ID": "region_id",
        "UACS_OPERDIV_ID": "division_code",
        "UACS_DIV_DSC": "division_name",
        "FUNDCD": "fund_code",
        "UACS_FUNDSUBCAT_DSC": "fund_subcat_name",
        "UACS_EXP_CD": "expense_code",
        "UACS_EXP_DSC": "expense_class",
        "AMT": "amount_thousands"
    }
    
    if fiscal_year == 2025:
        col_map["UACS_SOBJ_CD"] = "object_code"
        col_map["UACS_SOBJ_DSC"] = "object_description"
    else:
        col_map["UACS_OBJ_CD"] = "object_code"
        col_map["UACS_OBJ_DSC"] = "object_description"
        
    df_normalized = pd.DataFrame()
    for raw_col, norm_col in col_map.items():
        if raw_col in df_leaf.columns:
            df_normalized[norm_col] = df_leaf[raw_col].values
        else:
            df_normalized[norm_col] = None
            
    df_normalized["fiscal_year"] = fiscal_year
    df_normalized["source_file"] = df_leaf["source_file"].values
    df_normalized["source_sheet"] = df_leaf["source_sheet"].values
    df_normalized["source_row"] = df_leaf["source_row"].values
    
    # Clean string descriptions
    df_normalized["raw_description"] = df_normalized["raw_description"].fillna("").astype(str)
    df_normalized["description"] = df_normalized["raw_description"].str.strip().str.replace(r"\s+", " ", regex=True)
    df_normalized["department_name"] = df_normalized["department_name"].fillna("Unknown Department").astype(str).str.strip()
    df_normalized["agency_name"] = df_normalized["agency_name"].fillna("Unknown Agency").astype(str).str.strip()
    
    # Numeric conversions
    df_normalized["amount_thousands"] = df_normalized["amount_thousands"].astype(float)
    df_normalized["amount_pesos"] = df_normalized["amount_thousands"] * 1000.0
    
    # Format codes as clean string
    for code_col in ["department_code", "agency_code", "prexc_fpap_id", "operating_unit_code", "region_id", "division_code", "fund_code", "expense_code", "object_code"]:
        if code_col in df_normalized.columns:
            df_normalized[code_col] = df_normalized[code_col].fillna("").astype(str).str.replace(r"\.0$", "", regex=True)

    print(f"[Normalize] FY {fiscal_year}: Normalized {len(df_normalized)} rows. Total sum: ₱{df_normalized['amount_pesos'].sum():,.2f}")
    return df_normalized

def run_normalization():
    os.makedirs("data/normalized", exist_ok=True)
    
    df_2025 = normalize_year_data("raw/2025/GAA-2025.xlsx", 2025)
    df_2026 = normalize_year_data("raw/2026/FY2026-GAA-Byobject.xlsx", 2026)
    
    path_2025 = "data/normalized/budget_2025.parquet"
    path_2026 = "data/normalized/budget_2026.parquet"
    
    df_2025.to_parquet(path_2025, index=False)
    df_2026.to_parquet(path_2026, index=False)
    
    print(f"[Normalize] Saved normalized Parquet files:")
    print(f"  2025: {path_2025} ({len(df_2025)} rows)")
    print(f"  2026: {path_2026} ({len(df_2026)} rows)")
    
    return path_2025, path_2026

if __name__ == "__main__":
    run_normalization()
