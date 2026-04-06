# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_pipeline_management():
    # Fetch user from database or external service
    user = {"id": 1, "name": "John Doe", "pipeline_id": 1}

    # Check if pipeline has at least one test case
    if user["pipeline_id"] and get_test_case_by_pipeline_id(user["pipeline_id"]):
        return {"status": "success", "pipeline_status": "active", "test_cases": get_test_cases()}
    else:
        return {"status": "success", "pipeline_status": "inactive"}

def get_pipeline_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("pipeline_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_pipeline_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_pipeline_management" in globals():
                result = get_pipeline_management()
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


def add_pipeline_management(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "pipeline_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "pipeline_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
