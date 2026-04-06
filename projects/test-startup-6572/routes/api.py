from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)


@api_bp.route("/api/run-feature")
def run_feature():
    return jsonify(
        {
            "status": "success",
            "data": [
                {"name": "Resume Score", "value": 85},
                {"name": "Keywords Matched", "value": 12},
                {"name": "ATS Compatibility", "value": "High"},
            ],
        }
    )
