# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_pipeline_management():
    # Define a dictionary to hold the pipeline management data
    pipeline_data = {
        "pipelines": [
            {"id": 1, "name": "Automated Testing", "status": "active"},
            {"id": 2, "name": "Manual Quality Assurance", "status": "inactive"}
        ]
    }

    # Define a dictionary to hold the filtered pipeline data
    filtered_data = {
        "pipelines": []
    }

    # Loop through each pipeline in the pipeline data
    for pipeline in pipeline_data["pipelines"]:
        # Check if the pipeline status is 'active'
        if pipeline["status"] == "active":
            # Add the active pipeline to the filtered data
            filtered_data["pipelines"].append(pipeline)

    # Return the filtered pipeline data under 'pipelines_management' key
    return {"pipelines_management": filtered_data}

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
