# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_result_analysis():
    # Get the test results from the database or API
    results = [{"test_name": "Test 1", "test_result": "pass"}, {"test_name": "Test 2", "test_result": "fail"}]

    # Calculate the pass rate
    pass_count = sum(1 for result in results if result["test_result"] == "pass")
    pass_rate = (pass_count / len(results)) * 100 if results else 0

    # Create the analysis dictionary
    analysis = {
        "test_results": results,
        "pass_rate": round(pass_rate, 2),
        "average_time_taken": sum(result.get("time_taken", 0) for result in results) / len(results) if results else 0
    }

    # Return the analysis
    return analysis


def get_result_analysis_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("result_analysis",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []


def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_result_analysis_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_result_analysis" in globals():
                result = get_result_analysis()
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


def add_result_analysis(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "result_analysis")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "result_analysis added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }



# or 

# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_result_analysis():
    # Get the test results from the database or API
    results = [{"test_name": "Test 1", "test_result": "pass"}, {"test_name": "Test 2", "test_result": "fail"}]

    # Calculate the pass rate
    pass_count = sum(1 for result in results if result["test_result"] == "pass")
    pass_rate = (pass_count / len(results)) * 100 if results else 0

    # Create the analysis dictionary
    analysis = {
        "test_results": results,
        "pass_rate": round(pass_rate, 2),
        "average_time_taken": sum(result.get("time_taken", 0) for result in results) / len(results) if results else 0
    }

    return {
        "status": "success",
        "data": analysis,
        "error": None
    }


def get_result_analysis_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("result_analysis",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []


def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_result_analysis_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_result_analysis" in globals():
                result = get_result_analysis()
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


def add_result_analysis(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "result_analysis")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "result_analysis added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }