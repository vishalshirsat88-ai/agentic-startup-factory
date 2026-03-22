from agents.agent_base import AgentBase
from tools.json_parser import extract_json

class ProductAgent(AgentBase):

    def __init__(self):
        super().__init__("Product Agent")

    def define_product(self, idea):

        prompt = f"""
        You are a product manager.

        Convert this startup idea into structured product features.

        Startup Idea:
        {idea}

        Return ONLY JSON:

        {{
          "core_features": ["feature1", "feature2"],
          "user_flows": ["flow1", "flow2"],
          "edge_cases": ["case1", "case2"]
        }}

        Do not explain anything.
        """

        response = self.think(prompt)

        product = extract_json(response)

        if not product:
            print("[Product Agent] Failed to parse product JSON")
            return None

        return product
