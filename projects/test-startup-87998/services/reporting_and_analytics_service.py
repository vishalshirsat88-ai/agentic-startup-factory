# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_reporting_and_analytics():
    # Generate test results
    test_results = [
        {"test_id": 1, "test_name": "Test Case 1", "status": "passed", "timestamp": "2024-01-01T12:00:00"},
        {"test_id": 2, "test_name": "Test Case 2", "status": "failed", "timestamp": "2024-01-01T12:05:00"}
    ]

    # Group results by test status
    grouped_results = {}
    for test_result in test_results:
        status = test_result["status"]
        if status not in grouped_results:
            grouped_results[status] = []
        grouped_results[status].append(test_result)

    # Calculate test metrics
    passed_results = grouped_results.get("passed", [])
    failed_results = grouped_results.get("failed", [])
    metrics = {
        "passed": len(passed_results),
        "failed": len(failed_results),
        "total": len(passed_results) + len(failed_results)
    }

    # Return reporting and analytics data
    return {"status": "success", "metrics": metrics, "results": grouped_results}

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