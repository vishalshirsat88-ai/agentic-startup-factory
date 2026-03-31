
        from flask import Blueprint, jsonify, request
        from services.event_planning_service import get_event_planning, add_event_planning

        event_planning_bp = Blueprint('event_planning', __name__)


        @event_planning_bp.route('/api/event_planning', methods=['GET'])
        def event_planning_route():
            result = get_event_planning()
            return jsonify(result), 200


        @event_planning_bp.route('/api/event_planning', methods=['POST'])
        def add_event_planning_route():
            data = request.get_json()
            name = data.get("name")

            result = add_event_planning(name)
            return jsonify(result), 200
        