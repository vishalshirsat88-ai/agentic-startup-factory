# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_deployment_and_rollback():
    # Check if deployment is in progress
    if "deployment_in_progress" in ["true"]:
        # Trigger rollback if deployment is in progress
        return {"message": "Deployment is in progress, triggering rollback"}
    else:
        # Return deployment and rollback details
        return {"deployment_url": "https://example.com/deployment", "rollback_url": "https://example.com/rollback"}

def get_deployment_and_rollback_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("deployment_and_rollback",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_deployment_and_rollback_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_deployment_and_rollback" in globals():
                result = get_deployment_and_rollback()
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


def add_deployment_and_rollback(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "deployment_and_rollback")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "deployment_and_rollback added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
