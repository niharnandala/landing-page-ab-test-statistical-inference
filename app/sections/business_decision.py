import streamlit as st


def render_business_decision(decision_result, threshold_result):
    st.header("4. Business Decision")

    st.markdown("### Practical Threshold")
    st.write(
        f"Practical threshold used: {threshold_result['relative_lift'] * 100:.2f}% "
        f"relative lift, which corresponds to an absolute improvement of "
        f"{threshold_result['absolute_threshold']:.6f}."
    )

    st.markdown("### Decision Summary")

    if (
        decision_result["is_statistically_significant"]
        and decision_result["observed_effect_meets_practical_threshold"]
    ):
        st.success("Decision: The new landing page shows meaningful evidence of improvement.")
    else:
        st.error("Decision: Do not deploy the new landing page.")

    st.write("Key checks:")
    st.write(f"- P-value: {decision_result['p_value']:.6f}")
    st.write(
        f"- Confidence interval: "
        f"({decision_result['ci_lower']:.6f}, {decision_result['ci_upper']:.6f})"
    )
    st.write(
        f"- Observed effect: {decision_result['observed_diff']:.6f}"
    )
    st.write(
        f"- CI reaches practical threshold: "
        f"{decision_result['ci_reaches_practical_threshold']}"
    )
    st.write(
        f"- Observed effect meets practical threshold: "
        f"{decision_result['observed_effect_meets_practical_threshold']}"
    )

    st.markdown(
        """
        Final interpretation:

        - there is no statistical evidence that the new page performs better
        - the observed effect is directionally negative
        - even optimistic plausible improvements remain below the practical threshold

        The existing landing page should be retained.
        """
    )