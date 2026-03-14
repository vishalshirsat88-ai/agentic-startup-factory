
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to E-commerce Product Recommendation Tool"

if __name__ == "__main__":
    app.run()

