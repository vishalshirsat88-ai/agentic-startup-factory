
from flask import Blueprint, jsonify, request, render_template
from services.analytics_and_insights_service import execute, add_analytics_and_insights

analytics_and_insights_bp = Blueprint('analytics_and_insights', __name__)

@analytics_and_insights_bp.route('/analytics_and_insights', methods=['GET'])
def analytics_and_insights_page():
    return render_template("analytics_and_insights.html")


@analytics_and_insights_bp.route('/api/analytics_and_insights', methods=['GET'])
def analytics_and_insights_route():
    result = execute()
    return jsonify(result), 200


@analytics_and_insights_bp.route('/api/analytics_and_insights', methods=['POST'])
def add_analytics_and_insights_route():
    data = request.get_json()
    name = data.get("name")

    result = add_analytics_and_insights(name)
    return jsonify(result), 200
