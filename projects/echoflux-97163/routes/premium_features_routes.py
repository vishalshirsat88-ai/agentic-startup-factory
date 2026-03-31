
        from flask import Blueprint, jsonify, request
        from services.premium_features_service import get_premium_features, add_premium_features

        premium_features_bp = Blueprint('premium_features', __name__)


        @premium_features_bp.route('/api/premium_features', methods=['GET'])
        def premium_features_route():
            result = get_premium_features()
            return jsonify(result), 200


        @premium_features_bp.route('/api/premium_features', methods=['POST'])
        def add_premium_features_route():
            data = request.get_json()
            name = data.get("name")

            result = add_premium_features(name)
            return jsonify(result), 200
        