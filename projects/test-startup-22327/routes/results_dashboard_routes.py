from flask import Blueprint, jsonify, request
from services.results_dashboard_service import execute, add_results_dashboard

results_dashboard_bp = Blueprint('results_dashboard', __name__)

@results_dashboard_bp.route('/api/results_dashboard', methods=['GET'])
def results_dashboard_route():
    result = execute()
    return jsonify(result), 200

@results_dashboard_bp.route('/api/results_dashboard', methods=['POST'])
def add_results_dashboard_route():
    data = request.get_json()
    name = data.get('name')

    result = add_results_dashboard(name)
    return jsonify(result), 200