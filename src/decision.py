def practical_threshold(control_rate: float, relative_lift: float = 0.01) -> dict:
    """
    Compute the practical significance threshold based on a chosen
    relative lift over the control conversion rate.
    """
    absolute_threshold = control_rate * relative_lift

    return {
        "control_rate": float(control_rate),
        "relative_lift": float(relative_lift),
        "absolute_threshold": float(absolute_threshold),
    }


def business_summary(
    observed_diff: float,
    ci_lower: float,
    ci_upper: float,
    p_value: float,
    practical_absolute_threshold: float,
    absolute_mde: float,
) -> dict:
    """
    Package key business decision signals into a single structured summary.
    """
    return {
        "observed_diff": float(observed_diff),
        "ci_lower": float(ci_lower),
        "ci_upper": float(ci_upper),
        "p_value": float(p_value),
        "practical_absolute_threshold": float(practical_absolute_threshold),
        "absolute_mde": float(absolute_mde),
        "is_statistically_significant": bool(p_value < 0.05),
        "ci_crosses_zero": bool(ci_lower <= 0 <= ci_upper),
        "ci_reaches_practical_threshold": bool(ci_upper >= practical_absolute_threshold),
        "observed_effect_meets_practical_threshold": bool(observed_diff >= practical_absolute_threshold),
    }