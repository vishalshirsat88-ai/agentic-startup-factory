# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_automation():
    test_suite = "functional_test"
    automation_status = "running"
    test_results = {"passed": [1, 2, 3], "failed": []}
    return {"test_suite": test_suite, "automation_status": automation_status, "test_results": test_results}

def get_test_automation_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_automation",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_automation_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_automation" in globals():
                result = get_test_automation()
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


def add_test_automation(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_automation")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_automation added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
