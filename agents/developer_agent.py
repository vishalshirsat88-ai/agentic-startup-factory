from agents.agent_base import AgentBase
from tools.file_writer import write_file
from tools.code_runner import run_app
import os
import re
import json
import time
import shutil
import traceback  # add at top if not already

# These are checker debugs
print("🔥 DEBUG: DeveloperAgent LOADED v2")


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
        # These are checker debugs
        print("🚀 DEBUG: build_mvp EXECUTED v1")

        print("DEBUG IDEA TEXT:")
        print(json.dumps(idea, indent=2) if isinstance(idea, dict) else idea)
        print("✅ ENTERED build_mvp")
        project_dir = None  # 🔥 track explicitly
        if idea:
            project_name = self.extract_project_name(idea)
        elif architecture and isinstance(architecture, dict):
            project_name = self.extract_project_name(architecture.get("product", {}))
        else:
            project_name = "startup"

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

            # 🔥 Prefer product features over architecture
            if architecture and isinstance(architecture, dict):
                # Try product first
                product_data = architecture.get("product", {})

                if isinstance(product_data, dict):
                    modules = product_data.get("modules", [])

                    if modules:
                        # extract features from modules
                        product_features = [
                            feature
                            for module in modules
                            for feature in module.get("features", [])
                        ]

                # fallback to architecture features
                if not product_features:
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
                if isinstance(module, dict):
                    module_name = module.get("name", "core")
                    module_features = module.get("features", [])

                    print(f"[Developer Agent] Preparing module: {module_name}")
                    print(f"  Features: {module_features}")

                else:
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

            # 🔥 NEW: pass product also if available
            if isinstance(idea, dict) and "product" in idea:
                architecture["product"] = idea["product"]

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
        # 🔥 AUTO FIX INDENTATION FOR ALL FILES
        import glob
        import textwrap

        print("[Developer Agent] Cleaning indentation across project...")

        py_files = glob.glob(os.path.join(project_dir, "**/*.py"), recursive=True)

        for file_path in py_files:
            try:
                with open(file_path, "r") as f:
                    code = f.read()

                cleaned_code = textwrap.dedent(code)

                with open(file_path, "w") as f:
                    f.write(cleaned_code)

            except Exception as e:
                print(f"[Developer Agent] Failed cleaning {file_path}:", e)
        return project_dir
