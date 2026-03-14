
This is a simple Flask MVP for the AI-powered Content Summarization Tool.

To run the application:

1. Install the required dependencies by running `pip install -r requirements.txt`
2. Run the application using `gunicorn app:app --bind 0.0.0.0:$PORT`

Note: This application is designed to run in a cloud deployment environment. The `Procfile` specifies the command to run the application using gunicorn.
