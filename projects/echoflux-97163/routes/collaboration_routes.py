
        from flask import Blueprint, jsonify, request
        from services.collaboration_service import get_collaboration, add_collaboration

        collaboration_bp = Blueprint('collaboration', __name__)


        @collaboration_bp.route('/api/collaboration', methods=['GET'])
        def collaboration_route():
            result = get_collaboration()
            return jsonify(result), 200


        @collaboration_bp.route('/api/collaboration', methods=['POST'])
        def add_collaboration_route():
            data = request.get_json()
            name = data.get("name")

            result = add_collaboration(name)
            return jsonify(result), 200
        