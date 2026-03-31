
        from flask import Blueprint, jsonify, request
        from services.data_analytics_service import get_data_analytics, add_data_analytics

        data_analytics_bp = Blueprint('data_analytics', __name__)


        @data_analytics_bp.route('/api/data_analytics', methods=['GET'])
        def data_analytics_route():
            result = get_data_analytics()
            return jsonify(result), 200


        @data_analytics_bp.route('/api/data_analytics', methods=['POST'])
        def add_data_analytics_route():
            data = request.get_json()
            name = data.get("name")

            result = add_data_analytics(name)
            return jsonify(result), 200
        