
from flask import Blueprint

hashtag_keyword_monitoring_bp = Blueprint('hashtag_keyword_monitoring', __name__)

@hashtag_keyword_monitoring_bp.route('/hashtag_keyword_monitoring')
def hashtag_keyword_monitoring_home():
    return "hashtag_keyword_monitoring route working"
