# 🔥 DEBUG: SERVICE FILE GENERATED v4

def get_integration_with_ci_cd():
    """
    Returns a list of CI/CD providers along with their details.
    """
    ci_cd_providers = []

    providers = {
        "jenkins": {"name": "Jenkins", "url": "https://www.jenkins.io"},
        "gitlab": {"name": "GitLab CI/CD", "url": "https://about.gitlab.com/stages/devops"},
        "travis": {"name": "Travis CI", "url": "https://www.travis-ci.com"}
    }

    for provider in providers.values():
        ci_cd_providers.append(provider)

    return {"ci_cd_providers": ci_cd_providers, "status": "success"}

def get_integration_with_ci_cd_from_db():
    """
    Retrieves CI/CD integrations from the database.
    """
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("integration_with_ci_cd",)
        )

        rows = cursor.fetchall()
        conn.close()

        return [row[0] for row in rows]

    except Exception as e:
        return []

def execute():
    """
    Retrieves CI/CD integrations, first from the database and then from the code.
    """
    try:
        # 🔥 FIRST TRY DB
        data = get_integration_with_ci_cd_from_db()

        if data:
            result = {"data": data, "source": "database"}

        else:
            if "get_integration_with_ci_cd" in globals():
                result = get_integration_with_ci_cd()
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

def add_integration_with_ci_cd(name):
    """
    Adds a new CI/CD integration to the database.
    """
    try:
        from engine.db import get_connection

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "integration_with_ci_cd")
        )
        conn.commit()
        conn.close()

        return {
            "status": "success",
            "data": {"message": "integration_with_ci_cd added"},
            "error": None
        }

    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }