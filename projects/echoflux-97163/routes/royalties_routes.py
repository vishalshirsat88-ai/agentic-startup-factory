
        from flask import Blueprint, jsonify, request
        from services.royalties_service import get_royalties, add_royalties

        royalties_bp = Blueprint('royalties', __name__)


        @royalties_bp.route('/api/royalties', methods=['GET'])
        def royalties_route():
            result = get_royalties()
            return jsonify(result), 200


        @royalties_bp.route('/api/royalties', methods=['POST'])
        def add_royalties_route():
            data = request.get_json()
            name = data.get("name")

            result = add_royalties(name)
            return jsonify(result), 200
        