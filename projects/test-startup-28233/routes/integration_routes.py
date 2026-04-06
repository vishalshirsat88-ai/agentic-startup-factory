
from flask import Blueprint, jsonify, request
from services.integration_service import execute, add_integration

integration_bp = Blueprint('integration', __name__)


@integration_bp.route('/api/integration', methods=['GET'])
def integration_route():
    result = execute()
    return jsonify(result), 200


@integration_bp.route('/api/integration', methods=['POST'])
def add_integration_route():
    data = request.get_json()
    name = data.get("name")

    result = add_integration(name)
    return jsonify(result), 200
