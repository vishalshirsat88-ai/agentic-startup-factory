
from flask import Blueprint

test_planner_bp = Blueprint('test_planner', __name__)

@test_planner_bp.route('/test_planner')
def test_planner_home():
    return "test_planner route working"
