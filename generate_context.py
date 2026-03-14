import os
from datetime import datetime

OUTPUT_FILE = "CODEBASE_CONTEXT.md"
PROJECT_ROOT = "."

context = []

context.append("# Codebase Context Snapshot")
context.append(f"Generated: {datetime.utcnow()} UTC\n")

context.append("## Project Structure\n")

for root, dirs, files in os.walk(PROJECT_ROOT):
    if ".git" in root:
        continue

    context.append(f"\n### Folder: {root}")

    for file in files:
        if file.endswith(".py") or file.endswith(".md"):
            context.append(f"- {file}")

context.append("\n---\n")
context.append("## File Contents (truncated)\n")

for root, dirs, files in os.walk(PROJECT_ROOT):
    if ".git" in root:
        continue

    for file in files:
        if file.endswith(".py") or file.endswith(".md"):

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

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(context))

print("Context snapshot updated.")
