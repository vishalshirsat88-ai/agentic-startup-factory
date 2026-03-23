import os


def wire_routes(project_dir):
    routes_dir = os.path.join(project_dir, "routes")
    app_file = os.path.join(project_dir, "app.py")

    if not os.path.exists(routes_dir) or not os.path.exists(app_file):
        print("[Auto Wire] Missing routes or app.py")
        return

    route_files = [f for f in os.listdir(routes_dir) if f.endswith("_routes.py")]

    import_lines = []
    register_lines = []

    for file in route_files:
        module_name = file.replace(".py", "")
        bp_name = module_name.replace("_routes", "_bp")

        import_lines.append(f"from routes.{module_name} import {bp_name}")
        register_lines.append(f"app.register_blueprint({bp_name})")

    with open(app_file, "r") as f:
        content = f.read()

    # ✅ Avoid duplicate wiring
    if "[AUTO_WIRE]" in content:
        print("[Auto Wire] Already wired, skipping")
        return

    new_content = (
        "# [AUTO_WIRE IMPORTS]\n"
        + "\n".join(import_lines)
        + "\n\n"
        + content
        + "\n\n# [AUTO_WIRE REGISTRATION]\n"
        + "\n".join(register_lines)
    )

    with open(app_file, "w") as f:
        f.write(new_content)

    print("[Auto Wire] Routes connected to app.py")
