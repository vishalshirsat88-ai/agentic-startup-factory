from flask import Blueprint, jsonify, request
from services.pipeline_management_service import execute, add_pipeline_management

pipeline_management_bp = Blueprint('pipeline_management', __name__)

@pipeline_management_bp.route('/api/pipeline_management', methods=['GET'])
def pipeline_management_route():
    result = execute()
    return jsonify(result), 200


@pipeline_management_bp.route('/api/pipeline_management', methods=['POST'])
def add_pipeline_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_pipeline_management(name)
    return jsonify(result), 200
