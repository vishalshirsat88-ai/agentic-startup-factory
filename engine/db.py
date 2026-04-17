import sqlite3


DB_PATH = "database.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    print("🚀 Initializing database...")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        module TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database initialized")
