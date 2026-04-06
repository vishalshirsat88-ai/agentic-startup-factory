# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_notifications_module():
    notification_data = {
        "new_test_run_available": "Run your automated tests with the latest test environment",
        "new_test_case_added": "Get notified when a new test case is added to the pipeline",
        "test_run_failed": "Get notified when a test run fails to help resolve the issue quickly"
    }
    return notification_data

def get_notifications_module_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("notifications_module",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_notifications_module_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_notifications_module" in globals():
                result = get_notifications_module()
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


def add_notifications_module(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "notifications_module")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "notifications_module added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
