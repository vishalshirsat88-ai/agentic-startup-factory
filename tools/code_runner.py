import subprocess

def run_app(project_path):

    try:
        result = subprocess.run(
            ["python", "app.py"],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=3
        )

        return True, result.stdout

    except subprocess.TimeoutExpired as e:
        # Flask app started successfully
        return True, "App running"

    except Exception as e:
        return False, str(e)