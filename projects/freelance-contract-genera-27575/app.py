
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    """Return homepage text."""
    return "Welcome to Freelance Contract Generator. This is a simple MVP to generate freelance contracts based on project details."

if __name__ == "__main__":
    app.run()

