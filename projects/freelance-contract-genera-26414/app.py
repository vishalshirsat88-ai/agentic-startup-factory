
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to Freelance Contract Generator. Automatically generate freelance contracts based on project details."

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=False)

