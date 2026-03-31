
        from flask import Blueprint, jsonify, request
        from services.animation_service import get_animation, add_animation

        animation_bp = Blueprint('animation', __name__)


        @animation_bp.route('/api/animation', methods=['GET'])
        def animation_route():
            result = get_animation()
            return jsonify(result), 200


        @animation_bp.route('/api/animation', methods=['POST'])
        def add_animation_route():
            data = request.get_json()
            name = data.get("name")

            result = add_animation(name)
            return jsonify(result), 200
        