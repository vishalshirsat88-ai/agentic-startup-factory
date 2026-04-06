
from flask import Blueprint, jsonify, request, render_template
from services.deployment_management_service import execute, add_deployment_management

deployment_management_bp = Blueprint('deployment_management', __name__)

@deployment_management_bp.route('/deployment_management', methods=['GET'])
def deployment_management_page():
    return render_template("deployment_management.html")


@deployment_management_bp.route('/api/deployment_management', methods=['GET'])
def deployment_management_route():
    result = execute()
    return jsonify(result), 200


@deployment_management_bp.route('/api/deployment_management', methods=['POST'])
def add_deployment_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_deployment_management(name)
    return jsonify(result), 200
