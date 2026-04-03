import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("🔥🔥 NEW AI_LOGIC FILE LOADED 🔥🔥")


def generate_service_logic(module_name, idea):
    print(f"\n[AI LOGIC] Generating logic for module: {module_name}")

    if not GROQ_API_KEY:
        print("❌ GROQ KEY NOT FOUND — using fallback")
        return f"""
def get_{module_name}():
    return {{
        "status": "fallback_no_api_key",
        "module": "{module_name}"
    }}
"""

    prompt = f"""
    You are building a SaaS backend.

    Startup Idea: {idea.get("name")}
    Description: {idea.get("description")}
    Target Users: {idea.get("market")}
    Revenue Model: {idea.get("revenue_model")}

    Module: {module_name}

    Write ONE Python function for this module.

    STRICT RULES:
    - Function name MUST be: get_{module_name}
    - Return ONLY ONE function
    - Do NOT create multiple functions
    - Do NOT include imports
    - Do NOT include classes
    - Do NOT include example usage
    - Do NOT include explanations
    - Do NOT include markdown
    - Use realistic business logic based on the startup idea

    Output format EXACTLY like:

    def get_{module_name}():
        # logic here
        return {{"status": "success"}}
    """

    print("[AI CONTEXT]", idea.get("name"), "| Module:", module_name)
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        print("[AI LOGIC] STATUS CODE:", response.status_code)
        print("[AI LOGIC] RAW TEXT:", response.text[:500])

        try:
            result = response.json()
        except Exception as e:
            print("❌ JSON PARSE FAILED:", e)
            print("RAW TEXT RESPONSE:", response.text)
            return f"def get_{module_name}(): return {{'error': 'json_parse_failed'}}"

        # 🔥 FORCE PRINT (NO CONDITIONS)
        print("\n================ RAW GROQ RESPONSE - V3 ================")
        print(result)
        print("==================================================\n")

        # 🔥 FULL DEBUG
        print("[AI LOGIC] FULL RESPONSE:", result)

        # ✅ SAFE EXTRACTION
        content = None  # 🔥 ADD THIS BEFORE

        if "choices" in result:
            try:
                content = result["choices"][0]["message"]["content"]

                # 🔥 REMOVE MARKDOWN BACKTICKS
                if content.startswith("```"):
                    content = (
                        content.replace("```python", "").replace("```", "").strip()
                    )

                # 🚨 HARD VALIDATION (MOVE HERE)
                if f"def get_{module_name}" not in content:
                    print("❌ INVALID FUNCTION NAME — USING FALLBACK")
                    return f"""def get_{module_name}():
            return {{"status": "invalid_ai_output"}}
        """

                print("[AI LOGIC] SUCCESSFULLY EXTRACTED")

                return content

            except Exception as e:
                print("❌ MALFORMED CHOICES:", e)

        # ❌ HANDLE API ERROR
        if "error" in result:
            print("❌ GROQ API ERROR:", result.get("error", {}).get("message", result))

        print("❌ UNKNOWN RESPONSE FORMAT")

        return f"""def get_{module_name}():
            return {{
                "status": "fallback_error",
                "module": "{module_name}"
            }}
        """

    except Exception as e:
        print("❌ AI LOGIC ERROR:", e)

    return f"""def get_{module_name}():
        return {{
            "status": "fallback_error",
            "module": "{module_name}"
        }}
    """
