# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_case_manager():
    return {
        "test_case_id": 1,
        "test_case_name": "Functional testing of login feature",
        "priority": "High",
        "status": "Pending",
        "assignee": "John Doe",
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-05T12:00:00"
    }

def get_test_case_manager_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",  # Removed unnecessary tuple wrapping
            "test_case_manager"
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_case_manager_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_case_manager" in globals():
                result = get_test_case_manager()
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

def add_test_case_manager(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_case_manager")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_case_manager added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }