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
from engine.file_generator import generate_backend_files
from engine.auto_wire import wire_routes
import subprocess
import os
from tools.code_runner import run_app

print("🔥🔥🔥 THIS ORCHESTRATOR IS RUNNING:", __file__)


class Orchestrator:
    def __init__(self):
        self.ceo = CEOAgent()
        self.cto = CTOAgent()
        self.product = ProductAgent()
        self.dev = DeveloperAgent()
        self.qa = QAAgent()
        self.deploy = DeploymentAgent()
        self.growth = GrowthAgent()
        self.finance = FinanceAgent()
        self.github = GitHubAgent()

    # 1. Add 'idea_id=None' here. Keep your 'idea' name exactly as is.

    def run_startup_cycle(self, idea, idea_id=None):  # New
        print("ORCHESTRATOR RECEIVED IDEA:", idea)
        print("\n==============================")
        print("🚀 STARTUP GENERATION STARTED")
        print("==============================")

        print(idea)
        print("[Product Agent] defining product features...")

        print("STEP 1: Entered run_startup_cycle")

        print("STEP 2: Before Product Agent")
        product = self.safe_run("Product Agent", self.product.define_product, idea)
        print("STEP 3: After Product Agent")

        print("STEP 4: Before CTO Agent")
        arch = self.safe_run(
            "CTO Agent",
            self.cto.design_architecture,
            {"idea": idea, "product": product},
        )
        print("STEP 5: After CTO Agent")

        print("STEP 6: Before Developer Agent")
        print("\n[Developer Agent] starting...")

        project_path = self.dev.build_mvp(idea, arch)

        print("[Developer Agent] DIRECT RETURN:", project_path)
        print("STEP 7: After Developer Agent → project_path:", project_path)

        if not project_path:
            raise Exception("❌ CRITICAL: DeveloperAgent returned None")

        print("PROJECT GENERATED AT:", project_path)

        project_name = os.path.basename(project_path)
        print("REPO NAME BEING CREATED:", project_name)

        # -------- TEMPLATE VALIDATION --------

        print("\n[QA CHECK] Validating Flask template usage...")

        # 🔥 Dynamically find Flask app file
        app_file = None

        for file in os.listdir(project_path):
            if file.endswith(".py"):
                path = os.path.join(project_path, file)
                with open(path, "r") as f:
                    for line in f:
                        if "Flask(__name__)" in line:
                            app_file = path
                            break
                if app_file:
                    break
        try:
            if not app_file:
                print("[QA CHECK] No Flask app file found, skipping validation")
            else:
                with open(app_file, "r") as f:
                    app_code = f.read()

                if "render_template(" not in app_code:
                    print(
                        f"[QA CHECK] FAILED in {os.path.basename(app_file)}: render_template missing"
                    )

                    fix_prompt = f"""
            The Flask application below does not render templates.
    
            Fix the code so it uses render_template() for pages.
    
            Required routes:
            / -> landing page
            /login -> login page
            /dashboard -> dashboard page
    
            Return ONLY corrected Python code for the Flask app file.
    
            Current code:
            {app_code}
            """

                    fixed_code = self.dev.think(fix_prompt)

                    if "```" in fixed_code:
                        fixed_code = fixed_code.replace("```python", "").replace(
                            "```", ""
                        )

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
        seen_errors = set()

        for attempt in range(max_attempts):
            print(f"[DEV LOOP] Attempt {attempt + 1}")

            success, output = run_app(project_path)

            if success:
                print("[DEV LOOP] Application started successfully")
                build_success = True
                break

            print("[DEV LOOP] Error detected:")
            print(output)

            # ✅ STOP if same error repeats (Patrick pattern)
            if output in seen_errors:
                print("[DEV LOOP] Same error repeating → stopping early")
                break

            seen_errors.add(output)

            print("[DEV LOOP] Sending error to Developer Agent for fix...")

            fix_prompt = f"""The following Flask application produced an error.

Error log:
{output}

The app is part of a SaaS platform.

Fix the issue while preserving:
- existing routes
- existing structure

Fix ONLY what is necessary in app.py.

Return ONLY valid Python code.
Do NOT include markdown or explanation.
"""

            fixed_code = self.dev.think(fix_prompt).strip()

            # ✅ REMOVE markdown if present
            if "```" in fixed_code:
                fixed_code = fixed_code.split("```")[1]

            # ✅ FIX INDENTATION ISSUE (YOUR BUG)
            import textwrap

            fixed_code = textwrap.dedent(fixed_code)

            app_file = os.path.join(project_path, "app.py")

            if not os.path.exists(app_file):
                print("[DEV LOOP] app.py not found → skipping fix")
                break

            try:
                with open(app_file, "w") as f:
                    f.write(fixed_code)

                print("[DEV LOOP] Updated app.py with fix")

            except Exception as e:
                print("[DEV LOOP] Failed to write fix:", e)

        if not build_success:
            print("[DEV LOOP] Max attempts reached. Continuing anyway.")

        # -------- END DEV LOOP --------

        # repo = self.safe_run(
        # "GitHub Agent",
        # self.github.create_repo_and_push,
        # project_name,
        # )
        # -------- ENV-BASED EXECUTION --------

        print("RAW ENV VALUE:", os.getenv("ENV"))

        env = os.getenv("ENV", "local")
        print(f"[ENV] Running in {env} mode")

        if env == "local":
            print("[GitHub Agent] Skipped (local mode)")
            repo = None

            print("[Deployment Agent] Skipped (local mode)")
            deploy = None

        else:
            # ✅ GitHub push
            repo = self.safe_run(
                "GitHub Agent",
                self.github.create_repo_and_push,
                project_name,
            )
            print("GitHub Repo:", repo)

            # ✅ Deployment
            deploy = self.safe_run(
                "Deployment Agent", self.deploy.deploy, project_path, idea_id=idea_id
            )
            print("Deployment URL:", deploy)

        if deploy and "failed" not in str(deploy).lower():
            print("🚀 STARTUP IS LIVE:", deploy)
        else:
            print("⚠️ Deployment failed or skipped")

        # ---- SAVE DEPLOYMENT TO MEMORY ----
        try:
            name = idea.get("name") if isinstance(idea, dict) else str(idea)
            description = idea.get("description") if isinstance(idea, dict) else ""

            add_entry(
                "startups.json",
                {
                    "name": name,
                    "description": description,
                    "project_path": project_path,
                    "status": "deployed",
                    "url": deploy,
                },
            )

        except Exception as e:
            print("Memory write failed:", e)

        # ----------------------------------

        marketing = self.safe_run(
            "Growth Agent", self.growth.launch_marketing, project_path
        )
        revenue = self.safe_run(
            "Finance Agent", self.finance.track_revenue, project_path
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

            if result is None:
                print(f"⚠️ WARNING: {agent_name} returned None")

            else:
                print(f"[{agent_name}] RETURN VALUE:", result)

            return result

        except Exception as e:
            print(f"[{agent_name}] FAILED:", str(e))

            raise  # 🔥 DO NOT SWALLOW


def update_context():
    print("Updating codebase context...")

    subprocess.run(["python", "generate_context.py"], check=False)

    print("Context snapshot refreshed.")


if __name__ == "__main__":
    o = Orchestrator()

    idea = {"name": "Test Startup", "description": "Testing pipeline"}

    o.run_startup_cycle(idea)
