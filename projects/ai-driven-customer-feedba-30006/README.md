
# AI-driven Customer Feedback Analytics

## Description
This is a Flask application for AI-driven Customer Feedback Analytics, which analyzes customer feedback and sentiment analysis.

## Usage
To run the application, use the following command:
bash
gunicorn app:app --bind 0.0.0.0:$PORT

or use the Procfile to run the application with gunicorn.

## API
The application has a single endpoint `/analyze` which returns a plain text response.

## Environment Variable
The application uses the `PORT` environment variable to determine the port number.
