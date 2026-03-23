
from flask import Blueprint

alert_system_bp = Blueprint('alert_system', __name__)

@alert_system_bp.route('/alert_system')
def alert_system_home():
    return "alert_system route working"
