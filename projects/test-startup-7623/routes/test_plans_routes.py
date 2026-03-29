
from flask import Blueprint

test_plans_bp = Blueprint('test_plans', __name__)

@test_plans_bp.route('/test_plans')
def test_plans_home():
    return "test_plans route working"
