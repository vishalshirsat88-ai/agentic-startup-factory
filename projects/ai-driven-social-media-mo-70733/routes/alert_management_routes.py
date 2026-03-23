
from flask import Blueprint

alert_management_bp = Blueprint('alert_management', __name__)

@alert_management_bp.route('/alert_management')
def alert_management_home():
    return "alert_management route working"
