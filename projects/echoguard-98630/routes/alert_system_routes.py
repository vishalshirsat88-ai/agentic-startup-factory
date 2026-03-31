
        from flask import Blueprint, jsonify, request
        from services.alert_system_service import get_alert_system, add_alert_system

        alert_system_bp = Blueprint('alert_system', __name__)


        @alert_system_bp.route('/api/alert_system', methods=['GET'])
        def alert_system_route():
            result = get_alert_system()
            return jsonify(result), 200


        @alert_system_bp.route('/api/alert_system', methods=['POST'])
        def add_alert_system_route():
            data = request.get_json()
            name = data.get("name")

            result = add_alert_system(name)
            return jsonify(result), 200
        