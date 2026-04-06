# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_results_dashboard():
    test_cases = [
        {"id": 1, "name": "Basic Test", "status": "passed"},
        {"id": 2, "name": "Advanced Test", "status": "failed"},
        {"id": 3, "name": "Regression Test", "status": "passed"}
    ]

    results = []
    for test_case in test_cases:
        if test_case["status"] == "passed":
            results.append({"test_case_id": test_case["id"], "result": "passed"})
        else:
            results.append({"test_case_id": test_case["id"], "result": "failed"})

    return {
        "results": results,
        "total_test_cases": len(test_cases),
        "success_rate": len(results) / len(test_cases) * 100 if len(test_cases) > 0 else 0
    }

def get_results_dashboard_from_db():
    try:
        from engine.db import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("results_dashboard",)
        )
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_results_dashboard_from_db()
        if data:
            result = {"data": data, "source": "database"}
        else:
            if "get_results_dashboard" in globals():
                result = get_results_dashboard()
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

def add_results_dashboard(name):
    try:
        from engine.db import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "results_dashboard")
        )
        conn.commit()
        conn.close()
        return {
            "status": "success",
            "data": {"message": "results_dashboard added"},
            "error": None
        }
    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }