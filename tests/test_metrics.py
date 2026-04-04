import pandas as pd

from src.metrics import group_conversion_rates, group_sizes, observed_difference


def test_group_conversion_rates():
    df = pd.DataFrame({
        "user_id": [1, 2, 3, 4],
        "group": ["control", "control", "treatment", "treatment"],
        "converted": [1, 0, 1, 1],
    })

    rates = group_conversion_rates(df)

    assert rates["control"] == 0.5
    assert rates["treatment"] == 1.0


def test_group_sizes():
    df = pd.DataFrame({
        "user_id": [1, 2, 3, 4, 5],
        "group": ["control", "control", "treatment", "treatment", "treatment"],
        "converted": [1, 0, 1, 0, 1],
    })

    sizes = group_sizes(df)

    assert sizes["control"] == 2
    assert sizes["treatment"] == 3


def test_observed_difference():
    df = pd.DataFrame({
        "user_id": [1, 2, 3, 4],
        "group": ["control", "control", "treatment", "treatment"],
        "converted": [1, 0, 1, 1],
    })

    diff = observed_difference(df)

    assert diff == 0.5