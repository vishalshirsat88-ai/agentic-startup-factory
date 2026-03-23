
from flask import Blueprint

social_media_platforms_bp = Blueprint('social_media_platforms', __name__)

@social_media_platforms_bp.route('/social_media_platforms')
def social_media_platforms_home():
    return "social_media_platforms route working"
