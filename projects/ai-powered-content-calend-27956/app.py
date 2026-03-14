
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to AI-powered Content Calendar Tool! Plan, schedule, and optimize content for social media"

if __name__ == "__main__":
    app.run()

