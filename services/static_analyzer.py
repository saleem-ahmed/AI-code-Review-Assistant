"""
Basic static analysis.
"""


def analyze(code: str):

    lines = len(code.splitlines())

    characters = len(code)

    blank_lines = sum(
        1 for line in code.splitlines()
        if not line.strip()
    )

    return {
        "lines": lines,
        "characters": characters,
        "blank_lines": blank_lines,
    }