"""
validators.py

Validation functions for uploaded files and projects.
"""

from pathlib import Path
from config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE


def is_allowed_file(filename: str) -> bool:
    """
    Check if a file extension is supported.
    """
    extension = Path(filename).suffix.lower()
    return extension in ALLOWED_EXTENSIONS


def is_file_size_valid(file_size: int) -> bool:
    """
    Check whether file size is within limits.
    """
    return file_size <= MAX_FILE_SIZE


def validate_file(filename: str, file_size: int):
    """
    Validate a file before processing.

    Returns:
        (bool, message)
    """

    if not is_allowed_file(filename):
        return False, "Unsupported file type."

    if not is_file_size_valid(file_size):
        return False, "File exceeds maximum allowed size."

    return True, "Valid file."