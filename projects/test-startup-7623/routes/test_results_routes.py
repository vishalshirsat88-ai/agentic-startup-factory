
from flask import Blueprint

test_results_bp = Blueprint('test_results', __name__)

@test_results_bp.route('/test_results')
def test_results_home():
    return "test_results route working"
