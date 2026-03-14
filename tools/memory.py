import json
import os

MEMORY_FOLDER = "memory"


def load_memory(file):

    path = os.path.join(MEMORY_FOLDER, file)

    if not os.path.exists(path):
        return []

    if os.path.getsize(path) == 0:
        return []

    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_memory(file, data):

    path = os.path.join(MEMORY_FOLDER, file)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def add_entry(file, entry):

    data = load_memory(file)

    data.append(entry)

    # keep last 100 startups only
    data = data[-100:]

    save_memory(file, data)