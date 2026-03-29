
from flask import Blueprint

wellness_planner_bp = Blueprint('wellness_planner', __name__)

@wellness_planner_bp.route('/wellness_planner')
def wellness_planner_home():
    return "wellness_planner route working"
