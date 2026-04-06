
        # 🔥 DEBUG: SERVICE FILE GENERATED v4

        def get_reporting_and_analytics():
    # Get all test cases from the database
    test_cases = [
        {"id": 1, "test_name": "Test Case 1", "status": "passed"},
        {"id": 2, "test_name": "Test Case 2", "status": "failed"},
        {"id": 3, "test_name": "Test Case 3", "status": "skipped"}
    ]

    # Calculate total number of test cases
    total_test_cases = len(test_cases)

    # Calculate number of passed test cases
    passed_test_cases = len([case for case in test_cases if case["status"] == "passed"])

    # Calculate number of failed test cases
    failed_test_cases = len([case for case in test_cases if case["status"] == "failed"])

    # Calculate number of skipped test cases
    skipped_test_cases = len([case for case in test_cases if case["status"] == "skipped"])

    # Calculate test case pass percentage
    pass_percentage = (passed_test_cases / total_test_cases) * 100 if total_test_cases > 0 else 0

    # Create reporting and analytics data
    reporting_and_analytics_data = {
        "total_test_cases": total_test_cases,
        "passed_test_cases": passed_test_cases,
        "failed_test_cases": failed_test_cases,
        "skipped_test_cases": skipped_test_cases,
        "pass_percentage": pass_percentage
    }

    return reporting_and_analytics_data

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
        