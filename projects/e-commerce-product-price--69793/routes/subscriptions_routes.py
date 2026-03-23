
from flask import Blueprint

subscriptions_bp = Blueprint('subscriptions', __name__)

@subscriptions_bp.route('/subscriptions')
def subscriptions_home():
    return "subscriptions route working"
