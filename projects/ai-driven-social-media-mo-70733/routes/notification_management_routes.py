
from flask import Blueprint

notification_management_bp = Blueprint('notification_management', __name__)

@notification_management_bp.route('/notification_management')
def notification_management_home():
    return "notification_management route working"
