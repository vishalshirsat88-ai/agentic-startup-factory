
from flask import Blueprint

social_media_posts_bp = Blueprint('social_media_posts', __name__)

@social_media_posts_bp.route('/social_media_posts')
def social_media_posts_home():
    return "social_media_posts route working"
