
from flask import Blueprint

testcase_bp = Blueprint('testcase', __name__)

@testcase_bp.route('/testcase')
def testcase_home():
    return "testcase route working"
