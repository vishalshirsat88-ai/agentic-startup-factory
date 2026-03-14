from agents.ceo_agent import CEOAgent
from agents.cto_agent import CTOAgent
from agents.developer_agent import DeveloperAgent
from agents.qa_agent import QAAgent
from agents.deployment_agent import DeploymentAgent
from agents.growth_agent import GrowthAgent
from agents.finance_agent import FinanceAgent
from agents.github_agent import GitHubAgent
from tools.memory import add_entry
import subprocess

class Orchestrator:

    def __init__(self):

        self.ceo = CEOAgent()
        self.cto = CTOAgent()
        self.dev = DeveloperAgent()
        self.qa = QAAgent()
        self.deploy = DeploymentAgent()
        self.growth = GrowthAgent()
        self.finance = FinanceAgent()
        self.github = GitHubAgent()

    # 1. Add 'idea_id=None' here. Keep your 'idea' name exactly as is.
    def run_startup_cycle(self, idea, idea_id=None): # New

        print(idea)
        arch = self.cto.design_architecture(idea)

        print("[Developer Agent] building MVP...")
        project_path = self.dev.build_mvp(idea)
        print(project_path)

        project_name = project_path.split("/")[-1]
        print("REPO NAME BEING CREATED:", project_name)

        repo = self.github.create_repo_and_push(project_name)
        print(repo)

        test = self.qa.test_product(project_path)

        # 2. Update this line to pass the idea_id to your deployment agent
        deploy = self.deploy.deploy(project_path, idea_id=idea_id)
        print(deploy)

        # ---- SAVE DEPLOYMENT TO MEMORY ----
        add_entry("startups.json", {
            "name": idea,
            "project_path": project_path,
            "status": "deployed",
            "url": deploy
        })

        # ----------------------------------

        marketing = self.growth.launch_marketing(project_path)
        revenue = self.finance.track_revenue(project_path)
        print(revenue)
        update_context()

def update_context():

    print("Updating codebase context...")

    subprocess.run(["python", "generate_context.py"])

    print("Context snapshot refreshed.")

if __name__ == "__main__":

    o = Orchestrator()
    o.run_startup_cycle()

