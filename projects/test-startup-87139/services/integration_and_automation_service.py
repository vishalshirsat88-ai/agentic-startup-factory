# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_integration_and_automation():
    pipeline_status = "success"
    ci_status = "failed"
    if ci_status == "failed":
        pipeline_status = "failed"
    cd_status = "success"
    if cd_status == "failed":
        pipeline_status = "failed"
    return {"pipeline_status": pipeline_status}

def get_integration_and_automation_from_db():
    try:
        from engine.db import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("integration_and_automation",)
        )
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_integration_and_automation_from_db()
        if data:
            result = {"data": data, "source": "database"}
        else:
            if "get_integration_and_automation" in globals():
                result = get_integration_and_automation()
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

def add_integration_and_automation(name):
    try:
        from engine.db import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "integration_and_automation")
        )
        conn.commit()
        conn.close()
        return {
            "status": "success",
            "data": {"message": "integration_and_automation added"},
            "error": None
        }
    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }