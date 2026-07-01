"""
Uploader UI.
"""

import streamlit as st


def upload_section():

    st.header("📥 Upload Source Code")

    option = st.radio(
        "Choose Input Method",
        [
            "Upload File",
            "Upload Project",
            "Paste Code",
        ],
        horizontal=True,
    )

    if option == "Upload File":

        uploaded = st.file_uploader(
            "Upload Source Code"
        )

        return option, uploaded

    elif option == "Upload Project":

        uploaded = st.file_uploader(
            "Upload Project",
            accept_multiple_files=True
        )

        return option, uploaded

    else:

        code = st.text_area(
            "Paste Code",
            height=300
        )

        return option, code