
from flask import Blueprint, jsonify, request
from services.automated_testing_service import execute, add_automated_testing

automated_testing_bp = Blueprint('automated_testing', __name__)


@automated_testing_bp.route('/api/automated_testing', methods=['GET'])
def automated_testing_route():
    result = execute()
    return jsonify(result), 200


@automated_testing_bp.route('/api/automated_testing', methods=['POST'])
def add_automated_testing_route():
    data = request.get_json()
    name = data.get("name")

    result = add_automated_testing(name)
    return jsonify(result), 200
