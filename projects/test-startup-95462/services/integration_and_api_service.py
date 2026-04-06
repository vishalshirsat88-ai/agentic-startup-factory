# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_integration_and_api():
    return {
        "test_pipeline_name": "Default Test Pipeline",
        "test_pipeline_id": 1,
        "api_endpoint": "https://example.com/api/test-pipeline",
        "api_key": "test-api-key"
    }

def get_integration_and_api_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("integration_and_api",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_integration_and_api_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_integration_and_api" in globals():
                result = get_integration_and_api()
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


def add_integration_and_api(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "integration_and_api")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "integration_and_api added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
