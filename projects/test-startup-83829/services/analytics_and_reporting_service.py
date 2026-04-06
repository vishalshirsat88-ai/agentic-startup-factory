# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_analytics_and_reporting():
    pipelines = [
        {"id": 1, "name": "Unit Tests", "status": "passed"},
        {"id": 2, "name": "Integration Tests", "status": "failed"},
        {"id": 3, "name": "E2E Tests", "status": "pending"},
        {"id": 4, "name": "Security Tests", "status": "pending"},
        {"id": 5, "name": "UI Tests", "status": "failed"}
    ]
    failed_and_pending_pipelines = [pipeline for pipeline in pipelines if pipeline["status"] in ["failed", "pending"]]
    return {
        "pipelines": pipelines,
        "failed_and_pending_pipelines": failed_and_pending_pipelines,
        "total_tests": len(pipelines),
        "passed_tests": len([pipeline for pipeline in pipelines if pipeline["status"] == "passed"])
    }

def get_analytics_and_reporting_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("analytics_and_reporting",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_analytics_and_reporting_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_analytics_and_reporting" in globals():
                result = get_analytics_and_reporting()
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


def add_analytics_and_reporting(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "analytics_and_reporting")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "analytics_and_reporting added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
