
from flask import Blueprint

focus_training_bp = Blueprint('focus_training', __name__)

@focus_training_bp.route('/focus_training')
def focus_training_home():
    return "focus_training route working"
