
        from flask import Blueprint, jsonify, request
        from services.dashboard_service import get_dashboard, add_dashboard

        dashboard_bp = Blueprint('dashboard', __name__)


        @dashboard_bp.route('/api/dashboard', methods=['GET'])
        def dashboard_route():
            result = get_dashboard()
            return jsonify(result), 200


        @dashboard_bp.route('/api/dashboard', methods=['POST'])
        def add_dashboard_route():
            data = request.get_json()
            name = data.get("name")

            result = add_dashboard(name)
            return jsonify(result), 200
        