
        from flask import Blueprint, jsonify, request
        from services.sleep_analysis_service import get_sleep_analysis, add_sleep_analysis

        sleep_analysis_bp = Blueprint('sleep_analysis', __name__)


        @sleep_analysis_bp.route('/api/sleep_analysis', methods=['GET'])
        def sleep_analysis_route():
            result = get_sleep_analysis()
            return jsonify(result), 200


        @sleep_analysis_bp.route('/api/sleep_analysis', methods=['POST'])
        def add_sleep_analysis_route():
            data = request.get_json()
            name = data.get("name")

            result = add_sleep_analysis(name)
            return jsonify(result), 200
        