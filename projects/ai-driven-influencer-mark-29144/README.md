
# AI-driven Influencer Marketing Platform

## Overview

This is a minimal Flask MVP for the AI-driven Influencer Marketing Platform. The application has two routes: a root route that displays a welcome message and an influencer route that displays a message related to managing influencer marketing campaigns.

## Running the Application

1. Install the required dependencies by running `pip install -r requirements.txt`
2. Run the application using `gunicorn -w 1 app:app`
3. Access the application at `http://localhost:5000` or the host IP address and the port number specified in the environment variable `PORT`

## Environment Variables

* `PORT`: The port number to run the application on. Default value is 5000.
