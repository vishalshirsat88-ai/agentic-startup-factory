
from flask import Blueprint

reward_system_bp = Blueprint('reward_system', __name__)

@reward_system_bp.route('/reward_system')
def reward_system_home():
    return "reward_system route working"
