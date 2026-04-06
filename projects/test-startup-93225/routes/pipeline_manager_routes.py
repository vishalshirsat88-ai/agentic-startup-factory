
from flask import Blueprint, jsonify, request, render_template
from services.pipeline_manager_service import execute, add_pipeline_manager

pipeline_manager_bp = Blueprint('pipeline_manager', __name__)

@pipeline_manager_bp.route('/pipeline_manager', methods=['GET'])
def pipeline_manager_page():
    return render_template("pipeline_manager.html")


@pipeline_manager_bp.route('/api/pipeline_manager', methods=['GET'])
def pipeline_manager_route():
    result = execute()
    return jsonify(result), 200


@pipeline_manager_bp.route('/api/pipeline_manager', methods=['POST'])
def add_pipeline_manager_route():
    data = request.get_json()
    name = data.get("name")

    result = add_pipeline_manager(name)
    return jsonify(result), 200
