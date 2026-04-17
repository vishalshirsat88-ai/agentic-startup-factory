import os

# These are checker debugs


class ProductLoop:
    def __init__(self, project_path):
        self.project_path = project_path

    def run(self):
        issues = []

        issues += self.check_empty_templates()

        # ✅ DEBUG HERE (correct scope)
        print("🧠 PRODUCT LOOP ISSUES:", issues)

        # 🔥 ENABLE AUTO FIX
        self.auto_fix_templates(issues)

        return {"status": "completed", "issues_found": issues}

    # 🔍 1. Detect empty dashboards/templates
    def check_empty_templates(self):
        issues = []
        templates_path = os.path.join(self.project_path, "templates")

        if not os.path.exists(templates_path):
            return issues

        for file in os.listdir(templates_path):
            if "dashboard" not in file:
                continue
            if file.endswith(".html"):
                file_path = os.path.join(templates_path, file)

                with open(file_path, "r") as f:
                    content = f.read().lower()

                if "app-data" not in content:
                    issues.append({"type": "NO_FRONTEND_BINDING", "file": file})

        return issues

    # 🔍 2. Detect APIs not used in UI
    def check_api_usage(self):
        issues = []

        routes_path = os.path.join(self.project_path, "routes")
        templates_path = os.path.join(self.project_path, "templates")

        if not os.path.exists(routes_path) or not os.path.exists(templates_path):
            return issues

        route_files = os.listdir(routes_path)
        template_files = os.listdir(templates_path)

        routes_content = []
        for file in route_files:
            if file.endswith(".py"):
                with open(os.path.join(routes_path, file), "r") as f:
                    routes_content.append(f.read())

        templates_content = []
        for file in template_files:
            if file.endswith(".html"):
                with open(os.path.join(templates_path, file), "r") as f:
                    templates_content.append(f.read().lower())

        all_templates = " ".join(templates_content)

        for route in routes_content:
            if "@app.route" in route and "jsonify" in route:
                # If API exists but no frontend call
                if "fetch(" not in all_templates and "axios" not in all_templates:
                    issues.append(
                        {
                            "type": "UNUSED_API",
                            "message": "API exists but not used in frontend",
                        }
                    )

        return issues

    # 🔧 AUTO FIX ENGINE — Inject API calls into templates
    def auto_fix_templates(self, issues):
        templates_path = os.path.join(self.project_path, "templates")

        if not os.path.exists(templates_path):
            return

        for issue in issues:
            if issue["type"] != "NO_FRONTEND_BINDING":
                continue

            file = issue.get("file")
            if not file:
                continue

            file_path = os.path.join(templates_path, file)

            if not os.path.exists(file_path):
                continue

            try:
                with open(file_path, "r") as f:
                    content = f.read()

                # Skip if already fixed
                if "fetch(" in content:
                    continue

                # 🔥 SMART ENDPOINT DETECTION
                endpoint = "/api/data"

                file_lower = file.lower()

                if "dashboard" in file_lower:
                    endpoint = "/test_execution"

                elif "index" in file_lower:
                    endpoint = "/test_analytics"

                elif "login" in file_lower:
                    endpoint = "/test_scheduling"

                # 🔥 INJECT BASIC FETCH SCRIPT
                injection = f"""
    <script>
    fetch('{endpoint}')
      .then(res => res.json())
      .then(data => {{
        const el = document.getElementById("app-data");
        if (el) {{
            el.innerText = JSON.stringify(data, null, 2);
        }}
      }});
    </script>

    <div id="app-data"></div>
    """

                # Inject before closing body
                if "</body>" in content:
                    content = content.replace("</body>", injection + "\n</body>")
                else:
                    content += injection

                with open(file_path, "w") as f:
                    f.write(content)

                print(f"🔥 AUTO-FIX APPLIED → {file}")

            except Exception as e:
                print(f"Auto-fix failed for {file}: {e}")
