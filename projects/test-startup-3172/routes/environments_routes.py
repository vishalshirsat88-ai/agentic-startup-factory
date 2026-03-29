
from flask import Blueprint

environments_bp = Blueprint('environments', __name__)

@environments_bp.route('/environments')
def environments_home():
    return "environments route working"
