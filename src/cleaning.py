import pandas as pd


def remove_mismatches(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows flagged as experiment mismatches.

    Expects the input DataFrame to already contain 'is_mismatch'.
    """
    if "is_mismatch" not in df.columns:
        raise ValueError("DataFrame must contain 'is_mismatch'. Run flag_mismatches() first.")

    return df.loc[~df["is_mismatch"]].copy()


def remove_duplicate_users(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate users, keeping the first occurrence only.

    This enforces a strict one-row-per-user structure for analysis.
    """
    return df.drop_duplicates(subset="user_id", keep="first").copy()