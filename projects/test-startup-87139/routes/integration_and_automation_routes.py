
from flask import Blueprint, jsonify, request
from services.integration_and_automation_service import execute, add_integration_and_automation

integration_and_automation_bp = Blueprint('integration_and_automation', __name__)


@integration_and_automation_bp.route('/api/integration_and_automation', methods=['GET'])
def integration_and_automation_route():
    result = execute()
    return jsonify(result), 200


@integration_and_automation_bp.route('/api/integration_and_automation', methods=['POST'])
def add_integration_and_automation_route():
    data = request.get_json()
    name = data.get("name")

    result = add_integration_and_automation(name)
    return jsonify(result), 200
