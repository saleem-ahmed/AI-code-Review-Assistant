"""
General helper functions.
"""

from pathlib import Path


def get_extension(filename: str) -> str:
    """
    Return file extension.
    """

    return Path(filename).suffix.lower()


def count_lines(code: str) -> int:
    """
    Count number of lines in code.
    """

    return len(code.splitlines())


def count_characters(code: str) -> int:
    """
    Count total characters.
    """

    return len(code)