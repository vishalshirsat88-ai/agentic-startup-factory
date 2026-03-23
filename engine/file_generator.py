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
class {safe_name.capitalize()}Service:
    def execute(self):
        return "{module} logic running"
"""

        write_file(f"{project_dir}/services/{safe_name}_service.py", service_code)

        route_code = f"""
from flask import Blueprint

{safe_name}_bp = Blueprint('{safe_name}', __name__)

@{safe_name}_bp.route('/{safe_name}')
def {safe_name}_home():
    return "{module} route working"
"""

        write_file(f"{project_dir}/routes/{safe_name}_routes.py", route_code)

    print("[File Generator] Backend files created")
