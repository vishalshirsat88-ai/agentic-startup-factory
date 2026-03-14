from agents.agent_base import AgentBase
from tools.file_writer import write_file
from tools.code_runner import run_app
import os
import re
import json
import time

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

    def build_mvp(self, idea):

        print("DEBUG IDEA TEXT:")
        print(json.dumps(idea, indent=2) if isinstance(idea, dict) else idea)

        project_name = self.extract_project_name(idea)

        print("EXTRACTED PROJECT NAME:", project_name)

        project_dir = f"projects/{project_name}"
        os.makedirs(project_dir, exist_ok=True)

        prompt = f"""
        Build a simple Flask MVP for this startup idea.

        Rules:
        - Use Flask
        - Use a single file app.py
        - Include "import os" at the top (REQUIRED)
        - Use: port = int(os.environ.get("PORT", 5000))
        - Use: app.run(host="0.0.0.0", port=port)
        - Keep it minimal and working
        - Do not use render_template.
        - Return plain text from the route.

        Idea Name: {idea.get("name","") if isinstance(idea, dict) else idea}
        Description: {idea.get("description","") if isinstance(idea, dict) else ""}

        Generate the following files EXACTLY in this format.

        FILE: app.py
        ...
        FILE: requirements.txt
        Flask==2.3.3
        gunicorn==21.2.0
        Werkzeug==2.3.7

        FILE: Procfile
        web: gunicorn app:app --bind 0.0.0.0:$PORT

        FILE: README.md
        <instructions>

        Do NOT output **app.py** or markdown headings.
        You MUST use the "FILE:" prefix exactly.
        """

        response = self.think(prompt)
        if not response:
            print("[Developer Agent] Empty response from LLM")
            return project_dir
        response = response.replace("**", "")
        # fallback conversion if LLM returns headings instead of FILE labels
       
        response = response.replace("**app.py**", "FILE: app.py")
        response = response.replace("**requirements.txt**", "FILE: requirements.txt")
        response = response.replace("**Procfile**", "FILE: Procfile")
        response = response.replace("**README.md**", "FILE: README.md")
        response = response.replace("**README**", "FILE: README.md")
        current_file = None
        buffer = []

        for line in response.splitlines():

            line_clean = line.replace("*", "").strip()

            if "FILE:" in line_clean:

                if current_file:
                    content = "\n".join(buffer)
                    content = content.replace("```python", "").replace("```", "")
                    write_file(f"{project_dir}/{current_file}", content)
                    print(f"[Developer Agent] created {current_file}")
                    buffer = []

                parts = line_clean.split("FILE:")

                if len(parts) > 1:
                    file_part = parts[1].strip()

                    if not file_part:
                        continue

                    current_file = file_part.split()[0].replace(":", "")

            else:
                buffer.append(line)

        # Save the last file
        if current_file:
            content = "\n".join(buffer)
            content = content.replace("```python", "").replace("```", "")
            
            # --- ADD THIS PATCH HERE ---
            if current_file == "app.py" and "import os" not in content:
                content = "import os\n" + content
            # ---------------------------

            write_file(f"{project_dir}/{current_file}", content)

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