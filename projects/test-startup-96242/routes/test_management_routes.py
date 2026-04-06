
from flask import Blueprint, jsonify, request, render_template
from services.test_management_service import execute, add_test_management

test_management_bp = Blueprint('test_management', __name__)

@test_management_bp.route('/test_management', methods=['GET'])
def test_management_page():
    return render_template("test_management.html")


@test_management_bp.route('/api/test_management', methods=['GET'])
def test_management_route():
    result = execute()
    return jsonify(result), 200


@test_management_bp.route('/api/test_management', methods=['POST'])
def add_test_management_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_management(name)
    return jsonify(result), 200
