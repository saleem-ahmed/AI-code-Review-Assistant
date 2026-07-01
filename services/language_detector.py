"""
Detect programming language.
"""

from pathlib import Path

LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".jsx": "React JSX",
    ".ts": "TypeScript",
    ".tsx": "React TSX",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".php": "PHP",
    ".go": "Go",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".html": "HTML",
    ".css": "CSS",
    ".json": "JSON",
    ".xml": "XML",
    ".sql": "SQL",
    ".md": "Markdown",
}


def detect_language(filename: str) -> str:
    """
    Detect language using the file extension.
    """

    extension = Path(filename).suffix.lower()

    return LANGUAGE_MAP.get(extension, "Unknown")