
from flask import Blueprint, jsonify, request, render_template
from services.test_suite_management_service import execute, add_test_suite_management

test_suite_management_bp = Blueprint('test_suite_management', __name__)

@test_suite_management_bp.route('/test_suite_management', methods=['GET'])
def test_suite_management_page():
    return render_template("test_suite_management.html")


@test_suite_management_bp.route('/api/test_suite_management', methods=['GET'])
def test_suite_management_route():
    result = execute()
    return jsonify(result), 200


@test_suite_management_bp.route('/api/test_suite_management', methods=['POST'])
def add_test_suite_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_suite_management(name)
    return jsonify(result), 200
