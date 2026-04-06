# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_security_module():
    access_token = "your_access_token_here"  # replace with actual access token
    return {"security_check": True, "access_token": access_token}

def get_security_module_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("security_module",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_security_module_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_security_module" in globals():
                result = get_security_module()
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


def add_security_module(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "security_module")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "security_module added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
