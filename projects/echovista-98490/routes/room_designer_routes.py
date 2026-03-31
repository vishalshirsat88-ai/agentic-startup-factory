
        from flask import Blueprint, jsonify, request
        from services.room_designer_service import get_room_designer, add_room_designer

        room_designer_bp = Blueprint('room_designer', __name__)


        @room_designer_bp.route('/api/room_designer', methods=['GET'])
        def room_designer_route():
            result = get_room_designer()
            return jsonify(result), 200


        @room_designer_bp.route('/api/room_designer', methods=['POST'])
        def add_room_designer_route():
            data = request.get_json()
            name = data.get("name")

            result = add_room_designer(name)
            return jsonify(result), 200
        