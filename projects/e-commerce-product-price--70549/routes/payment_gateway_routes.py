
from flask import Blueprint

payment_gateway_bp = Blueprint('payment_gateway', __name__)

@payment_gateway_bp.route('/payment_gateway')
def payment_gateway_home():
    return "payment_gateway route working"
