
from flask import Blueprint

integration_bp = Blueprint('integration', __name__)

@integration_bp.route('/integration')
def integration_home():
    return "integration route working"
