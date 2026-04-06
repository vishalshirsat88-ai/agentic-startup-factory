
from flask import Blueprint, jsonify, request, render_template
from services.integration_and_api_service import execute, add_integration_and_api

integration_and_api_bp = Blueprint('integration_and_api', __name__)

@integration_and_api_bp.route('/integration_and_api', methods=['GET'])
def integration_and_api_page():
    return render_template("integration_and_api.html")


@integration_and_api_bp.route('/api/integration_and_api', methods=['GET'])
def integration_and_api_route():
    result = execute()
    return jsonify(result), 200


@integration_and_api_bp.route('/api/integration_and_api', methods=['POST'])
def add_integration_and_api_route():
    data = request.get_json()
    name = data.get("name")

    result = add_integration_and_api(name)
    return jsonify(result), 200
