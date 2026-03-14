
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """Return plain text from the homepage route"""
    return "Welcome to AI-driven Website Content Analyzer"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

