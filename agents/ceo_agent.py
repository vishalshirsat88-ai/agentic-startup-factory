from agents.agent_base import AgentBase
from tools.memory import load_memory
from tools.json_parser import extract_json
import json
import os
import re


class CEOAgent(AgentBase):
    def __init__(self):
        super().__init__("CEO Agent")

    def generate_idea(self):
        ideas_file = "data/ideas.json"

        if not os.path.exists(ideas_file):
            with open(ideas_file, "w") as f:
                json.dump([], f)

        with open(ideas_file, "r") as f:
            ideas = json.load(f)

        past_startups = load_memory("startups.json")

        past_startup_names = [
            s.get("name") for s in past_startups if isinstance(s, dict)
        ]

        previous_ideas = [
            i.get("idea", {}).get("name")
            for i in ideas
            if isinstance(i.get("idea"), dict)
        ]

        prompt = f"""
        Generate one innovative startup idea.

        Avoid repeating or being similar to these existing ideas:
        {previous_ideas}

        Also avoid startups that were already built and deployed:
        {past_startup_names}

        Return ONLY valid JSON in this format:

        {{
        "name": "Startup Name",
        "description": "Short description",
        "market": "Target users",
        "revenue_model": "How it makes money"
        }}
        """

        response = self.think(prompt)

        idea = extract_json(response)

        if not idea:
            print("CEO Agent: Invalid JSON response")
            return None

        # score = 5

        next_id = max([i.get("id", 0) for i in ideas], default=0) + 1
        idea_entry = {
            "id": next_id,
            "idea": idea,
            "name": idea.get("name"),
            "description": idea.get("description"),
            "score": self.score_locally(idea),
            "status": "pending",
        }

        ideas.append(idea_entry)

        with open(ideas_file, "w") as f:
            json.dump(ideas, f, indent=2)

        return idea_entry

    def generate_multiple_ideas(self, count=20):
        ideas_file = "data/ideas.json"

        if not os.path.exists(ideas_file):
            with open(ideas_file, "w") as f:
                json.dump([], f)

        with open(ideas_file, "r") as f:
            existing = json.load(f)

        past_startups = load_memory("startups.json")

        past_startup_names = set()

        for s in past_startups:
            if not isinstance(s, dict):
                continue

            name = s.get("name")

            if isinstance(name, str):
                past_startup_names.add(name)

            elif isinstance(name, dict):
                n = name.get("name")
                if n:
                    past_startup_names.add(n)

        previous_ideas = [
            i.get("idea", {}).get("name")
            for i in existing[-10:]
            if isinstance(i.get("idea"), dict)
        ]

        prompt = f"""
        You are an AI startup generator.

        Generate EXACTLY {count} startup ideas.

        Rules:
        - Must be MICRO SaaS
        - Must be AI tool, automation tool, SaaS, or browser extension
        - Must be realistic for a small team
        - Avoid healthcare, government, satellites, manufacturing, climate infrastructure

        Avoid these previous ideas:
        {previous_ideas}

        Avoid already deployed startups:
        {past_startup_names}

        Return ONLY a JSON array.

        Do NOT include explanations.
        Do NOT include markdown.
        Do NOT include numbering.

        Schema:

        [
        {{
            "name": "Startup Name",
            "description": "One sentence description"
        }}
        ]

        Return EXACTLY {count} objects.
        """

        for attempt in range(2):
            response = self.think(prompt).strip()

            json_match = re.search(r"\[[\s\S]*?\]", response)

            if json_match:
                break

            print("CEO retrying JSON generation...")
        print("\n----- CEO RESPONSE -----")
        print(response)
        print("------------------------\n")

        # Extract JSON array safely
        json_match = re.search(r"\[[\s\S]*?\]", response)

        if not json_match:
            print("CEO Agent: No JSON found in response")
            return []

        try:
            new_ideas = json.loads(json_match.group())
            new_ideas = new_ideas[:count]
        except Exception as e:
            print("CEO Agent JSON parse error:", e)
            return []

        saved = []

        next_id = max([i.get("id", 0) for i in existing], default=0) + 1
        existing_names = [i.get("idea", {}).get("name") for i in existing]

        existing_names = set(existing_names)
        past_startup_names = set(past_startup_names)

        for idea in new_ideas:
            if not isinstance(idea, dict):
                continue

            if "name" not in idea or "description" not in idea:
                continue

            if idea.get("name") in existing_names:
                continue

            if idea.get("name") in past_startup_names:
                continue

            bad_words = [
                "hospital",
                "government",
                "satellite",
                "climate",
                "manufacturing",
            ]

            text = (idea.get("name", "") + idea.get("description", "")).lower()

            if any(word in text for word in bad_words):
                continue

            idea_entry = {
                "id": next_id,
                "idea": idea,
                "name": idea.get("name"),
                "description": idea.get("description"),
                "score": self.score_locally(idea),
                "status": "pending",
            }

            next_id += 1

            existing.append(idea_entry)
            saved.append(idea_entry)
            existing_names.add(idea.get("name"))

        existing = existing[-200:]

        with open(ideas_file, "w") as f:
            json.dump(existing, f, indent=2)

        return saved

    def score_locally(self, idea):
        score = 5

        name = idea.get("name", "")
        description = idea.get("description", "")
        text = (name + " " + description).lower()

        if "ai" in text:
            score += 1

        if "automation" in text:
            score += 1

        if "tool" in text or "assistant" in text:
            score += 1

        if "platform" in text or "marketplace" in text:
            score -= 1

        if "government" in text or "hospital" in text:
            score -= 2

        return max(1, min(score, 10))
