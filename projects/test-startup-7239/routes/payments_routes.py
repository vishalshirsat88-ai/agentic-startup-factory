
from flask import Blueprint

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/payments')
def payments_home():
    return "payments route working"
