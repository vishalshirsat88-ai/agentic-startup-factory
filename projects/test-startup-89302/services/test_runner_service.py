# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_runner():
    test_config = {
        "python_version": "3.9.5",
        "test_environment": "docker",
        "test_suite": ["unit_tests", "integration_tests"]
    }
    return test_config


def get_test_runner_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_runner",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []


def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_runner_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_runner" in globals():
                result = get_test_runner()
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


def add_test_runner(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_runner")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_runner added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }