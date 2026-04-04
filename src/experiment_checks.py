import pandas as pd


def flag_mismatches(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add an 'is_mismatch' column to flag rows where
    group assignment and landing page exposure do not align.

    Valid mappings:
    - control -> old_page
    - treatment -> new_page
    """
    df_checked = df.copy()

    valid_control = (
        (df_checked["group"] == "control") &
        (df_checked["landing_page"] == "old_page")
    )
    valid_treatment = (
        (df_checked["group"] == "treatment") &
        (df_checked["landing_page"] == "new_page")
    )

    df_checked["is_mismatch"] = ~(valid_control | valid_treatment)
    return df_checked


def mismatch_summary(df: pd.DataFrame) -> dict:
    """
    Return a summary of experiment contamination based on the
    'is_mismatch' column.

    Expects the input DataFrame to already contain 'is_mismatch'.
    """
    if "is_mismatch" not in df.columns:
        raise ValueError("DataFrame must contain 'is_mismatch'. Run flag_mismatches() first.")

    total_rows = len(df)
    mismatch_rows = int(df["is_mismatch"].sum())
    mismatch_rate = mismatch_rows / total_rows if total_rows > 0 else 0.0

    crosstab = pd.crosstab(df["group"], df["landing_page"])

    mismatch_breakdown = (
        df[df["is_mismatch"]]
        .groupby(["group", "landing_page"])
        .size()
        .reset_index(name="count")
    )

    return {
        "total_rows": total_rows,
        "mismatch_rows": mismatch_rows,
        "mismatch_rate": mismatch_rate,
        "group_landing_page_table": crosstab,
        "mismatch_breakdown": mismatch_breakdown,
    }


def duplicate_user_summary(df: pd.DataFrame) -> dict:
    """
    Return duplicate-user statistics for user-level validation.
    """
    total_rows = len(df)
    unique_users = int(df["user_id"].nunique())

    duplicate_counts = df["user_id"].value_counts()
    duplicate_users = duplicate_counts[duplicate_counts > 1]

    num_duplicate_users = int(len(duplicate_users))
    extra_duplicate_rows = int(duplicate_users.sum() - len(duplicate_users))

    return {
        "total_rows": total_rows,
        "unique_users": unique_users,
        "num_duplicate_users": num_duplicate_users,
        "extra_duplicate_rows": extra_duplicate_rows,
        "duplicate_user_counts": duplicate_users,
    }