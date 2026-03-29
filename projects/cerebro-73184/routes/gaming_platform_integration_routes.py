
from flask import Blueprint

gaming_platform_integration_bp = Blueprint('gaming_platform_integration', __name__)

@gaming_platform_integration_bp.route('/gaming_platform_integration')
def gaming_platform_integration_home():
    return "gaming_platform_integration route working"
