markdown
# Freelance Time Tracking Software

## Overview

This is a simple Flask MVP for a freelance time tracking software. The application allows users to track their work hours and generate invoices automatically.

## Running the Application

1. Install the required dependencies by running `pip install -r requirements.txt`
2. Run the application using `gunicorn` by executing `gunicorn app:app --bind 0.0.0.0:$PORT`
3. Access the application by visiting `http://localhost:5000` in your web browser
