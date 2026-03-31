
        from flask import Blueprint, jsonify, request
        from services.design_service import get_design, add_design

        design_bp = Blueprint('design', __name__)


        @design_bp.route('/api/design', methods=['GET'])
        def design_route():
            result = get_design()
            return jsonify(result), 200


        @design_bp.route('/api/design', methods=['POST'])
        def add_design_route():
            data = request.get_json()
            name = data.get("name")

            result = add_design(name)
            return jsonify(result), 200
        