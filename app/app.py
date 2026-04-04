from pathlib import Path
import sys

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.metrics import group_conversion_rates, group_sizes, observed_difference
from src.inference import run_proportion_test, confidence_interval_diff, compute_mde
from src.decision import practical_threshold, business_summary

from sections.overview import render_overview
from sections.integrity_checks import render_integrity_checks
from sections.statistical_results import render_statistical_results
from sections.business_decision import render_business_decision


st.set_page_config(
    page_title="A/B Testing Decision App",
    layout="wide",
)

st.title("A/B Testing Project: Landing Page Experiment")

processed_data_path = PROJECT_ROOT / "data" / "processed" / "ab_clean.csv"

if not processed_data_path.exists():
    st.error(
        "Processed dataset not found. Run `python src/pipeline.py` first "
        "to generate `data/processed/ab_clean.csv`."
    )
    st.stop()

df_clean = pd.read_csv(processed_data_path)

conversion_rates = group_conversion_rates(df_clean)
sizes = group_sizes(df_clean)
diff = observed_difference(df_clean)

test_result = run_proportion_test(df_clean, alternative="larger")
ci_result = confidence_interval_diff(df_clean)

control_rate = conversion_rates["control"]
n_per_group = int(min(sizes["control"], sizes["treatment"]))
mde_result = compute_mde(control_rate=control_rate, n_per_group=n_per_group)

threshold_result = practical_threshold(control_rate=control_rate, relative_lift=0.01)

decision_result = business_summary(
    observed_diff=diff,
    ci_lower=ci_result["ci_lower"],
    ci_upper=ci_result["ci_upper"],
    p_value=test_result["p_value"],
    practical_absolute_threshold=threshold_result["absolute_threshold"],
    absolute_mde=mde_result["absolute_mde"],
)

render_overview(df_clean, conversion_rates, sizes)
render_integrity_checks()
render_statistical_results(diff, test_result, ci_result, mde_result)
render_business_decision(decision_result, threshold_result)