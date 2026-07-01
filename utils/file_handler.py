"""
Handles reading a single source code file.
"""

from utils.validators import validate_file


def read_uploaded_file(uploaded_file):
    """
    Read an uploaded Streamlit file.

    Returns:
        dict
    """

    valid, message = validate_file(
        uploaded_file.name,
        uploaded_file.size
    )

    if not valid:
        raise ValueError(message)

    code = uploaded_file.read().decode("utf-8")

    return {
        "filename": uploaded_file.name,
        "size": uploaded_file.size,
        "code": code,
    }