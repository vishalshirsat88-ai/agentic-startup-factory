
from flask import Blueprint

action_item_bp = Blueprint('action_item', __name__)

@action_item_bp.route('/action_item')
def action_item_home():
    return "action_item route working"
