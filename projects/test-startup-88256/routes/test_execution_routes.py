
from flask import Blueprint, jsonify, request
from services.test_execution_service import execute, add_test_execution

test_execution_bp = Blueprint('test_execution', __name__)


@test_execution_bp.route('/api/test_execution', methods=['GET'])
def test_execution_route():
    result = execute()
    return jsonify(result), 200


@test_execution_bp.route('/api/test_execution', methods=['POST'])
def add_test_execution_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_execution(name)
    return jsonify(result), 200
