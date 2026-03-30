from flask import Blueprint, jsonify
from services.health_service import get_health

health_bp = Blueprint("health", __name__)


@health_bp.route("/api/health", methods=["GET"])
def health():
    result = get_health()

    if result["status"] == "success":
        return jsonify(result), 200
    else:
        return jsonify(result), 500
