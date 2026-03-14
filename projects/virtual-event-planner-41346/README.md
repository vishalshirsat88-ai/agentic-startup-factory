
# Virtual Event Planner

Automate event planning tasks with AI-powered suggestions.

## Running the Application

1. Install dependencies by running `pip install -r requirements.txt`
2. Run the application by executing `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
3. Access the homepage at `http://localhost:5000` (or the port specified in the `PORT` environment variable)

Note: For cloud deployment on Railway, use the provided `Procfile` and `PORT` environment variable to run the application.