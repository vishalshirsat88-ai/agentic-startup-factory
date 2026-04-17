from tools.llm import generate
import json


def detect_domain(module_name):
    name = module_name.lower()

    if any(x in name for x in ["pipeline", "lead", "sales", "crm"]):
        return "sales"

    if any(x in name for x in ["employee", "hr", "attendance", "recruitment"]):
        return "hr"

    if any(x in name for x in ["finance", "revenue", "invoice", "payment"]):
        return "finance"

    if any(x in name for x in ["inventory", "stock", "supply"]):
        return "operations"

    return "general"


def generate_insights(module_name, data):
    print("🧠 INSIGHT ENGINE CALLED:", module_name)
    print("🧠 INPUT DATA:", data)
    # 🧠 TRY AI INSIGHTS FIRST
    try:
        if data and isinstance(data, list):
            sample_data = data[:10]

            domain = detect_domain(module_name)

            prompt = f"""You are a SaaS business analyst specialized in {domain} domain.

            Analyze the module data and provide BUSINESS INSIGHTS.

            Module: {module_name}
            Domain: {domain}

            Data:
            {sample_data}

            Return ONLY JSON:
            {{
              "summary": "...",
              "insights": ["...", "..."],
              "risks": ["...", "..."],
              "recommendations": ["...", "..."]
            }}

            Guidelines:
            - Use domain-specific language
            - Focus on business impact
            - Avoid generic statements
            - Be concise but meaningful
            """

            response = generate(prompt)

            cleaned = response.strip()
            cleaned = cleaned.replace("```json", "").replace("```", "").strip()

            try:
                parsed = json.loads(cleaned)
            except:
                raise Exception("Invalid JSON from AI")

            return {
                "summary": parsed.get("summary", ""),
                "insights": parsed.get("insights", []),
                "risks": parsed.get("risks", []),
                "recommendations": parsed.get("recommendations", []),
            }

    except Exception as e:
        print("⚠️ AI failed, using fallback:", e)

    if not data or not isinstance(data, list):
        return {
            "summary": "No data available",
            "insights": [],
            "risks": [],
            "recommendations": [],
        }

    total = len(data)

    # Detect status field
    status_counts = {}
    for item in data:
        status = item.get("status", "unknown").lower()
        status_counts[status] = status_counts.get(status, 0) + 1

    active = status_counts.get("active", 0)
    inactive = status_counts.get("inactive", 0)

    insights = []
    risks = []
    recommendations = []

    # Summary
    summary = f"{total} records analyzed in {module_name}"

    # Insight: Activity ratio
    if total > 0:
        active_ratio = (active / total) * 100

        insights.append(f"{round(active_ratio)}% items are active")

        if active_ratio < 50:
            risks.append(f"Low activity detected ({round(active_ratio)}%)")
            recommendations.append(
                "Increase activation through follow-ups or automation"
            )

    # Insight: Status diversity
    if len(status_counts) > 1:
        insights.append(f"Multiple statuses present: {', '.join(status_counts.keys())}")

    # Insight: Value detection (if amount exists)
    amounts = [
        item.get("amount")
        for item in data
        if isinstance(item.get("amount"), (int, float))
    ]
    if amounts:
        avg_value = sum(amounts) / len(amounts)
        insights.append(f"Average value: {round(avg_value, 2)}")

        if avg_value < 1000:
            risks.append("Low average transaction value")
            recommendations.append("Focus on higher value opportunities")

    # 🧠 TREND DETECTION (LIGHTWEIGHT)

    try:
        if data and isinstance(data, list):
            statuses = [item.get("status", "").lower() for item in data]

            active_count = statuses.count("active")
            inactive_count = statuses.count("inactive")

            if inactive_count > active_count:
                insights.append("Inactive items dominate — declining engagement trend")
                risks.append("Possible drop in performance over time")
                recommendations.append("Reactivation strategy needed")

            # High-value trend
            amounts = [
                item.get("amount")
                for item in data
                if isinstance(item.get("amount"), (int, float))
            ]

            if amounts:
                high_value = [a for a in amounts if a > 5000]

                if len(high_value) > len(amounts) * 0.3:
                    insights.append("High-value transactions increasing")

    except Exception as e:
        print("⚠️ Trend detection error:", e)
        print("🧠 FINAL INSIGHTS READY")
    return {
        "summary": summary,
        "insights": insights,
        "risks": risks,
        "recommendations": recommendations,
    }
