
from flask import Blueprint

vendor_management_bp = Blueprint('vendor_management', __name__)

@vendor_management_bp.route('/vendor_management')
def vendor_management_home():
    return "vendor_management route working"
