import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"


def generate_review(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a senior software engineer reviewing a pull request."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(GROQ_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
