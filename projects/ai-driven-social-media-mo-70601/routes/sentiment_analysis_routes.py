
from flask import Blueprint

sentiment_analysis_bp = Blueprint('sentiment_analysis', __name__)

@sentiment_analysis_bp.route('/sentiment_analysis')
def sentiment_analysis_home():
    return "sentiment_analysis route working"
