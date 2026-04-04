import pandas as pd
from src.experiment_checks import flag_mismatches


def test_flag_mismatches_basic():
    df = pd.DataFrame({
        "group": ["control", "treatment", "control"],
        "landing_page": ["old_page", "new_page", "new_page"]
    })

    df_checked = flag_mismatches(df)

    # First two are valid, last one is mismatch
    assert df_checked["is_mismatch"].tolist() == [False, False, True]