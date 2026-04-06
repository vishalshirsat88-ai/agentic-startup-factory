# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_pipeline_management():
    # Create a list to simulate testing pipelines
    testing_pipelines = ["UI Testing", "Integration Testing", "End-to-End Testing"]
    # Check if there are any pipelines to manage
    if not testing_pipelines:
        return {"error": "No testing pipelines to manage"}
    # Create a new pipeline
    new_pipeline = {"name": "Manual Testing", "status": "pending"}
    # Add the new pipeline to the list
    testing_pipelines.append(new_pipeline)
    # Return the updated list of pipelines
    return {"pipelines": testing_pipelines}

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
