
    # 🔥 DEBUG: SERVICE FILE GENERATED v4

    def get_test_analytics():
test_runs = [
    {"id": 1, "success": True, "date": "2022-01-01"},
    {"id": 2, "success": False, "date": "2022-01-02"},
    {"id": 3, "success": True, "date": "2022-01-03"},
]
successful_tests = [test for test in test_runs if test["success"]]
failed_tests = [test for test in test_runs if not test["success"]]
total_tests = len(test_runs)
successful_test_percentage = (len(successful_tests) / total_tests) * 100 if total_tests > 0 else 0
return {
    "successful_tests": successful_tests,
    "failed_tests": failed_tests,
    "total_tests": total_tests,
    "successful_test_percentage": successful_test_percentage,
}

    def get_test_analytics_from_db():
        try:
            from engine.db import get_connection

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT name FROM items WHERE module = ?",
                ("test_analytics",)
            )

            rows = cursor.fetchall()
            conn.close()

            return [row[0] for row in rows]

        except Exception as e:
            return []

    def execute():
        try:

            # 🔥 FIRST TRY DB
            data = get_test_analytics_from_db()

            if data:
                result = {"data": data, "source": "database"}

            else:
                if "get_test_analytics" in globals():
                    result = get_test_analytics()
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


    def add_test_analytics(name):
        try:
            from engine.db import get_connection

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO items (name, module) VALUES (?, ?)",
                (name, "test_analytics")
            )
            conn.commit()
            conn.close()

            return {
                "status": "success",
                "data": {"message": "test_analytics added"},
                "error": None
            }

        except Exception as e:
            return {
                "status": "error",
                "data": None,
                "error": str(e)
            }
