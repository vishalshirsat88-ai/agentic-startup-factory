
from flask import Blueprint, jsonify, request
from services.analytics_dashboard_service import execute, add_analytics_dashboard

analytics_dashboard_bp = Blueprint('analytics_dashboard', __name__)


@analytics_dashboard_bp.route('/api/analytics_dashboard', methods=['GET'])
def analytics_dashboard_route():
    result = execute()
    return jsonify(result), 200


@analytics_dashboard_bp.route('/api/analytics_dashboard', methods=['POST'])
def add_analytics_dashboard_route():
    data = request.get_json()
    name = data.get("name")

    result = add_analytics_dashboard(name)
    return jsonify(result), 200
