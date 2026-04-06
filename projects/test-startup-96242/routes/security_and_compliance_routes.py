
from flask import Blueprint, jsonify, request, render_template
from services.security_and_compliance_service import execute, add_security_and_compliance

security_and_compliance_bp = Blueprint('security_and_compliance', __name__)

@security_and_compliance_bp.route('/security_and_compliance', methods=['GET'])
def security_and_compliance_page():
    return render_template("security_and_compliance.html")


@security_and_compliance_bp.route('/api/security_and_compliance', methods=['GET'])
def security_and_compliance_route():
    result = execute()
    return jsonify(result), 200


@security_and_compliance_bp.route('/api/security_and_compliance', methods=['POST'])
def add_security_and_compliance_route():
    data = request.get_json()
    name = data.get("name")

    result = add_security_and_compliance(name)
    return jsonify(result), 200
