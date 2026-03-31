
        from flask import Blueprint, jsonify, request
        from services.payments_service import get_payments, add_payments

        payments_bp = Blueprint('payments', __name__)


        @payments_bp.route('/api/payments', methods=['GET'])
        def payments_route():
            result = get_payments()
            return jsonify(result), 200


        @payments_bp.route('/api/payments', methods=['POST'])
        def add_payments_route():
            data = request.get_json()
            name = data.get("name")

            result = add_payments(name)
            return jsonify(result), 200
        