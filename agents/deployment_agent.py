from agents.agent_base import AgentBase

class DeploymentAgent(AgentBase):
    def __init__(self):
        super().__init__("Deployment Agent")

    def deploy(self, build):
        return self.execute(f"Deploying {build}")