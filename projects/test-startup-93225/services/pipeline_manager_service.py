# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_pipeline_manager():
        pipeline_definition = {
            "name": "Default Testing Pipeline",
            "stages": [
                {"name": "Pre-Test", "steps": ["run_test_prep_task"]},
                {"name": "Testing", "steps": ["run_test_tasks"]},
                {"name": "Post-Test", "steps": ["run_test_cleanup_task"]}
            ]
        }
        return pipeline_definition

def get_pipeline_manager_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("pipeline_manager",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_pipeline_manager_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_pipeline_manager" in globals():
                result = get_pipeline_manager()
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


def add_pipeline_manager(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "pipeline_manager")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "pipeline_manager added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
