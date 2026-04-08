from agents.agent_base import AgentBase
from tools.json_parser import extract_json

# These are checker debugs
print("🔥 DEBUG: ProductAgent LOADED v4")


class ProductAgent(AgentBase):
    def __init__(self):
        super().__init__("Product Agent")

    def define_product(self, idea):
        # These are checker debugs
        print("🚀 DEBUG: ProductAgent EXECUTED v1")
        prompt = f"""
        You are a Product Manager & Design Architect.

        Convert this startup idea into a structured product definition, Visual Design System, and Landing Page Copy.

        Startup Idea:
        {idea}

        Return ONLY JSON:
        {{
          "name": "product name",
          "description": "short description",
          "design_tokens": {{
            "colors": {{
              "primary": "#HEX",
              "secondary": "#HEX",
              "accent": "#HEX",
              "background": "#HEX"
            }},
            "typography": {{
              "heading_font": "Inter | Playfair Display | Roboto",
              "body_font": "Inter | Open Sans"
            }},
            "vibe": "minimalist | bold | playful | professional",
            "border_radius": "none | sm | md | lg | full"
          }},
          "marketing_copy": {{
            "hero_title": "Catchy 5-word headline",
            "hero_subtitle": "Persuasive 15-word subheadline",
            "cta_text": "Get Started Now",
            "pricing": [
                {{"plan": "Starter", "price": "$0", "features": ["Feature A", "Feature B"]}},
                {{"plan": "Pro", "price": "$49", "features": ["Unlimited access", "Priority support"]}}
            ]
          }},
          "modules": [
            {{
              "name": "module_name",
              "description": "what this module does",
              "features": ["feature1", "feature2"]
            }}
          ],
          "user_flows": ["flow1", "flow2"]
        }}

        Rules:
        1. Choose colors that match the startup category vibe.
        2. Break product into 3-6 backend modules.
        3. Do not explain anything.
        """

        response = self.think(prompt)

        product = extract_json(response)
        if product and "modules" not in product:
            print("[Product Agent] Missing modules — applying fallback structure")
            product["modules"] = [
                {
                    "name": "core",
                    "description": "Core functionality",
                    "features": product.get("core_features", ["basic operations"]),
                }
            ]

        # 🔥 Ensure modules exist (CRITICAL FOR BACKEND)
        if product and "modules" not in product:
            print("[Product Agent] Adding modules fallback")

            product["modules"] = [
                {
                    "name": "core",
                    "description": "Core functionality",
                    "features": product.get("core_features", ["basic operations"]),
                }
            ]
        if not product:
            print("[Product Agent] Failed to parse product JSON")
            return None

        return product
