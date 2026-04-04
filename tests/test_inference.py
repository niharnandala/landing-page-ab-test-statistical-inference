import pandas as pd

from src.inference import run_proportion_test, confidence_interval_diff, compute_mde


def test_run_proportion_test_returns_expected_keys():
    df = pd.DataFrame({
        "user_id": [1, 2, 3, 4, 5, 6],
        "group": ["control", "control", "control", "treatment", "treatment", "treatment"],
        "converted": [0, 0, 1, 1, 1, 1],
    })

    result = run_proportion_test(df, alternative="larger")

    assert "z_stat" in result
    assert "p_value" in result
    assert isinstance(result["z_stat"], float)
    assert isinstance(result["p_value"], float)


def test_confidence_interval_diff_returns_ordered_interval():
    df = pd.DataFrame({
        "user_id": [1, 2, 3, 4, 5, 6],
        "group": ["control", "control", "control", "treatment", "treatment", "treatment"],
        "converted": [0, 0, 1, 1, 1, 1],
    })

    result = confidence_interval_diff(df)

    assert "diff" in result
    assert "ci_lower" in result
    assert "ci_upper" in result
    assert result["ci_lower"] <= result["ci_upper"]


def test_compute_mde_returns_positive_detectable_effect():
    result = compute_mde(control_rate=0.12, n_per_group=10000, alpha=0.05, power=0.80)

    assert result["absolute_mde"] > 0
    assert result["relative_mde"] > 0
    assert result["treatment_rate_mde"] > result["control_rate"]