
from flask import Blueprint

note_bp = Blueprint('note', __name__)

@note_bp.route('/note')
def note_home():
    return "note route working"
