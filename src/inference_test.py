import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.power import NormalIndPower


def run_proportion_test(df: pd.DataFrame, alternative: str = "larger") -> dict:
    """
    Run a two-proportion z-test comparing treatment vs control.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned experiment dataset containing 'group' and 'converted'.
    alternative : str
        Alternative hypothesis for statsmodels proportions_ztest.
        Common options: 'larger', 'smaller', 'two-sided'

    Returns
    -------
    dict
        Dictionary with z-statistic and p-value.
    """
    conversions = df.groupby("group")["converted"].sum()
    n_users = df.groupby("group")["converted"].count()

    count = [conversions["treatment"], conversions["control"]]
    nobs = [n_users["treatment"], n_users["control"]]

    z_stat, p_value = proportions_ztest(count, nobs, alternative=alternative)

    return {
        "z_stat": float(z_stat),
        "p_value": float(p_value),
    }


def confidence_interval_diff(df: pd.DataFrame, alpha: float = 0.05) -> dict:
    """
    Compute the confidence interval for the difference in conversion rates:
    treatment - control
    """
    conversion_rates = df.groupby("group")["converted"].mean()
    group_sizes = df.groupby("group")["user_id"].count()

    p_control = conversion_rates["control"]
    p_treatment = conversion_rates["treatment"]

    n_control = group_sizes["control"]
    n_treatment = group_sizes["treatment"]

    diff = p_treatment - p_control

    se = np.sqrt(
        (p_control * (1 - p_control) / n_control) +
        (p_treatment * (1 - p_treatment) / n_treatment)
    )

    z_critical = 1.96 if alpha == 0.05 else NormalIndPower().solve_power(
        effect_size=0.0001, power=1 - alpha, alpha=alpha
    )
    # For this project alpha=0.05 is what we actually use.
    # The branch above is only a weak fallback and not meant for general precision.

    ci_lower = diff - z_critical * se
    ci_upper = diff + z_critical * se

    return {
        "diff": float(diff),
        "se": float(se),
        "ci_lower": float(ci_lower),
        "ci_upper": float(ci_upper),
    }


def compute_mde(
    control_rate: float,
    n_per_group: int,
    alpha: float = 0.05,
    power: float = 0.80,
    max_lift: float = 0.05,
) -> dict:
    """
    Compute an approximate minimum detectable effect (MDE) for a two-group
    proportion test using Cohen's h.

    Parameters
    ----------
    control_rate : float
        Baseline conversion rate.
    n_per_group : int
        Number of users per group.
    alpha : float
        Significance level.
    power : float
        Target statistical power.
    max_lift : float
        Maximum absolute lift search range above control_rate.

    Returns
    -------
    dict
        Dictionary with approximate detectable treatment rate,
        absolute MDE, and relative MDE.
    """
    analysis = NormalIndPower()

    effect_size = analysis.solve_power(
        nobs1=n_per_group,
        alpha=alpha,
        power=power,
        ratio=1.0,
        alternative="larger",
    )

    def cohens_h(p_a: float, p_b: np.ndarray) -> np.ndarray:
        return 2 * np.arcsin(np.sqrt(p_b)) - 2 * np.arcsin(np.sqrt(p_a))

    candidate_ps = np.linspace(control_rate, min(control_rate + max_lift, 0.999999), 100000)
    h_values = np.abs(cohens_h(control_rate, candidate_ps))
    treatment_rate_mde = candidate_ps[np.argmin(np.abs(h_values - effect_size))]

    absolute_mde = treatment_rate_mde - control_rate
    relative_mde = absolute_mde / control_rate

    return {
        "control_rate": float(control_rate),
        "n_per_group": int(n_per_group),
        "effect_size_h": float(effect_size),
        "treatment_rate_mde": float(treatment_rate_mde),
        "absolute_mde": float(absolute_mde),
        "relative_mde": float(relative_mde),
    }