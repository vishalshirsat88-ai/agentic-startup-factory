
        from flask import Blueprint, jsonify, request
        from services.partnerships_service import get_partnerships, add_partnerships

        partnerships_bp = Blueprint('partnerships', __name__)


        @partnerships_bp.route('/api/partnerships', methods=['GET'])
        def partnerships_route():
            result = get_partnerships()
            return jsonify(result), 200


        @partnerships_bp.route('/api/partnerships', methods=['POST'])
        def add_partnerships_route():
            data = request.get_json()
            name = data.get("name")

            result = add_partnerships(name)
            return jsonify(result), 200
        