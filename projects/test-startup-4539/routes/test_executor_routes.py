
from flask import Blueprint

test_executor_bp = Blueprint('test_executor', __name__)

@test_executor_bp.route('/test_executor')
def test_executor_home():
    return "test_executor route working"
