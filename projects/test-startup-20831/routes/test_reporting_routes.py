
from flask import Blueprint, jsonify, request
from services.test_reporting_service import execute, add_test_reporting

test_reporting_bp = Blueprint('test_reporting', __name__)


@test_reporting_bp.route('/api/test_reporting', methods=['GET'])
def test_reporting_route():
    result = execute()
    return jsonify(result), 200


@test_reporting_bp.route('/api/test_reporting', methods=['POST'])
def add_test_reporting_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_reporting(name)
    return jsonify(result), 200
