# Agentic Startup Factory

## Overview
An automated system that ideates, builds, and deploys SaaS applications autonomously using a multi-agent AI architecture powered by the Groq API (Llama models).

## Architecture

### Workflow
Idea Generation (CEO) → Product Definition → Architecture Design (CTO) → Code (Developer) → QA → Deployment → Growth → Revenue

### Key Directories
- `agents/` — AI agent implementations (ceo, cto, product, developer, qa, deployment, growth, finance, github)
- `orchestrator/orchestrator.py` — Coordinates the full startup pipeline
- `dashboard/dashboard.py` — Flask web interface (Founder Control Room)
- `engine/` — Template renderer for generating SaaS apps
- `saas_master_template/` — Gold master Flask app used as blueprint
- `projects/` — Generated startup source code
- `tools/` — Utilities: llm.py (Groq), github_tool.py, code_runner.py, memory.py
- `data/` — Persistent state: ideas.json, ideas_history.json
- `memory/` — Agent decision logs

## Tech Stack
- **Language:** Python 3.12
- **Framework:** Flask
- **AI Provider:** Groq SDK (Llama models)
- **Package Manager:** pip (`requirements.txt`)
- **Production Server:** Gunicorn

## Running the App
- **Workflow:** "Start application"
- **Command:** `PYTHONPATH=/home/runner/workspace python /home/runner/workspace/dashboard/dashboard.py`
- **Port:** 5000

## Key Routes
- `/` — Dashboard home
- `/generate_idea` — Generate a single startup idea
- `/generate_batch` — Generate 20 ideas
- `/ideas` — View and approve ideas
- `/approve/<id>` — Approve & trigger full build pipeline

## Environment Variables
- `GROQ_API_KEY` — Required. Groq API key for LLM calls.

## Dependencies
- flask, groq, python-dotenv, PyGithub, gunicorn
