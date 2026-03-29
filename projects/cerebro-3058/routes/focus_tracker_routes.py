
from flask import Blueprint

focus_tracker_bp = Blueprint('focus_tracker', __name__)

@focus_tracker_bp.route('/focus_tracker')
def focus_tracker_home():
    return "focus_tracker route working"
