
To run the application, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`
2. Run the application using `gunicorn -b 0.0.0.0:$PORT app:app`
3. Access the application at `http://localhost:5000` or the specified port in the `PORT` environment variable

Note: Make sure to replace `$PORT` with the actual port number in the `Procfile` and `README.md` files.