
from flask import Blueprint

testcases_bp = Blueprint('testcases', __name__)

@testcases_bp.route('/testcases')
def testcases_home():
    return "testcases route working"
