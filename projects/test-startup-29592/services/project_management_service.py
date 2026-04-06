# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_project_management():
    project_status = ['pending', 'in_progress', 'completed']
    due_date = False
    milestones = []
    for milestone in range(5):
        milestones.append({
            'milestone_number': milestone,
            'description': f'Milestone {milestone}',
            'due_date': due_date
        })
        due_date = not due_date
    return {
        'status': 'success',
        'project_status': project_status,
        'due_date': due_date,
        'milestones': milestones
    }

def get_project_management_from_db():
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("project_management",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    try:
        # 🔥 FIRST TRY DB
        data = get_project_management_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_project_management" in globals():
                result = get_project_management()
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

def add_project_management(name):
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "project_management")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "project_management added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }