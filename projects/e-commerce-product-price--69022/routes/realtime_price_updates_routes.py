
from flask import Blueprint

realtime_price_updates_bp = Blueprint('realtime_price_updates', __name__)

@realtime_price_updates_bp.route('/realtime_price_updates')
def realtime_price_updates_home():
    return "realtime_price_updates route working"
