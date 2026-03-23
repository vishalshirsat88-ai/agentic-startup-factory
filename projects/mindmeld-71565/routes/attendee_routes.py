
from flask import Blueprint

attendee_bp = Blueprint('attendee', __name__)

@attendee_bp.route('/attendee')
def attendee_home():
    return "attendee route working"
