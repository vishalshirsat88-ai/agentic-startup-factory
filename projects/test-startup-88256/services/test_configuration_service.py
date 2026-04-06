# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_configuration():
    test_environment = input("Enter your test environment (dev, staging, prod): ")
    test_framework = input("Enter your test framework (pytest, unittest, behave): ")

    if test_environment == "dev" and test_framework in ["pytest", "unittest"]:
        return {"status": "success", "details": "Test configuration for dev environment with pytest or unittest"}
    elif test_environment == "prod" and test_framework in ["pytest", "unittest"]:
        return {"status": "partial success", "details": "Test configuration for prod environment with pytest or unittest"}
    else:
        return {"status": "failure", "details": "Invalid test environment or test framework"}

def get_test_configuration_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_configuration",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_configuration_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_configuration" in globals():
                result = get_test_configuration()
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

def add_test_configuration(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_configuration")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": f"test_configuration '{name}' added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }