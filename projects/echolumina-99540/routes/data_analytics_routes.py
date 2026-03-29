
from flask import Blueprint

data_analytics_bp = Blueprint('data_analytics', __name__)

@data_analytics_bp.route('/data_analytics')
def data_analytics_home():
    return "data_analytics route working"
