
from flask import Blueprint

achievements_bp = Blueprint('achievements', __name__)

@achievements_bp.route('/achievements')
def achievements_home():
    return "achievements route working"
