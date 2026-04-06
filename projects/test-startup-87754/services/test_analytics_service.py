# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_analytics():
    try:
        test_results_data = {
            "tests_run": 10,
            "tests_passed": 9,
            "tests_failed": 1,
            "average_duration": 30,
            "average_difficulty": 5
        }
        return {"test_results": test_results_data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_test_analytics_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_analytics",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_analytics_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_analytics" in globals():
                result = get_test_analytics()
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

def add_test_analytics(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_analytics")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_analytics added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }