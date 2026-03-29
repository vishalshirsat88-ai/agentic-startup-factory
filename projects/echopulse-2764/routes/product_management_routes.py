
from flask import Blueprint

product_management_bp = Blueprint('product_management', __name__)

@product_management_bp.route('/product_management')
def product_management_home():
    return "product_management route working"
