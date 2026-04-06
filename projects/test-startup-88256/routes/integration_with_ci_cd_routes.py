
from flask import Blueprint, jsonify, request
from services.integration_with_ci_cd_service import execute, add_integration_with_ci_cd

integration_with_ci_cd_bp = Blueprint('integration_with_ci_cd', __name__)


@integration_with_ci_cd_bp.route('/api/integration_with_ci_cd', methods=['GET'])
def integration_with_ci_cd_route():
    result = execute()
    return jsonify(result), 200


@integration_with_ci_cd_bp.route('/api/integration_with_ci_cd', methods=['POST'])
def add_integration_with_ci_cd_route():
    data = request.get_json()
    name = data.get("name")

    result = add_integration_with_ci_cd(name)
    return jsonify(result), 200
