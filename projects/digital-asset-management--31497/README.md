This is a simple Digital Asset Management Tool MVP built using Flask.
To run the application, navigate to the project directory and execute the following commands:
1. `pip install -r requirements.txt` to install the required dependencies.
2. `gunicorn -w 1 -b 0.0.0.0:$PORT app:app` to run the application.
The application will be available at `http://localhost:$PORT`.