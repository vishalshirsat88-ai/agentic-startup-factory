def build_domain_prompt(module_name, idea):
    idea_context = ""

    if isinstance(idea, dict):
        idea_context = f"""
Startup Name: {idea.get("name", "")}
Description: {idea.get("description", "")}
Market: {idea.get("market", "")}
Revenue Model: {idea.get("revenue_model", "")}
"""

    return f"""
You are a senior Python backend engineer.

Generate ONLY clean, executable Python code.

Module: {module_name}

Context:
{idea_context}

STRICT RULES:

1. Output ONLY valid Python code (NO markdown, NO ```).
2. DO NOT include explanations.
3. DO NOT include comments.
4. Function must be EXACTLY:

def get_{module_name}():

5. ALWAYS return:

{{
  "status": "success",
  "data": ...
}}

6. Code MUST:
- Have correct indentation
- Have NO syntax errors
- Close all brackets
- Not use undefined variables

7. Keep logic SIMPLE and SAFE:
- No nested complex conditions
- No random imports
- No datetime unless necessary

8. Use STATIC realistic data (not dynamic calculations)

GOOD EXAMPLE:

def get_{module_name}():
    return {{
        "status": "success",
        "data": {{
            "{module_name}": [
                {{
                    "id": 1,
                    "name": "Sample",
                    "status": "active",
                    "amount": 100
                }}
            ],
            "total": 1
        }}
    }}

OUTPUT ONLY VALID PYTHON FUNCTION.
"""
