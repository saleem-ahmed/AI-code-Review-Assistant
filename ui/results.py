import streamlit as st


def show_result(file, result):

    st.divider()

    st.subheader("Review Information")

    st.write("Filename:", file["filename"])

    st.write("Language:", result["language"])

    st.write(result["analysis"])

    with st.expander("Prompt"):

        st.code(result["prompt"])


def show_text_result(code, result):

    st.divider()

    st.subheader("Review Information")

    st.write("Language:", result["language"])

    st.write(result["analysis"])

    with st.expander("Prompt"):

        st.code(result["prompt"])