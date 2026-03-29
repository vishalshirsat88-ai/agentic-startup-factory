
from flask import Blueprint

meditation_bp = Blueprint('meditation', __name__)

@meditation_bp.route('/meditation')
def meditation_home():
    return "meditation route working"
