
from flask import Blueprint

testrunner_bp = Blueprint('testrunner', __name__)

@testrunner_bp.route('/testrunner')
def testrunner_home():
    return "testrunner route working"
