import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY not found in environment")


def generate_review(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "llama-3.1-8b-instant",  # ✅ supported
        "messages": [
            {
                "role": "system",
                "content": "You are a senior software engineer reviewing a pull request."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 400,
    }

    response = requests.post(GROQ_ENDPOINT, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Groq API Error {response.status_code}: {response.text}")

    return response.json()["choices"][0]["message"]["content"]
