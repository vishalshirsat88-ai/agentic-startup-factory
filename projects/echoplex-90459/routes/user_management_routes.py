
from flask import Blueprint

user_management_bp = Blueprint('user_management', __name__)

@user_management_bp.route('/user_management')
def user_management_home():
    return "user_management route working"
