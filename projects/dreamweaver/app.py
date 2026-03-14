**DreamWeaver MVP**

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample in-memory data store (replace with a database in production)
users = {}
sessions = {}

# API Endpoints
@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.json
    user_id = data['user_id']
    users[user_id] = {
        'name': data['name'],
        'email': data['email']
    }
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Login an existing user"""
    data = request.json
    user_id = data['user_id']
    if user_id in users:
        return jsonify({'message': 'User logged in successfully'}), 200
    return jsonify({'message': 'Invalid user ID'}), 401

@app.route('/sessions', methods=['POST'])
def create_session():
    """Create a new meditation session"""
    data = request.json
    session_id = data['session_id']
    sessions[session_id] = {
        'user_id': data['user_id'],
        'session_type': data['session_type'],
        'duration': data['duration']
    }
    return jsonify({'message': 'Session created successfully'}), 201

@app.route('/sessions/<session_id>', methods=['GET'])
def get_session(session_id):
    """Retrieve a meditation session"""
    if session_id in sessions:
        return jsonify(sessions[session_id]), 200
    return jsonify({'message': 'Session not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
