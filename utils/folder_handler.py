"""
Handles uploaded project folders.
"""

from utils.file_handler import read_uploaded_file


def read_project(uploaded_files):
    """
    Read all uploaded files.

    Returns:
        list
    """

    project = []

    for file in uploaded_files:

        try:
            project.append(
                read_uploaded_file(file)
            )

        except Exception:
            continue

    return project