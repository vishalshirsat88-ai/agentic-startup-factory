
from flask import Blueprint

gaming_integration_bp = Blueprint('gaming_integration', __name__)

@gaming_integration_bp.route('/gaming_integration')
def gaming_integration_home():
    return "gaming_integration route working"
