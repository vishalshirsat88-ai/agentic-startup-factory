
        from flask import Blueprint, jsonify, request
        from services.core_logic_service import get_core_logic, add_core_logic

        core_logic_bp = Blueprint('core_logic', __name__)


        @core_logic_bp.route('/api/core_logic', methods=['GET'])
        def core_logic_route():
            result = get_core_logic()
            return jsonify(result), 200


        @core_logic_bp.route('/api/core_logic', methods=['POST'])
        def add_core_logic_route():
            data = request.get_json()
            name = data.get("name")

            result = add_core_logic(name)
            return jsonify(result), 200
        