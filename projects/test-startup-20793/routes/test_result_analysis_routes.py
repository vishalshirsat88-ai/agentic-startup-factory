
from flask import Blueprint, jsonify, request
from services.test_result_analysis_service import execute, add_test_result_analysis

test_result_analysis_bp = Blueprint('test_result_analysis', __name__)


@test_result_analysis_bp.route('/api/test_result_analysis', methods=['GET'])
def test_result_analysis_route():
    result = execute()
    return jsonify(result), 200


@test_result_analysis_bp.route('/api/test_result_analysis', methods=['POST'])
def add_test_result_analysis_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_result_analysis(name)
    return jsonify(result), 200
