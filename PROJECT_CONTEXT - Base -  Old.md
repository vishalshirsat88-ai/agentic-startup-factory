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


The orchestrator manages the communication between agents and ensures each stage of the startup creation pipeline runs sequentially.

To prevent dashboard timeouts, the pipeline runs in background threads triggered from the approval route.

Example:

/approve/<idea_id>

The pipeline runs asynchronously while the dashboard returns immediately.
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

Full SaaS scaffold generation **(UI + backend structure)**.

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

Deploys the generated startup automatically using Railway CLI.

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
    system retrieves the public domain URL.

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

The system includes a Flask dashboard for managing the startup pipeline.

Run the dashboard:

    python -m dashboard.dashboard

Open:

    http://127.0.0.1:5000

Routes:

    /generate_batch
    /ideas
    /approve/<idea_id>

The dashboard allows manual approval before startup creation begins.
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
    ↓
    Threaded execution pipeline

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

------------------------------------------------------------------------
# Current Folder Structure

Key project directories:

agents
orchestrator
dashboard
tools
projects
data
memory
logs
constitution

------------------------------------------------------------------------

2️⃣ PROJECT_CONTEXT.md

Auto-generated system snapshot.

Example from your file:

agents

folders

architecture summary

generation timestamp

Seen in:


Purpose:

LLM quick context

This file is automatically regenerated.

Do not edit manually.

3️⃣ CODEBASE_CONTEXT.md (automated)

This file is typically generated by the agent scanning:

folders
files
classes
functions
dependencies

Purpose:

Help agents understand the codebase structure

Example content usually includes:

agents/
orchestrator/
tools/
dashboard/

This is machine-generated context.

Again:

❌ never edit manually.


------------------------------------------------------------------------


Perfect Vishal — this is exactly the right time to **formalize everything**.
I’ll give you a **clean, structured, ready-to-paste summary** for your `Project_context-base.md`.

I’ve also aligned it with your existing architecture from your files  so everything stays consistent.

---

# ✅ 1️⃣ WHAT HAS BEEN COMPLETED (This Chat)

## 🎯 SaaS UI Engine (Major Upgrade)

You successfully built a **reusable SaaS frontend system**:

```text
FlexStart → Landing Page
Sneat → Dashboard
Sneat → Login (optional, later removed)
Flask → Routing
```

### Current Routes

```text
/ → landing.html
/dashboard → dashboard.html
```

---

## 🧱 SaaS Master Template Created

```text
saas_master_template/

templates/
   landing.html
   dashboard.html

static/
   assets (FlexStart)
   sneat  (Dashboard assets)
```

---

## 🔧 Flask Integration Completed

* Templates connected via Flask
* Static assets mapped using `url_for`
* UI renders correctly

---

## 🧠 Key Architecture Shift

❌ Old:

```text
Developer Agent generates full HTML apps
```

✅ New:

```text
Developer Agent → SaaS Template Injection + Backend Generation
```

This is a **critical upgrade toward scalability**

---

# ⚠️ 2️⃣ WHAT IS PENDING

## 🔹 UI-Level Pending

* Convert landing.html → dynamic variables

```text
{{product_name}}
{{product_description}}
{{features}}
```

* Make dashboard partially dynamic (branding at least)

---

## 🔹 Agent Integration Pending

* Developer Agent still generates static MVP
* Needs to:

```text
→ use saas_master_template
→ inject idea into UI
```

---

## 🔹 CTO Agent Limitation

Current issue:

```text
Generates repetitive / monotonous ideas
```

Needs upgrade:

* Market research capability
* Trend-based idea generation
* User input idea option (manual override)

(Already saved in memory ✔️)

---

## 🔹 Payment System (Not started here yet)

* No monetization layer in this project yet
* Will be modularized

---

# 💳 3️⃣ PAYMENT SYSTEM DECISION (FINALIZED)

## ✅ Architecture Decision

Create **reusable universal module**

```text
core_modules/payments/
    payments_module.py
```

---

## 🧠 Design Principle

> Payment flow is SAME across all SaaS
> Only inputs change:

```text
product_name
price
email
```

---

## 🔁 Universal Flow

```text
Landing
   ↓
Payment
   ↓
Token generated
   ↓
Email sent
   ↓
Dashboard access
```

---

## 🔐 Access Pattern

```text
/dashboard?token=abc123
```

---

## ✅ Key Advantage

```text
All generated startups become monetizable instantly
```

---

# 🧪 4️⃣ IMMEDIATE NEXT STEP (PRIORITY)

Before payment, we do:

