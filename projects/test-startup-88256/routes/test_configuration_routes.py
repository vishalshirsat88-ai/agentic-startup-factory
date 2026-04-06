
from flask import Blueprint, jsonify, request
from services.test_configuration_service import execute, add_test_configuration

test_configuration_bp = Blueprint('test_configuration', __name__)


@test_configuration_bp.route('/api/test_configuration', methods=['GET'])
def test_configuration_route():
    result = execute()
    return jsonify(result), 200


@test_configuration_bp.route('/api/test_configuration', methods=['POST'])
def add_test_configuration_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_configuration(name)
    return jsonify(result), 200
