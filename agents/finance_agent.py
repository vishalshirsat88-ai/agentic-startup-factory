from agents.agent_base import AgentBase

class FinanceAgent(AgentBase):
    def __init__(self):
        super().__init__("Finance Agent")

    def track_revenue(self, product):
        return self.execute(f"Tracking revenue for {product}")