from typing import List, Dict, Any, Optional
import pandas as pd
from rapidfuzz import fuzz, process

def build_pap_aggregated_comparison(df_2025: pd.DataFrame, df_2026: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates budget rows by Program/Activity/Project (PAP) level:
    Group by: department_name, agency_name, prexc_fpap_id, description, expense_class
    """
    print("[Entity Resolution] Aggregating FY 2025 & FY 2026 rows at PAP level...")
    
    group_cols = ["department_name", "agency_name", "prexc_fpap_id", "description", "expense_class"]
    
    agg_2025 = df_2025.groupby(group_cols, dropna=False).agg(
        amount_2025_pesos=("amount_pesos", "sum"),
        count_2025=("amount_pesos", "count"),
        source_rows_2025=("source_row", lambda x: list(x)[:10])
    ).reset_index()
    
    agg_2026 = df_2026.groupby(group_cols, dropna=False).agg(
        amount_2026_pesos=("amount_pesos", "sum"),
        count_2026=("amount_pesos", "count"),
        source_rows_2026=("source_row", lambda x: list(x)[:10])
    ).reset_index()
    
    df_merged = pd.merge(
        agg_2025,
        agg_2026,
        on=group_cols,
        how="outer"
    )
    
    df_merged["amount_2025_pesos"] = df_merged["amount_2025_pesos"].fillna(0.0)
    df_merged["amount_2026_pesos"] = df_merged["amount_2026_pesos"].fillna(0.0)
    df_merged["absolute_change_pesos"] = df_merged["amount_2026_pesos"] - df_merged["amount_2025_pesos"]
    
    def calc_pct(row) -> Optional[float]:
        a25 = float(row["amount_2025_pesos"])
        a26 = float(row["amount_2026_pesos"])
        if a25 == 0.0 and a26 > 0.0:
            return None  # NEW ITEM
        if a25 > 0.0 and a26 == 0.0:
            return -100.0  # DISAPPEARED
        if a25 == 0.0 and a26 == 0.0:
            return 0.0
        return ((a26 - a25) / a25) * 100.0
        
    df_merged["percent_change"] = df_merged.apply(calc_pct, axis=1)
    
    def determine_status(row) -> str:
        a25 = float(row["amount_2025_pesos"])
        a26 = float(row["amount_2026_pesos"])
        if a25 == 0.0 and a26 > 0.0:
            return "NEW_IN_2026"
        elif a25 > 0.0 and a26 == 0.0:
            return "DISAPPEARED"
        elif a26 > a25:
            return "INCREASE"
        elif a26 < a25:
            return "DECREASE"
        else:
            return "UNCHANGED"
            
    df_merged["change_status"] = df_merged.apply(determine_status, axis=1)
    
    print(f"[Entity Resolution] PAP Comparison Matrix built: {len(df_merged)} total unique PAP entries.")
    return df_merged

def find_fuzzy_rename_candidates(df_unmatched_2025: pd.DataFrame, df_unmatched_2026: pd.DataFrame, score_threshold: float = 82.0, limit: int = 50) -> List[Dict[str, Any]]:
    """
    Finds potential renamed items between unmatched 2025 items and new 2026 items within the same agency.
    """
    candidates: List[Dict[str, Any]] = []
    
    agencies_2026 = df_unmatched_2026["agency_name"].unique()
    
    for agency in agencies_2026:
        sub_25 = df_unmatched_2025.loc[df_unmatched_2025["agency_name"] == agency]
        sub_26 = df_unmatched_2026.loc[df_unmatched_2026["agency_name"] == agency]
        
        if sub_25.empty or sub_26.empty:
            continue
            
        desc_list_25: List[str] = [str(x) for x in sub_25["description"].tolist()]
        
        for _, row_26 in sub_26.iterrows():
            desc_26 = str(row_26["description"])
            if len(desc_26) < 10:
                continue
                
            match_res = process.extractOne(desc_26, desc_list_25, scorer=fuzz.token_set_ratio)
            if match_res is not None:
                matched_desc_25, matched_score, _ = match_res
                if matched_score >= score_threshold:
                    matched_rows = sub_25.loc[sub_25["description"] == matched_desc_25]
                    if matched_rows.empty:
                        continue
                    row_25 = matched_rows.iloc[0]
                    
                    a25 = float(row_25.get("amount_2025_pesos", 0.0))
                    a26 = float(row_26.get("amount_2026_pesos", 0.0))
                    amt_diff_pct = abs(a26 - a25) / max(a25, 1.0)
                    
                    if amt_diff_pct <= 0.5:
                        candidates.append({
                            "department_name": str(row_26["department_name"]),
                            "agency_name": str(agency),
                            "description_2025": str(matched_desc_25),
                            "description_2026": desc_26,
                            "amount_2025_pesos": a25,
                            "amount_2026_pesos": a26,
                            "similarity_score": round(float(matched_score), 2),
                            "match_reason": f"Fuzzy description similarity ({matched_score:.1f}%) within same agency with comparable amounts (₱{a25/1e6:.1f}M -> ₱{a26/1e6:.1f}M)"
                        })
                        
                if len(candidates) >= limit:
                    break
        if len(candidates) >= limit:
            break
            
    return candidates
