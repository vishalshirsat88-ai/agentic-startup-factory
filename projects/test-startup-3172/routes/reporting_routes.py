
from flask import Blueprint

reporting_bp = Blueprint('reporting', __name__)

@reporting_bp.route('/reporting')
def reporting_home():
    return "reporting route working"
