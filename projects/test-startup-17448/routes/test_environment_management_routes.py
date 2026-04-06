
        from flask import Blueprint, jsonify, request
        from services.test_environment_management_service import execute, add_test_environment_management

        test_environment_management_bp = Blueprint('test_environment_management', __name__)


        @test_environment_management_bp.route('/api/test_environment_management', methods=['GET'])
        def test_environment_management_route():
            result = execute()
            return jsonify(result), 200


        @test_environment_management_bp.route('/api/test_environment_management', methods=['POST'])
        def add_test_environment_management_route():
            data = request.get_json()
            name = data.get("name")

            result = add_test_environment_management(name)
            return jsonify(result), 200
        