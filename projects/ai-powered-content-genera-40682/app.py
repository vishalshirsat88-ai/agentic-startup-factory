
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the AI-powered Content Generation Tool. Automatically generate high-quality content for blogs and social media."

if __name__ == "__main__":
    app.run(debug=True)

