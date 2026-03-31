
        from flask import Blueprint, jsonify, request
        from services.payments_gateway_service import get_payments_gateway, add_payments_gateway

        payments_gateway_bp = Blueprint('payments_gateway', __name__)


        @payments_gateway_bp.route('/api/payments_gateway', methods=['GET'])
        def payments_gateway_route():
            result = get_payments_gateway()
            return jsonify(result), 200


        @payments_gateway_bp.route('/api/payments_gateway', methods=['POST'])
        def add_payments_gateway_route():
            data = request.get_json()
            name = data.get("name")

            result = add_payments_gateway(name)
            return jsonify(result), 200
        