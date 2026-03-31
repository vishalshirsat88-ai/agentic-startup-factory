
        from flask import Blueprint, jsonify, request
        from services.iot_device_registry_service import get_iot_device_registry, add_iot_device_registry

        iot_device_registry_bp = Blueprint('iot_device_registry', __name__)


        @iot_device_registry_bp.route('/api/iot_device_registry', methods=['GET'])
        def iot_device_registry_route():
            result = get_iot_device_registry()
            return jsonify(result), 200


        @iot_device_registry_bp.route('/api/iot_device_registry', methods=['POST'])
        def add_iot_device_registry_route():
            data = request.get_json()
            name = data.get("name")

            result = add_iot_device_registry(name)
            return jsonify(result), 200
        