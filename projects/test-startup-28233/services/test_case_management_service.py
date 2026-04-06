# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_case_management():
    # Initialize test case list
    test_cases = [
        {"id": 1, "name": "Test case 1", "description": "Description for test case 1"},
        {"id": 2, "name": "Test case 2", "description": "Description for test case 2"},
        {"id": 3, "name": "Test case 3", "description": "Description for test case 3"}
    ]

    # Filter test cases by status (default is pending)
    filtered_test_cases = [test_case for test_case in test_cases if test_case.get("status") == "pending"]

    # Return response with list of filtered test cases
    return {"status": "success", "test_cases": filtered_test_cases}


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