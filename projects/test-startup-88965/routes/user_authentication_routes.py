
from flask import Blueprint, jsonify, request, render_template
from services.user_authentication_service import execute, add_user_authentication

user_authentication_bp = Blueprint('user_authentication', __name__)

@user_authentication_bp.route('/user_authentication', methods=['GET'])
def user_authentication_page():
    return render_template("user_authentication.html")


@user_authentication_bp.route('/api/user_authentication', methods=['GET'])
def user_authentication_route():
    result = execute()
    return jsonify(result), 200


@user_authentication_bp.route('/api/user_authentication', methods=['POST'])
def add_user_authentication_route():
    data = request.get_json()
    name = data.get("name")

    result = add_user_authentication(name)
    return jsonify(result), 200
