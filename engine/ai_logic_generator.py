from tools.llm import generate

def generate_ai_logic(module_name, description):

    prompt = f"""
    Write a Python service class for a SaaS module.

    Module: {module_name}
    Description: {description}

    Requirements:
    - Class named {module_name.capitalize()}AIService
    - Method: execute(self, input_data) that processes input and returns a result dict
    - Keep it simple and production-ready
    - No external dependencies beyond standard library

    Return ONLY valid Python code. No explanations. No markdown.
    """

    code = generate(prompt)

    if "```" in code:
        code = code.replace("```python", "").replace("```", "").strip()

    return code


def generate_ai_logic_for_architecture(project_dir, architecture):

    if not architecture:
        print("[AI Logic Generator] No architecture provided")
        return

    modules = architecture.get("modules", [])
    features = architecture.get("features", [])

    print("[AI Logic Generator] Generating AI logic for modules...")

    for i, module in enumerate(modules):
        description = features[i] if i < len(features) else f"Core logic for {module}"

        code = generate_ai_logic(module, description)

        file_path = f"{project_dir}/services/{module.lower().replace(' ', '_')}_ai_service.py"

        with open(file_path, "w") as f:
            f.write(code)

        print(f"[AI Logic Generator] Created {file_path}")

    print("[AI Logic Generator] Done")
