
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to AI-driven Sales Forecasting Tool! Predict sales based on historical data and market trends."

if __name__ == "__main__":
    app.run(debug=True)

