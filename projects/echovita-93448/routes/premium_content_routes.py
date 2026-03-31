
        from flask import Blueprint, jsonify, request
        from services.premium_content_service import get_premium_content, add_premium_content

        premium_content_bp = Blueprint('premium_content', __name__)


        @premium_content_bp.route('/api/premium_content', methods=['GET'])
        def premium_content_route():
            result = get_premium_content()
            return jsonify(result), 200


        @premium_content_bp.route('/api/premium_content', methods=['POST'])
        def add_premium_content_route():
            data = request.get_json()
            name = data.get("name")

            result = add_premium_content(name)
            return jsonify(result), 200
        