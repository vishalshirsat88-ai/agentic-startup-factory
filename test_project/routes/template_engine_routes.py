
from flask import Blueprint

template_engine_bp = Blueprint('template_engine', __name__)

@template_engine_bp.route('/template_engine')
def template_engine_home():
    return "template_engine route working"
