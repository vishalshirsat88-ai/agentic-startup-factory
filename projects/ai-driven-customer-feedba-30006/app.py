
import os
from flask import Flask

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/analyze', methods=['GET'])
def analyze_feedback():
    return "AI-driven Customer Feedback Analytics: Analyze customer feedback and sentiment analysis"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

