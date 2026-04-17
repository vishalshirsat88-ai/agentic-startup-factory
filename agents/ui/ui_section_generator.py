import json
from utils.llm import call_llm


class UISectionGenerator:
    def __init__(self, idea, features):
        self.idea = idea
        self.features = features

    def generate_sections(self):
        prompt = f"""
You are a world-class SaaS UI designer.

Given a startup idea and its features, generate a high-converting landing page structure.

Return STRICT JSON only.

---

IDEA:
{self.idea}

FEATURES:
{json.dumps(self.features, indent=2)}

---

OUTPUT FORMAT:

[
  {{
    "type": "hero",
    "headline": "...",
    "subheadline": "...",
    "cta": "..."
  }},
  {{
    "type": "features",
    "items": ["...", "..."]
  }},
  {{
    "type": "workflow",
    "steps": ["...", "..."]
  }},
  {{
    "type": "cta",
    "headline": "...",
    "cta": "..."
  }}
]

---

RULES:

• Sections must be relevant to the product
• Copy must be domain-aware
• Avoid generic phrases
• Make it feel like a real SaaS landing page
"""

        response = call_llm(prompt)

        try:
            return json.loads(response)
        except:
            return []