## 🎯 Goal

Test **data injection into UI**

---

## Step

Modify `landing.html`

### BEFORE

```html
<h1>AI Resume Builder</h1>
```

### AFTER

```html
<h1>{{ product_name }}</h1>
```

---

## Update app.py

```python
idea = {
    "name": "AI Resume Builder",
    "description": "Create ATS optimized resumes using AI"
}

@app.route("/")
def landing():
    return render_template(
        "landing.html",
        product_name=idea["name"],
        product_description=idea["description"]
    )
```

---

## ✅ Outcome

Your UI becomes:

```text
Agent-driven dynamic SaaS UI
```

---

# 🧪 5️⃣ DUMMY PAYMENT MODULE (NEXT STEP)

Create:

```text
core_modules/payments/dummy_payment.py
```

---

## Example

```python
def process_payment():
    return {
        "status": "success",
        "token": "test123"
    }
```

---

## Route

```python
@app.route("/pay")
def pay():
    result = process_payment()

    if result["status"] == "success":
        return redirect(f"/dashboard?token={result['token']}")
    else:
        return "Payment Failed"
```

---

## Purpose

✔ test flow
✔ no real payment yet
✔ fast iteration

---

# 🧠 6️⃣ CTO AGENT FUTURE IMPROVEMENTS

Already identified + saved ✔️

## Current Problem

```text
Static idea generation
```

---

## Planned Upgrade

### 1. Market Research Layer

* Trends
* demand signals
* problem discovery

---

### 2. Smarter Idea Generation

```text
Not random → data-driven
```

---

### 3. Manual Idea Input UI

Dashboard input:

```text
"Enter your startup idea"
```

Agents build it.

---

# 🚀 7️⃣ OVERALL SYSTEM DIRECTION

## Current State

From your file :

```text
Idea → Build → Deploy → Show URL
```

---

## Upgraded Direction

```text
Idea
   ↓
SaaS Template Injection
   ↓
UI Generated
   ↓
Payment Module
   ↓
Deploy
   ↓
Live SaaS Product
```

---

# 🔥 FINAL EVOLUTION (BIG PICTURE)

You are moving from:

```text
AI generates apps
```

to:

```text
AI generates SaaS businesses
```

---

# 🧾 CONSOLIDATED ACTION PLAN

## Phase 1 (NOW)

* [ ] Make landing dynamic
* [ ] Inject idea into UI
* [ ] Test dashboard rendering

---

## Phase 2

* [ ] Create dummy payment module
* [ ] Test success/failure flow

---

## Phase 3

* [ ] Convert JobHunt payment into reusable module
* [ ] Plug into SaaS template

---

## Phase 4

* [ ] Upgrade Developer Agent → template injection
* [ ] Stop raw HTML generation

---

## Phase 5

* [ ] Upgrade CTO Agent:

  * market research
  * idea input UI

---

# ⭐ FINAL SUMMARY (FOR YOUR FILE)

```text
We have successfully built a reusable SaaS UI engine using FlexStart (landing) and Sneat (dashboard), integrated with Flask.

We are transitioning from static MVP generation to a template-based SaaS generation system where agents inject startup ideas into predefined UI templates.

Next steps include enabling dynamic UI injection, building a reusable payment module, and upgrading agents (especially Developer and CTO) to support scalable, autonomous SaaS creation.

The long-term goal is to transform the system from generating applications to generating fully monetizable SaaS businesses.
```

---

# 🔄 SYSTEM UPGRADE — AGENTIC ENGINE EVOLUTION (MAR 2026)

## 🎯 Objective

Upgrade system from simple Flask app generation to full SaaS-ready system generation.

---

## 🚀 Major Enhancements Implemented

### 1️⃣ Product Layer Added

A Product Agent now defines:

- Core features
- User flows
- Edge cases

This improves architecture quality and downstream generation.

---

### 2️⃣ Backend File Generation Engine

System now generates structured backend:

- models/
- services/
- routes/

Each module corresponds to system architecture.

---

### 3️⃣ Auto Wiring Engine

Routes are automatically connected to Flask app.

No manual blueprint registration required.

Dynamic app detection implemented (no dependency on app.py filename).

---

### 4️⃣ Self-Healing Development Loop

System now:

- Runs generated app
- Detects runtime errors
- Sends errors to Developer Agent
- Rewrites code
- Retries execution

Up to multiple attempts.

---

### 5️⃣ SaaS Template Injection

Shift from raw HTML generation to template-based system.

Reusable UI:

- Landing page (FlexStart)
- Dashboard (Sneat)

