
from flask import Blueprint

meeting_bp = Blueprint('meeting', __name__)

@meeting_bp.route('/meeting')
def meeting_home():
    return "meeting route working"
