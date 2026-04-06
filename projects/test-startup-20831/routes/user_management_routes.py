
from flask import Blueprint, jsonify, request
from services.user_management_service import execute, add_user_management

user_management_bp = Blueprint('user_management', __name__)


@user_management_bp.route('/api/user_management', methods=['GET'])
def user_management_route():
    result = execute()
    return jsonify(result), 200


@user_management_bp.route('/api/user_management', methods=['POST'])
def add_user_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_user_management(name)
    return jsonify(result), 200
