
        from flask import Blueprint, jsonify, request
        from services.auth_service import get_auth, add_auth

        auth_bp = Blueprint('auth', __name__)


        @auth_bp.route('/api/auth', methods=['GET'])
        def auth_route():
            result = get_auth()
            return jsonify(result), 200


        @auth_bp.route('/api/auth', methods=['POST'])
        def add_auth_route():
            data = request.get_json()
            name = data.get("name")

            result = add_auth(name)
            return jsonify(result), 200
        