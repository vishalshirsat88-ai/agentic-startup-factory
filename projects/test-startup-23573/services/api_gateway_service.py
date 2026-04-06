
# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_api_gateway():
            result = {
                "status": "safe_fallback",
                "module": "api_gateway"
            }
            return result


def get_api_gateway_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("api_gateway",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:

        # 🔥 FIRST TRY DB
        data = get_api_gateway_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_api_gateway" in globals():
                result = get_api_gateway()
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


def add_api_gateway(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "api_gateway")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "api_gateway added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
