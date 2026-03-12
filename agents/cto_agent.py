from agents.agent_base import AgentBase

class CTOAgent(AgentBase):
    def __init__(self):
        super().__init__("CTO Agent")

    def design_architecture(self, idea):
        return self.think(f"Design architecture for {idea}")