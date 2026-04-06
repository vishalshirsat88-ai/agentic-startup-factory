# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_deployment_manager():
    return {
        "status": "success",
        "test_pipeline_id": "TP123",
        "test_run_id": "TR456",
        "deployment_status": "deployed"
    }

def get_deployment_manager_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("deployment_manager",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_deployment_manager_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_deployment_manager" in globals():
                result = get_deployment_manager()
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


def add_deployment_manager(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "deployment_manager")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "deployment_manager added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
