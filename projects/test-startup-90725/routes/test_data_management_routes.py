
from flask import Blueprint, jsonify, request, render_template
from services.test_data_management_service import execute, add_test_data_management

test_data_management_bp = Blueprint('test_data_management', __name__)

@test_data_management_bp.route('/test_data_management', methods=['GET'])
def test_data_management_page():
    return render_template("test_data_management.html")


@test_data_management_bp.route('/api/test_data_management', methods=['GET'])
def test_data_management_route():
    result = execute()
    return jsonify(result), 200


@test_data_management_bp.route('/api/test_data_management', methods=['POST'])
def add_test_data_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_data_management(name)
    return jsonify(result), 200
