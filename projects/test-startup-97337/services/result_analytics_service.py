# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_result_analytics():
    test_results = [
        {"test_name": "Unit Test", "status": "passed", "time_taken": 0.5},
        {"test_name": "Integration Test", "status": "failed", "time_taken": 1.2},
        {"test_name": "System Test", "status": "passed", "time_taken": 0.8}
    ]
    result = {"test_results": test_results, "overall_success_percentage": 66}
    return result

def get_result_analytics_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("result_analytics",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_result_analytics_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_result_analytics" in globals():
                result = get_result_analytics()
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


def add_result_analytics(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "result_analytics")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "result_analytics added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
