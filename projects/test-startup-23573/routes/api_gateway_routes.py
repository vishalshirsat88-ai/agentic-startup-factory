
from flask import Blueprint, jsonify, request
from services.api_gateway_service import execute, add_api_gateway

api_gateway_bp = Blueprint('api_gateway', __name__)


@api_gateway_bp.route('/api/api_gateway', methods=['GET'])
def api_gateway_route():
    result = execute()
    return jsonify(result), 200


@api_gateway_bp.route('/api/api_gateway', methods=['POST'])
def add_api_gateway_route():
    data = request.get_json()
    name = data.get("name")

    result = add_api_gateway(name)
    return jsonify(result), 200
