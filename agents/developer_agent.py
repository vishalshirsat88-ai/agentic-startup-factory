from agents.agent_base import AgentBase
from tools.file_writer import write_file
from tools.code_runner import run_app
import os
import re
import json
import time
import shutil

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

            return f"{slug}-{int(time.time())%100000}"

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


   

    def copy_template(self, project_dir):
        template_path = "saas_master_template"

        if not os.path.exists(template_path):
            raise Exception("SaaS template not found")

        shutil.copytree(template_path, project_dir, dirs_exist_ok=True)

    def build_mvp(self, idea, architecture=None):

        print("DEBUG IDEA TEXT:")
        print(json.dumps(idea, indent=2) if isinstance(idea, dict) else idea)

        project_name = self.extract_project_name(idea)

        print("EXTRACTED PROJECT NAME:", project_name)

        project_dir = f"projects/{project_name}"
        os.makedirs(project_dir, exist_ok=True)
        
        # ✅ NEW: Copy SaaS template
        self.copy_template(project_dir)
        
        app_file = os.path.join(project_dir, "app.py")

        if os.path.exists(app_file):

            with open(app_file, "r") as f:
                content = f.read()

            # Extract idea safely (your CEO agent sends dict)
            product_name = "AI Tool"
            product_description = "AI powered solution"

            if isinstance(idea, dict):
                product_name = idea.get("name", product_name)
                product_description = idea.get("description", product_description)

            # Replace PRODUCT_NAME
            content = content.replace(
                'PRODUCT_NAME = "AI Resume Builder"',
                f'PRODUCT_NAME = "{product_name}"'
            )

            # Optional: Inject description if you add it later in template
            content = content.replace(
                'product_description="Our AI analyzes job descriptions and builds optimized resumes."',
                f'product_description="{product_description}"'
            )

            with open(app_file, "w") as f:
                f.write(content)

            print("[Developer Agent] Injected idea into SaaS template")
        else:
            print("[Developer Agent] app.py not found for injection")

        # ✅ STOP LLM GENERATION — USE TEMPLATE ONLY

        print("[Developer Agent] Using SaaS template — skipping LLM generation")

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

        # Run debug
        self.auto_debug(project_dir)

        return project_dir


        # Optional: still run debug to ensure app runs
        self.auto_debug(project_dir)

        return project_dir
        
        arch_text = ""

        if architecture:
            arch_text = f"""

        Architecture Specification:
        {json.dumps(architecture, indent=2)}

        Follow this architecture when generating the SaaS application.

        """
        prompt = f"""
        {arch_text}

        Build a simple Flask MVP for this startup idea.

        Rules:

        - Use Flask
        - Generate a SaaS web application
        - You MUST use templates with render_template
        - Include signup, login and dashboard pages
        - Include SQLite database for users
        - Include import os at the top
        - The Flask server must start using:

        if __name__ == "__main__":
            port = int(os.environ.get("PORT", 5000))
            app.run(host="0.0.0.0", port=port)

        Do NOT run app.run() outside this block.

        Database architecture rules:

        - db.py must initialize the SQLite database connection
        - models.py must define a User model/table
        - app.py must import db.py and models.py
        - Signup route must create users in the database
        - Login route must authenticate users from the database

        Project structure:

        FILE: app.py
        FILE: db.py
        FILE: models.py
        FILE: requirements.txt
        FILE: Procfile
        FILE: README.md
        FILE: templates/index.html
        FILE: templates/signup.html
        FILE: templates/login.html
        FILE: templates/dashboard.html
        FILE: static/style.css

        Idea Name: {idea.get("name","") if isinstance(idea, dict) else idea}
        Description: {idea.get("description","") if isinstance(idea, dict) else ""}

        Generate the following files EXACTLY in this format.

        FILE: app.py
        ...
        FILE: requirements.txt
        Flask==2.2.5
        gunicorn==21.2.0
        Werkzeug==2.2.3

        Additional requirements:

        The app must be a real SaaS style product.

        app.py must include:
        - Flask routes
        - SQLite database initialization
        - Signup endpoint
        - Login endpoint
        - Dashboard route

        The landing page should explain the product clearly.

        Use clean readable code.

        Avoid placeholder comments like:
        # TODO
        # implement later

        FILE: Procfile
        web: gunicorn app:app --bind 0.0.0.0:$PORT

        FILE: README.md
        <instructions>

        Do NOT output **app.py** or markdown headings.
        You MUST use the "FILE:" prefix exactly.
        """

        response = self.think(prompt)
        print("\n===== LLM RESPONSE PREVIEW =====")
        print(response[:1000])
        print("===== END PREVIEW =====\n")

        if not response:
            print("[Developer Agent] Empty response from LLM")
            return project_dir

        if "FILE:" not in response:
            print("[Developer Agent] Invalid LLM output format")
            return project_dir

        response = response.replace("**", "")
        # fallback conversion if LLM returns headings instead of FILE labels
        response = response.replace("### ", "")
        response = response.replace("## ", "")
        response = response.replace("# ", "")
        response = response.replace("**app.py**", "FILE: app.py")
        response = response.replace("**requirements.txt**", "FILE: requirements.txt")
        response = response.replace("**Procfile**", "FILE: Procfile")
        response = response.replace("**README.md**", "FILE: README.md")
        response = response.replace("**README**", "FILE: README.md")
        current_file = None
        buffer = []

        for line in response.splitlines():

            line_clean = line.replace("*", "").replace("`", "").strip()

            if line_clean.startswith("FILE:"):

                if current_file:
                    content = "\n".join(buffer)
                    content = content.replace("```python", "").replace("```", "")
                    write_file(f"{project_dir}/{current_file}", content)
                    print(f"[Developer Agent] created {current_file}")

                    if "templates/" in current_file:
                        print(f"[Developer Agent DEBUG] LLM generated template: {current_file}")
                    buffer = []

                parts = line_clean.split("FILE:", 1)

                if len(parts) > 1:
                    file_part = parts[1].strip()

                    if not file_part:
                        continue

                    current_file = file_part.split()[0].replace(":", "").strip()

                    # --- FIX TEMPLATE PATHS ---
                    if current_file in ["index.html", "login.html", "signup.html", "dashboard.html"]:
                        current_file = f"templates/{current_file}"
                    # --------------------------

            else:
                buffer.append(line)

        # Save the last file
        if current_file:
            content = "\n".join(buffer)
            content = content.replace("```python", "").replace("```", "")

            # Ensure Railway compatibility
            if current_file == "app.py":

                # ensure os import
                if "import os" not in content:
                    content = "import os\n" + content

                # prevent Railway double-server crash
                if "app.run(" in content and "__main__" not in content:
                    content = content.replace(
                        "app.run(",
                        'if __name__ == "__main__":\n    app.run('
                    )

                # remove common LLM inline explanation errors
                content = re.sub(
                    r"(app\.config\['SECRET_KEY'\]\s*=\s*['\"].*?['\"])\s+.*",
                    r"\1",
                    content
                )

            write_file(f"{project_dir}/{current_file}", content)

        # Ensure templates directory exists
        templates_dir = f"{project_dir}/templates"
        os.makedirs(templates_dir, exist_ok=True)

        # -------- DEBUG: SHOW TEMPLATE DIRECTORY STATE --------
        print("[Developer Agent DEBUG] Current templates directory contents:")

        try:
            existing_templates = os.listdir(templates_dir)

            if not existing_templates:
                print("[Developer Agent DEBUG] No templates generated yet.")

            for t in existing_templates:
                print(f"[Developer Agent DEBUG] Found template: {t}")

        except Exception as e:
            print("[Developer Agent DEBUG] Failed to read templates directory:", e)

        # ------------------------------------------------------

        # Ensure static directory exists
        static_dir = f"{project_dir}/static"
        os.makedirs(static_dir, exist_ok=True)

        required_templates = [
            "index.html",
            "signup.html",
            "login.html",
            "dashboard.html"
        ]

        for template in required_templates:

            path = f"{templates_dir}/{template}"

            if not os.path.exists(path):

                fallback_html = f"""
<html>
<head>
<title>{template}</title>
</head>
<body>
<h1>{template}</h1>
<p>Placeholder page generated by DeveloperAgent.</p>
</body>
</html>
"""

                print(f"[Developer Agent DEBUG] Writing fallback template: {template}")
                write_file(path, fallback_html)
                print(f"[Developer Agent DEBUG] Fallback template written: {path}")

        # Ensure default CSS exists
        css_path = f"{static_dir}/style.css"

        if not os.path.exists(css_path):

            fallback_css = """
body {
    font-family: Arial, sans-serif;
    margin: 40px;
}

h1 {
    color: #333;
}
"""

            write_file(css_path, fallback_css)


        # Force correct Procfile (LLM sometimes breaks it)
        procfile_path = f"{project_dir}/Procfile"
        write_file(procfile_path, "web: gunicorn app:app --bind 0.0.0.0:$PORT")

        
        # Build requirements dynamically from imports
        dependencies = {
            "Flask==2.2.5",
            "gunicorn==21.2.0",
            "Werkzeug==2.2.3",
            "Flask-SQLAlchemy==3.0.5"
        }

        # Scan all generated Python files
        for file in os.listdir(project_dir):

            if file.endswith(".py"):

                path = os.path.join(project_dir, file)

                with open(path) as f:
                    code = f.read()

                detected = self.detect_dependencies(code)

                dependencies.update(detected)

        req_path = f"{project_dir}/requirements.txt"
        write_file(req_path, "\n".join(sorted(dependencies)))

        self.auto_debug(project_dir)

        return project_dir

    

    def auto_debug(self, project_dir):

        print("[Developer Agent] Running auto-debug loop...")

        attempts = 3

        for i in range(attempts):
            print(f"Debug attempt {i+1}/{attempts}")

            success, output = run_app(project_dir)

            if "Running on http" in output:
                print("Server started successfully.")
                return

            if success:
                print("App ran successfully.")
                return

            print("Error detected:")
            print(output)

            print("Attempting AI fix...")

            app_path = f"{project_dir}/app.py"

            if not os.path.exists(app_path):
                print("app.py not found. Skipping debug.")
                return

            with open(app_path) as f:
                current_code = f.read()

            fix_prompt = f"""
            The following Flask app has an error.

            Error message:
            {output}

            Fix the code.

            Return ONLY the corrected full app.py code.
            Do not include explanations.
            Do not include markdown.

            Current code:
            {current_code}
            """

            fixed_code = self.think(fix_prompt)
            fixed_code = fixed_code.replace("```python", "").replace("```", "")

            # --- ADD THIS PATCH HERE ---
            if "import os" not in fixed_code:
                fixed_code = "import os\n" + fixed_code
            # ---------------------------

            write_file(app_path, fixed_code)

        print("Auto-debug failed after 3 attempts.")