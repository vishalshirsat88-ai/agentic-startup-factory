
from flask import Blueprint

ecommerce_platform_integrations_bp = Blueprint('ecommerce_platform_integrations', __name__)

@ecommerce_platform_integrations_bp.route('/ecommerce_platform_integrations')
def ecommerce_platform_integrations_home():
    return "ecommerce_platform_integrations route working"
