
from flask import Blueprint

user_feedback_bp = Blueprint('user_feedback', __name__)

@user_feedback_bp.route('/user_feedback')
def user_feedback_home():
    return "user_feedback route working"
