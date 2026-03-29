
from flask import Blueprint

journaling_bp = Blueprint('journaling', __name__)

@journaling_bp.route('/journaling')
def journaling_home():
    return "journaling route working"
