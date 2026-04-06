
from flask import Blueprint, jsonify, request
from services.result_analysis_service import execute, add_result_analysis

result_analysis_bp = Blueprint('result_analysis', __name__)


@result_analysis_bp.route('/api/result_analysis', methods=['GET'])
def result_analysis_route():
    result = execute()
    return jsonify(result), 200


@result_analysis_bp.route('/api/result_analysis', methods=['POST'])
def add_result_analysis_route():
    data = request.get_json()
    name = data.get("name")

    result = add_result_analysis(name)
    return jsonify(result), 200
