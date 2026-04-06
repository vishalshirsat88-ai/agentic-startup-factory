# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_suite_management():
    test_suites = [{"suite_name": "Functional Test Suite", "tests": 10, "results": "passed"},
                  {"suite_name": "Unit Test Suite", "tests": 20, "results": "passed"},
                  {"suite_name": "Integration Test Suite", "tests": 15, "results": "failed"}]
    return {"test_suites": test_suites}

def get_test_suite_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_suite_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_suite_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_suite_management" in globals():
                result = get_test_suite_management()
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


def add_test_suite_management(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_suite_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_suite_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
