
from flask import Blueprint

test_pipelines_bp = Blueprint('test_pipelines', __name__)

@test_pipelines_bp.route('/test_pipelines')
def test_pipelines_home():
    return "test_pipelines route working"
