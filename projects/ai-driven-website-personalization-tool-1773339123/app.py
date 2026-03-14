
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to AI-driven Website Personalization Tool"

if __name__ == "__main__":
    app.run()

