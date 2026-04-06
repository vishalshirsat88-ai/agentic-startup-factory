
from flask import Blueprint, jsonify, request, render_template
from services.result_analytics_service import execute, add_result_analytics

result_analytics_bp = Blueprint('result_analytics', __name__)

@result_analytics_bp.route('/result_analytics', methods=['GET'])
def result_analytics_page():
    return render_template("result_analytics.html")


@result_analytics_bp.route('/api/result_analytics', methods=['GET'])
def result_analytics_route():
    result = execute()
    return jsonify(result), 200


@result_analytics_bp.route('/api/result_analytics', methods=['POST'])
def add_result_analytics_route():
    data = request.get_json()
    name = data.get("name")

    result = add_result_analytics(name)
    return jsonify(result), 200
