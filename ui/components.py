"""
Reusable UI components.
"""

import streamlit as st


def page_header():
    """Display application header."""

    st.title("AI Code Review Assistant")

    st.markdown(
        """
Analyze, understand and improve your source code using Artificial Intelligence.
"""
    )

    st.divider()


def feature_cards():
    """Display feature highlights."""

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.success("Bug Detection")

    with col2:
        st.info("Performance")

    with col3:
        st.warning("Security")

    with col4:
        st.success("ecurity")


def statistics():
    """Display application metrics."""

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Languages", "20+")

    with col2:
        st.metric("AI Status", "Ready")

    with col3:
        st.metric("Version", "1.0")