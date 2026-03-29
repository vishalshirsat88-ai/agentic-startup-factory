
from flask import Blueprint

recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/recommendations')
def recommendations_home():
    return "recommendations route working"
