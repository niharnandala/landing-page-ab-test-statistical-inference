import pandas as pd


def group_conversion_rates(df: pd.DataFrame) -> pd.Series:
    """
    Return conversion rates by experiment group.
    """
    return df.groupby("group")["converted"].mean()


def group_sizes(df: pd.DataFrame) -> pd.Series:
    """
    Return user counts by experiment group.
    """
    return df.groupby("group")["user_id"].count()


def observed_difference(df: pd.DataFrame) -> float:
    """
    Return the observed difference in conversion rate:
    treatment - control
    """
    conversion_rates = group_conversion_rates(df)
    return float(conversion_rates["treatment"] - conversion_rates["control"])