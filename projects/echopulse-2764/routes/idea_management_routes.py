
from flask import Blueprint

idea_management_bp = Blueprint('idea_management', __name__)

@idea_management_bp.route('/idea_management')
def idea_management_home():
    return "idea_management route working"
