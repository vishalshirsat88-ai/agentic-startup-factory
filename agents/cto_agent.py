from agents.agent_base import AgentBase
from tools.json_parser import extract_json
import json


class CTOAgent(AgentBase):

    def __init__(self):
        super().__init__("CTO Agent")

    def design_architecture(self, idea):

        prompt = f"""
        You are a senior software architect.
        
        Design a production-ready SaaS architecture.
        
        Startup Context:
        {idea}
        
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
          "modules": ["auth", "core_logic", "payments"]
        }}
        
        Do NOT explain anything.
        """

        response = self.think(prompt)

        architecture = extract_json(response)

        if not architecture:
            print("[CTO Agent] Invalid architecture JSON")
            return None

        return architecture
