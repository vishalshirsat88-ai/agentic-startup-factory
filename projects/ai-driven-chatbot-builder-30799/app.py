
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    """Return a message to indicate the server is running."""
    return 'AI-driven Chatbot Builder for Small Businesses is running!'

@app.route('/chatbot-builder')
def chatbot_builder():
    """Return a message to indicate the chatbot builder is available."""
    return 'Create conversational chatbots for small businesses.'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

