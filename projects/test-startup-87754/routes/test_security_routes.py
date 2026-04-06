
from flask import Blueprint, jsonify, request
from services.test_security_service import execute, add_test_security

test_security_bp = Blueprint('test_security', __name__)


@test_security_bp.route('/api/test_security', methods=['GET'])
def test_security_route():
    result = execute()
    return jsonify(result), 200


@test_security_bp.route('/api/test_security', methods=['POST'])
def add_test_security_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_security(name)
    return jsonify(result), 200
