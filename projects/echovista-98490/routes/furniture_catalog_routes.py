
        from flask import Blueprint, jsonify, request
        from services.furniture_catalog_service import get_furniture_catalog, add_furniture_catalog

        furniture_catalog_bp = Blueprint('furniture_catalog', __name__)


        @furniture_catalog_bp.route('/api/furniture_catalog', methods=['GET'])
        def furniture_catalog_route():
            result = get_furniture_catalog()
            return jsonify(result), 200


        @furniture_catalog_bp.route('/api/furniture_catalog', methods=['POST'])
        def add_furniture_catalog_route():
            data = request.get_json()
            name = data.get("name")

            result = add_furniture_catalog(name)
            return jsonify(result), 200
        