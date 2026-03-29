
from flask import Blueprint

anxiety_management_bp = Blueprint('anxiety_management', __name__)

@anxiety_management_bp.route('/anxiety_management')
def anxiety_management_home():
    return "anxiety_management route working"
