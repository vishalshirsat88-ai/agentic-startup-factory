
from flask import Blueprint

core_logic_bp = Blueprint('core_logic', __name__)

@core_logic_bp.route('/core_logic')
def core_logic_home():
    return "core_logic route working"
