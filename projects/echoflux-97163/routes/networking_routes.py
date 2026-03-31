
        from flask import Blueprint, jsonify, request
        from services.networking_service import get_networking, add_networking

        networking_bp = Blueprint('networking', __name__)


        @networking_bp.route('/api/networking', methods=['GET'])
        def networking_route():
            result = get_networking()
            return jsonify(result), 200


        @networking_bp.route('/api/networking', methods=['POST'])
        def add_networking_route():
            data = request.get_json()
            name = data.get("name")

            result = add_networking(name)
            return jsonify(result), 200
        