
        from flask import Blueprint, jsonify, request
        from services.event_management_service import get_event_management, add_event_management

        event_management_bp = Blueprint('event_management', __name__)


        @event_management_bp.route('/api/event_management', methods=['GET'])
        def event_management_route():
            result = get_event_management()
            return jsonify(result), 200


        @event_management_bp.route('/api/event_management', methods=['POST'])
        def add_event_management_route():
            data = request.get_json()
            name = data.get("name")

            result = add_event_management(name)
            return jsonify(result), 200
        