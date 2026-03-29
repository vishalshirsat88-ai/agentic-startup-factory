
from flask import Blueprint

induction_bp = Blueprint('induction', __name__)

@induction_bp.route('/induction')
def induction_home():
    return "induction route working"
