# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_execution() -> dict:
    """Retrieve test execution details."""
    return {"status": "success", "test_name": "Basic Test", "execution_time": 10}

def get_test_execution_from_db() -> list:
    """Retrieve test execution details from database."""
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_execution",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute() -> dict:
    """Execute test execution."""
    try:

        # 🔥 FIRST TRY DB
        data = get_test_execution_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_execution" in globals():
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

def add_test_execution(name: str) -> dict:
    """Add test execution."""
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