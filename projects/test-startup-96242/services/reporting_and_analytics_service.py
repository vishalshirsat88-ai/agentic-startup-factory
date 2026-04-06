# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_reporting_and_analytics():
    current_testing_pipelines = 5
    passed_testing_pipelines = 3
    failed_testing_pipelines = current_testing_pipelines - passed_testing_pipelines

    pipeline_status = {"total": current_testing_pipelines, "passed": passed_testing_pipelines, "failed": failed_testing_pipelines}

    test_execution_time = 120 # in seconds
    average_execution_time = test_execution_time / 2
    avg_exec_time_pipeline = {"average_execution_time": average_execution_time}

    reporting_and_analytics = {"pipeline_status": pipeline_status, "avg_exec_time_pipeline": avg_exec_time_pipeline}
    return reporting_and_analytics

def get_reporting_and_analytics_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("reporting_and_analytics",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_reporting_and_analytics_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_reporting_and_analytics" in globals():
                result = get_reporting_and_analytics()
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


def add_reporting_and_analytics(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "reporting_and_analytics")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "reporting_and_analytics added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
