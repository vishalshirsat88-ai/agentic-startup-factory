
from flask import Blueprint, jsonify, request, render_template
from services.analytics_and_reporting_service import execute, add_analytics_and_reporting

analytics_and_reporting_bp = Blueprint('analytics_and_reporting', __name__)

@analytics_and_reporting_bp.route('/analytics_and_reporting', methods=['GET'])
def analytics_and_reporting_page():
    return render_template("analytics_and_reporting.html")


@analytics_and_reporting_bp.route('/api/analytics_and_reporting', methods=['GET'])
def analytics_and_reporting_route():
    result = execute()
    return jsonify(result), 200


@analytics_and_reporting_bp.route('/api/analytics_and_reporting', methods=['POST'])
def add_analytics_and_reporting_route():
    data = request.get_json()
    name = data.get("name")

    result = add_analytics_and_reporting(name)
    return jsonify(result), 200
