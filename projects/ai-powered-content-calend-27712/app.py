
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Welcome to the AI-powered Content Calendar Tool!'

if __name__ == '__main__':
    app.run()

