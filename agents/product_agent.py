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
        # --- [REPLACE PROMPT BLOCK START] ---
        prompt = f"""
        You are a Senior Product Architect & Vibe-Coder.

        TASK: Convert this idea into a structured product definition and a 'Lovable' Visual Design System.

        Startup Idea: {idea}

        PHASE 1: DESIGN EVALUATION (Mandatory Internal Monologue)
        Before generating JSON, provide a 3-sentence critique:
        1. Rating: Grade the idea clarity (A-F).
        2. Premium Vibe: Identify what specific 'Glassmorphism' or 'Glow' elements are needed.
        3. Generic Risk: What standard 'cheap' design patterns must we avoid?
        4. CRITICAL: Always provide at least 4 unique modules in the "modules" list to ensure a rich dashboard layout.

        PHASE 2: DEFINITION
        Return ONLY JSON:
        {{
          "name": "product name",
          "description": "short description",
          "design_tokens": {{
            "colors": {{
              "primary": "#HEX",
              "background": "#030712",
              "surface": "rgba(255,255,255,0.03)",
              "accent": "#HEX"
            }},
            "typography": {{
              "heading_font": "Inter | Playfair Display",
              "body_font": "Inter"
            }},
            "vibe": "Cyber-Premium | Minimalist-Glass",
            "animations": "framer-motion-standard",
            "component_style": "shadcn-inspired"
          }},
          "marketing_copy": {{
            "hero_title": "...",
            "hero_subtitle": "...",
            "cta_text": "..."
          }},
          "modules": [ ... ],
          "scores": {{ "clarity": "A", "premium_index": "9/10" }}
        }}
        """
        # --- [REPLACE PROMPT BLOCK END] ---

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

            # --- [INSERT BEFORE return product] ---
            # 🧪 LOVABLE.AI BENCHMARK DEBUG EXPORT
            print("\n" + "=" * 50)
            print("🚀 LOVABLE.AI COPY-PASTE PROMPT START")
            print("=" * 50)
            lovable_prompt = f"""
            Act as a World-Class Frontend Developer. Build a high-fidelity React component for: {
                product.get("name")
            }

            VIBE: {product.get("design_tokens", {}).get("vibe")}
            COLORS: Primary {
                product.get("design_tokens", {}).get("colors", {}).get("primary")
            }, BG #030712
            DESCRIPTION: {product.get("description")}

            "theme_config": {
                "vibe_key": "cyber_midnight", // Evaluator chooses from: cyber_midnight, solar_white, emerald_glass
                "glow_color": "#HEX",
                "glass_opacity": "0.03"
              },

            MARKETING COPY:
            - Title: {product.get("marketing_copy", {}).get("hero_title")}
            - Subtitle: {product.get("marketing_copy", {}).get("hero_subtitle")}
            - CTA: {product.get("marketing_copy", {}).get("cta_text")}

            FEATURES TO INCLUDE:
            {json.dumps(product.get("modules"), indent=2)}

            TECH STACK: Vite, React, Tailwind CSS, Lucide Icons, Framer Motion.
            STYLE GUIDE: Use glassmorphism, 1px borders (white/10), and neon glow effects.
            """
            print(lovable_prompt)
            print("=" * 50)
            print("🚀 LOVABLE.AI COPY-PASTE PROMPT END\n")
        # ---------------------------------------

        return product
