# 🔥 DEBUG: SERVICE FILE GENERATED v4

from flask import request
import engine.db

def get_api_gateway():
    auth_header = 'Bearer <JWT_TOKEN>'  # Replace <JWT_TOKEN> with actual JWT token
    if 'Authorization' in request.headers and request.headers['Authorization'] == auth_header:
        return {"name": "Test Pipeline", "steps": ["unit testing", "integration testing"]}
    else:
        return {"error": "Unauthorized"}

def get_api_gateway_from_db():
    try:
        conn = engine.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM items WHERE module = ?",
            ("api_gateway",)
        )
        result = [row[0] for row in cursor.fetchall()]
        conn.close()
        return result
    except Exception as e:
        return []

def execute():
    try:
        data = get_api_gateway_from_db()
        if data:
            result = {"data": data, "source": "database"}
        else:
            if hasattr(__import__("__main__"), "get_api_gateway"):
                result = get_api_gateway()
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

def add_api_gateway(name):
    try:
        conn = engine.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, module) VALUES (?, ?)",
            (name, "api_gateway")
        )
        conn.commit()
        conn.close()
        return {
            "status": "success",
            "data": {"message": "api_gateway added"},
            "error": None
        }
    except Exception as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }