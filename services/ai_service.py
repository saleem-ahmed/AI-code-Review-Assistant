"""
Base AI Service.

This class will later support:
- OpenAI
- Gemini
- OpenRouter
"""

from abc import ABC, abstractmethod


class AIService(ABC):

    @abstractmethod
    def review(self, prompt: str) -> str:
        """
        Generate an AI review.
        """
        pass