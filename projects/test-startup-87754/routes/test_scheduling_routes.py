
from flask import Blueprint, jsonify, request
from services.test_scheduling_service import execute, add_test_scheduling

test_scheduling_bp = Blueprint('test_scheduling', __name__)


@test_scheduling_bp.route('/api/test_scheduling', methods=['GET'])
def test_scheduling_route():
    result = execute()
    return jsonify(result), 200


@test_scheduling_bp.route('/api/test_scheduling', methods=['POST'])
def add_test_scheduling_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_scheduling(name)
    return jsonify(result), 200
