# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_management():
    # Check if test pipeline status is active
    if "test_pipeline_active" in TestStartupDatabase.get_all_test_configurations():
        # If test pipeline status is active, check if all test cases completed successfully
        if all(test_case["status"] == "success" for test_case in TestStartupDatabase.get_all_test_results()):
            # If all test cases were completed successfully, retrieve the test report
            test_report = TestStartupDatabase.get_test_report()
            return {"status": "success", "test_report": test_report}
        else:
            # If not all test cases were completed successfully, return an error message
            return {"status": "error", "message": "Not all test cases were completed successfully"}
    else:
        # If test pipeline status is not active, return an error message
        return {"status": "error", "message": "Test pipeline is not active"}

def get_test_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
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
