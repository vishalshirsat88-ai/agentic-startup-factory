
        from flask import Blueprint, jsonify, request
        from services.data_import_service import get_data_import, add_data_import

        data_import_bp = Blueprint('data_import', __name__)


        @data_import_bp.route('/api/data_import', methods=['GET'])
        def data_import_route():
            result = get_data_import()
            return jsonify(result), 200


        @data_import_bp.route('/api/data_import', methods=['POST'])
        def add_data_import_route():
            data = request.get_json()
            name = data.get("name")

            result = add_data_import(name)
            return jsonify(result), 200
        