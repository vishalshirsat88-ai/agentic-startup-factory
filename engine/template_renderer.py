
from jinja2 import Environment, FileSystemLoader
import json
import os

def render_startup(config_path, output_dir):
    with open(config_path) as f:
        data = json.load(f)

    env = Environment(loader=FileSystemLoader("saas_master_template/templates"))
    template = env.get_template("index.html")

    html = template.render(data=data)

    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/index.html", "w") as f:
        f.write(html)

    print("Startup generated:", output_dir)
