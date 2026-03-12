from agents.agent_base import AgentBase

class DeveloperAgent(AgentBase):
    def __init__(self):
        super().__init__("Developer Agent")

    def build_feature(self, architecture):
        return self.execute(f"Build MVP for {architecture}")