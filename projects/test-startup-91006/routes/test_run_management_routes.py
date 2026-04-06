
from flask import Blueprint, jsonify, request, render_template
from services.test_run_management_service import execute, add_test_run_management

test_run_management_bp = Blueprint('test_run_management', __name__)

@test_run_management_bp.route('/test_run_management', methods=['GET'])
def test_run_management_page():
    return render_template("test_run_management.html")


@test_run_management_bp.route('/api/test_run_management', methods=['GET'])
def test_run_management_route():
    result = execute()
    return jsonify(result), 200


@test_run_management_bp.route('/api/test_run_management', methods=['POST'])
def add_test_run_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_run_management(name)
    return jsonify(result), 200
