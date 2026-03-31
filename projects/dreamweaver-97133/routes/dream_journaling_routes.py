
        from flask import Blueprint, jsonify, request
        from services.dream_journaling_service import get_dream_journaling, add_dream_journaling

        dream_journaling_bp = Blueprint('dream_journaling', __name__)


        @dream_journaling_bp.route('/api/dream_journaling', methods=['GET'])
        def dream_journaling_route():
            result = get_dream_journaling()
            return jsonify(result), 200


        @dream_journaling_bp.route('/api/dream_journaling', methods=['POST'])
        def add_dream_journaling_route():
            data = request.get_json()
            name = data.get("name")

            result = add_dream_journaling(name)
            return jsonify(result), 200
        