Idea data injected dynamically.

---

### 6️⃣ Improved Orchestration Debugging

Step-by-step logging added:

- Pipeline tracing
- Failure point detection
- Execution visibility

---

## 🧠 Updated Pipeline

Idea → Product → Architecture → Code → Backend → Auto-wire → QA → Dev Loop

---

## ⚠️ Current Limitations

- Generated applications lack real business logic
- Routes and services are not fully connected
- No database integration yet

---

## 🎯 Next Milestone

Convert generated systems into functional SaaS by:

- Connecting routes → services
- Adding real API responses
- Integrating database layer
- Adding authentication and payments

---

## ⭐ System Evolution

From:

AI-generated Flask apps

To:

AI-generated SaaS-ready systems

---



# Next Development Phase

## 🎯 Phase 1 — Application Functionalization (CURRENT PRIORITY)

Convert generated apps into usable SaaS products.

Tasks:

• Connect routes → services  
• Implement real API responses  
• Add request/response handling  
• Remove placeholder logic  
• Ensure endpoints return meaningful data  

---

## 🧱 Phase 2 — Basic Database Integration

Introduce persistent storage.

Tasks:

• Add SQLite database  
• Create basic models (User, Data)  
• Connect services to database  
• Implement simple CRUD operations  

---

## 🎨 Phase 3 — SaaS Template Enhancement

Make generated apps user-ready.

Tasks:

• Fully dynamic landing page  
• Dynamic dashboard content  
• Branding injection from idea  
• Feature display from Product Agent  

---

## 💰 Phase 4 — Monetization Layer

Enable revenue generation.

Tasks:

• Integrate reusable payment module  
• Token/session-based access  
• Dashboard protection  
• Email delivery  

---

## 📈 Phase 5 — Growth Automation

Add marketing intelligence.

Tasks:

• Growth Agent (launch copy)  
• Social media automation  
• Product positioning  

---

## 🤖 Phase 6 — Startup Factory Mode (SCALING)

Scale system after validation.

Tasks:

• Generate multiple startups  
• Deploy multiple apps  
• Track performance  
• Kill low-performing ideas  

# 🔒 SYSTEM ARCHITECTURE DECISIONS (LOCKED)

## 🎯 Core Product Model — "No Login SaaS (Token-Based Access)"

We are NOT building traditional SaaS with user accounts.

### ❌ What we DO NOT use:

* No login/signup system
* No user authentication
* No session management
* No user database
* No credential storage

---

## ✅ What we ARE building (JobHunt++ Model)

### Flow:

Landing Page → Payment → Token Generation → Tool Access

---

### 🟢 Step-by-step flow:

1. User lands on homepage (Landing Page)

2. User clicks **Pay / Get Access**

3. Payment is processed (Razorpay / PayPal)

4. System generates a **unique access token**

5. Token is sent via email

6. User accesses product using:

   /app?token=xxxx

7. Backend validates token

8. User gets access to tool

---

## 🔐 Token-Based Access Rules

* Token = single source of identity
* No login required
* No password system
* Token can be:

  * time-limited (optional)
  * usage-limited (optional)

---

## 💡 Why this model?

* Faster user onboarding (no friction)
* Higher conversion rates
* Simpler backend (no auth system)
* Matches JobHunt++ architecture
* Ideal for MVP + micro SaaS

---

# 🧱 Backend Architecture Implications

## ❌ REMOVE from all generated apps:

* /login routes
* /signup routes
* auth models
* auth services
* session handling

---

## ✅ ADD to all generated apps:

### Required Components:

1. **Landing Page**
2. **Payment Integration**
3. **Token Generation System**
4. **Token Validation Middleware**
5. **Protected Tool Routes**

---

## Example:

/ → Landing Page
/pay → Payment
/app?token=xyz → Tool access

---

# 🗂️ Repository Strategy (CRITICAL)

## ✅ SINGLE REPO MODEL (MANDATORY)

All generated startups must follow:

agentic-startup-factory/
└── projects/
├── startup-1
├── startup-2
├── ...

---

## ❌ STRICTLY FORBIDDEN:

* Creating new GitHub repos per startup
* Separate repositories for each idea

---

## ✅ Git Behavior:

* Each new project is added under `/projects`
* Only that folder + context is committed
* Same repo is continuously updated

---

# 🧠 System Memory

* CODEBASE_CONTEXT.md is the **single source of memory**
* Used for:

  * duplicate prevention
  * architecture consistency
  * decision persistence

---

# ⚠️ NON-NEGOTIABLE RULES

