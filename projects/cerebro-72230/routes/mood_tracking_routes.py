
from flask import Blueprint

mood_tracking_bp = Blueprint('mood_tracking', __name__)

@mood_tracking_bp.route('/mood_tracking')
def mood_tracking_home():
    return "mood_tracking route working"
