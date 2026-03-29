
from flask import Blueprint

experiences_bp = Blueprint('experiences', __name__)

@experiences_bp.route('/experiences')
def experiences_home():
    return "experiences route working"
