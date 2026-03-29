
from flask import Blueprint

mental_wellness_bp = Blueprint('mental_wellness', __name__)

@mental_wellness_bp.route('/mental_wellness')
def mental_wellness_home():
    return "mental_wellness route working"
