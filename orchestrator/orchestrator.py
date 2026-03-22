from agents.ceo_agent import CEOAgent
from agents.cto_agent import CTOAgent
from agents.product_agent import ProductAgent
from agents.developer_agent import DeveloperAgent
from agents.qa_agent import QAAgent
from agents.deployment_agent import DeploymentAgent
from agents.growth_agent import GrowthAgent
from agents.finance_agent import FinanceAgent
from agents.github_agent import GitHubAgent
from tools.memory import add_entry
import subprocess
import os
from tools.code_runner import run_app

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
            idea,
            arch
        )

        if not project_path:
            print("Developer failed — aborting startup cycle.")
            return
        print(project_path)
        
        project_name = os.path.basename(project_path)
        print("REPO NAME BEING CREATED:", project_name)

         
        # -------- TEMPLATE VALIDATION --------

        print("\n[QA CHECK] Validating Flask template usage...")

        app_file = os.path.join(project_path, "app.py")

        try:

            if not os.path.exists(app_file):

                print("[QA CHECK] app.py not found, skipping template validation")

            else:

                with open(app_file, "r") as f:
                    app_code = f.read()

                if "render_template(" not in app_code:

                    print("[QA CHECK] FAILED: app.py does not use render_template")

                    fix_prompt = f"""
            The Flask application below does not render templates.

            Fix the code so it uses render_template() for pages.

            Required routes:
            / -> landing page
            /login -> login page
            /dashboard -> dashboard page

            Return ONLY corrected Python code for app.py.

            Current code:
            {app_code}
            """

                    fixed_code = self.dev.think(fix_prompt)

                    if "```" in fixed_code:
                        fixed_code = fixed_code.replace("```python", "").replace("```", "")

                    with open(app_file, "w") as f:
                        f.write(fixed_code)

                    print("[QA CHECK] Developer Agent fixed template issue")

                else:
                    print("[QA CHECK] Template usage OK")

        except Exception as e:
            print("[QA CHECK] Validation failed:", e)

        # -------- END TEMPLATE VALIDATION --------
        
        # -------- UPDATE CODEBASE CONTEXT --------

        try:
            update_context()
        except Exception as e:
            print("Context update failed:", e)

        # -----------------------------------------
        
        # -------- AUTONOMOUS DEV LOOP --------

        print("\n[DEV LOOP] Starting autonomous debug cycle...")

        max_attempts = 5
        build_success = False

        for attempt in range(max_attempts):

            print(f"[DEV LOOP] Attempt {attempt+1}")

            success, output = run_app(project_path)

            if success:
                print("[DEV LOOP] Application started successfully")
                build_success = True
                break

            print("[DEV LOOP] Error detected:")
            print(output)

            print("[DEV LOOP] Sending error to Developer Agent for fix...")

            fix_prompt = f"""
The following Flask application produced an error.

            Error log:
            {output}

            Provide corrected Python code for app.py only.
            Return ONLY valid Python code.
            """

            fixed_code = self.dev.think(fix_prompt)

            # Remove markdown formatting if present
            if "```" in fixed_code:
                fixed_code = fixed_code.replace("```python", "").replace("```", "")

            # Remove accidental explanations before code
            lines = fixed_code.splitlines()
            clean_lines = []

            for line in lines:
                if (
                    line.strip().startswith("from ")
                    or line.strip().startswith("import ")
                    or line.strip().startswith("app")
                    or line.strip().startswith("@")
                    or line.strip().startswith("def")
                    or line.strip().startswith("if __name__")
                ):
                    clean_lines.append(line)
                elif clean_lines:
                    clean_lines.append(line)

            fixed_code = "\n".join(clean_lines)

            app_file = os.path.join(project_path, "app.py")

            print("[DEV LOOP] Writing cleaned code to app.py")

            try:
                with open(app_file, "w") as f:
                    f.write(fixed_code)

                print("[DEV LOOP] Updated app.py with fix")

            except Exception as e:
                print("[DEV LOOP] Failed to write fix:", e)

        if not build_success:
            print("[DEV LOOP] Max attempts reached. Continuing anyway.")

        # -------- END DEV LOOP --------

        repo = self.safe_run(
            "GitHub Agent",
            self.github.create_repo_and_push,
            project_name
        )
        print(repo)

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

    subprocess.run(["python", "generate_context.py"], check=False)

    print("Context snapshot refreshed.")

if __name__ == "__main__":

    o = Orchestrator()

    idea = {
        "name": "Test Startup",
        "description": "Testing pipeline"
    }

    o.run_startup_cycle(idea)

