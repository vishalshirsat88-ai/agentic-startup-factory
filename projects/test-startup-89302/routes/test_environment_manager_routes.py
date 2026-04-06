
from flask import Blueprint, jsonify, request, render_template
from services.test_environment_manager_service import execute, add_test_environment_manager

test_environment_manager_bp = Blueprint('test_environment_manager', __name__)

@test_environment_manager_bp.route('/test_environment_manager', methods=['GET'])
def test_environment_manager_page():
    return render_template("test_environment_manager.html")


@test_environment_manager_bp.route('/api/test_environment_manager', methods=['GET'])
def test_environment_manager_route():
    result = execute()
    return jsonify(result), 200


@test_environment_manager_bp.route('/api/test_environment_manager', methods=['POST'])
def add_test_environment_manager_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_environment_manager(name)
    return jsonify(result), 200
