
from flask import Blueprint, jsonify, request, render_template
from services.test_data_module_service import execute, add_test_data_module

test_data_module_bp = Blueprint('test_data_module', __name__)

@test_data_module_bp.route('/test_data_module', methods=['GET'])
def test_data_module_page():
    return render_template("test_data_module.html")


@test_data_module_bp.route('/api/test_data_module', methods=['GET'])
def test_data_module_route():
    result = execute()
    return jsonify(result), 200


@test_data_module_bp.route('/api/test_data_module', methods=['POST'])
def add_test_data_module_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_data_module(name)
    return jsonify(result), 200
