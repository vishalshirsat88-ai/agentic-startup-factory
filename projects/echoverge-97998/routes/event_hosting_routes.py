
        from flask import Blueprint, jsonify, request
        from services.event_hosting_service import get_event_hosting, add_event_hosting

        event_hosting_bp = Blueprint('event_hosting', __name__)


        @event_hosting_bp.route('/api/event_hosting', methods=['GET'])
        def event_hosting_route():
            result = get_event_hosting()
            return jsonify(result), 200


        @event_hosting_bp.route('/api/event_hosting', methods=['POST'])
        def add_event_hosting_route():
            data = request.get_json()
            name = data.get("name")

            result = add_event_hosting(name)
            return jsonify(result), 200
        