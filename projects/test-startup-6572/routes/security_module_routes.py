
from flask import Blueprint, jsonify, request, render_template
from services.security_module_service import execute, add_security_module

security_module_bp = Blueprint('security_module', __name__)

@security_module_bp.route('/security_module', methods=['GET'])
def security_module_page():
    return render_template("security_module.html")


@security_module_bp.route('/api/security_module', methods=['GET'])
def security_module_route():
    result = execute()
    return jsonify(result), 200


@security_module_bp.route('/api/security_module', methods=['POST'])
def add_security_module_route():
    data = request.get_json()
    name = data.get("name")

    result = add_security_module(name)
    return jsonify(result), 200
