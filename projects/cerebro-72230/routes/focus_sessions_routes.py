
from flask import Blueprint

focus_sessions_bp = Blueprint('focus_sessions', __name__)

@focus_sessions_bp.route('/focus_sessions')
def focus_sessions_home():
    return "focus_sessions route working"
