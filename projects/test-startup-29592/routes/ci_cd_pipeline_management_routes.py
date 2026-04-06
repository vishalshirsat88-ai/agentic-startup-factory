
from flask import Blueprint, jsonify, request
from services.ci_cd_pipeline_management_service import execute, add_ci_cd_pipeline_management

ci_cd_pipeline_management_bp = Blueprint('ci_cd_pipeline_management', __name__)


@ci_cd_pipeline_management_bp.route('/api/ci_cd_pipeline_management', methods=['GET'])
def ci_cd_pipeline_management_route():
    result = execute()
    return jsonify(result), 200


@ci_cd_pipeline_management_bp.route('/api/ci_cd_pipeline_management', methods=['POST'])
def add_ci_cd_pipeline_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_ci_cd_pipeline_management(name)
    return jsonify(result), 200
