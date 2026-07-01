"""
Main review workflow.
"""

from services.language_detector import detect_language
from services.static_analyzer import analyze
from services.prompt_builder import PromptBuilder


class ReviewService:

    def prepare_review(
        self,
        filename: str,
        code: str,
    ):

        language = detect_language(filename)

        analysis = analyze(code)

        prompt = PromptBuilder.build(
            filename,
            language,
            code,
            analysis,
        )

        return {
            "language": language,
            "analysis": analysis,
            "prompt": prompt,
        }