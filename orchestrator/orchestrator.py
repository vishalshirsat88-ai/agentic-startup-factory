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
from tools.product_loop import ProductLoop
import signal
import subprocess
import os
import re
import sys

from tools.code_runner import run_app

# These are checker debugs
print("🔥 DEBUG: Orchestrator LOADED v11")

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
        # These are checker debugs
        print("🚀 DEBUG: run_startup_cycle EXECUTED v1")

        print("ORCHESTRATOR RECEIVED IDEA:", idea)
        print("\n==============================")
        print("🚀 STARTUP GENERATION STARTED")
        print("==============================")

        print(idea)
        print("[Product Agent] defining product features...")

        print("STEP 1: Entered run_startup_cycle")

        print("STEP 2: Before Product Agent")
        product = self.safe_run("Product Agent", self.product.define_product, idea)

        # 🔥 CRITICAL FIX: Ensure product is NEVER None
        if not product or not isinstance(product, dict):
            print("⚠️ Product Agent failed → using fallback")

            product = {
                "name": idea.get("name", "Startup")
                if isinstance(idea, dict)
                else "Startup",
                "description": idea.get("description", "Auto-generated"),
                "design_tokens": {},
                "marketing_copy": {},
                "modules": [],
            }
        print("STEP 3: After Product Agent")

        print("STEP 4: Before CTO Agent")
        arch = self.safe_run(
            "CTO Agent",
            self.cto.design_architecture,
            {"idea": idea, "product": product},
        )
        # 🔥 CRITICAL: Ensure arch has the full product context for the Developer
        if arch and isinstance(arch, dict):
            arch["product"] = product
        print("STEP 5: After CTO Agent")
        # 🔥 CRITICAL: Bridge the Product Agent tokens into the Architecture for the Developer

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

                print("🚀 SWITCHING TO GENERATED APP...")

                # --- START AUTO-DETECT LOGIC ---
                possible_files = ["app.py", "main.py", "server.py", "run.py"]
                app_path = None

                # 1. Try preferred filenames first
                for f in possible_files:
                    path = os.path.join(project_path, f)
                    if os.path.exists(path):
                        app_path = path
                        break

                # 2. Fallback: If no preferred file, find any .py file in the root
                if not app_path:
                    all_py_files = [
                        f for f in os.listdir(project_path) if f.endswith(".py")
                    ]
                    if all_py_files:
                        app_path = os.path.join(project_path, all_py_files[0])

                if app_path:
                    import sys

                    print(f"🚀 [AUTO-DETECT] Running entry point: {app_path}")

                    os.environ["PORT"] = "3000"

                    os.execv(sys.executable, [sys.executable, app_path])
                else:
                    print(f"❌ ERROR: No runnable python files found in {project_path}")
                # --- END AUTO-DETECT LOGIC ---

                break

            print("[DEV LOOP] Error detected:")
            print(output)

            # 🔥 HANDLE TIMEOUT (NOT CODE ISSUE)
            if "timed out" in output.lower():
                print("[DEV LOOP] Timeout detected → skipping fix")
                break

            # ✅ STOP if same error repeats (Patrick pattern)
            if output in seen_errors:
                print("[DEV LOOP] Same error repeating → stopping early")
                break

            seen_errors.add(output)

            print("[DEV LOOP] Sending error to Developer Agent for fix...")

            # 🔥 Extract error file from traceback
            matches = re.findall(r'File "(.+?\.py)"', output)

            if matches:
                error_file = matches[-1]  # 🔥 take LAST file (actual error source)

                # Ensure file exists before fixing
                if not os.path.exists(error_file):
                    print(f"[DEV LOOP] File not found: {error_file}")
                    break
                print(f"[DEV LOOP] Targeting error file: {error_file}")
            else:
                print("[DEV LOOP] Could not detect error file, skipping fix")
                break

            try:
                with open(error_file, "r") as f:
                    code = f.read()

                fix_prompt = f"""Fix syntax and indentation errors in this Python file.

Return ONLY valid Python code.

Code:
{code}
"""

                fixed_code = self.dev.think(fix_prompt)

                if not fixed_code or len(fixed_code.strip()) < 10:
                    print("[DEV LOOP] Skipping overwrite due to invalid fix")
                    continue

                if "```" in fixed_code:
                    fixed_code = fixed_code.replace("```python", "").replace("```", "")

                fixed_code = fixed_code.strip()

                if fixed_code.startswith("python"):
                    fixed_code = fixed_code.replace("python", "", 1).strip()

                import textwrap

                fixed_code = textwrap.dedent(fixed_code)

                with open(error_file, "w") as f:
                    f.write(fixed_code)

                print(f"[DEV LOOP] Fixed: {error_file}")

            except Exception as e:
                print(f"[DEV LOOP] Failed fixing {error_file}: {e}")

        if not build_success:
            print("[DEV LOOP] Max attempts reached. Continuing anyway.")

        # -------- END DEV LOOP --------

        print("\n[QA AGENT] Starting product validation...")

        validation_report = self.qa.test_product(project_path)

        print("\n==============================")
        print("📊 FINAL VALIDATION REPORT")
        print("==============================")
        print(validation_report)

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
                    "status": "validated",
                    "url": deploy,
                    "validation": validation_report,
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
