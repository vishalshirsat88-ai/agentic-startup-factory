# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_deployment_management():
    deployment_status = check_deployment_status()
    pipeline_logs = retrieve_pipeline_logs()
    deployment_management_info = compile_deployment_management_info(deployment_status, pipeline_logs)
    return {"deployment_status": deployment_status, "pipeline_logs": pipeline_logs, "deployment_management_info": deployment_management_info}

def get_deployment_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("deployment_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_deployment_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_deployment_management" in globals():
                result = get_deployment_management()
            else:
                result = {"message": "no data available"}

        return {
            "status": "success",
            "data": result,
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }

def add_deployment_management(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "deployment_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "deployment_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }