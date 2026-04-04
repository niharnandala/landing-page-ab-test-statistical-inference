import streamlit as st
import matplotlib.pyplot as plt


def render_statistical_results(diff, test_result, ci_result, mde_result):
    st.header("3. Statistical Results")

    col1, col2, col3 = st.columns(3)
    col1.metric("Observed Difference", f"{diff:.4%}")
    col2.metric("Z-statistic", f"{test_result['z_stat']:.4f}")
    col3.metric("P-value", f"{test_result['p_value']:.4f}")

    st.markdown("### Confidence Interval")
    st.write(
        f"95% CI for (treatment - control): "
        f"({ci_result['ci_lower']:.6f}, {ci_result['ci_upper']:.6f})"
    )

    st.markdown("### MDE / Sensitivity")
    st.write(
        f"Approximate detectable uplift: {mde_result['absolute_mde']:.6f} "
        f"({mde_result['relative_mde'] * 100:.2f}% relative lift)"
    )

    fig = plt.figure()
    plt.errorbar(
        x=0,
        y=ci_result["diff"],
        yerr=1.96 * ci_result["se"],
        fmt="o"
    )
    plt.axhline(0)
    plt.xlim(-1, 1)
    plt.ylabel("Difference (Treatment - Control)")
    plt.title("Confidence Interval for Conversion Rate Difference")
    st.pyplot(fig)