from flask import Blueprint, jsonify, request
from services.testing_engine_service import execute, add_testing_engine

testing_engine_bp = Blueprint('testing_engine', __name__)

@testing_engine_bp.route('/api/testing_engine', methods=['GET'])
def testing_engine_route():
    result = execute()
    return jsonify(result), 200

@testing_engine_bp.route('/api/testing_engine', methods=['POST'])
def add_testing_engine_route():
    data = request.get_json()
    name = data.get("name")

    if name:
        result = add_testing_engine(name)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Missing required parameter 'name'"}), 400