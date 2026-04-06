
from flask import Blueprint, jsonify, request, render_template
from services.notifications_module_service import execute, add_notifications_module

notifications_module_bp = Blueprint('notifications_module', __name__)

@notifications_module_bp.route('/notifications_module', methods=['GET'])
def notifications_module_page():
    return render_template("notifications_module.html")


@notifications_module_bp.route('/api/notifications_module', methods=['GET'])
def notifications_module_route():
    result = execute()
    return jsonify(result), 200


@notifications_module_bp.route('/api/notifications_module', methods=['POST'])
def add_notifications_module_route():
    data = request.get_json()
    name = data.get("name")

    result = add_notifications_module(name)
    return jsonify(result), 200
