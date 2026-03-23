
from flask import Blueprint

suggestion_engine_bp = Blueprint('suggestion_engine', __name__)

@suggestion_engine_bp.route('/suggestion_engine')
def suggestion_engine_home():
    return "suggestion_engine route working"
