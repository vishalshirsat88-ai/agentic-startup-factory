
from flask import Blueprint, jsonify, request, render_template
from services.testing_module_service import execute, add_testing_module

testing_module_bp = Blueprint('testing_module', __name__)

@testing_module_bp.route('/testing_module', methods=['GET'])
def testing_module_page():
    return render_template("testing_module.html")


@testing_module_bp.route('/api/testing_module', methods=['GET'])
def testing_module_route():
    result = execute()
    return jsonify(result), 200


@testing_module_bp.route('/api/testing_module', methods=['POST'])
def add_testing_module_route():
    data = request.get_json()
    name = data.get("name")

    result = add_testing_module(name)
    return jsonify(result), 200
