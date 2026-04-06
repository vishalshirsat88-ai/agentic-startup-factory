# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_test_scheduling():
    """
    Set the scheduling frequency to daily and the test start time to 8am
    and return the scheduling configuration as a JSON object.
    """
    scheduling_frequency = "daily"
    test_start_time = "08:00"

    # Create a dictionary to store the scheduling configuration
    scheduling_config = {"frequency": scheduling_frequency, "test_start_time": test_start_time}

    # Return the scheduling configuration as a JSON object
    return {"status": "success", "scheduling_config": scheduling_config}

def get_test_scheduling_from_db():
    """
    Retrieve test scheduling configurations from the database.
    """
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("test_scheduling",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    """
    Execute the test scheduling service.
    """
    try:
        # 🔥 FIRST TRY DB
        data = get_test_scheduling_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_test_scheduling" in globals():
                result = get_test_scheduling()
            else:
                result = {"message": "no data available"}

        # Return the result as a JSON object
        return {
            "status": "success",
            "data": result,
            "error": None
        }

    except Exception as e:
        # Return the error message as a JSON object
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }

def add_test_scheduling(name):
    """
    Add a new test scheduling configuration to the database.
    """
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "test_scheduling")
        )
        conn.commit()
        conn.close()

        # Return the result as a JSON object
        return {
            "status": "success",
            "data": {"message": "test_scheduling added"},
            "error": None
        }

    except Exception as e:
        # Return the error message as a JSON object
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }