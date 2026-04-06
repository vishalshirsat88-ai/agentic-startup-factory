# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_data_management():
    test_data_ids = ["data_1", "data_2", "data_3"]
    test_data = {
        "data_1": {"test_case_id": 1, "description": "First test case"},
        "data_2": {"test_case_id": 2, "description": "Second test case"},
        "data_3": {"test_case_id": 3, "description": "Third test case"}
    }
    return {"test_data_ids": test_data_ids, "test_data": test_data}

def get_test_data_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_data_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_test_data_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_data_management" in globals():
                result = get_test_data_management()
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


def add_test_data_management(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_data_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "test_data_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
