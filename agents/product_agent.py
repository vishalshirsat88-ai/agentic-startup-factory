from agents.agent_base import AgentBase
from tools.json_parser import extract_json

# These are checker debugs


class ProductAgent(AgentBase):
    def __init__(self):
        super().__init__("Product Agent")

    def define_product(self, idea):
        # These are checker debugs
        print("🚀 DEBUG: ProductAgent EXECUTED v1")
        prompt = f"""
        You are a product manager.

        Convert this startup idea into structured product features.

        Startup Idea:
        {idea}
        
        Break the product into 3–6 modules.
        Each module should represent a backend component (like users, orders, analytics, etc).

        Return ONLY JSON:

        {{
          "name": "product name",
          "description": "short description",
          "modules": [
            {{
              "name": "module_name",
              "description": "what this module does",
              "features": ["feature1", "feature2"]
            }}
          ],
          "user_flows": ["flow1", "flow2"],
          "edge_cases": ["case1", "case2"]
        }}

        Do not explain anything.
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
