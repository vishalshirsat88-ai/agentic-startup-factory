# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_testing_engine():
    """Returns a test pipeline."""
    test_pipeline = {
        "steps": [
            {"name": "step1", "description": "test step 1"},
            {"name": "step2", "description": "test step 2"}
        ],
        "execution_status": "pending",
        "created_at": "2022-01-01T00:00:00"
    }
    return test_pipeline

def get_testing_engine_from_db():
    """Retrieves testing engine from the database."""
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("testing_engine",)
        )
        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    """Executes the testing engine."""
    try:
        # 🔥 FIRST TRY DB
        data = get_testing_engine_from_db()

        if data:
            result = {"data": data, "source": "database"}

        elif 'get_testing_engine' in globals():
            result = get_testing_engine()
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

def add_testing_engine(name):
    """Adds a testing engine to the database."""
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "testing_engine")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "testing_engine added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }