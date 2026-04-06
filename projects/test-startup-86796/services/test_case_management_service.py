# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_case_management():
    test_cases = [
        {"id": 1, "name": "Test Case 1", "description": "This is test case 1"},
        {"id": 2, "name": "Test Case 2", "description": "This is test case 2"},
        {"id": 3, "name": "Test Case 3", "description": "This is test case 3"}
    ]
    return {"test_cases": test_cases, "status": "success"}

def get_test_case_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_case_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_case_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_case_management" in globals():
                result = get_test_case_management()
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


def add_test_case_management(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_case_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_case_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
