from agents.agent_base import AgentBase
from tools.json_parser import extract_json
import json


class CTOAgent(AgentBase):

    def __init__(self):
        super().__init__("CTO Agent")

    def design_architecture(self, idea):

        prompt = f"""
        You are a senior software architect.

        Design a simple micro-SaaS architecture.

        Startup Idea:
        {idea}

        Return ONLY valid JSON in this format:

        {{
          "backend": "Flask",
          "database": "SQLite",
          "models": ["User"],
          "routes": ["/", "/signup", "/login", "/dashboard"],
          "pages": ["index.html", "signup.html", "login.html", "dashboard.html"],
          "features": ["user authentication", "core feature of the startup"]
        }}

        Do NOT include explanations.
        Do NOT include markdown.
        """

        response = self.think(prompt)

        architecture = extract_json(response)

        if not architecture:
            print("[CTO Agent] Invalid architecture JSON")
            return None

        return architecture