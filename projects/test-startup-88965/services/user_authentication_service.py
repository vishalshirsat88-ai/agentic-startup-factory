# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_user_authentication():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if not username or not password:
        return {"status": "error", "message": "Username and password are required"}
    if username == "admin" and password == "password":
        return {"status": "success", "user": {"username": "admin"}}
    return {"status": "error", "message": "Invalid username or password"}

def get_user_authentication_from_db():
    from engine.db import get_connection
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("user_authentication",)
        )
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_user_authentication_from_db()
        if data:
            result = {"data": data, "source": "database"}
        else:
            if "get_user_authentication" in globals():
                result = get_user_authentication()
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

def add_user_authentication(name):
    from engine.db import get_connection
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "user_authentication")
        )
        conn.commit()
        conn.close()
        return {
            "status": "success",
            "data": {"message": "user_authentication added"},
            "error": None
        }
    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }