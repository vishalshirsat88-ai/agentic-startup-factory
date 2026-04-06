# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_integration_module():
    """Return available integration modules and actions"""
    supported_modules = ["gitlab", "jira", "slack", "google_drive"]
    module_actions = {
        "gitlab": ["get_issues", "create_merge_request"],
        "jira": ["get_issues", "create_issue"],
        "slack": ["send_message", "post_to_channel"],
        "google_drive": ["upload_file", "download_file"]
    }
    return {
        "status": "success",
        "integration_modules": supported_modules,
        "module_actions": module_actions
    }

def get_integration_module_from_db():
    """Return integration modules from database"""
    try:
        from engine.db import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM items WHERE module = ?", ("integration_module",))
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
    except Exception as e:
        return []

def execute():
    """Execute and return result"""
    try:
        data = get_integration_module_from_db()
        if data:
            result = {"data": data, "source": "database"}
        elif hasattr(__import__("__main__"), "get_integration_module"):
            result = get_integration_module()
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

def add_integration_module(name):
    """Add integration module to database"""
    try:
        from engine.db import get_connection
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO items (name, module) VALUES (?, ?)"
        cursor.execute(query, (name, "integration_module"))
        conn.commit()
        conn.close()
        return {
            "status": "success",
            "data": {"message": "integration_module added"},
            "error": None
        }
    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }