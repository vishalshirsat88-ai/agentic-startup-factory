
# AI-driven Chatbot Builder for Small Businesses

## Project Overview

This is a simple Flask MVP for the AI-driven Chatbot Builder for Small Businesses. The application is designed to create conversational chatbots for small businesses.

## Getting Started

1. Clone the repository using `git clone`.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Start the application using `gunicorn -w 4 app:app --bind 0.0.0.0:$PORT`.
4. Access the application at `http://localhost:5000/chatbot-builder`.

## API Endpoints

* `/health`: Returns a message to indicate the server is running.
* `/chatbot-builder`: Returns a message to indicate the chatbot builder is available.

## Running the Application

To run the application, use the following command:

`gunicorn -w 4 app:app --bind 0.0.0.0:$PORT`

This will start the application on port 5000. You can access the application at `http://localhost:5000/chatbot-builder`.

## Deployment

To deploy the application, use the following command:

`gunicorn -w 4 app:app --bind 0.0.0.0:$PORT`

This will start the application on the specified port.

## Contributing

Contributions are welcome! Please submit a pull request with your changes.
