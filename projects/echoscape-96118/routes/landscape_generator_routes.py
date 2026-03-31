
        from flask import Blueprint, jsonify, request
        from services.landscape_generator_service import get_landscape_generator, add_landscape_generator

        landscape_generator_bp = Blueprint('landscape_generator', __name__)


        @landscape_generator_bp.route('/api/landscape_generator', methods=['GET'])
        def landscape_generator_route():
            result = get_landscape_generator()
            return jsonify(result), 200


        @landscape_generator_bp.route('/api/landscape_generator', methods=['POST'])
        def add_landscape_generator_route():
            data = request.get_json()
            name = data.get("name")

            result = add_landscape_generator(name)
            return jsonify(result), 200
        