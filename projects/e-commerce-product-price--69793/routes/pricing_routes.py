
from flask import Blueprint

pricing_bp = Blueprint('pricing', __name__)

@pricing_bp.route('/pricing')
def pricing_home():
    return "pricing route working"
