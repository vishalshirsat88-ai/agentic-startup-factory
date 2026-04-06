# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_integration():
    integration_type = input("Select integration type (API, Webhook, or Database): ")
    if integration_type.lower() in ["api", "webhook", "database"]:
        return {"status": "success", "selected_integration": integration_type}
    else:
        return {"status": "failed", "error": "Invalid integration type"}

def get_integration_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("integration",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_integration_from_db()

        if data:
            result = {"data": data, "source": "database"}
        else:
            if "get_integration" in globals():
                result = get_integration()
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

def add_integration(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "integration")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "integration added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }