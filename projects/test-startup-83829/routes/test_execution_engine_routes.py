
from flask import Blueprint, jsonify, request, render_template
from services.test_execution_engine_service import execute, add_test_execution_engine

test_execution_engine_bp = Blueprint('test_execution_engine', __name__)

@test_execution_engine_bp.route('/test_execution_engine', methods=['GET'])
def test_execution_engine_page():
    return render_template("test_execution_engine.html")


@test_execution_engine_bp.route('/api/test_execution_engine', methods=['GET'])
def test_execution_engine_route():
    result = execute()
    return jsonify(result), 200


@test_execution_engine_bp.route('/api/test_execution_engine', methods=['POST'])
def add_test_execution_engine_route():
    data = request.get_json()
    name = data.get("name")

    result = add_test_execution_engine(name)
    return jsonify(result), 200
