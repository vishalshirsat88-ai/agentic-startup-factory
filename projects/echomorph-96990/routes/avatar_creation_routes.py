
        from flask import Blueprint, jsonify, request
        from services.avatar_creation_service import get_avatar_creation, add_avatar_creation

        avatar_creation_bp = Blueprint('avatar_creation', __name__)


        @avatar_creation_bp.route('/api/avatar_creation', methods=['GET'])
        def avatar_creation_route():
            result = get_avatar_creation()
            return jsonify(result), 200


        @avatar_creation_bp.route('/api/avatar_creation', methods=['POST'])
        def add_avatar_creation_route():
            data = request.get_json()
            name = data.get("name")

            result = add_avatar_creation(name)
            return jsonify(result), 200
        