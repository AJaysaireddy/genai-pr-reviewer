PRIORITY = 1
REVIEW_ID = "LOGIC"

from engines.groq_engine import generate_review


def run(before_code, after_code):
    prompt = f"""
Here is the BEFORE code:
{before_code}

Here is the AFTER code:
{after_code}

Task:
- Identify logic changes
- Explain risks
- Use bullet points
- Tag each point with [HIGH], [MEDIUM], or [LOW]
"""

    ai_output = generate_review(prompt)
    return "LOGIC REVIEW (AI)", "\n" + ai_output
