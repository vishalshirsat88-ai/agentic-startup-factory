
from flask import Blueprint

product_service_bp = Blueprint('product_service', __name__)

@product_service_bp.route('/product_service')
def product_service_home():
    return "product_service route working"
