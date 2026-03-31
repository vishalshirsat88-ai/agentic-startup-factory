
        from db import get_connection


        def get_subscription_manager():
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM items")
                rows = cursor.fetchall()

                data = [dict(row) for row in rows]

                conn.close()

                return {
                    "status": "success",
                    "data": data,
                    "error": None
                }

            except Exception as e:
                return {
                    "status": "error",
                    "data": None,
                    "error": str(e)
                }


        def add_subscription_manager(name):
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("INSERT INTO items (name) VALUES (?)", (name,))
                conn.commit()
                conn.close()

                return {
                    "status": "success",
                    "data": {"message": "subscription_manager added"},
                    "error": None
                }

            except Exception as e:
                return {
                    "status": "error",
                    "data": None,
                    "error": str(e)
                }
        