# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_analytics_module():
    # Define the function to handle the testing pipeline analytics
    pass

def get_analytics_module_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("analytics_module",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        print(f"Error: {e}")
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_analytics_module_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_analytics_module" in globals():
                result = get_analytics_module()
            else:
                result = {"message": "no data available"}

        return {
            "status": "success",
            "data": result,
            "error": None
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }


def add_analytics_module(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "analytics_module")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "analytics_module added"},
            "error": None
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }