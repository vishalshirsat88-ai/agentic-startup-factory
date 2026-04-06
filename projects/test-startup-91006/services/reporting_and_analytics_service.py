# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_reporting_and_analytics():
    test_results = [
        {"test_name": "Unit Test 1", "status": "passed", "time_taken": 0.05},
        {"test_name": "Integration Test 2", "status": "failed", "time_taken": 0.2},
        {"test_name": "End-to-End Test 3", "status": "passed", "time_taken": 0.15}
    ]
    reporting_and_analytics_data = {
        "test_results": test_results,
        "total_passed_tests": len([test for test in test_results if test["status"] == "passed"]),
        "total_failed_tests": len([test for test in test_results if test["status"] == "failed"]),
        "average_time_taken": sum([test["time_taken"] for test in test_results]) / len(test_results)
    }
    return reporting_and_analytics_data

def get_reporting_and_analytics_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("reporting_and_analytics",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_reporting_and_analytics_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_reporting_and_analytics" in globals():
                result = get_reporting_and_analytics()
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


def add_reporting_and_analytics(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "reporting_and_analytics")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "reporting_and_analytics added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
