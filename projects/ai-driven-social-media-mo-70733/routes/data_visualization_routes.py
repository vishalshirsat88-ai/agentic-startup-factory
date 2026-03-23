
from flask import Blueprint

data_visualization_bp = Blueprint('data_visualization', __name__)

@data_visualization_bp.route('/data_visualization')
def data_visualization_home():
    return "data_visualization route working"
