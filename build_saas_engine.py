import os

def write_file(path, content):
    directory = os.path.dirname(path)
    if directory != "":
        os.makedirs(directory, exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

print("🚀 Building Master SaaS Engine...")

# Create folders
folders = [
    "saas_master_template/templates",
    "saas_master_template/static/css",
    "saas_master_template/static/js",
    "engine",
    "generated_startups"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# -----------------------------
# base.html
# -----------------------------
base_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{ data.product_name }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="../static/css/style.css">
</head>
<body class="bg-black text-white">
    {% block content %}
    {% endblock %}
    <script src="../static/js/main.js"></script>
</body>
</html>
"""

write_file("saas_master_template/templates/base.html", base_html)

# -----------------------------
# index.html
# -----------------------------
index_html = """
{% extends "base.html" %}
{% block content %}
    {% include "hero.html" %}
    {% include "features.html" %}
{% endblock %}
"""

write_file("saas_master_template/templates/index.html", index_html)

# -----------------------------
# hero.html
# -----------------------------
hero_html = """
<section class="py-32 text-center">
    <h1 class="text-5xl font-bold mb-6">
        {{ data.headline }}
    </h1>
    <p class="text-gray-400 mb-8">
        {{ data.subheadline }}
    </p>
    <button class="px-6 py-3 bg-indigo-600 rounded-lg">
        {{ data.cta_text }} — {{ data.price }}
    </button>
</section>
"""

write_file("saas_master_template/templates/hero.html", hero_html)

# -----------------------------
# features.html
# -----------------------------
features_html = """
<section class="py-20 max-w-6xl mx-auto grid md:grid-cols-3 gap-8">
    {% for feature in data.features %}
    <div class="p-6 bg-gray-900 rounded-xl">
        <h3 class="text-xl font-bold mb-2">
            {{ feature.title }}
        </h3>
        <p class="text-gray-400">
            {{ feature.desc }}
        </p>
    </div>
    {% endfor %}
</section>
"""

write_file("saas_master_template/templates/features.html", features_html)

# -----------------------------
# CSS
# -----------------------------
css = """
body {
    background: black;
    color: white;
    font-family: sans-serif;
}
"""

write_file("saas_master_template/static/css/style.css", css)

# -----------------------------
# JS
# -----------------------------
js = """
console.log("Startup Factory UI Loaded")
"""

write_file("saas_master_template/static/js/main.js", js)

# -----------------------------
# Renderer
# -----------------------------
renderer = """
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
"""

write_file("engine/template_renderer.py", renderer)