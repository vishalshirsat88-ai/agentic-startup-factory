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

        # 🛡️ SAFETY GUARD
        if architecture is None:
            architecture = {"modules": [], "product": {}, "routes": []}

        project_name = self.extract_project_name(idea)
        project_dir = f"projects/{project_name}"
        os.makedirs(project_dir, exist_ok=True)
        self.copy_template(project_dir)

        # 🎨 1. SAFE DATA EXTRACTION
        arch_safe: dict = architecture if isinstance(architecture, dict) else {}
        product_raw = arch_safe.get("product", {})
        p_data: dict = product_raw if isinstance(product_raw, dict) else {}

        design_raw = p_data.get("design_tokens", {})
        design_safe: dict = design_raw if isinstance(design_raw, dict) else {}

        copy_raw = p_data.get("marketing_copy", {})
        copy_safe: dict = copy_raw if isinstance(copy_raw, dict) else {}

        colors_raw = design_safe.get("colors", {})
        colors_safe: dict = colors_raw if isinstance(colors_raw, dict) else {}

        # Safe String Assignments
        p_name = str(p_data.get("name", "AI Startup"))
        p_desc = str(p_data.get("description", "Next-gen solution"))
        primary_color = str(colors_safe.get("primary", "#3498db"))

        # 🏗️ 2. PREPARE COMMON UI STRINGS
        navbar_html = COMPONENTS["navbar"].format(product_name=p_name)
        footer_html = COMPONENTS["footer"].format(product_name=p_name)

        vibe_style = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
            :root {{ 
                --primary: {primary_color}; 
                --bg: {colors.get('background', '#030014')}; 
                --surface: {design.get('theme_config', {}).get('glass_opacity', '0.03')};
            }}
            body { background-color: #030014 !important; color: white !important; font-family: 'Inter', sans-serif; margin: 0; }
            .lovable-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at 50% -20%, #1e1b4b, #030014); z-index: -1; }
            .glass-card { background: rgba(255, 255, 255, 0.03) !important; backdrop-filter: blur(24px) saturate(200%) !important; border: 1px solid rgba(255, 255, 255, 0.1) !important; border-radius: 24px !important; }
            .bg-white, .bg-gray-50, .bg-slate-50 { background-color: transparent !important; }
        </style>
        """
        # --- [END REPLACE] ---

        # 📂 3. MULTI-PAGE ASSEMBLER
        templates_dir = os.path.join(project_dir, "templates")
        if os.path.exists(templates_dir):
            seen_routes = set()
            final_routes = []
            arch_routes = arch_safe.get("routes", [])
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
                        route=rp, name=rp.replace("-", " ").title()
                    )
                    for rp in final_routes
                ]
            )

            for t_name in os.listdir(templates_dir):
                if not t_name.endswith(".html"):
                    continue
                t_path = os.path.join(templates_dir, t_name)

                if t_name == "index.html":
                    h_sub = copy_safe.get("hero_subtitle", p_desc)
                    hero_sec = COMPONENTS["hero"].format(
                        product_name=p_name,
                        hero_title=copy_safe.get(
                            "hero_title", "Streamline Your Workflow"
                        ),
                        hero_subtitle=h_sub,
                        cta_text=copy_safe.get("cta_text", "Get Started Today"),
                    )

                    # Extract modules safely from the dictionary we already validated
                    raw_modules = p_data.get("modules", [])
                    modules_for_index = (
                        raw_modules if isinstance(raw_modules, list) else []
                    )

                    feat_items = "".join(
                        [
                            COMPONENTS["feature_item"].format(
                                title=str(m.get("name", "Feature"))
                                if isinstance(m, dict)
                                else "Feature",
                                description=str(
                                    m.get("description", "Innovative Solution")
                                )
                                if isinstance(m, dict)
                                else "Description",
                            )
                            for m in modules_for_index[:4]
                        ]
                    )
                    feats_sec = COMPONENTS["features"].format(feature_items=feat_items)
                    page_body = f"{navbar_html}\n{hero_sec}\n{feats_sec}\n{footer_html}"

                else:
                    # DYNAMIC DASHBOARD DATA INJECTION
                    p_title_str = str(
                        t_name.replace(".html", "").replace("_", " ").title()
                    )
                    module_name_clean = t_name.replace(".html", "").replace("-", " ")

                    raw_modules_list = arch_safe.get("modules", [])
                    modules_list = (
                        raw_modules_list if isinstance(raw_modules_list, list) else []
                    )

                    relevant_module = {
                        "name": "Overview",
                        "features": ["System Active", "Cloud Sync", "AI Ready"],
                    }
                    for m in modules_list:
                        if isinstance(m, dict):
                            m_name = str(m.get("name", "")).lower()
                            if m_name in module_name_clean.lower():
                                relevant_module = m
                                break

                    features_list = (
                        relevant_module.get("features", [])
                        if isinstance(relevant_module, dict)
                        else []
                    )
                    grid_items = "".join(
                        [
                            COMPONENTS["stat_card"].format(
                                label=str(feat), value="Active"
                            )
                            for feat in (
                                features_list[:3]
                                if features_list
                                else ["Status", "Network", "Uptime"]
                            )
                        ]
                    )

                    page_body = COMPONENTS["dashboard_shell"].format(
                        product_name=p_name,
                        page_title=p_title_str,
                        sidebar_links=sidebar_links,
                        main_content=f"<div class='grid grid-cols-1 md:grid-cols-3 gap-6'>{grid_items}</div>",
                    )

                # LOVABLE HARD-OVERWRITE
                final_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');
        :root {{ --primary: {primary_color}; --bg: {colors_safe.get("background", "#030014")}; --surface: {design_safe.get("surface", "rgba(255, 255, 255, 0.03)")}; }}
        body {{ background-color: var(--bg); color: white; font-family: 'Inter', sans-serif; margin: 0; overflow-x: hidden; }}
        .lovable-bg {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at 50% -20%, {primary_color}33, var(--bg)); z-index: -1; }}
        .lovable-orb {{ position: absolute; width: 600px; height: 600px; background: radial-gradient(circle, var(--primary), transparent 70%); filter: blur(140px); opacity: 0.15; pointer-events: none; z-index: 0; }}
        .glass-card {{ background: var(--surface); backdrop-filter: blur(24px) saturate(200%); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 24px; transition: all 0.5s ease; }}
        .glass-card:hover {{ transform: translateY(-10px); border-color: var(--primary); background: rgba(255, 255, 255, 0.05); }}
        .hero-glow {{ filter: drop-shadow(0 0 30px rgba(59, 130, 246, 0.3)); }}
    </style>
</head>
<body>
    <div class="lovable-bg"></div>
    <div class="lovable-orb" style="top: -10%; right: -10%;"></div>
    <div class="lovable-orb" style="bottom: -10%; left: -10%; background: radial-gradient(circle, #818cf8, transparent 70%);"></div>
    <div class="relative z-10">{page_body}</div>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>AOS.init({{ duration: 1000, once: true }}); lucide.createIcons();</script>
</body>
</html>
"""
                if t_name == "index.html":
                    print(
                        "\n"
                        + "💎" * 20
                        + "\n🔥 VIBE CHECK: SUCCESSFUL REWRITE\n"
                        + "💎" * 20
                        + "\n"
                    )
                with open(t_path, "w") as f:
                    f.write(final_html)

        # ⚙️ 4. BACKEND GENERATION
        from engine.file_generator import generate_backend_files

        if arch_safe:
            arch_safe["product"] = p_data
            generate_backend_files(project_dir, arch_safe)

        from engine.auto_wire import wire_routes

        try:
            wire_routes(project_dir)
        except:
            pass

        import glob, textwrap

        for py_file in glob.glob(os.path.join(project_dir, "**/*.py"), recursive=True):
            with open(py_file, "r") as f:
                p_code = f.read()
            with open(py_file, "w") as f:
                f.write(textwrap.dedent(p_code))

        print(f"[Developer Agent] ✅ Vibe Orchestration Complete: {p_name}")
        return project_dir
