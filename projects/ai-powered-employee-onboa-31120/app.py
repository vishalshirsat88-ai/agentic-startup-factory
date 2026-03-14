
import os

from flask import Flask

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    return 'Welcome to AI-powered Employee Onboarding Platform!'

@app.route('/onboarding')
def onboarding():
    return 'Automate employee onboarding and training with our AI-powered platform.'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

