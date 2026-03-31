
        from flask import Blueprint, jsonify, request
        from services.web_service import get_web, add_web

        web_bp = Blueprint('web', __name__)


        @web_bp.route('/api/web', methods=['GET'])
        def web_route():
            result = get_web()
            return jsonify(result), 200


        @web_bp.route('/api/web', methods=['POST'])
        def add_web_route():
            data = request.get_json()
            name = data.get("name")

            result = add_web(name)
            return jsonify(result), 200
        