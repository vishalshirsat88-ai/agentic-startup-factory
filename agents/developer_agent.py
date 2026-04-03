from agents.agent_base import AgentBase
from tools.file_writer import write_file
from tools.code_runner import run_app
import os
import re
import json
import time
import shutil
import traceback  # add at top if not already


class DeveloperAgent(AgentBase):
    def __init__(self):
        super().__init__("Developer Agent")

    def extract_project_name(self, idea):
        # If idea is dictionary (new CEO agent format)
        if isinstance(idea, dict):
            name = idea.get("name", "startup")

            # create slug
            slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.lower()).strip("-")

            # limit length for GitHub repo safety
            slug = slug[:25]

            return f"{slug}-{int(time.time()) % 100000}"

        # If idea is text (older format)
        for line in idea.splitlines():
            if "name" in line.lower():
                words = re.findall(r"[A-Za-z0-9_-]+", line)

                if len(words) >= 2:
                    return words[1].lower()

        words = re.findall(r"[A-Za-z]+", idea)

        if words:
            return words[0].lower()

        return "startup"

    def detect_dependencies(self, code):
        deps = set()

        if "flask_sqlalchemy" in code.lower():
            deps.add("Flask-SQLAlchemy==3.0.5")

        if "flask_login" in code.lower():
            deps.add("Flask-Login==0.6.3")

        if "requests" in code:
            deps.add("requests==2.31.0")

        if "pandas" in code:
            deps.add("pandas==2.2.2")

        return deps

    def validate_backend_structure(self, project_dir):
        services_dir = os.path.join(project_dir, "services")
        routes_dir = os.path.join(project_dir, "routes")

        if not os.path.exists(services_dir) or not os.path.exists(routes_dir):
            print("[Developer Agent] Missing backend folders")
            return False

        for file in os.listdir(routes_dir):
            if file.endswith("_routes.py"):
                service_name = file.replace("_routes.py", "_service.py")
                service_path = os.path.join(services_dir, service_name)

                if not os.path.exists(service_path):
                    print(f"[Developer Agent] Missing service for {file}")
                    return False

        return True

    def copy_template(self, project_dir):
        template_path = "saas_master_template"

        if not os.path.exists(template_path):
            raise Exception("SaaS template not found")

        shutil.copytree(template_path, project_dir, dirs_exist_ok=True)

    def build_mvp(self, idea, architecture=None):
        print("DEBUG IDEA TEXT:")
        print(json.dumps(idea, indent=2) if isinstance(idea, dict) else idea)
        print("✅ ENTERED build_mvp")
        project_dir = None  # 🔥 track explicitly
        project_name = self.extract_project_name(idea)

        print("EXTRACTED PROJECT NAME:", project_name)

        project_dir = f"projects/{project_name}"
        print("📁 PROJECT DIR SET:", project_dir)
        os.makedirs(project_dir, exist_ok=True)

        # ✅ NEW: Copy SaaS template
        if not os.path.exists(project_dir):
            os.makedirs(project_dir, exist_ok=True)

        self.copy_template(project_dir)

        app_file = os.path.join(project_dir, "app.py")

        if os.path.exists(app_file):
            with open(app_file, "r") as f:
                content = f.read()

            # Extract idea safely
            product_name = "AI Tool"
            product_description = "AI powered solution"
            product_features = []

            if isinstance(idea, dict):
                product_name = idea.get("name", product_name)
                product_description = idea.get("description", product_description)

            # ✅ NEW: Extract features from architecture
            if architecture and isinstance(architecture, dict):
                product_features = architecture.get("features", [])

            # Replace PRODUCT_NAME
            content = content.replace(
                'PRODUCT_NAME = "AI Resume Builder"', f'PRODUCT_NAME = "{product_name}"'
            )

            # ✅ Inject features into template (basic version)
            features_text = (
                ", ".join(product_features)
                if product_features
                else "AI-powered features"
            )

            content = content.replace(
                'feature_1_title="AI Resume Analysis"',
                f'feature_1_title="{features_text}"',
            )

            # Optional: Inject description if you add it later in template
            content = content.replace(
                'product_description="Our AI analyzes job descriptions and builds optimized resumes."',
                f'product_description="{product_description}"',
            )

            with open(app_file, "w") as f:
                f.write(content)

            print("[Developer Agent] Injected idea into SaaS template")
        else:
            print("[Developer Agent] app.py not found for injection")

        # ✅ STOP LLM GENERATION — USE TEMPLATE ONLY

        print("[Developer Agent] Using SaaS template — skipping LLM generation")
        print("[Developer Agent] Enforcing backend API contract...")

        if architecture:
            for module in architecture.get("modules", []):
                print(f"[Developer Agent] Preparing module: {module}")

        # ✅ Ensure requirements.txt exists
        req_path = f"{project_dir}/requirements.txt"

        requirements = """Flask==2.2.5
gunicorn==21.2.0
Werkzeug==2.2.3
"""

        with open(req_path, "w") as f:
            f.write(requirements)

        print("[Developer Agent] requirements.txt created")

        # ✅ FORCE correct Procfile for Railway

        procfile_path = f"{project_dir}/Procfile"

        with open(procfile_path, "w") as f:
            f.write("web: gunicorn app:app --bind 0.0.0.0:$PORT")

        print("[Developer Agent] Procfile fixed")

        # 🔥 GENERATE BACKEND FILES

        from engine.file_generator import generate_backend_files

        # 🔥 ADD THIS BLOCK BEFORE CALL
        if architecture and isinstance(architecture, dict):
            architecture["idea"] = idea

        try:
            if architecture:
                generate_backend_files(project_dir, architecture)
            else:
                print(
                    "[Developer Agent] No architecture provided — skipping backend generation"
                )
        except Exception as e:
            print("❌ FULL BACKEND ERROR BELOW:")
            traceback.print_exc()
            raise e

        # 🔥 VALIDATE BACKEND

        if not self.validate_backend_structure(project_dir):
            print("⚠️ Backend validation failed — continuing")

        # 🔥 AUTO WIRE ROUTES
        from engine.auto_wire import wire_routes

        try:
            wire_routes(project_dir)
            print("[Developer Agent] Backend + Routes successfully wired")
        except Exception as e:
            print("⚠️ Auto-wire failed:", e)

        # ✅ RETURN PROJECT DIR (CRITICAL FIX)

        # 🔥 FORCE SAFETY
        if not project_dir:
            print("⚠️ project_dir is None — fixing fallback")
            project_dir = "projects/fallback_project"

        print("✅ FINAL RETURN:", project_dir)
        print("🔥 RETURN TYPE:", type(project_dir))
        return project_dir
