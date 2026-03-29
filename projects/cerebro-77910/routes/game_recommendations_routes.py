
from flask import Blueprint

game_recommendations_bp = Blueprint('game_recommendations', __name__)

@game_recommendations_bp.route('/game_recommendations')
def game_recommendations_home():
    return "game_recommendations route working"
