"""
Builds prompts for the AI model.
"""

from typing import Dict


class PromptBuilder:
    """
    Creates prompts for AI code review.
    """

    @staticmethod
    def build(
        filename: str,
        language: str,
        code: str,
        analysis: Dict
    ) -> str:

        prompt = f"""
You are an expert Senior Software Engineer and AI Code Reviewer.

Analyze the following source code.

Filename:
{filename}

Programming Language:
{language}

Project Statistics

- Lines: {analysis['lines']}
- Characters: {analysis['characters']}
- Blank Lines: {analysis['blank_lines']}

Your tasks:

1. Explain what the code does.
2. Find bugs.
3. Find security issues.
4. Suggest performance improvements.
5. Suggest readability improvements.
6. Follow best coding practices.
7. Give an overall code quality score out of 10.

Source Code:

{code}
"""

        return prompt