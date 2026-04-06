# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_pipeline_module():
    # Define the pipeline stages
    pipeline_stages = {'preprocessing', 'testing', 'analysis', 'reporting'}

    # Define the current stage of the pipeline
    current_stage = 'preprocessing'

    # Update the current stage if it's already been executed
    if 'preprocessing' not in pipeline_stages:
        current_stage = 'testing'

    # Define the pipeline module
    pipeline_module = {
        "current_stage": current_stage,
        "stages": list(pipeline_stages)
    }

    return pipeline_module

def get_pipeline_module_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("pipeline_module",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_pipeline_module_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_pipeline_module" in globals():
                result = get_pipeline_module()
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


def add_pipeline_module(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "pipeline_module")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "pipeline_module added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
