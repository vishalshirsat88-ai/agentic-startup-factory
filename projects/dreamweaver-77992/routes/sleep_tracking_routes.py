
from flask import Blueprint

sleep_tracking_bp = Blueprint('sleep_tracking', __name__)

@sleep_tracking_bp.route('/sleep_tracking')
def sleep_tracking_home():
    return "sleep_tracking route working"
