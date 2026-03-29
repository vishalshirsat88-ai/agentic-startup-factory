
from flask import Blueprint

results_bp = Blueprint('results', __name__)

@results_bp.route('/results')
def results_home():
    return "results route working"
