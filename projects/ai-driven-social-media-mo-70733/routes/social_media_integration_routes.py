
from flask import Blueprint

social_media_integration_bp = Blueprint('social_media_integration', __name__)

@social_media_integration_bp.route('/social_media_integration')
def social_media_integration_home():
    return "social_media_integration route working"
