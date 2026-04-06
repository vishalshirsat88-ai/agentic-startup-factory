
from flask import Blueprint, jsonify, request, render_template
from services.test_case_manager_service import execute, add_test_case_manager

test_case_manager_bp = Blueprint('test_case_manager', __name__)

@test_case_manager_bp.route('/test_case_manager', methods=['GET'])
def test_case_manager_page():
    return render_template("test_case_manager.html")


@test_case_manager_bp.route('/api/test_case_manager', methods=['GET'])
def test_case_manager_route():
    result = execute()
    return jsonify(result), 200


@test_case_manager_bp.route('/api/test_case_manager', methods=['POST'])
def add_test_case_manager_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_case_manager(name)
    return jsonify(result), 200
