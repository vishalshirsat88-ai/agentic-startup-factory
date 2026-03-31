
        from flask import Blueprint, jsonify, request
        from services.subscription_management_service import get_subscription_management, add_subscription_management

        subscription_management_bp = Blueprint('subscription_management', __name__)


        @subscription_management_bp.route('/api/subscription_management', methods=['GET'])
        def subscription_management_route():
            result = get_subscription_management()
            return jsonify(result), 200


        @subscription_management_bp.route('/api/subscription_management', methods=['POST'])
        def add_subscription_management_route():
            data = request.get_json()
            name = data.get("name")

            result = add_subscription_management(name)
            return jsonify(result), 200
        