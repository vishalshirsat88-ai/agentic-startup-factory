# PROJECT_CONTEXT.md

# Agentic Startup Factory --- System Context

## Project Overview

The **Agentic Startup Factory** is an autonomous AI system designed to
launch software startups automatically.

The system uses a **multi-agent architecture** where specialized agents
collaborate to:

1.  Generate startup ideas
2.  Design system architecture
3.  Build a working MVP
4.  Automatically debug the code
5.  Create a GitHub repository
6.  Deploy the application to Railway
7.  Capture and store the live URL
8.  Display the deployed product in a dashboard

The long‑term goal is to allow the system to **launch and manage
multiple startups autonomously**.

------------------------------------------------------------------------

# Current System Architecture

The system is coordinated by an **Orchestrator** that manages
communication between agents.

A **threaded orchestration model** is used to prevent dashboard timeouts
during long-running tasks such as deployments.

    Dashboard (Flask UI)
            │
            ▼
         Orchestrator
            │
     ┌───────────────┬───────────────┬───────────────┬───────────────┐
     │               │               │               │
    CEO Agent     CTO Agent     Developer Agent   QA Agent
    Ideas         Architecture    Build MVP        Debug Code
     │
     ▼
    GitHub Agent
    (Create repo + push code)
     │
     ▼
    Deployment Agent
    (Deploy to Railway)
     │
     ▼
    Live Web Application

------------------------------------------------------------------------

# Threaded Execution Model

Previously, the dashboard waited for the entire startup pipeline to
complete, which caused **504 timeouts** during long deployments.

This was solved using **background threading**.

### Dashboard Route

    /approve/<idea_id>

The pipeline launches in a background thread:

``` python
threading.Thread(target=run_pipeline, args=(idea_id,)).start()
```

This allows the dashboard to return immediately while the agents
continue running in the background.

------------------------------------------------------------------------

# Agents Implemented

## CEO Agent

Responsible for **startup idea generation**.

Ideas are stored in:

    data/ideas.json

Example:

``` json
{
"name": "Automated Social Media Content Generator",
"description": "Generate social media content using AI"
}
```

------------------------------------------------------------------------

## CTO Agent

Designs the **system architecture** for the startup.

Outputs include:

-   System components
-   Infrastructure plan
-   APIs
-   Tech stack

Example stack:

    Backend: Flask
    Deployment: Railway
    Server: Gunicorn
    Database: SQLite / PostgreSQL

------------------------------------------------------------------------

## Developer Agent

Automatically generates a **Flask MVP**.

Generated files:

    app.py
    requirements.txt
    Procfile
    README.md

Example Flask app:

``` python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the startup"
```

### Railway Compatibility

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

### Dependency Pinning

    Flask==2.3.3
    Werkzeug==2.3.7
    gunicorn==21.2.0

### Production Server

Procfile:

    web: gunicorn app:app --bind 0.0.0.0:$PORT

------------------------------------------------------------------------

## QA Agent

Runs an **auto-debug loop**.

Workflow:

    run app
    if error:
        send error to LLM
        regenerate fixed code
    retry up to 3 times

------------------------------------------------------------------------

## GitHub Agent

Automatically:

    create repository
    initialize git
    commit files
    push code

------------------------------------------------------------------------

## Deployment Agent

Handles deployment through **Railway CLI in non‑interactive mode**.

Deployment:

    railway init --name <project>
    railway link
    railway up --detach

After deployment:

    wait 15 seconds
    railway domain

Example domain:

    https://startup-production.up.railway.app

------------------------------------------------------------------------

# Orchestrator

The orchestrator coordinates the pipeline and passes **idea_id** across
agents so the final URL can be written back to the database.

------------------------------------------------------------------------

# Automatic URL Persistence

After deployment the system updates:

    data/ideas.json

Example:

``` json
{
"id": 3,
"name": "Automated Social Media Content Generator",
"status": "deployed",
"url": "https://startup-production.up.railway.app"
}
```

This enables the dashboard to display the live link.

------------------------------------------------------------------------

# Dashboard

Run the dashboard:

    python -m dashboard.dashboard

Open:

    http://127.0.0.1:5000

Routes:

    /generate_batch
    /ideas
    /approve/<idea_id>

------------------------------------------------------------------------

# Example Pipeline Execution

    Idea generated
    ↓
    Architecture created
    ↓
    Code generated
    ↓
    QA auto-debug
    ↓
    GitHub repository created
    ↓
    Railway deployment
    ↓
    Public URL generated
    ↓
    ideas.json updated
    ↓
    Dashboard shows live link

Example output:

    🚀 SUCCESS! YOUR STARTUP IS LIVE:
    https://startup-production.up.railway.app

------------------------------------------------------------------------

# Current System Status

Fully working:

-   Idea generation
-   Architecture generation
-   Flask MVP generation
-   Auto-debug loop
-   GitHub repo creation
-   Railway deployment
-   Automatic domain retrieval
-   JSON URL update
-   Dashboard live link display
-   Background threaded execution

------------------------------------------------------------------------

# Next Development Goals

## SaaS Landing Page Generation

Generate full landing pages including:

-   Hero section
-   Feature list
-   Pricing section
-   Signup form

## Database Model Generation

Automatically generate:

-   User tables
-   Signup endpoints
-   Database migrations

## Growth Agent

Marketing automation agent capable of:

-   Landing page copy
-   Social media posts
-   Product launch announcements
-   Reddit launch threads

## Autonomous Startup Factory Mode

Future automation goal:

    generate 20 ideas
    build 20 startups
    deploy 20 apps

------------------------------------------------------------------------

# Quick Handoff Prompt

If starting a new debugging session:

    Agentic Startup Factory with agents:
    CEO → ideas
    CTO → architecture
    Developer → Flask MVP
    QA → auto-debug
    GitHub → repo creation
    Deployment → Railway

    Pipeline:
    approve idea → threaded run → build → debug → push → deploy → retrieve domain → update JSON → dashboard link.

    Next goals:
    landing pages, database models, growth agent, autonomous startup factory.
