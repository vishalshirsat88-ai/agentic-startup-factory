import os
from tools.file_writer import write_file


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
        safe_name = module.lower().replace(" ", "_")

        model_code = f"""
class {safe_name.capitalize()}Model:
    def __init__(self):
        pass
"""

        write_file(f"{project_dir}/models/{safe_name}_model.py", model_code)

        print(f"\n[DEBUG] Calling AI logic for module: {safe_name}")

        from engine.ai_logic import generate_service_logic

        print(f"[DEBUG] Import successful")

        ai_logic = generate_service_logic(safe_name)

        print("[DEBUG] AI LOGIC TYPE:", type(ai_logic))
        print("[DEBUG] AI LOGIC VALUE:\n", ai_logic)
        print("AI LOGIC GENERATED:\n", ai_logic)

        service_code = f"""
        from db import get_connection

        {ai_logic}


        def add_{safe_name}(name):
            try:
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
                    "data": {{"message": "{module} added"}},
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
        from flask import Blueprint, jsonify, request
        from services.{safe_name}_service import get_{safe_name}, add_{safe_name}

        {safe_name}_bp = Blueprint('{safe_name}', __name__)


        @{safe_name}_bp.route('/api/{safe_name}', methods=['GET'])
        def {safe_name}_route():
            result = get_{safe_name}()
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
