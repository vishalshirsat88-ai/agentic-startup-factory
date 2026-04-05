import subprocess
import time
import requests
import socket

print("🔥🔥 NEW CODE_RUNNER v3 Loaded🔥🔥")


def get_free_port():
    s = socket.socket()
    s.bind(("", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def run_app(project_path):
    try:
        port = get_free_port()

        process = subprocess.Popen(
            ["python", "app.py", str(port)],
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        time.sleep(5)

        base_url = f"http://127.0.0.1:{port}"

        try:
            res = requests.get(base_url)
            return True, f"App running at {base_url}"
        except:
            stdout, stderr = process.communicate(timeout=2)
            error_output = stdout + "\n" + stderr
            return False, error_output

    except Exception as e:
        return False, str(e)
