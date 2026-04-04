import streamlit as st


def render_overview(df_clean, conversion_rates, sizes):
    st.header("1. Overview")

    st.markdown(
        """
        This app summarizes the final results of a landing-page A/B test.
        The goal is to evaluate whether the new landing page should replace the existing page.
        """
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Cleaned Rows", f"{len(df_clean):,}")
    col2.metric("Control Conversion Rate", f"{conversion_rates['control']:.4%}")
    col3.metric("Treatment Conversion Rate", f"{conversion_rates['treatment']:.4%}")

    st.subheader("Group Sizes")
    st.dataframe(
        sizes.rename("n_users").reset_index(),
        use_container_width=True
    )