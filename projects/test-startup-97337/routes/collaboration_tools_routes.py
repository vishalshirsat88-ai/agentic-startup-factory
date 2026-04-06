
from flask import Blueprint, jsonify, request, render_template
from services.collaboration_tools_service import execute, add_collaboration_tools

collaboration_tools_bp = Blueprint('collaboration_tools', __name__)

@collaboration_tools_bp.route('/collaboration_tools', methods=['GET'])
def collaboration_tools_page():
    return render_template("collaboration_tools.html")


@collaboration_tools_bp.route('/api/collaboration_tools', methods=['GET'])
def collaboration_tools_route():
    result = execute()
    return jsonify(result), 200


@collaboration_tools_bp.route('/api/collaboration_tools', methods=['POST'])
def add_collaboration_tools_route():
    data = request.get_json()
    name = data.get("name")

    result = add_collaboration_tools(name)
    return jsonify(result), 200
