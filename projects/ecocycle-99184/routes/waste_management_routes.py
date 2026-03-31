
        from flask import Blueprint, jsonify, request
        from services.waste_management_service import get_waste_management, add_waste_management

        waste_management_bp = Blueprint('waste_management', __name__)


        @waste_management_bp.route('/api/waste_management', methods=['GET'])
        def waste_management_route():
            result = get_waste_management()
            return jsonify(result), 200


        @waste_management_bp.route('/api/waste_management', methods=['POST'])
        def add_waste_management_route():
            data = request.get_json()
            name = data.get("name")

            result = add_waste_management(name)
            return jsonify(result), 200
        