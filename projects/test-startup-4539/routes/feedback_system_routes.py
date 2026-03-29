
from flask import Blueprint

feedback_system_bp = Blueprint('feedback_system', __name__)

@feedback_system_bp.route('/feedback_system')
def feedback_system_home():
    return "feedback_system route working"
