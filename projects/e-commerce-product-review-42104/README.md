markdown
# E-commerce Product Review Analysis Tool

This is a minimal Flask application for the E-commerce Product Review Analysis Tool.

## Running the Application

1. Clone the repository using `git clone`.
2. Navigate to the project directory using `cd`.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the application using `gunicorn` (recommended) or `python app.py`.
5. Access the application at `http://localhost:5000` or the specified port.

## Cloud Deployment

To deploy the application on Railway, create a new Railway project and link it to this repository. Update the `Procfile` to `web: gunicorn app:app` and deploy the application.
