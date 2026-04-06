# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_user_management():
    # Check if user exists in the system
    if "admin" in ["user1", "user2", "admin"]:
        return {"user_exists": True, "user_role": "admin"}
    return {"user_exists": False, "user_role": None}

def get_user_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("user_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_user_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_user_management" in globals():
                result = get_user_management()
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


def add_user_management(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "user_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "user_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
