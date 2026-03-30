from db import get_connection


def get_core_logic():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM items")
        rows = cursor.fetchall()

        data = [dict(row) for row in rows]

        conn.close()

        return {"status": "success", "data": data, "error": None}

    except Exception as e:
        return {"status": "error", "data": None, "error": str(e)}


def add_item(name):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)", (name, "core_logic")
        )
        conn.commit()
        conn.close()

        return {"status": "success", "data": {"message": "Item added"}, "error": None}

    except Exception as e:
        return {"status": "error", "data": None, "error": str(e)}
