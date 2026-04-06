
from flask import Blueprint, jsonify, request
from services.test_results_analysis_service import execute, add_test_results_analysis

test_results_analysis_bp = Blueprint('test_results_analysis', __name__)


@test_results_analysis_bp.route('/api/test_results_analysis', methods=['GET'])
def test_results_analysis_route():
    result = execute()
    return jsonify(result), 200


@test_results_analysis_bp.route('/api/test_results_analysis', methods=['POST'])
def add_test_results_analysis_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_results_analysis(name)
    return jsonify(result), 200
