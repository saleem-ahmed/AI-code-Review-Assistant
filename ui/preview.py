"""
Preview uploaded code.
"""

import streamlit as st


def preview_code(code, language="text"):
    """
    Display uploaded code.
    """

    st.subheader("👀 Code Preview")

    st.code(
        code,
        language=language,
        line_numbers=True,
    )