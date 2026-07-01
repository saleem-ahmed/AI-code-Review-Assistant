"""
Application configuration.

Loads environment variables and stores
global application settings.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_FOLDER = BASE_DIR / "uploads"

REPORT_FOLDER = BASE_DIR / "reports"

ASSETS_FOLDER = BASE_DIR / "assets"

# --------------------------------------------------
# Security
# --------------------------------------------------

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".cpp",
    ".c",
    ".cs",
    ".go",
    ".php",
    ".rb",
    ".swift",
    ".kt",
    ".html",
    ".css",
    ".json",
    ".xml",
    ".yaml",
    ".yml",
    ".sql",
    ".md",
}

IGNORED_FOLDERS = {
    "__pycache__",
    ".git",
    "node_modules",
    "dist",
    "build",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
}

# --------------------------------------------------
# API Keys
# --------------------------------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --------------------------------------------------
# Streamlit
# --------------------------------------------------

APP_NAME = "AI Code Review Assistant"

APP_ICON = "🤖"

PAGE_LAYOUT = "wide"