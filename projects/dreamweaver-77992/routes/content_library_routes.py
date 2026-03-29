
from flask import Blueprint

content_library_bp = Blueprint('content_library', __name__)

@content_library_bp.route('/content_library')
def content_library_home():
    return "content_library route working"
