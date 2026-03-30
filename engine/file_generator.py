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

        service_code = f"""
        def get_{safe_name}():
            try:
                # TODO: implement real logic for {module}

                return {{
                    "status": "success",
                    "data": {{
                        "message": "{module} working"
                    }},
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
        from flask import Blueprint, jsonify
        from services.{safe_name}_service import get_{safe_name}

        {safe_name}_bp = Blueprint('{safe_name}', __name__)

        @{safe_name}_bp.route('/api/{safe_name}', methods=['GET'])
        def {safe_name}_route():
            result = get_{safe_name}()

            if result["status"] == "success":
                return jsonify(result), 200
            else:
                return jsonify(result), 500
        """

        write_file(f"{project_dir}/routes/{safe_name}_routes.py", route_code)

    print("[File Generator] Backend files created")
