
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to AI-driven Lead Generation Tool. Identify and qualify leads using AI-powered lead generation tools."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

