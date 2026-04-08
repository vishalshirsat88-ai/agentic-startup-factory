from agents.agent_base import AgentBase
from tools.file_writer import write_file
from tools.code_runner import run_app
import os
import re
import json
import time
import shutil
import traceback
from engine.ui_components import COMPONENTS

print("🔥 DEBUG: DeveloperAgent LOADED v5 - Full Logic Restored")


class DeveloperAgent(AgentBase):
    def __init__(self):
        super().__init__("Developer Agent")

    def extract_project_name(self, idea):
        if isinstance(idea, dict):
            name = idea.get("name", "startup")
            slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.lower()).strip("-")
            return f"{slug[:25]}-{int(time.time()) % 100000}"
        for line in str(idea).splitlines():
            if "name" in line.lower():
                words = re.findall(r"[A-Za-z0-9_-]+", line)
                if len(words) >= 2:
                    return words[1].lower()
        words = re.findall(r"[A-Za-z]+", str(idea))
        return words[0].lower() if words else "startup"

    def detect_dependencies(self, code):
        deps = set()
        low_code = code.lower()
        if "flask_sqlalchemy" in low_code:
            deps.add("Flask-SQLAlchemy==3.0.5")
        if "flask_login" in low_code:
            deps.add("Flask-Login==0.6.3")
        if "requests" in low_code:
            deps.add("requests==2.31.0")
        if "pandas" in low_code:
            deps.add("pandas==2.2.2")
        return deps

    def validate_backend_structure(self, project_dir):
        services_dir = os.path.join(project_dir, "services")
        routes_dir = os.path.join(project_dir, "routes")
        if not os.path.exists(services_dir) or not os.path.exists(routes_dir):
            return False
        for file in os.listdir(routes_dir):
            if file.endswith("_routes.py"):
                svc = file.replace("_routes.py", "_service.py")
                if not os.path.exists(os.path.join(services_dir, svc)):
                    return False
        return True

    def copy_template(self, project_dir):
        template_path = "saas_master_template"
        if not os.path.exists(template_path):
            raise Exception("SaaS template not found")
        shutil.copytree(template_path, project_dir, dirs_exist_ok=True)

    def build_mvp(self, idea, architecture=None):
        print("🚀 DEBUG: build_mvp EXECUTED v5")
        project_name = self.extract_project_name(idea)
        project_dir = f"projects/{project_name}"
        os.makedirs(project_dir, exist_ok=True)
        self.copy_template(project_dir)

        # 🎨 1. SAFE DATA EXTRACTION
        product_data = (
            architecture.get("product", {}) if isinstance(architecture, dict) else {}
        )
        design = product_data.get("design_tokens", {})
        copy = product_data.get("marketing_copy", {})
        colors = design.get("colors", {})

        p_name = product_data.get("name", "AI Startup")
        p_desc = product_data.get("description", "Next-gen solution")
        primary_color = colors.get("primary", "#3498db")

        # 🏗️ 2. PREPARE COMMON UI STRINGS
        navbar_html = COMPONENTS["navbar"].format(product_name=p_name)
        footer_html = COMPONENTS["footer"].format(product_name=p_name)
        vibe_style = f"""
        <style>
            :root {{
                --primary: {primary_color};
                --secondary: {colors.get("secondary", "#10b981")};
                --bg-app: {colors.get("background", "#ffffff")};
                --radius: {"9999px" if "full" in str(design.get("border_radius", "")) else "0.5rem"};
            }}
            .bg-primary {{ background-color: var(--primary) !important; }}
            .text-primary {{ color: var(--primary) !important; }}
            .rounded-custom {{ border-radius: var(--radius) !important; }}
            .fade-in-up {{ animation: fadeInUp 0.8s ease-out forwards; }}
            @keyframes fadeInUp {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        </style>
        """

        # 📂 3. MULTI-PAGE ASSEMBLER
        templates_dir = os.path.join(project_dir, "templates")
        if os.path.exists(templates_dir):
            seen_routes = set()
            final_routes = []
            arch_routes = (
                architecture.get("routes", []) if isinstance(architecture, dict) else []
            )
            for r in arch_routes:
                clean_r = str(r).strip("/")
                if (
                    clean_r
                    and clean_r not in ["login", "signup", "dashboard"]
                    and clean_r not in seen_routes
                ):
                    final_routes.append(clean_r)
                    seen_routes.add(clean_r)

            sidebar_links = "".join(
                [
                    COMPONENTS["sidebar_link"].format(
                        route=rp, name=rp.replace("-", " ").replace("_", " ").title()
                    )
                    for rp in final_routes
                ]
            )

            for t_name in os.listdir(templates_dir):
                if not t_name.endswith(".html"):
                    continue
                t_path = os.path.join(templates_dir, t_name)
                with open(t_path, "r") as f:
                    t_content = f.read()

                if t_name == "index.html":
                    h_title = copy.get("hero_title", "Streamline Your Workflow")
                    h_sub = copy.get("hero_subtitle", p_desc)
                    hero_sec = COMPONENTS["hero"].format(
                        product_name=h_title, product_description=h_sub
                    )
                    feat_items = "".join(
                        [
                            COMPONENTS["feature_item"].format(
                                title=m.get("name"), description=m.get("description")
                            )
                            for m in product_data.get("modules", [])[:3]
                        ]
                    )
                    feats_sec = COMPONENTS["features"].format(feature_items=feat_items)
                    cta_sec = COMPONENTS["cta_section"].format(product_name=p_name)
                    page_body = f"{navbar_html}\n{hero_sec}\n{feats_sec}\n{cta_sec}\n{footer_html}"
                else:
                    p_title = t_name.replace(".html", "").replace("_", " ").title()
                    if "dashboard" in t_name.lower():
                        stats = "".join(
                            [
                                COMPONENTS["stat_card"].format(label=l, value=v)
                                for l, v in [
                                    ("Active Users", "1,200"),
                                    ("Revenue", "$4k"),
                                    ("Uptime", "99%"),
                                ]
                            ]
                        )
                        m_content = COMPONENTS["stats_grid"].format(stats_cards=stats)
                    else:
                        th = "".join(
                            [
                                f"<th class='p-4 text-xs font-semibold text-gray-500'>{x}</th>"
                                for x in ["ID", "Name", "Status"]
                            ]
                        )
                        tr = "".join(
                            [
                                f"<tr class='border-b border-gray-50'><td class='p-4 text-sm'>#10{i}</td><td class='p-4 text-sm'>Data Point {i}</td><td class='p-4 text-xs text-green-600 font-bold'>ACTIVE</td></tr>"
                                for i in range(3)
                            ]
                        )
                        m_content = COMPONENTS["data_table"].format(
                            table_headers=th, table_rows=tr
                        )
                    page_body = COMPONENTS["dashboard_shell"].format(
                        product_name=p_name,
                        page_title=p_title,
                        sidebar_links=sidebar_links,
                        main_content=m_content,
                    )

                if "</head>" in t_content:
                    t_content = t_content.replace("</head>", f"{vibe_style}\n</head>")
                b_match = re.search(r"<body[^>]*>", t_content)
                if b_match and "</body>" in t_content:
                    t_content = (
                        t_content[: b_match.end()]
                        + f"\n<div class='fade-in-up'>{page_body}</div>\n"
                        + t_content[t_content.find("</body>") :]
                    )
                with open(t_path, "w") as f:
                    f.write(t_content)

        # ⚙️ 4. APP.PY AND BACKEND
        app_file = os.path.join(project_dir, "app.py")
        if os.path.exists(app_file):
            with open(app_file, "r") as f:
                a_content = f.read()
            a_content = a_content.replace(
                'PRODUCT_NAME = "AI Resume Builder"', f'PRODUCT_NAME = "{p_name}"'
            )
            if "<title>" in a_content:
                a_content = re.sub(
                    r"<title>.*?</title>",
                    f"<title>{p_name} | {copy.get('hero_title', 'SaaS')}</title>",
                    a_content,
                )
            with open(app_file, "w") as f:
                f.write(a_content)

        from engine.file_generator import generate_backend_files

        if architecture:
            architecture["product"] = product_data
            generate_backend_files(project_dir, architecture)

        from engine.auto_wire import wire_routes

        try:
            wire_routes(project_dir)
        except:
            pass

        # Indentation Cleanup for Python Files
        import glob, textwrap

        for py_file in glob.glob(os.path.join(project_dir, "**/*.py"), recursive=True):
            with open(py_file, "r") as f:
                p_code = f.read()
            with open(py_file, "w") as f:
                f.write(textwrap.dedent(p_code))

        print(f"[Developer Agent] ✅ Vibe Orchestration Complete: {p_name}")
        return project_dir
