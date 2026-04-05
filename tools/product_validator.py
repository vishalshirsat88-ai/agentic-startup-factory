import requests
import sqlite3


def test_api(base_url):
    results = {}

    try:
        res = requests.get(f"{base_url}/")
        results["root_status"] = res.status_code
    except Exception as e:
        results["root_error"] = str(e)

    return results


def test_endpoint(base_url, endpoint):
    try:
        res = requests.get(f"{base_url}{endpoint}")
        return {
            "status": res.status_code,
            "response": res.json() if res.status_code == 200 else None,
        }
    except Exception as e:
        return {"error": str(e)}


def test_post_endpoint(base_url, endpoint, payload):
    try:
        res = requests.post(f"{base_url}{endpoint}", json=payload)
        return {
            "status": res.status_code,
            "response": res.json() if res.status_code in [200, 201] else None,
        }
    except Exception as e:
        return {"error": str(e)}


def test_db(db_path="database.db"):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        return {"status": "success", "tables": tables}
    except Exception as e:
        return {"status": "fail", "error": str(e)}
