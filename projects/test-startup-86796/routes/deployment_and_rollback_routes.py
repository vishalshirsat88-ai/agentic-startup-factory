
from flask import Blueprint, jsonify, request, render_template
from services.deployment_and_rollback_service import execute, add_deployment_and_rollback

deployment_and_rollback_bp = Blueprint('deployment_and_rollback', __name__)

@deployment_and_rollback_bp.route('/deployment_and_rollback', methods=['GET'])
def deployment_and_rollback_page():
    return render_template("deployment_and_rollback.html")


@deployment_and_rollback_bp.route('/api/deployment_and_rollback', methods=['GET'])
def deployment_and_rollback_route():
    result = execute()
    return jsonify(result), 200


@deployment_and_rollback_bp.route('/api/deployment_and_rollback', methods=['POST'])
def add_deployment_and_rollback_route():
    data = request.get_json()
    name = data.get("name")

    result = add_deployment_and_rollback(name)
    return jsonify(result), 200
