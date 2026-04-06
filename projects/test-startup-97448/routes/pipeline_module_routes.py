
from flask import Blueprint, jsonify, request, render_template
from services.pipeline_module_service import execute, add_pipeline_module

pipeline_module_bp = Blueprint('pipeline_module', __name__)

@pipeline_module_bp.route('/pipeline_module', methods=['GET'])
def pipeline_module_page():
    return render_template("pipeline_module.html")


@pipeline_module_bp.route('/api/pipeline_module', methods=['GET'])
def pipeline_module_route():
    result = execute()
    return jsonify(result), 200


@pipeline_module_bp.route('/api/pipeline_module', methods=['POST'])
def add_pipeline_module_route():
    data = request.get_json()
    name = data.get("name")

    result = add_pipeline_module(name)
    return jsonify(result), 200
