
    # 🔥 DEBUG: SERVICE FILE GENERATED v4

    def get_test_reporting():
if "test_results" in session or "test_results" in flask.g:
    return {"test_results": session["test_results"]}
else:
    return {"error": "Test results not available"}

    def get_test_reporting_from_db():
        try:
            from engine.db import get_connection

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT name FROM items WHERE module = ?",
                ("test_reporting",)
            )

            rows = cursor.fetchall()
            conn.close()

            return [row[0] for row in rows]

        except Exception as e:
            return []

    def execute():
        try:

            # 🔥 FIRST TRY DB
            data = get_test_reporting_from_db()

            if data:
                result = {"data": data, "source": "database"}

            else:
                if "get_test_reporting" in globals():
                    result = get_test_reporting()
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


    def add_test_reporting(name):
        try:
            from engine.db import get_connection

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO items (name, module) VALUES (?, ?)",
                (name, "test_reporting")
            )
            conn.commit()
            conn.close()

            return {
                "status": "success",
                "data": {"message": "test_reporting added"},
                "error": None
            }

        except Exception as e:
            return {
                "status": "error",
                "data": None,
                "error": str(e)
            }
