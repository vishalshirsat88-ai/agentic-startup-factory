# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_data_management():
    """Returns test data management information."""
    test_data = {
        "tests": ["test1", "test2", "test3"],
        "environment": "local",
        "status": "active"
    }
    return test_data

def get_test_data_management_from_db():
    """Retrieves test data management data from the database."""
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_data_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    """Executes the data management logic."""
    try:
        # 🔥 FIRST TRY DB
        data = get_test_data_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_data_management" in globals():
                result = get_test_data_management()
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

def add_test_data_management(name):
    """Adds test data management to the database."""
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_data_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_data_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }