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
import os

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

        print("\n==============================")
        print("🚀 STARTUP GENERATION STARTED")
        print("==============================")

        print(idea)
        arch = self.safe_run(
            "CTO Agent",
            self.cto.design_architecture,
            idea
        )

        print("[Developer Agent] building MVP...")
        project_path = self.safe_run(
            "Developer Agent",
            self.dev.build_mvp,
            idea
        )

        if not project_path:
            print("Developer failed — aborting startup cycle.")
            return
        print(project_path)

        
        project_name = os.path.basename(project_path)
        print("REPO NAME BEING CREATED:", project_name)

        repo = self.safe_run(
            "GitHub Agent",
            self.github.create_repo_and_push,
            project_name
        )
        print(repo)

        test = self.safe_run(
            "QA Agent",
            self.qa.test_product,
            project_path
        )

        # 2. Update this line to pass the idea_id to your deployment agent
        deploy = self.safe_run(
            "Deployment Agent",
            self.deploy.deploy,
            project_path,
            idea_id=idea_id
        )
        if deploy:
            print("\n🚀 STARTUP IS LIVE:", deploy)

        # ---- SAVE DEPLOYMENT TO MEMORY ----
        try:

            name = idea.get("name") if isinstance(idea, dict) else str(idea)
            description = idea.get("description") if isinstance(idea, dict) else ""

            add_entry("startups.json", {
                "name": name,
                "description": description,
                "project_path": project_path,
                "status": "deployed",
                "url": deploy
            })

        except Exception as e:
            print("Memory write failed:", e)

        # ----------------------------------

        marketing = self.safe_run(
            "Growth Agent",
            self.growth.launch_marketing,
            project_path
        )
        revenue = self.safe_run(
            "Finance Agent",
            self.finance.track_revenue,
            project_path
        )
        print(revenue)
        try:
            update_context()
        except Exception as e:
            print("Context update failed:", e)

    def safe_run(self, agent_name, func, *args, **kwargs):

        print(f"\n[{agent_name}] starting...")

        try:
            result = func(*args, **kwargs)

            print(f"[{agent_name}] completed successfully")

            return result

        except Exception as e:

            print(f"[{agent_name}] FAILED:", e)

            return None

def update_context():

    print("Updating codebase context...")

    subprocess.Popen(["python", "generate_context.py"])

    print("Context snapshot refreshed.")

if __name__ == "__main__":

    o = Orchestrator()

    idea = {
        "name": "Test Startup",
        "description": "Testing pipeline"
    }

    o.run_startup_cycle(idea)

