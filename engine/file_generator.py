import os
import re
import textwrap
import engine.ai_logic

# These are checker debugs
print("🔥 DEBUG: File_generator LOADED v13")

from tools.file_writer import write_file

print("AI LOGIC FILE:", engine.ai_logic.__file__)


def indent_code(code, spaces=8):
    return "\n".join((" " * spaces) + line for line in code.split("\n"))


def validate_ai_logic(logic, module_name):
    """Ensures AI logic is not empty and has proper Python structure."""
    if not logic or "def" not in logic:
        return f"def get_{module_name}():\n    return {{'status': 'active', 'info': 'Default logic for {module_name}'}}"

    # Check if the function has a body (prevent IndentationError)
    if logic.strip().endswith(":"):
        return logic + "\n    pass"

    return logic


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

        # 🔥 Dynamic logic generation with integrated validation
        from engine.ai_logic import generate_service_logic

        raw_ai_logic = generate_service_logic(safe_name, architecture.get("idea", {}))

        # Clean and Validate
        # 🔥 greedy logic extraction
        raw_ai_logic = generate_service_logic(safe_name, architecture.get("idea", {}))

        # Strip markdown and whitespace but preserve the body
        ai_logic = raw_ai_logic.replace("```python", "").replace("```", "").strip()

        # Ensure it didn't cut off at the header
        if ai_logic.count("\n") < 1:
            ai_logic += "\n    return {'status': 'active'}"

        # Only use validate_ai_logic as a safety net
        ai_logic = validate_ai_logic(ai_logic, safe_name)

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
                # 🔥 Dynamic logic generation
                from engine.ai_logic import generate_service_logic

                raw_ai_logic = generate_service_logic(
                    safe_name, architecture.get("idea", {})
                )

                # Clean the logic: Only remove markdown backticks, keep the indentation
                ai_logic = (
                    raw_ai_logic.replace("```python", "").replace("```", "").strip()
                )

                # Validation fallback: If AI failed to provide a body, add pass
                if ai_logic.endswith(":"):
                    ai_logic += "\n    pass"

                print(f"[File Generator] Logic verified for {safe_name}")

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

        route_code = textwrap.dedent(route_code).strip()
        write_file(f"{project_dir}/routes/{safe_name}_routes.py", route_code)

    print("[File Generator] Backend files created")
    # 🔥 CREATE MAIN FLASK APP (CRITICAL)

    app_code = """
    from flask import Flask, render_template
    import os

    app = Flask(__name__)

    # --- BASIC ROUTES ---
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")


    # --- AUTO REGISTER BLUEPRINTS ---
    from routes import *

    # --- RUN APP ---
    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 3000))
        app.run(host="0.0.0.0", port=port, debug=True)
    """

    write_file(f"{project_dir}/app.py", app_code)

    print("🔥 app.py created with PORT + routes")
    print(
        "🔥 DEBUG: generate_backend_files EXISTS:",
        "generate_backend_files" in globals(),
    )
