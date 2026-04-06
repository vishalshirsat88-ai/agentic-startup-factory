# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_execution():
    """
    Returns test execution data as a dictionary.
    """
    test_data = {
        "test_id": 12345,
        "description": "E2E API Test",
        "execution_status": "running",
        "start_time": "2023-02-15 14:30:00",
        "end_time": "2023-02-15 14:35:00",
        "result": "passed"
    }
    return test_data

def get_test_execution_from_db():
    """
    Retrieves test execution data from the database.
    """
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",  # Removed the extra parenthesis
            ("test_execution",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    """
    Tries to retrieve test execution data from the database.
    If no data is found, it uses the get_test_execution function.
    """
    try:

        # 🔥 FIRST TRY DB
        data = get_test_execution_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_execution" in globals():  # No indentation change needed here
                result = get_test_execution()
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

def add_test_execution(name):
    """
    Adds a test execution to the database.
    """
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_execution")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_execution added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }