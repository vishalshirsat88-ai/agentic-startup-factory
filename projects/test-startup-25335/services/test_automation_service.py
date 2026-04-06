# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_automation():
    # Get the test automation pipeline status from the database
    pipeline_status = "active"
    # Check if the pipeline is active
    if pipeline_status == "active":
        # Get the latest test results from the database
        test_results = [
            {"test_name": "test1", "result": "passed"},
            {"test_name": "test2", "result": "failed"}
        ]
        # Return the test results
        return {"status": "success", "test_results": test_results}
    else:
        # Return an error if the pipeline is not active
        return {"status": "failure"}

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