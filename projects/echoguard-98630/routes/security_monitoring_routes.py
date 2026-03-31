
        from flask import Blueprint, jsonify, request
        from services.security_monitoring_service import get_security_monitoring, add_security_monitoring

        security_monitoring_bp = Blueprint('security_monitoring', __name__)


        @security_monitoring_bp.route('/api/security_monitoring', methods=['GET'])
        def security_monitoring_route():
            result = get_security_monitoring()
            return jsonify(result), 200


        @security_monitoring_bp.route('/api/security_monitoring', methods=['POST'])
        def add_security_monitoring_route():
            data = request.get_json()
            name = data.get("name")

            result = add_security_monitoring(name)
            return jsonify(result), 200
        