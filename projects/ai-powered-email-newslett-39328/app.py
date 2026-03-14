
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    """Return the homepage content"""
    return "Welcome to AI-powered Email Newsletter Creator. Automatically generate engaging email newsletters."

if __name__ == '__main__':
    app.run()

