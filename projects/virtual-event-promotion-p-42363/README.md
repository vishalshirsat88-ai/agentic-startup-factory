
This is a minimal Flask MVP for the Virtual Event Promotion Platform.

### To run the application:
1. Create a new virtual environment using `python -m venv venv`
2. Activate the virtual environment using `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows)
3. Install the dependencies using `pip install -r requirements.txt`
4. Run the application using `gunicorn app:app` (for production) or `python app.py` (for development)

### To deploy on Railway:
1. Create a new Railway project
2. Add the `Procfile` to the project directory
3. Set the `PORT` environment variable to 5000
4. Deploy the application using the Railway dashboard
