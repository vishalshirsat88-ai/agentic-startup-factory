
from flask import Blueprint

email_service_bp = Blueprint('email_service', __name__)

@email_service_bp.route('/email_service')
def email_service_home():
    return "email_service route working"
