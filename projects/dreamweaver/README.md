```markdown
# DreamWeaver MVP

A simple Flask backend for the DreamWeaver mental wellness platform.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/dreamweaver-mvp.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the API endpoints using a tool like `curl` or a REST client (e.g., Postman)

## API Endpoints

* `POST /register`: Register a new user
* `POST /login`: Login an existing user
* `POST /sessions`: Create a new meditation session
* `GET /sessions/<session_id>`: Retrieve a meditation session

## Example Use Cases

* Register a new user: `curl -X POST -H "Content-Type: application/json" -d '{"user_id": "user123", "name": "John Doe", "email": "johndoe@example.com"}' http://localhost:5000/register`
* Create a new meditation session: `curl -X POST -H "Content-Type: application/json" -d '{"session_id": "session123", "user_id": "user123", "session_type": "meditation", "duration": 30}' http://localhost:5000/sessions`
```