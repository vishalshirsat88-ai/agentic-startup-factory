
from flask import Blueprint

project_bp = Blueprint('project', __name__)

@project_bp.route('/project')
def project_home():
    return "project route working"
