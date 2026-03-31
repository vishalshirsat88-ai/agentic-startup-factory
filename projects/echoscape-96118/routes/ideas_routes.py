
        from flask import Blueprint, jsonify, request
        from services.ideas_service import get_ideas, add_ideas

        ideas_bp = Blueprint('ideas', __name__)


        @ideas_bp.route('/api/ideas', methods=['GET'])
        def ideas_route():
            result = get_ideas()
            return jsonify(result), 200


        @ideas_bp.route('/api/ideas', methods=['POST'])
        def add_ideas_route():
            data = request.get_json()
            name = data.get("name")

            result = add_ideas(name)
            return jsonify(result), 200
        