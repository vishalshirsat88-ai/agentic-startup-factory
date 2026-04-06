
from flask import Blueprint, jsonify, request
from services.test_automation_service import execute, add_test_automation

test_automation_bp = Blueprint('test_automation', __name__)


@test_automation_bp.route('/api/test_automation', methods=['GET'])
def test_automation_route():
    result = execute()
    return jsonify(result), 200


@test_automation_bp.route('/api/test_automation', methods=['POST'])
def add_test_automation_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_automation(name)
    return jsonify(result), 200
