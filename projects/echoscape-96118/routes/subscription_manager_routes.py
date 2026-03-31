
        from flask import Blueprint, jsonify, request
        from services.subscription_manager_service import get_subscription_manager, add_subscription_manager

        subscription_manager_bp = Blueprint('subscription_manager', __name__)


        @subscription_manager_bp.route('/api/subscription_manager', methods=['GET'])
        def subscription_manager_route():
            result = get_subscription_manager()
            return jsonify(result), 200


        @subscription_manager_bp.route('/api/subscription_manager', methods=['POST'])
        def add_subscription_manager_route():
            data = request.get_json()
            name = data.get("name")

            result = add_subscription_manager(name)
            return jsonify(result), 200
        