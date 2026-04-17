from engine.section_generator import generate_sections
import random
import re


def generate_full_ui(product):
    sections = generate_sections(product)

    gradients = [
        "from-indigo-500 to-purple-600",
        "from-blue-500 to-cyan-500",
        "from-pink-500 to-red-500",
        "from-green-500 to-emerald-600",
    ]

    gradient = random.choice(gradients)

    html_sections = ""

    for section in sections:
        # 🔥 HERO
        if section["type"] == "hero":
            html_sections += f"""
            <section class="min-h-screen flex flex-col justify-center items-center text-center bg-gradient-to-r {gradient} text-white px-6">
                <h1 class="text-5xl md:text-6xl font-bold mb-4">{section["title"]}</h1>
                <p class="text-lg mb-6">{section["subtitle"]}</p>
                <a href="/dashboard" class="bg-white text-indigo-600 px-6 py-3 rounded-lg shadow hover:scale-105 transition">
                    {section["cta"]}
                </a>
            </section>
            """

        # 🔥 PAIN
        elif section["type"] == "pain":
            points = "".join(
                [f"<li class='mb-2'>❌ {p}</li>" for p in section.get("points", [])]
            )

            html_sections += f"""
            <section class="py-20 bg-gray-900 text-white text-center">
                <h2 class="text-3xl font-bold mb-6">Problems You Face</h2>
                <ul class="max-w-xl mx-auto text-lg">{points}</ul>
            </section>
            """

        # 🔥 SOLUTION
        elif section["type"] == "solution":
            html_sections += f"""
            <section class="py-20 text-center">
                <h2 class="text-3xl font-bold mb-4">The Solution</h2>
                <p class="text-lg text-gray-600">{section["text"]}</p>
            </section>
            """

        # 🔥 FEATURES
        elif section["type"] == "features":
            cards = ""
            for m in section["modules"]:
                cards += f"""
                <div class="group p-6 bg-white rounded-xl shadow hover:shadow-xl transition">
                    <h3 class="text-xl font-semibold mb-2 group-hover:text-indigo-600">{m["name"]}</h3>
                    <p class="text-gray-600 mb-3">{m["description"]}</p>
                    <ul class="text-sm text-gray-500">
                        {"".join([f"<li>• {f}</li>" for f in m.get("features", [])[:3]])}
                    </ul>
                </div>
                """

            html_sections += f"""
            <section class="py-20 px-6 max-w-6xl mx-auto">
                <h2 class="text-3xl font-bold text-center mb-12">Product Capabilities</h2>
                <div class="grid md:grid-cols-3 gap-8">{cards}</div>
            </section>
            """

        # 🔥 WORKFLOW
        elif section["type"] == "workflow":
            steps = ""
            for i, step in enumerate(section.get("steps", []), 1):
                steps += f"""
                <div class="text-center">
                    <div class="text-3xl font-bold text-indigo-600 mb-2">{i}</div>
                    <p>{step}</p>
                </div>
                """

            html_sections += f"""
            <section class="py-20 bg-gray-100">
                <h2 class="text-3xl font-bold text-center mb-12">How It Works</h2>
                <div class="grid md:grid-cols-4 gap-6 max-w-5xl mx-auto">{steps}</div>
            </section>
            """

        # 🔥 TRUST
        elif section["type"] == "trust":
            items = "".join(
                [
                    f"<div class='p-4 bg-white rounded shadow'>{i}</div>"
                    for i in section.get("items", [])
                ]
            )

            html_sections += f"""
            <section class="py-20 bg-gray-100 text-center">
                <h2 class="text-3xl font-bold mb-8">Why Choose Us</h2>
                <div class="grid md:grid-cols-4 gap-6 max-w-5xl mx-auto">
                    {items}
                </div>
            </section>
            """

        # 🔥 CTA (NO JS HERE)
        elif section["type"] == "cta":
            html_sections += f"""
            <section class="py-20 text-center">
                <h2 class="text-3xl font-bold mb-6">{section["text"]}</h2>
                <a href="/dashboard" class="bg-indigo-600 text-white px-6 py-3 rounded-lg">
                    {section["button"]}
                </a>
            </section>
            """

        # 🔥 DATA (FULLY FIXED)
        elif section["type"] == "data":
            tables = ""
            endpoints = []

            for m in section["modules"]:
                endpoint = re.sub(
                    r"[^a-z0-9_]", "", m["name"].lower().replace(" ", "_")
                )
                endpoints.append(endpoint)

                tables += f"""
                <div class="bg-white p-6 rounded-xl shadow hover:shadow-xl transition duration-300">
                    <h3 class="text-xl font-bold mb-4">{m["name"]}</h3>
                    <div id="{endpoint}-data" class="text-sm text-gray-700">
                        <span class="animate-pulse text-gray-400"><div class="animate-pulse text-gray-400">Loading data...</div></span>
                    </div>
                </div>
                """

            fetch_scripts = "\n".join(
                [
                    f"""
fetch('/api/{endpoint}')
.then(res => res.json())
.then(response => {{
    const el = document.getElementById("{endpoint}-data");
    if (!el) return;

    const payload = response.data || response;
    el.innerHTML = renderData(payload);

    // 🔥 INSIGHTS RENDERING (NEW)
    if (response.insights) {{
        const insights = response.insights;

        let insightHTML = "<div style='margin-top:15px;padding:15px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;'>";

        insightHTML += "<h4 style='margin-bottom:8px;'>🧠 Summary</h4>";
        insightHTML += "<p>" + (insights.summary || "No summary available") + "</p>";
        
        insightHTML += "<h4>📊 Insights</h4><ul>";
        (insights.insights || []).forEach(function(i) {{
            insightHTML += "<li>" + i + "</li>";
        }});
        insightHTML += "</ul>";
        
        insightHTML += "<h4>⚠️ Risks</h4><ul>";
        (insights.risks || []).forEach(function(r) {{
            insightHTML += "<li>" + r + "</li>";
        }});
        insightHTML += "</ul>";
        
        insightHTML += "<h4>💡 Recommendations</h4><ul>";
        (insights.recommendations || []).forEach(function(r) {{
            insightHTML += "<li>" + r + "</li>";
        }});
        insightHTML += "</ul>";
        
        insightHTML += "</div>";

        el.innerHTML += insightHTML;
    }}

    GLOBAL_DATA["{endpoint}"] = payload;
    renderKPIs(GLOBAL_DATA);
}})
.catch(() => {{
    document.getElementById("{endpoint}-data").innerHTML =
        "<span class='text-red-500'>Error loading data</span>";
}});
"""
                    for endpoint in endpoints
                ]
            )

            html_sections += f"""
            <section class="py-20 bg-gray-100">
                <div id="kpi-cards" class="grid md:grid-cols-4 gap-6 max-w-6xl mx-auto mb-12"></div>
                
                <div class="grid md:grid-cols-2 gap-6 max-w-6xl mx-auto">
                    {tables}
                </div>
            </section>

            <script>

            function formatStatus(value) {{
                if (!value) return "-";

                const v = value.toLowerCase();

                if (v === "active") return `<span class="text-green-600 font-semibold">● Active</span>`;
                if (v === "inactive") return `<span class="text-red-600 font-semibold">● Inactive</span>`;
                if (v === "pending") return `<span class="text-yellow-600 font-semibold">● Pending</span>`;

                return value;
            }}


            let GLOBAL_DATA = {{}};
            function renderData(data) {{
                if (!data || (Array.isArray(data) && data.length === 0)) {{
                    return `<div class="text-gray-400 italic">No data available</div>`;
                }}
                if (!data) return "<div>No data</div>";
            
                // ✅ ARRAY → TABLE
                if (Array.isArray(data) && data.length > 0 && typeof data[0] === "object") {{
                    const headers = Object.keys(data[0]);
            
                    return `
                    <div class="overflow-x-auto">
                        <table class="min-w-full bg-white border rounded-lg">
                            <thead class="bg-gray-100">
                                <tr>
                                    ${{headers.map(h => `<th class="px-4 py-2">${{h}}</th>`).join("")}}
                                </tr>
                            </thead>
                            <tbody>
                                ${{data.map(row => `
                                    <tr>
                                        ${{headers.map(h => `<td class="px-4 py-2">${{h === "status" ? formatStatus(row[h]) : formatValue(row[h])}}</td>`).join("")}}
                                    </tr>
                                `).join("")}}
                            </tbody>
                        </table>
                    </div>`;
                }}
            
                // ✅ OBJECT → RECURSIVE DISPLAY
                if (typeof data === "object") {{
                    return Object.entries(data)
                        .map(([k, v]) => `
                            <div class="mb-2">
                                <strong>${{k}}:</strong>
                                <div class="ml-4">${{formatValue(v)}}</div>
                            </div>
                        `)
                        .join("");
                }}
            
                return `<div>${{data}}</div>`;
            }}
            
            // 🔥 FORMAT HANDLER (NEW)
            function formatValue(value) {{
                if (value === null || value === undefined) return "-";
            
                if (Array.isArray(value) || typeof value === "object") {{
                    return renderData(value);
                }}
            
                return value;
            }}

            {fetch_scripts}

            function renderKPIs(allData) {{
                let total = 0;
                let active = 0;
                let inactive = 0;

                Object.values(allData).forEach(module => {{
                    if (!Array.isArray(module)) return;

                    module.forEach(item => {{
                        total++;

                        if (item.status === "active") active++;
                        if (item.status === "inactive") inactive++;
                    }});
                }});

                const successRate = total ? Math.round((active / total) * 100) : 0;

                const kpis = [
                    {{ label: "Total Items", value: total }},
                    {{ label: "Active", value: active }},
                    {{ label: "Inactive", value: inactive }},
                    {{ label: "Success Rate", value: successRate + "%" }},
                ];

                const container = document.getElementById("kpi-cards");

                if (!container) return;

                container.innerHTML = kpis.map(k => `
                    <div class="bg-white p-6 rounded-xl shadow text-center">
                        <div class="text-gray-500 text-sm">${{k.label}}</div>
                        <div class="text-2xl font-bold mt-2">${{k.value}}</div>
                    </div>
                `).join("");
            }}
            </script>
            """

    return f"""
<!doctype html>
<html>
<head>
<script src="https://cdn.tailwindcss.com"></script>
<title>{product.get("name", "Startup")}</title>
</head>

<body class="bg-gray-50">
{html_sections}
</body>
</html>
"""
