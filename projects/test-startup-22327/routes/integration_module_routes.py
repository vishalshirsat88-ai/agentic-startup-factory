from flask import Blueprint, jsonify, request
from services.integration_module_service import execute, add_integration_module

integration_module_bp = Blueprint('integration_module', __name__)

@integration_module_bp.route('/api/integration-module', methods=['GET'])
def integration_module_route():
    result = execute()
    return jsonify(result), 200

@integration_module_bp.route('/api/integration-module', methods=['POST'])
def add_integration_module_route():
    data = request.get_json()
    name = data.get('name')

    result = add_integration_module(name)
    return jsonify(result), 200