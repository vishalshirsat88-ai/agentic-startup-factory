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
            s.get("name")
            for s in past_startups
            if isinstance(s, dict)
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

        score = 5

        idea_entry = {
            "id": next_id,
            "idea": idea,
            "name": idea.get("name"),
            "description": idea.get("description"),
            "score": self.score_locally(idea),
            "status": "pending"
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

        past_startup_names = [
            s.get("name")
            for s in past_startups
            if isinstance(s, dict)
        ]

        previous_ideas = [
            i.get("idea", {}).get("name")
            for i in existing[-5:]
            if isinstance(i.get("idea"), dict)
        ]

        prompt = f"""
        Generate EXACTLY {count} MICRO-SaaS startup ideas.

        Rules:
        - Must be buildable by a small team
        - Must be an AI tool, automation tool, SaaS, or browser extension
        - Avoid ideas requiring hospitals, governments, hardware, or huge infrastructure

        Avoid repeating these ideas:
        {previous_ideas}

        Also avoid startups that were already built and deployed:
        {past_startup_names}

        IMPORTANT:
        Return EXACTLY {count} ideas.

        Return ONLY valid JSON.

        Example:

        [
        {{
        "name": "AI Resume Tailor",
        "description": "Automatically customize resumes for each job application"
        }},
        {{
        "name": "Freelancer Payment Tracker",
        "description": "Track invoices and late payments for freelancers"
        }}
        ]
        """

        response = self.think(prompt).strip()
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

        next_id = len(existing) + 1
        existing_names = [
            i["idea"].get("name")
            for i in existing
            if isinstance(i.get("idea"), dict)
        ]

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

            bad_words = ["hospital", "government", "satellite", "climate", "manufacturing"]

            text = (idea.get("name","") + idea.get("description","")).lower()

            if any(word in text for word in bad_words):
                continue

            idea_entry = {
                "id": next_id,
                "idea": idea,
                "name": idea.get("name"),
                "description": idea.get("description"),
                "score": self.score_locally(idea),
                "status": "pending"
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