# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_reporting_and_analytics():
    test_runs = [
        {"name": "Manual Testing", "duration": 120, "environment": "Dev"},
        {"name": "Automated Testing", "duration": 30, "environment": "Stg"},
        {"name": "UAT", "duration": 60, "environment": "Prod"}
    ]

    test_results = [
        {"test_id": 1, "status": "pass", "message": "Test passed successfully"},
        {"test_id": 2, "status": "fail", "message": "Test failed due to assertion error"},
        {"test_id": 3, "status": "incomplete", "message": "Test was incomplete due to network issues"}
    ]

    reporting_data = {
        "test_runs": test_runs,
        "test_results": test_results
    }

    return reporting_data

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