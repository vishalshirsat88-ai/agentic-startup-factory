
def get_health():
    try:
        return {"status": "success", "message": "Service is healthy"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
