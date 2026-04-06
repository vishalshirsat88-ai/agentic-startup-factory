
from flask import Blueprint, jsonify, request
from services.test_repository_service import execute, add_test_repository

test_repository_bp = Blueprint('test_repository', __name__)


@test_repository_bp.route('/api/test_repository', methods=['GET'])
def test_repository_route():
    result = execute()
    return jsonify(result), 200


@test_repository_bp.route('/api/test_repository', methods=['POST'])
def add_test_repository_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_repository(name)
    return jsonify(result), 200
