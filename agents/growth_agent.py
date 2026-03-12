from agents.agent_base import AgentBase

class GrowthAgent(AgentBase):
    def __init__(self):
        super().__init__("Growth Agent")

    def launch_marketing(self, product):
        return self.execute(f"Launch marketing for {product}")