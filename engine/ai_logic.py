print("[DEBUG] About to import ai_logic...")
import requests
import os

print("[DEBUG] ai_logic imported successfully")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if GROQ_API_KEY:
    print("GROQ KEY LOADED")
else:
    print("❌ GROQ KEY NOT FOUND")
if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY is missing")


def generate_service_logic(module_name):
    print(f"\n[AI LOGIC] Generating logic for module: {module_name}")

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

    print("[AI LOGIC] Sending request to Groq...")

    response = requests.post(url, headers=headers, json=data)

    print("[AI LOGIC] Response status:", response.status_code)

    try:
        result = response.json()
        print("[AI LOGIC] Response type:", type(result))
    except Exception as e:
        print("❌ Failed to parse JSON:", e)
        return f"def get_{module_name}():\n    return {{'error': 'invalid response'}}"

    # 🔥 CRITICAL FIX — ALWAYS EXTRACT STRING
    try:
        content = result["choices"][0]["message"]["content"]
        print("[AI LOGIC] Extracted content successfully")
        return content
    except Exception as e:
        print("❌ EXTRACTION FAILED:", e)
        print("[AI LOGIC] RAW RESPONSE:", result)

        return f"""
def get_{module_name}():
    return {{
        "status": "fallback",
        "module": "{module_name}"
    }}
"""
