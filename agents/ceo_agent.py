from agents.agent_base import AgentBase

class CEOAgent(AgentBase):
    def __init__(self):
        super().__init__("CEO Agent")

    def generate_idea(self):
        return self.think("Generate startup idea")