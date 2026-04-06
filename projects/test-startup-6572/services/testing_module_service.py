# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_testing_module():
    return {
        "test_id": "TEST-001",
        "test_name": "Smoke Test",
        "test_status": "running"
    }

def get_testing_module_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("testing_module",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_testing_module_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_testing_module" in globals():
                result = get_testing_module()
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


def add_testing_module(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "testing_module")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "testing_module added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
