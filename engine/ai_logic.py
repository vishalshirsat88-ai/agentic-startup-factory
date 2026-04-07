import requests
import os
import textwrap

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("🔥🔥 NEW AI_LOGIC FILE LOADED v3🔥🔥")


def fallback_function(module_name):
    return textwrap.dedent(f"""\
    def get_{module_name}():
        return {{
            "status": "success",
            "data": {{
                "{module_name}": [
                    {{
                        "id": 1,
                        "name": "Fallback Data",
                        "status": "active",
                        "amount": 100
                    }}
                ],
                "total": 1
            }}
        }}
    """)


def generate_service_logic(module_name, idea):
    print(f"\n[AI LOGIC] Generating logic for module: {module_name}")

    if not GROQ_API_KEY:
        print("❌ GROQ KEY NOT FOUND — using fallback")

        return fallback_function(module_name)

    from tools.domain_prompt_builder import build_domain_prompt

    prompt = build_domain_prompt(module_name, idea)

    # AFTER
    idea_name = idea.get("name") if isinstance(idea, dict) else "unknown"
    print("[AI CONTEXT]", idea_name, "| Module:", module_name)
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

            return fallback_function(module_name)

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

                # 🔥 CLEAN MARKDOWN (STRONG VERSION)
                if "```" in content:
                    content = content.replace("```python", "")
                    content = content.replace("```", "")
                    content = content.strip()

                if not content:
                    print("❌ EMPTY AI RESPONSE")
                    return fallback_function(module_name)

                # 🚨 HARD VALIDATION (MOVE HERE)
                if f"def get_{module_name}" not in content:
                    print("❌ INVALID FUNCTION NAME — USING FALLBACK")

                    return fallback_function(module_name)

                print("[AI LOGIC] SUCCESSFULLY EXTRACTED")
                # 🔥 REMOVE EXTRA FUNCTIONS (CRITICAL)
                # 🔥 STRICT FUNCTION EXTRACTION (FINAL FIX)

                start_index = content.find(f"def get_{module_name}")
                if start_index == -1:
                    return fallback_function(module_name)

                content = content[start_index:]

                # REMOVE DUPLICATE FUNCTION DEFINITIONS
                parts = content.split(f"def get_{module_name}")
                if len(parts) > 1:
                    content = f"def get_{module_name}" + parts[1]

                # 🔥 REMOVE DUPLICATE LINES
                lines = content.split("\n")
                cleaned = []

                for i, line in enumerate(lines):
                    if i > 0 and line.strip() == lines[i - 1].strip():
                        continue
                    cleaned.append(line)

                content = "\n".join(cleaned)
                # 🔥 AUTO FIX COMMON SYNTAX ISSUES

                if content.count("{") > content.count("}"):
                    content += "\n}"

                if content.count("[") > content.count("]"):
                    content += "\n]"

                # 🔥 FINAL VALIDATION
                if "return" not in content:
                    print("❌ INVALID FUNCTION — NO RETURN")

                    return fallback_function(module_name)

                # ✂️ KEEP ONLY FIRST FUNCTION BLOCK (FIXED)
                lines = content.split("\n")
                cleaned = []

                for line in lines:
                    # STOP at second function (safer logic)
                    if line.strip().startswith("def ") and cleaned:
                        break

                    cleaned.append(line)

                content = "\n".join(cleaned)
                print("🔥 FINAL CLEANED AI FUNCTION:\n", content)

                # 🔥 FINAL SAFETY EXEC CHECK (VERY IMPORTANT)
                try:
                    exec(content, {})
                    print("✅ EXEC VALIDATION PASSED")
                except Exception as e:
                    print("⚠️ EXEC VALIDATION FAILED:", e)
                    print("⚠️ USING AI OUTPUT ANYWAY (NON-BLOCKING MODE)")

                # 🔥 ENSURE SAFE DATA STRUCTURE (ALWAYS RUN)
                if '"data"' not in content:
                    print("⚠️ MISSING DATA — PATCHING")
                    return fallback_function(module_name)

                return content

            except Exception as e:
                print("❌ MALFORMED CHOICES:", e)

        # ❌ HANDLE API ERROR
        if "error" in result:
            print("❌ GROQ API ERROR:", result.get("error", {}).get("message", result))

        print("❌ UNKNOWN RESPONSE FORMAT")

        return fallback_function(module_name)

    except Exception as e:
        print("❌ AI LOGIC ERROR:", e)

    return fallback_function(module_name)
