
    # 🔥 DEBUG: SERVICE FILE GENERATED v4

    def get_test_result_analysis():
results = [
    {"test_id": 1, "pass_rate": 90, "duration": 45},
    {"test_id": 2, "pass_rate": 85, "duration": 30},
    {"test_id": 3, "pass_rate": 98, "duration": 60}
]
return {"test_results": results, "analysis": "Overall pass rate is 91%"}

    def get_test_result_analysis_from_db():
        try:
            from engine.db import get_connection

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT name FROM items WHERE module = ?",
                ("test_result_analysis",)
            )

            rows = cursor.fetchall()
            conn.close()

            return [row[0] for row in rows]

        except Exception as e:
            return []

    def execute():
        try:

            # 🔥 FIRST TRY DB
            data = get_test_result_analysis_from_db()

            if data:
                result = {"data": data, "source": "database"}

            else:
                if "get_test_result_analysis" in globals():
                    result = get_test_result_analysis()
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


    def add_test_result_analysis(name):
        try:
            from engine.db import get_connection

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO items (name, module) VALUES (?, ?)",
                (name, "test_result_analysis")
            )
            conn.commit()
            conn.close()

            return {
                "status": "success",
                "data": {"message": "test_result_analysis added"},
                "error": None
            }

        except Exception as e:
            return {
                "status": "error",
                "data": None,
                "error": str(e)
            }
