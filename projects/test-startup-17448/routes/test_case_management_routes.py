
        from flask import Blueprint, jsonify, request
        from services.test_case_management_service import execute, add_test_case_management

        test_case_management_bp = Blueprint('test_case_management', __name__)


        @test_case_management_bp.route('/api/test_case_management', methods=['GET'])
        def test_case_management_route():
            result = execute()
            return jsonify(result), 200


        @test_case_management_bp.route('/api/test_case_management', methods=['POST'])
        def add_test_case_management_route():
            data = request.get_json()
            name = data.get("name")

            result = add_test_case_management(name)
            return jsonify(result), 200
        