1. Never introduce login/signup again
2. Never create separate repos per startup
3. Always follow token-based access model
4. Always update context after each run

---

# 🚀 Summary

We are building:

👉 Fast-launch, token-based micro SaaS factory
👉 Not traditional multi-user SaaS platform
👉 Not auth-heavy systems

---

System philosophy:

"Pay → Get Token → Use Tool"

------------------------------------------------------------------------

# 🔄 SYSTEM UPGRADE — MARCH 2026 (CRITICAL UPDATE)

## 🎯 Architecture Evolution

The system has evolved from a basic Flask app generator to a **structured SaaS generation engine**.

New pipeline:

Idea → Product → Architecture → Code → Backend → Auto-wire → QA → Dev Loop → GitHub → Deployment

---

## 🧠 Key Architectural Upgrades

### 1️⃣ Product Layer Introduced

A Product Agent now defines:

• Core features  
• User flows  
• Functional requirements  

This improves consistency between idea → architecture → implementation.

---

### 2️⃣ Backend Generation Engine (Structured)

System now generates:

• models/  
• services/  
• routes/  

Each aligned with architecture output.

---

### 3️⃣ Auto-Wiring System (Stabilized)

Routes are automatically connected to the Flask app.

• No manual blueprint registration  
• Dynamic app detection  
• Works across all generated projects  

---

### 4️⃣ SaaS Template System (MAJOR SHIFT)

System now uses **pre-built reusable UI templates** instead of generating raw HTML.

Templates:

• Landing Page (FlexStart-based)  
• Dashboard (Sneat-based)  

Injected dynamically using:

• product_name  
• product_description  
• feature variables  
• contact details  

🚫 UI is now LOCKED and must NOT be modified further.

---

### 5️⃣ GitHub Strategy (FINALIZED)

System now follows a **single repository model**:

• All projects stored under:

    projects/<project_name>/

• GitHub Agent:
  - adds project folder
  - commits
  - pushes to main repo

❌ No new repo per startup  
❌ No dynamic repo creation  

---

### 6️⃣ Environment-Based Execution (CRITICAL)

System behavior is now environment-aware:

• ENV=local  
  - skips GitHub push  
  - skips deployment  

• ENV=prod  
  - enables full automation  

🚫 Manual toggling is prohibited  

---

### 7️⃣ Deployment System (Stabilized)

• Deployment handled via Railway CLI  
• Non-interactive execution  
• Domain auto-fetch implemented  

Environments:

• Replit → testing  
• GitHub / Codespaces → production  

---

### 8️⃣ Threaded Execution (Retained)

Pipeline continues to run in background threads to prevent dashboard timeouts.

---

## 📊 Current System Status (UPDATED)

### ✅ Fully Functional

• Idea generation  
• Product definition  
• Architecture design  
• Backend file generation  
• Auto-wiring  
• QA debug loop  
• GitHub integration (single repo)  
• Deployment via Railway  
• URL persistence  
• Dashboard execution  
• SaaS UI template system  

---

### ❌ Critical Gap (BLOCKER)

Generated applications are NOT fully functional.

Issues:

• routes exist but do not call services  
• services return placeholder data  
• APIs are not usable  
• no real business logic  

---

## 🎯 CURRENT PRIORITY

### 🔥 Phase 1 — Application Functionalization

This is the **highest priority and blocking phase**.

Objective:

Convert generated apps into **usable SaaS backends**

---

## 🧱 Required Fix (SYSTEM LEVEL)

Modify generation logic so that:

• routes call services  
• services return real data  
• APIs return JSON responses  

---

## 🧩 Target Pattern

Standard architecture to enforce:

Route → Service → JSON

Example:

```python
@app.route("/api/users")
def users():
    data = user_service.get_users()
    return jsonify(data)



---

# 🧠 WHAT I FIXED (IMPORTANT)

Compared to your original file, I:

✔ Removed outdated “HTML generation” assumption  
✔ Added **SaaS template system (your biggest upgrade)**  
✔ Fixed GitHub logic (single repo model)  
✔ Added ENV-based execution (critical)  
✔ Marked Phase 1 as **true blocker**  
✔ Aligned pipeline with actual system  
✔ Removed contradictions with earlier sections  

---

# 🚀 NEXT STEP

Now:

1. ✅ Paste this at bottom of your file  
2. ✅ Save  
3. ✅ System context is now CLEAN  

---

# 💬 NEXT

When ready:

👉 **"start phase 1 step 1"**

We now move into **core backend logic (real SaaS)** 🚀
