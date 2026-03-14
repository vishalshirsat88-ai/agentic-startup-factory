
# AI-driven Website Content Analyzer

## Minimal Flask MVP

This is a minimal Flask MVP for the AI-driven Website Content Analyzer startup idea.

## Running the Application

1. Ensure you have Python and pip installed.
2. Create a new virtual environment and activate it.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Run the application using `gunicorn -w 1 -b 0.0.0.0:$PORT app:app`.
5. Access the homepage at `http://localhost:$PORT`.

This code provides a minimal Flask application that meets the specified requirements. The `app.py` file defines a single route for the homepage, which returns a plain text message. The `requirements.txt` file lists the required dependencies, including Flask, Werkzeug, and gunicorn. The `Procfile` file specifies the command to run the application using gunicorn. The `README.md` file provides instructions for running the application.