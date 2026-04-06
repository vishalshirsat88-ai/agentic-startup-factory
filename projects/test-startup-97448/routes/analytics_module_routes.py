
from flask import Blueprint, jsonify, request, render_template
from services.analytics_module_service import execute, add_analytics_module

analytics_module_bp = Blueprint('analytics_module', __name__)

@analytics_module_bp.route('/analytics_module', methods=['GET'])
def analytics_module_page():
    return render_template("analytics_module.html")


@analytics_module_bp.route('/api/analytics_module', methods=['GET'])
def analytics_module_route():
    result = execute()
    return jsonify(result), 200


@analytics_module_bp.route('/api/analytics_module', methods=['POST'])
def add_analytics_module_route():
    data = request.get_json()
    name = data.get("name")

    result = add_analytics_module(name)
    return jsonify(result), 200
