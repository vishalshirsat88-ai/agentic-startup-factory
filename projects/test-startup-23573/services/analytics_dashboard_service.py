
# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_analytics_dashboard():
            result = {
                "status": "safe_fallback",
                "module": "analytics_dashboard"
            }
            return result


def get_analytics_dashboard_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("analytics_dashboard",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:

        # 🔥 FIRST TRY DB
        data = get_analytics_dashboard_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_analytics_dashboard" in globals():
                result = get_analytics_dashboard()
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


def add_analytics_dashboard(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "analytics_dashboard")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "analytics_dashboard added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
