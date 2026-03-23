
from flask import Blueprint

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/notifications')
def notifications_home():
    return "notifications route working"
