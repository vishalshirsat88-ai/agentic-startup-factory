
```markdown
# DreamWeaver MVP
## Introduction
DreamWeaver is an AI-powered mental wellness platform that utilizes brain-computer interface (BCI) technology to monitor and regulate users' sleep patterns. This repository contains a simple Flask MVP for the DreamWeaver platform.

## Prerequisites
* Python 3.8+
* pip 20.0+

## Installation
1. Clone this repository: `git clone https://github.com/your-username/dreamweaver-mvp.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Run the Application
1. Run the application: `python app.py`
2. Open a web browser and navigate to `http://localhost:5000`

## API Endpoints
* `GET /users`: Retrieve a list of all users
* `POST /users`: Create a new user

## Example Usage
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}' http://localhost:5000/users
```
This will create a new user with the name "John Doe" and email "john@example.com".
```