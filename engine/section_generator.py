def detect_domain(product):
    text = (product.get("name", "") + " " + product.get("description", "")).lower()

    if "ai" in text:
        return "ai"

    elif "test" in text or "pipeline" in text:
        return "testing"

    elif "job" in text or "career" in text:
        return "job"

    elif "marketing" in text:
        return "marketing"

    else:
        return "generic"


def generate_sections(product):
    name = product.get("name", "AI Product")
    description = product.get("description", "")
    modules = product.get("modules", [])

    domain = detect_domain(product)

    sections = []

    # 🔥 HERO
    sections.append(
        {"type": "hero", "title": name, "subtitle": description, "cta": "Get Access"}
    )

    # 🔥 DOMAIN-SPECIFIC SECTIONS

    if domain == "testing":
        sections.append(
            {
                "type": "pain",
                "points": [
                    "Flaky test pipelines",
                    "Manual debugging takes hours",
                    "No visibility into failures",
                    "Slow release cycles",
                ],
            }
        )

        sections.append(
            {
                "type": "solution",
                "text": f"{name} automates testing workflows and debugging",
            }
        )

    elif domain == "job":
        sections.append(
            {
                "type": "pain",
                "points": [
                    "Applying to hundreds of jobs",
                    "No response from recruiters",
                    "Low salary visibility",
                    "Time-consuming applications",
                ],
            }
        )

        sections.append(
            {"type": "solution", "text": f"{name} helps you land better jobs faster"}
        )

    elif domain == "ai":
        sections.append(
            {
                "type": "pain",
                "points": [
                    "Too many tools to manage",
                    "Low productivity workflows",
                    "Manual repetitive tasks",
                    "No automation",
                ],
            }
        )

        sections.append(
            {"type": "solution", "text": f"{name} uses AI to automate your workflows"}
        )

        # 🔥 AI-SPECIFIC (NEW 🔥)
        sections.append(
            {"type": "demo", "text": "See AI in action with real-time outputs"}
        )

    else:
        # fallback
        sections.append(
            {
                "type": "pain",
                "points": [
                    "Inefficient workflows",
                    "Manual processes",
                    "Lack of visibility",
                    "Scaling challenges",
                ],
            }
        )

        sections.append(
            {"type": "solution", "text": f"{name} simplifies your workflow"}
        )

    # 🔥 FEATURES (COMMON)
    if modules:
        sections.append({"type": "features", "modules": modules})

    # 🔥 WORKFLOW (ONLY FOR CERTAIN DOMAINS)
    if domain in ["testing", "ai", "marketing"]:
        sections.append(
            {"type": "workflow", "steps": ["Setup", "Run", "Analyze", "Optimize"]}
        )

    # 🔥 TRUST (ALWAYS)
    sections.append(
        {"type": "trust", "items": ["Secure", "Scalable", "Fast", "Reliable"]}
    )

    # 🔥 CTA
    sections.append(
        {"type": "cta", "text": f"Start using {name} today", "button": "Get Started"}
    )

    sections.append({"type": "data", "modules": modules})

    return sections
