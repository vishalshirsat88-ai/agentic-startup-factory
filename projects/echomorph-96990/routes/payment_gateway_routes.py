
        from flask import Blueprint, jsonify, request
        from services.payment_gateway_service import get_payment_gateway, add_payment_gateway

        payment_gateway_bp = Blueprint('payment_gateway', __name__)


        @payment_gateway_bp.route('/api/payment_gateway', methods=['GET'])
        def payment_gateway_route():
            result = get_payment_gateway()
            return jsonify(result), 200


        @payment_gateway_bp.route('/api/payment_gateway', methods=['POST'])
        def add_payment_gateway_route():
            data = request.get_json()
            name = data.get("name")

            result = add_payment_gateway(name)
            return jsonify(result), 200
        