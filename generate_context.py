import os
from datetime import datetime, UTC

PROJECT_ROOT = "."

CODEBASE_FILE = "CODEBASE_CONTEXT.md"
PROJECT_FILE = "PROJECT_CONTEXT.md"


def generate_codebase_context():

    context = []

    context.append("# Codebase Context Snapshot")
    context.append(f"Generated: {datetime.now(UTC)}\n")

    context.append("## Project Structure\n")

    for root, dirs, files in os.walk(PROJECT_ROOT):

        if ".git" in root or "projects/" in root:
            continue

        context.append(f"\n### Folder: {root}")

        for file in files:
            if file.endswith(".py") or file.endswith(".md"):
                context.append(f"- {file}")

    context.append("\n---\n")
    context.append("## File Contents (truncated)\n")

    for root, dirs, files in os.walk(PROJECT_ROOT):

        if ".git" in root or "projects/" in root:
            continue

        for file in files:

            if file.endswith(".py"):

                path = os.path.join(root, file)

                context.append(f"\n### {path}\n")

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()

                    context.append("```python")
                    context.append(content[:2000])
                    context.append("```")

                except:
                    context.append("Could not read file")

    with open(CODEBASE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(context))


def generate_project_context():

    agents = []
    folders = []

    for root, dirs, files in os.walk(PROJECT_ROOT):

        if ".git" in root:
            continue

        for file in files:

            if file.endswith("_agent.py"):
                agents.append(file.replace(".py", ""))

        for d in dirs:
            folders.append(d)

    context = []

    context.append("# Project Context\n")

    context.append("## Architecture\n")
    context.append("Dashboard → Orchestrator → Agents → Tools → Deployment\n")

    context.append("## Agents\n")

    for a in agents:
        context.append(f"- {a}")

    context.append("\n## Main Folders\n")

    for f in set(folders):
        context.append(f"- {f}")

    context.append("\n## Generated\n")
    context.append(str(datetime.now(UTC)))

    with open(PROJECT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(context))


generate_codebase_context()
generate_project_context()

print("Context files updated.")