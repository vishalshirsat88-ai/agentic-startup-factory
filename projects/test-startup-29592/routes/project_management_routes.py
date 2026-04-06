
from flask import Blueprint, jsonify, request
from services.project_management_service import execute, add_project_management

project_management_bp = Blueprint('project_management', __name__)


@project_management_bp.route('/api/project_management', methods=['GET'])
def project_management_route():
    result = execute()
    return jsonify(result), 200


@project_management_bp.route('/api/project_management', methods=['POST'])
def add_project_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_project_management(name)
    return jsonify(result), 200
