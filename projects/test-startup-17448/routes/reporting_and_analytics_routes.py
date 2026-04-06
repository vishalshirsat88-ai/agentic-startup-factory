
        from flask import Blueprint, jsonify, request
        from services.reporting_and_analytics_service import execute, add_reporting_and_analytics

        reporting_and_analytics_bp = Blueprint('reporting_and_analytics', __name__)


        @reporting_and_analytics_bp.route('/api/reporting_and_analytics', methods=['GET'])
        def reporting_and_analytics_route():
            result = execute()
            return jsonify(result), 200


        @reporting_and_analytics_bp.route('/api/reporting_and_analytics', methods=['POST'])
        def add_reporting_and_analytics_route():
            data = request.get_json()
            name = data.get("name")

            result = add_reporting_and_analytics(name)
            return jsonify(result), 200
        