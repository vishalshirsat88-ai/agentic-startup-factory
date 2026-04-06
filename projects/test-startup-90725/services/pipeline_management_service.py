# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_pipeline_management():
    """Returns a list of pipeline management objects"""
    pipeline = [
        {"id": 1, "name": "Test Pipeline", "description": "Default testing pipeline"},
        {"id": 2, "name": "Staging Pipeline", "description": "Pipeline for staging environment"},
        {"id": 3, "name": "Production Pipeline", "description": "Pipeline for production environment"}
    ]
    return pipeline

def get_pipeline_management_from_db():
    """Returns a list of pipeline management names from the database"""
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",  # Removed unnecessary parentheses
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
    """Adds a pipeline management to the database"""
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