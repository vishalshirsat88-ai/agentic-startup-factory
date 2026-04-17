from jinja2 import Environment, FileSystemLoader
import json
import os
from tools.llm import generate  # 🔥 NEW


def generate_lovable_ui(data):
    """
    Generate dynamic SaaS UI using AI (Lovable Layer v1)
    """

    prompt = f"""
You are a world-class SaaS UI generator.

Generate a modern SaaS landing page.

STRICT RULES:
- Return ONLY HTML (no markdown)
- Use TailwindCSS
- Must include:
  • Hero section
  • Features section
  • CTA section
- Must look like Stripe / Notion / Linear
- Use good spacing, gradients, shadows
- Keep it clean and premium

PRODUCT DATA:
{json.dumps(data)}

OUTPUT:
Return full HTML page
"""

    try:
        response = generate(prompt)

        # Basic validation
        if "<html" in response.lower() and "</html>" in response.lower():
            return response

    except Exception as e:
        print("❌ Lovable UI generation failed:", e)

    return None


def render_startup(config_path, output_dir):
    with open(config_path) as f:
        data = json.load(f)

    html = None

    # 🔥 STEP 1: Try Lovable UI generation
    print("🧠 Attempting Lovable UI generation...")
    html = generate_lovable_ui(data)

    # 🔁 STEP 2: Fallback to template if AI fails
    if not html:
        print("⚠️ Falling back to template UI")

        env = Environment(loader=FileSystemLoader("saas_master_template/templates"))
        template = env.get_template("index.html")
        html = template.render(data=data)

    # ✅ STEP 3: Write output safely
    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/index.html", "w") as f:
        f.write(html)

    print("🚀 Startup generated:", output_dir)
