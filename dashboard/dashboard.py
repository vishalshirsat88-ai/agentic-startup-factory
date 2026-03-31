from flask import Flask, jsonify
from orchestrator.orchestrator import Orchestrator
import json
import os
import threading  # <--- Step 1: Add this import

app = Flask(__name__)
orch = Orchestrator()


@app.route("/")
def home():
    return "Founder Control Room Dashboard Running"


@app.route("/generate_idea")
def generate_idea():
    idea = orch.ceo.generate_idea()

    return "Idea generated. Go to /ideas to approve."


@app.route("/generate_batch")
def generate_batch():
    ideas = orch.ceo.generate_multiple_ideas(20)

    return f"{len(ideas)} ideas generated. Visit /ideas to review."


@app.route("/ideas")
def show_ideas():
    if not os.path.exists("data/ideas.json"):
        return "No ideas yet. Generate one at /generate_idea"

    with open("data/ideas.json") as f:
        ideas = json.load(f)

    html = "<h1>Startup Ideas</h1>"

    for idea in ideas:
        if idea.get("processed"):
            continue  # skip already processed ideas
        # Check if a URL was saved by the Deployment Agent
        url_display = (
            f"<br><b>URL:</b> <a href='{idea['url']}' target='_blank'>{idea['url']}</a>"
            if idea.get("url")
            else ""
        )

        html += f"""
        <div style='border:1px solid #ccc;padding:10px;margin:10px;border-radius:10px;'>
        <h3>Idea #{idea["id"]}</h3>
        <pre>{idea["idea"]}</pre>
        Score: {idea.get("score", "N/A")} <br>
        Status: <b>{idea["status"]}</b> {url_display} <br>
        <a href="/approve/{idea["id"]}">Approve & Deploy</a>
        </div>
        """

    return html


@app.route("/approve/<int:idea_id>")
def approve_idea(idea_id):
    with open("data/ideas.json") as f:
        ideas = json.load(f)

    selected_idea = None

    for idea in ideas:
        if idea["id"] == idea_id:
            idea["status"] = "approved"
            idea["processed"] = True  # ✅ ADD THIS LINE
            selected_idea = idea
            break

    if selected_idea:
        # Save updated ideas
        with open("data/ideas.json", "w") as f:
            json.dump(ideas, f, indent=2)

        print("🚀 Starting startup cycle...")
        print("DEBUG SELECTED IDEA:", selected_idea)

        # ✅ RUN ORCHESTRATOR
        def run_safe():
            try:
                orch.run_startup_cycle(selected_idea, idea_id)
            except Exception as e:
                print("❌ THREAD ERROR:", str(e))

        thread = threading.Thread(target=run_safe)
        thread.start()

        return f"""
        <h1>Build Started!</h1>
        <p>Idea #{idea_id} is being processed.</p>
        <a href='/ideas'>Back to Ideas</a>
        """

    return "Idea not found."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
