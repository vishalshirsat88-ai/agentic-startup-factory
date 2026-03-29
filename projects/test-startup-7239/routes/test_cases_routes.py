
from flask import Blueprint

test_cases_bp = Blueprint('test_cases', __name__)

@test_cases_bp.route('/test_cases')
def test_cases_home():
    return "test_cases route working"
