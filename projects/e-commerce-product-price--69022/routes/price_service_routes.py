
from flask import Blueprint

price_service_bp = Blueprint('price_service', __name__)

@price_service_bp.route('/price_service')
def price_service_home():
    return "price_service route working"
