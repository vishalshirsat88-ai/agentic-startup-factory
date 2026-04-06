# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_collaboration_tools():
    return {"status": "syntax_error"}

def get_collaboration_tools_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("collaboration_tools",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_collaboration_tools_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_collaboration_tools" in globals():
                result = get_collaboration_tools()
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


def add_collaboration_tools(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "collaboration_tools")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "collaboration_tools added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
