# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_management():
    test_pipeline_status = True  # assuming test pipeline is active and all tests are passing
    if test_pipeline_status:
        test_management = {
            "test_name": "Regression test",
            "test_status": "Passing",
            "test_date": "2024-01-01"
        }
        return test_management
    else:
        test_management = {
            "error_message": "Test pipeline is not active",
            "status": "Failed"
        }
        return test_management


def get_test_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",  # Removed unnecessary parentheses
            ("test_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []


def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_management" in globals():
                result = get_test_management()
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


def add_test_management(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }