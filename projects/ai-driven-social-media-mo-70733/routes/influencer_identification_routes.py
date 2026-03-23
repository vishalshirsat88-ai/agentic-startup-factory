
from flask import Blueprint

influencer_identification_bp = Blueprint('influencer_identification', __name__)

@influencer_identification_bp.route('/influencer_identification')
def influencer_identification_home():
    return "influencer_identification route working"
