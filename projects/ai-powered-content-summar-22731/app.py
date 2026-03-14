
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """Return a plain text message"""
    return "Welcome to the AI-powered Content Summarization Tool"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

