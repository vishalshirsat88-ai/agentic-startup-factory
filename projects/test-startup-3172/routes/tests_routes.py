
from flask import Blueprint

tests_bp = Blueprint('tests', __name__)

@tests_bp.route('/tests')
def tests_home():
    return "tests route working"
