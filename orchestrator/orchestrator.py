from agents.ceo_agent import CEOAgent
from agents.cto_agent import CTOAgent
from agents.developer_agent import DeveloperAgent
from agents.qa_agent import QAAgent
from agents.deployment_agent import DeploymentAgent
from agents.growth_agent import GrowthAgent
from agents.finance_agent import FinanceAgent

MODE = "controlled"

class Orchestrator:

    def __init__(self):
        self.ceo = CEOAgent()
        self.cto = CTOAgent()
        self.dev = DeveloperAgent()
        self.qa = QAAgent()
        self.deploy = DeploymentAgent()
        self.growth = GrowthAgent()
        self.finance = FinanceAgent()

    def run_startup_cycle(self):

        idea = self.ceo.generate_idea()
        print(idea)

        approval = input("Approve idea? (y/n): ")
        if approval != "y":
            print("Idea rejected")
            return

        arch = self.cto.design_architecture(idea)
        print(arch)

        build = self.dev.build_feature(arch)
        print(build)

        test = self.qa.test_product(build)
        print(test)

        deploy = self.deploy.deploy(build)
        print(deploy)

        marketing = self.growth.launch_marketing(build)
        print(marketing)

        revenue = self.finance.track_revenue(build)
        print(revenue)

if __name__ == "__main__":
    o = Orchestrator()
    o.run_startup_cycle()