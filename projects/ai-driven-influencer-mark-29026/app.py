
import os

from flask import Flask

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to AI-driven Influencer Marketing Platform'

@app.route('/influencer', methods=['GET'])
def influencer():
    return 'Identify and manage influencer marketing campaigns'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

