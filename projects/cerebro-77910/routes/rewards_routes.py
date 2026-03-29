
from flask import Blueprint

rewards_bp = Blueprint('rewards', __name__)

@rewards_bp.route('/rewards')
def rewards_home():
    return "rewards route working"
