
        from flask import Blueprint, jsonify, request
        from services.music_composition_service import get_music_composition, add_music_composition

        music_composition_bp = Blueprint('music_composition', __name__)


        @music_composition_bp.route('/api/music_composition', methods=['GET'])
        def music_composition_route():
            result = get_music_composition()
            return jsonify(result), 200


        @music_composition_bp.route('/api/music_composition', methods=['POST'])
        def add_music_composition_route():
            data = request.get_json()
            name = data.get("name")

            result = add_music_composition(name)
            return jsonify(result), 200
        