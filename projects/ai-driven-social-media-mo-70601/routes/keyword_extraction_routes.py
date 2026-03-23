
from flask import Blueprint

keyword_extraction_bp = Blueprint('keyword_extraction', __name__)

@keyword_extraction_bp.route('/keyword_extraction')
def keyword_extraction_home():
    return "keyword_extraction route working"
