
from flask import Blueprint, jsonify, request
from services.test_runner_service import execute, add_test_runner

test_runner_bp = Blueprint('test_runner', __name__)


@test_runner_bp.route('/api/test_runner', methods=['GET'])
def test_runner_route():
    result = execute()
    return jsonify(result), 200


@test_runner_bp.route('/api/test_runner', methods=['POST'])
def add_test_runner_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_runner(name)
    return jsonify(result), 200
