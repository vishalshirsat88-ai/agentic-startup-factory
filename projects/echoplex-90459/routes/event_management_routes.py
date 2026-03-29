
from flask import Blueprint

event_management_bp = Blueprint('event_management', __name__)

@event_management_bp.route('/event_management')
def event_management_home():
    return "event_management route working"
