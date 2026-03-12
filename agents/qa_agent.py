from agents.agent_base import AgentBase

class QAAgent(AgentBase):
    def __init__(self):
        super().__init__("QA Agent")

    def test_product(self, build):
        return self.execute(f"Testing {build}")