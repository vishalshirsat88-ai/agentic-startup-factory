
from flask import Blueprint, jsonify, request
from services.test_analytics_service import execute, add_test_analytics

test_analytics_bp = Blueprint('test_analytics', __name__)


@test_analytics_bp.route('/api/test_analytics', methods=['GET'])
def test_analytics_route():
    result = execute()
    return jsonify(result), 200


@test_analytics_bp.route('/api/test_analytics', methods=['POST'])
def add_test_analytics_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_analytics(name)
    return jsonify(result), 200
