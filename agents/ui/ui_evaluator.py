from tools.llm import generate
import re


class UIEvaluator:
    def __init__(self):
        pass

    def evaluate(self, ui_code, idea):
        trimmed_ui = ui_code[:1200]

        prompt = f"""
You are a world-class UI/UX critic.

Your job is to evaluate and improve a SaaS landing page UI.

STRICT RULES:
- DO NOT be generic
- DO NOT praise unnecessarily
- Do NOT use line breaks inside JSON values
- BE brutally honest
- Focus on premium SaaS quality (like Stripe, Linear, Notion)
- MUST use Tailwind-style spacing (p-4, p-6 etc.)
- MUST include visual depth (shadow, gradient, or layered background)
- MUST include clear CTA (large, high contrast)
- MUST avoid flat or plain UI
- MUST include at least one of:
  • hover effect
  • animation
  • gradient

---

PRODUCT CONTEXT:
{idea}

---

UI CODE (TRIMMED):
{trimmed_ui}

---

Evaluate based on:

1. Visual Hierarchy
2. Spacing & Layout
3. Modern Aesthetic
4. Conversion Clarity
5. Micro Polish

---

Return ONLY JSON:

{{
  "score": <number 1-10>,
  "issues": ["issue1", "issue2"],
  "fixes": ["fix1", "fix2"],
  "improved_code": "<ONLY modified sections, NOT full page>"
}}

---

CRITICAL BEHAVIOR:
- If score < 8 → MUST improve aggressively
- Make SIGNIFICANT visual improvements (not minor tweaks)
- Improve layout, spacing, CTA visibility

---

CRITICAL OUTPUT RULES:
- Output MUST be strictly valid JSON
- NO text before or after JSON
- NO markdown (```json)
- Ensure JSON is complete (no truncation)

---

HTML RULES:
- DO NOT return full HTML
- ONLY improve key sections (hero, CTA, layout)
- Keep improved_code under 1200 characters
- Use SINGLE quotes for HTML attributes (class='hero')
"""

        response = generate(prompt)

        match = re.search(r"\{.*\}", response, re.DOTALL)

        if match:
            return match.group(0).strip()

        print("❌ No JSON found. RAW:", response[:300])
        return response
