
from flask import Blueprint, jsonify, request
from services.test_executor_service import execute, add_test_executor

test_executor_bp = Blueprint('test_executor', __name__)


@test_executor_bp.route('/api/test_executor', methods=['GET'])
def test_executor_route():
    result = execute()
    return jsonify(result), 200


@test_executor_bp.route('/api/test_executor', methods=['POST'])
def add_test_executor_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_executor(name)
    return jsonify(result), 200
