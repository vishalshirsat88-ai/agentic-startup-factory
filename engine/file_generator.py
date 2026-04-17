import os
import re
import textwrap
import engine.ai_logic

# These are checker debugs
print("🔥 DEBUG: File_generator LOADED v12")

from tools.file_writer import write_file

print("AI LOGIC FILE:", engine.ai_logic.__file__)


def validate_and_fix_ai_code(code):
    try:
        local_env = {}
        exec(code, {}, local_env)

        # 🔥 ensure at least one function exists
        functions = [k for k, v in local_env.items() if callable(v)]

        if not functions:
            raise Exception("No function found in AI code")

        # 🔥 NEW STRICT CHECK
        fn = local_env[functions[0]]
        result = fn()

        if not isinstance(result, dict):
            raise Exception("Function must return dict")

        if "data" not in result:
            raise Exception("Missing 'data' key")

        print("✅ AI CODE VALID (STRICT)")
        return code

    except Exception as e:
        print("❌ AI CODE BROKEN — FIXING...", str(e))

        # basic structural fixes
        if code.count("{") > code.count("}"):
            code += "\n}"

        if code.count("[") > code.count("]"):
            code += "\n]"

        try:
            local_env = {}
            exec(code, {}, local_env)

            functions = [k for k, v in local_env.items() if callable(v)]
            if not functions:
                raise Exception("Still no function")

            print("✅ AI CODE FIXED SUCCESSFULLY")
            return code

        except Exception:
            print("🚨 AI CODE STILL BROKEN — APPLYING FALLBACK")
            return None


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

        safe_name = str(module_name).lower()
        safe_name = re.sub(r"[^a-z0-9_]", "_", safe_name)

        class_name = "".join(word.capitalize() for word in safe_name.split("_"))

        model_code = f"""
        class {class_name}Model:
            def __init__(self):
                pass
        """
        model_code = textwrap.dedent(model_code).strip()
        write_file(f"{project_dir}/models/{safe_name}_model.py", model_code)

        print(f"\n[DEBUG] Calling AI logic for module: {safe_name}")

        from engine.ai_logic import generate_service_logic

        print(f"[DEBUG] Import successful")

        ai_logic = generate_service_logic(safe_name, architecture.get("idea", {}))

        # 🔥 NEW: VALIDATE AI CODE
        validated_code = validate_and_fix_ai_code(ai_logic)

        if not validated_code:
            print("⚠️ USING SAFE FALLBACK")

            ai_logic = f"""
def get_{safe_name}():
    return {{
        "status": "fallback",
        "module": "{safe_name}"
}}
"""
            ai_logic = textwrap.dedent(ai_logic).strip()
        else:
            ai_logic = validated_code

        # 🔥 SAFETY FILTER (FIXED - PRODUCTION SAFE)
        unsafe_patterns = [
            "os.system",
            "subprocess",
            "eval(",
            "exec(",
            "__import__",
        ]

        for pattern in unsafe_patterns:
            if re.search(rf"\b{re.escape(pattern)}\b", ai_logic):
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

        route_code = textwrap.dedent(f"""
        from flask import Blueprint, jsonify, request, render_template
        from services.{safe_name}_service import execute, add_{safe_name}

        {safe_name}_bp = Blueprint('{safe_name}', __name__)

        @{safe_name}_bp.route('/{safe_name}', methods=['GET'])
        def {safe_name}_page():
            return render_template("{safe_name}.html")


        @{safe_name}_bp.route('/api/{safe_name}', methods=['GET'])
        def {safe_name}_route():
            result = execute()
        
            try:

                
                from engine.insight_engine import generate_insights
                
                if not result or not isinstance(result, dict):
                    result = {{}}
                    
                data_block = result.get("data", {{}})

                # Handle nested AI response safely
                if isinstance(data_block, dict) and "data" in data_block:
                    data_block = data_block.get("data", {{}})
                
                module_data = data_block.get("{safe_name}", [])
                
                print("🔥 MODULE DATA:", module_data)
                

                insights = generate_insights("{safe_name}", module_data)
                
                result["insights"] = insights
        
            except Exception as e:
                print("⚠️ Insight generation failed:", e)
                result["insights"] = {{
                    "summary": "Insight unavailable",
                    "insights": [],
                    "risks": [],
                    "recommendations": []
                }}

      
            print("🚨 API HIT:", "{safe_name}")
            print("🚨 FINAL RESULT:", result)
            print("🚨 INSIGHTS BLOCK:", result.get("insights"))

                
        
            return jsonify(result), 200


        @{safe_name}_bp.route('/api/{safe_name}', methods=['POST'])
        def add_{safe_name}_route():
            data = request.get_json()
            name = data.get("name")

            result = add_{safe_name}(name)
            return jsonify(result), 200
        """).strip()

        write_file(f"{project_dir}/routes/{safe_name}_routes.py", route_code)

    print("[File Generator] Backend files created")

    print(
        "🔥 DEBUG: generate_backend_files EXISTS:",
        "generate_backend_files" in globals(),
    )

    inject_dashboard_ui(project_dir)
    # 🔥 COPY INSIGHT ENGINE INTO PROJECT (CRITICAL FIX)

    import shutil

    engine_src = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "insight_engine.py")
    )
    print("🔥 DEBUG: insight_engine source path:", engine_src)
    print("🔥 DEBUG: file exists?", os.path.exists(engine_src))

    engine_dest_dir = os.path.join(project_dir, "engine")

    os.makedirs(engine_dest_dir, exist_ok=True)

    engine_dest = os.path.join(engine_dest_dir, "insight_engine.py")

    if os.path.exists(engine_src):
        shutil.copy(engine_src, engine_dest)
        print("✅ insight_engine.py copied to project")
        print("📂 DEST:", engine_dest)
    else:
        print("❌ CRITICAL: insight_engine.py NOT FOUND")
        print("LOOKED AT:", engine_src)
    # 🔥 ENSURE GLOBAL API ROUTE EXISTS
    app_file = os.path.join(project_dir, "app.py")

    if os.path.exists(app_file):
        with open(app_file, "r") as f:
            code = f.read()

        print("[File Generator] Injecting global API route (SAFE INSERT)")

        api_code = textwrap.dedent("""
@app.route("/api/run-feature")
def run_feature():
    print("🔥 API HIT: /api/run-feature")
    return {
        "status": "success",
        "data": [
            {"name": "System Health", "value": "OK"},
            {"name": "Modules Active", "value": 3},
            {"name": "Status", "value": "Running"}
        ]
    }
""").strip()

        # 🔥 SAFE ROUTE INSERTION (FINAL FIX)

        if 'if __name__ == "__main__":' in code:
            code = code.replace(
                'if __name__ == "__main__":',
                f'\n\n{api_code}\n\nif __name__ == "__main__":',
            )

        else:
            print("⚠️ WARNING: __main__ block not found — skipping API injection")

        # 🔥 ALWAYS SAVE (CRITICAL FIX)
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

        # 🔥 GUARANTEED WORKING CONTAINER (FROM YOUR WORKING VERSION)
        if "</body>" in content and "INSIGHT_FETCH_V1" not in content:
            content = content.replace(
                "<h6>Available Features:</h6>",
                """<h6>Available Features:</h6>
        <div id="app-data" style="
            margin-top:20px;
            font-size:14px;
            background:#f9f9f9;
            padding:10px;
            border-radius:6px;
        "></div>
        """,
            )

        # 🔥 REMOVE ANY OLD SCRIPT BLOCKS COMPLETELY
        content = re.sub(
            r"<script>.*?</script>",
            "",
            content,
            flags=re.DOTALL,
        )

        # 🔥 FORCE INSERT CORRECT SCRIPT
        script_block = """
        <script>
        alert("STEP 1: SCRIPT LOADED");
        console.log("STEP 1: SCRIPT LOADED");

        console.log("STEP 2: BEFORE FETCH");

        const module = window.location.pathname.split('/').pop();
        console.log("STEP 2: MODULE NAME =", module);

        let module = window.location.pathname.split('/').pop();

        if (module === "dashboard" || module === "") {
            module = "test_suite_management"; // default module
        }
        
        const apiUrl = `/api/${module}`;

        console.log("STEP 3: FETCH URL =", apiUrl);

        fetch(apiUrl)
          .then(res => {
              console.log("STEP 4: RAW RESPONSE RECEIVED");
              return res.json();
          })
          .then(data => {
              console.log("STEP 5: PARSED DATA =", data);

              const container = document.getElementById('app-data') || document.body;

              const insights = data.insights || {};

              console.log("STEP 6: INSIGHTS =", insights);

              let html = "<div style='padding:20px;'>";

              if (insights.summary) {
                  html += `<h3>Summary</h3><p>${insights.summary}</p>`;
              }

              if (insights.insights) {
                  html += "<h3>Insights</h3><ul>";
                  insights.insights.forEach(i => {
                      html += `<li>${i}</li>`;
                  });
                  html += "</ul>";
              }

              if (insights.risks) {
                  html += "<h3>Risks</h3><ul>";
                  insights.risks.forEach(r => {
                      html += `<li>${r}</li>`;
                  });
                  html += "</ul>";
              }

              if (insights.recommendations) {
                  html += "<h3>Recommendations</h3><ul>";
                  insights.recommendations.forEach(r => {
                      html += `<li>${r}</li>`;
                  });
                  html += "</ul>";
              }

              html += "</div>";

              container.innerHTML += html;

              console.log("STEP 7: RENDER COMPLETE");
          })
          .catch(err => {
              console.error("STEP ERROR:", err);
          });
        </script>
        """

        if "</body>" in content:
            content = content.replace("</body>", script_block + "\n</body>")

        with open(file_path, "w") as f:
            f.write(content)

        print(f"[File Generator] UI injected → {file}")
