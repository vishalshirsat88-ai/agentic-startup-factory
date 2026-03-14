
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Virtual Event Promotion Platform - Promoting virtual events and tracking attendee engagement"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

