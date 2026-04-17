import os
import sqlite3

try:
    import requests
except ImportError:
    requests = None


REQUIRED_KEYS = ["core_features", "user_flows", "edge_cases"]


def validate_product(product):

    if not product:
        return False, "Product definition is empty"

    if not isinstance(product, dict):
        return False, "Product must be a dictionary"

    for key in REQUIRED_KEYS:
        if key not in product:
            return False, f"Missing required key: {key}"

        value = product[key]

        if not isinstance(value, list):
            return False, f"Key '{key}' must be a list"

        if len(value) == 0:
            return False, f"Key '{key}' must not be empty"

        for item in value:
            if not isinstance(item, str) or not item.strip():
                return False, f"Items in '{key}' must be non-empty strings"

    return True, "Valid product definition"


def is_valid(product):
    ok, _ = validate_product(product)
    return ok


# ---- QA Agent helpers ----

def test_api(base_url):

    if requests is None:
        return {"status": "skipped", "reason": "requests not installed"}

    try:
        response = requests.get(base_url, timeout=5)
        return {
            "status": "ok" if response.status_code == 200 else "fail",
            "code": response.status_code,
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def test_endpoint(base_url, path):

    if requests is None:
        return {"status": "skipped", "reason": "requests not installed"}

    try:
        url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
        response = requests.get(url, timeout=5)
        return {
            "endpoint": path,
            "status": "ok" if response.status_code == 200 else "fail",
            "code": response.status_code,
        }
    except Exception as e:
        return {"endpoint": path, "status": "error", "error": str(e)}


def test_post_endpoint(base_url, path, payload=None):

    if requests is None:
        return {"status": "skipped", "reason": "requests not installed"}

    try:
        url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
        response = requests.post(url, json=payload or {}, timeout=5)
        return {
            "endpoint": path,
            "status": "ok" if response.status_code in (200, 201) else "fail",
            "code": response.status_code,
        }
    except Exception as e:
        return {"endpoint": path, "status": "error", "error": str(e)}


def test_db(db_path="database.db"):

    if not os.path.exists(db_path):
        return {"status": "missing", "path": db_path}

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()

        return {
            "status": "ok",
            "path": db_path,
            "tables": tables,
            "table_count": len(tables),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}
