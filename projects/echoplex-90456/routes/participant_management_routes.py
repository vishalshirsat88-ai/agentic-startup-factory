
from flask import Blueprint

participant_management_bp = Blueprint('participant_management', __name__)

@participant_management_bp.route('/participant_management')
def participant_management_home():
    return "participant_management route working"
