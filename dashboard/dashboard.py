from flask import Flask, jsonify
from orchestrator.orchestrator import Orchestrator

app = Flask(__name__)
orch = Orchestrator()

@app.route("/")
def home():
    return "Founder Control Room Dashboard Running"

@app.route("/run_cycle")
def run_cycle():
    orch.run_startup_cycle()
    return jsonify({"status": "cycle started"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)