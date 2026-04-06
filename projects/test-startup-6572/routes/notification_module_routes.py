
from flask import Blueprint, jsonify, request, render_template
from services.notification_module_service import execute, add_notification_module

notification_module_bp = Blueprint('notification_module', __name__)

@notification_module_bp.route('/notification_module', methods=['GET'])
def notification_module_page():
    return render_template("notification_module.html")


@notification_module_bp.route('/api/notification_module', methods=['GET'])
def notification_module_route():
    result = execute()
    return jsonify(result), 200


@notification_module_bp.route('/api/notification_module', methods=['POST'])
def add_notification_module_route():
    data = request.get_json()
    name = data.get("name")

    result = add_notification_module(name)
    return jsonify(result), 200
