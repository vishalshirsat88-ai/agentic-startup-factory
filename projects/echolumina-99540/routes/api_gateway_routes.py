
from flask import Blueprint

api_gateway_bp = Blueprint('api_gateway', __name__)

@api_gateway_bp.route('/api_gateway')
def api_gateway_home():
    return "api_gateway route working"
