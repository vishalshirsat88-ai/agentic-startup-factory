
from flask import Blueprint

sound_therapy_bp = Blueprint('sound_therapy', __name__)

@sound_therapy_bp.route('/sound_therapy')
def sound_therapy_home():
    return "sound_therapy route working"
