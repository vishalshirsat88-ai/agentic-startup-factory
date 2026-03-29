
from flask import Blueprint

pipelines_bp = Blueprint('pipelines', __name__)

@pipelines_bp.route('/pipelines')
def pipelines_home():
    return "pipelines route working"
