import os
import re
import textwrap
import engine.ai_logic

# These are checker debugs
print("🔥 DEBUG: File_generator LOADED v10")

from tools.file_writer import write_file

print("AI LOGIC FILE:", engine.ai_logic.__file__)


def indent_code(code, spaces=8):
    return "\n".join((" " * spaces) + line for line in code.split("\n"))


def generate_backend_files(project_dir, architecture):
    if not architecture:
        print("[File Generator] No architecture provided")
        return

    modules = architecture.get("modules", [])

    print("[File Generator] Generating backend structure...")

    folders = ["models", "routes", "services"]

    for folder in folders:
        os.makedirs(os.path.join(project_dir, folder), exist_ok=True)

    for module in modules:
        print(f"🔥 DEBUG: Processing module → {module}")
        # 🔥 Handle both string and dict modules
        if isinstance(module, dict):
            module_name = module.get("name", "core")
        else:
            module_name = module

        safe_name = module_name.lower()
        safe_name = re.sub(r"[^a-z0-9_]", "_", safe_name)

        model_code = f"""
class {safe_name.capitalize()}Model:
    def __init__(self):
        pass
"""
        write_file(f"{project_dir}/models/{safe_name}_model.py", model_code)

        print(f"\n[DEBUG] Calling AI logic for module: {safe_name}")

        from engine.ai_logic import generate_service_logic

        print(f"[DEBUG] Import successful")

        ai_logic = generate_service_logic(safe_name, architecture.get("idea", {}))
        ai_logic = textwrap.dedent(ai_logic).strip()

        # 🔥 SAFETY FILTER (CRITICAL)
        unsafe_patterns = [
            "users",
            "datetime",
            "timedelta",
            "user_authenticated",
            "encrypt_",
            "verify_",
            "hash_",
            "store_data",
        ]

        for pattern in unsafe_patterns:
            if pattern in ai_logic:
                print(f"⚠️ Unsafe pattern detected: {pattern} — applying fallback")

                ai_logic = f"""def get_{safe_name}():
                    result = {{
                        "status": "safe_fallback",
                        "module": "{safe_name}"
                    }}
                    return result
                """
                ai_logic = textwrap.dedent(ai_logic).strip()
                break

        print("[DEBUG] AI LOGIC TYPE:", type(ai_logic))
        print("[DEBUG] AI LOGIC VALUE:\n", ai_logic)
        print("AI LOGIC GENERATED:\n", ai_logic)

        raw_execution = f"""
        # 🔥 FIRST TRY DB
        data = get_{safe_name}_from_db()

        if data:
            result = {{"data": data, "source": "database"}}

        else:
            if "get_{safe_name}" in globals():
                result = get_{safe_name}()
            else:
                result = {{"message": "no data available"}}
        """

        execution_block = indent_code(textwrap.dedent(raw_execution).strip(), 8)

        service_code = f"""# 🔥 DEBUG: SERVICE FILE GENERATED v4

{ai_logic}

def get_{safe_name}_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("{safe_name}",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
{execution_block}

        return {{
            "status": "success",
            "data": result,
            "error": None
        }}

    except Exception as e:
        return {{
            "status": "error",
            "data": None,
            "error": str(e)
        }}


def add_{safe_name}(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "{safe_name}")
        )
        conn.commit()
        conn.close()

        return {{
            "status": "success",
            "data": {{"message": "{safe_name} added"}},
            "error": None
        }}

    except Exception as e:
        return {{
            "status": "error",
            "data": None,
            "error": str(e)
        }}
"""

        write_file(f"{project_dir}/services/{safe_name}_service.py", service_code)

        route_code = f"""
        from flask import Blueprint, jsonify, request, render_template
        from services.{safe_name}_service import execute, add_{safe_name}

        {safe_name}_bp = Blueprint('{safe_name}', __name__)
        
        @{safe_name}_bp.route('/{safe_name}', methods=['GET'])
        def {safe_name}_page():
            return render_template("{safe_name}.html")


        @{safe_name}_bp.route('/api/{safe_name}', methods=['GET'])
        def {safe_name}_route():
            result = execute()
            return jsonify(result), 200


        @{safe_name}_bp.route('/api/{safe_name}', methods=['POST'])
        def add_{safe_name}_route():
            data = request.get_json()
            name = data.get("name")

            result = add_{safe_name}(name)
            return jsonify(result), 200
        """

        write_file(f"{project_dir}/routes/{safe_name}_routes.py", route_code)

    print("[File Generator] Backend files created")
    print(
        "🔥 DEBUG: generate_backend_files EXISTS:",
        "generate_backend_files" in globals(),
    )

    inject_dashboard_ui(project_dir)
    # 🔥 ENSURE GLOBAL API ROUTE EXISTS
    app_file = os.path.join(project_dir, "app.py")

    if os.path.exists(app_file):
        with open(app_file, "r") as f:
            code = f.read()

        if "/api/run-feature" not in code:
            print("[File Generator] Injecting global API route")

            api_code = """
@app.route("/api/run-feature")
def run_feature():
    return {
        "status": "success",
        "data": [
            {"name": "System Health", "value": "OK"},
            {"name": "Modules Active", "value": 3},
            {"name": "Status", "value": "Running"}
        ]
    }
"""

            code += api_code

            with open(app_file, "w") as f:
                f.write(code)


def inject_dashboard_ui(project_dir):
    templates_path = os.path.join(project_dir, "templates")

    if not os.path.exists(templates_path):
        return

    for file in os.listdir(templates_path):
        if "dashboard" not in file:
            continue

        file_path = os.path.join(templates_path, file)

        with open(file_path, "r") as f:
            content = f.read()

        if "app-data" in content:
            continue  # already injected

        # 🔥 INSERT UI CONTAINER
        if "<h6>Available Features:</h6>" in content:
            content = content.replace(
                "<h6>Available Features:</h6>",
                """<h6>Available Features:</h6>
<div id="app-data" style="margin-top:20px;"></div>
""",
            )

        # 🔥 INSERT SCRIPT
        injection = """
<script>
fetch('/api/run-feature')
  .then(res => res.json())
  .then(data => {
      const container = document.getElementById('app-data');
      if (!container) return;

      const items = data.data;

      let html = '<div style="display:flex; gap:15px;">';

      items.forEach(item => {
          html += `
              <div style="
                  background:white;
                  padding:15px;
                  border-radius:8px;
                  box-shadow:0 2px 6px rgba(0,0,0,0.1);
              ">
                  <div>${item.name}</div>
                  <div><b>${item.value}</b></div>
              </div>
          `;
      });

      html += '</div>';
      container.innerHTML = html;
  });
</script>
"""

        if "</body>" in content:
            content = content.replace("</body>", injection + "\n</body>")
        else:
            content += injection

        with open(file_path, "w") as f:
            f.write(content)

        print(f"[File Generator] UI injected → {file}")
