from agents.agent_base import AgentBase
from tools.json_parser import extract_json
import json

# These are checker debugs
print("🔥 DEBUG: CTOAgent LOADEDv2")


class CTOAgent(AgentBase):
    def __init__(self):
        super().__init__("CTO Agent")

    def design_architecture(self, input_data):
        # These are checker debugs
        print("🚀 DEBUG: CTO design_architecture EXECUTEDv2")
        # 🔥 Extract idea and product properly
        if isinstance(input_data, dict):
            idea = input_data.get("idea", {})
            product = input_data.get("product", {})
        else:
            idea = input_data
            product = {}

        prompt = f"""
        You are a senior software architect.
        
        Design a production-ready SaaS architecture.
        
        Startup Idea:
        {json.dumps(idea, indent=2)}
        
        Product Definition:
        {json.dumps(product, indent=2)}
        
        IMPORTANT:
        Use product["modules"] and product["core_features"] to design backend modules.
        Modules must directly map to backend structure (routes, services, models).
        
        IMPORTANT:
        Use product features to design real APIs and modules.
        
        Return ONLY JSON:
        
        {{
          "backend": "Flask",
          "database": "SQLite",
          "models": ["User"],
          "routes": ["/", "/signup", "/login", "/dashboard"],
          "pages": ["index.html", "dashboard.html"],
          "features": ["list of features"],
          "modules": [
                {{
                    "name": "module_name",
                    "description": "what it does",
                    "features": ["feature1", "feature2"]
                }}
            ]
        }}
        
        Do NOT explain anything.
        """

        response = self.think(prompt)

        architecture = extract_json(response)

        if not architecture:
            print("[CTO Agent] Invalid architecture JSON")
            return None

        return architecture
