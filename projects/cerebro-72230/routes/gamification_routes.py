
from flask import Blueprint

gamification_bp = Blueprint('gamification', __name__)

@gamification_bp.route('/gamification')
def gamification_home():
    return "gamification route working"
