import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("GROQ KEY:", GROQ_API_KEY[:5] if GROQ_API_KEY else "NOT FOUND")


def generate_service_logic(module_name):
    prompt = f"""
You are a backend engineer.

Write a Python function for a Flask service.

Module: {module_name}

Rules:
- Only return Python function code
- Function name: get_{module_name}
- Use realistic business logic
- No explanations
- No markdown

Example:
def get_users():
    return {{"users": []}}
"""

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    return result["choices"][0]["message"]["content"]
