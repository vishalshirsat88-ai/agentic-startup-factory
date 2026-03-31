
        from flask import Blueprint, jsonify, request
        from services.api_service import get_api, add_api

        api_bp = Blueprint('api', __name__)


        @api_bp.route('/api/api', methods=['GET'])
        def api_route():
            result = get_api()
            return jsonify(result), 200


        @api_bp.route('/api/api', methods=['POST'])
        def add_api_route():
            data = request.get_json()
            name = data.get("name")

            result = add_api(name)
            return jsonify(result), 200
        