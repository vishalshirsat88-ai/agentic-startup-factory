
from flask import Blueprint, jsonify, request, render_template
from services.deployment_manager_service import execute, add_deployment_manager

deployment_manager_bp = Blueprint('deployment_manager', __name__)

@deployment_manager_bp.route('/deployment_manager', methods=['GET'])
def deployment_manager_page():
    return render_template("deployment_manager.html")


@deployment_manager_bp.route('/api/deployment_manager', methods=['GET'])
def deployment_manager_route():
    result = execute()
    return jsonify(result), 200


@deployment_manager_bp.route('/api/deployment_manager', methods=['POST'])
def add_deployment_manager_route():
    data = request.get_json()
    name = data.get("name")

    result = add_deployment_manager(name)
    return jsonify(result), 200
