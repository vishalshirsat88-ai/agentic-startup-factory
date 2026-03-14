
from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    """Homepage route"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
