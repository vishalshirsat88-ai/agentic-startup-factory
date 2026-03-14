import json
import os

MEMORY_FOLDER = "memory"


def load_memory(file):

    path = os.path.join(MEMORY_FOLDER, file)

    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        return json.load(f)


def save_memory(file, data):

    path = os.path.join(MEMORY_FOLDER, file)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def add_entry(file, entry):

    data = load_memory(file)

    data.append(entry)

    save_memory(file, data)