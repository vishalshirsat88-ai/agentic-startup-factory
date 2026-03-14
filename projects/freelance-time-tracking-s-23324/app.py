
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    """Return plain text from the homepage route"""
    return "Welcome to Freelance Time Tracking Software! Track your freelance work hours and generate invoices automatically."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

