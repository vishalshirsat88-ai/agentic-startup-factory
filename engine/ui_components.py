import re


def generate(prompt):
    return None  # SAFE FALLBACK (no AI for now)


def get_header_section(product_name, description):
    # 🔥 TRY AI GENERATION (SAFE)
    try:
        prompt = f"""
Generate a modern SaaS hero section.

Return ONLY HTML.

Product:
Name: {product_name}
Description: {description}

Requirements:
- TailwindCSS
- Premium SaaS look
- Big headline
- CTA button
"""

        ai_html = generate(prompt)

        if ai_html and "<section" in ai_html.lower():
            print("🧠 AI Hero Generated")
            return ai_html

    except Exception as e:
        print("❌ AI Hero failed:", e)

    # 🔁 FALLBACK (UNCHANGED ORIGINAL)
    return f"""
<section class='relative overflow-hidden bg-gradient-to-r from-indigo-500 to-purple-600 text-white min-h-[60vh] flex flex-col justify-center items-center text-center px-6 pt-32 pb-16'>

<div class='absolute inset-0 bg-gradient-to-br from-white/10 to-transparent backdrop-blur-sm pointer-events-none'></div>
<div class='absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_top,white,transparent)]'></div>

<div class='relative z-10 max-w-5xl mx-auto'>
  <h1 class='text-6xl md:text-7xl font-extrabold tracking-tight mb-6'>
    {product_name} — AI Powered Platform
  </h1>

  <p class='text-lg md:text-xl text-white/90 max-w-2xl mx-auto mb-8'>
    {description}
  </p>

  <button class='mt-2 bg-indigo-600 text-white font-semibold px-10 py-4 rounded-xl shadow-xl hover:shadow-2xl hover:scale-105 hover:bg-indigo-700 transition'>
    Get Access
  </button>
</div>

</section>
"""


def get_features_section(modules):
    # 🔥 TRY AI GENERATION
    try:
        prompt = f"""
Generate a SaaS features section.

Return ONLY HTML.

Modules:
{modules}

Requirements:
- Grid layout
- Cards UI
- Clean SaaS design
- TailwindCSS
"""

        ai_html = generate(prompt)

        if ai_html and "<section" in ai_html.lower():
            print("🧠 AI Features Generated")
            return ai_html

    except Exception as e:
        print("❌ AI Features failed:", e)

    # 🔁 FALLBACK (UNCHANGED ORIGINAL)
    sections = ""

    for module in modules:
        module_name = module.get("name")
        module_slug = re.sub(r"[^a-z0-9]+", "_", module_name.lower()).strip("_")

        feature_items = ""
        for f in module.get("features", [])[:3]:
            feature_items += f"<li class='text-gray-600 text-sm'>• {f}</li>"

        sections += f"""
        <div class='p-6 bg-white rounded-2xl shadow-lg'>

            <h3 class='text-lg font-bold mb-3 text-indigo-700'>
                {module_name}
            </h3>

            <ul class='mb-4'>
                {feature_items}
            </ul>

            <div id="insights-{module_slug}" class="text-sm text-gray-500">
                Loading insights...
            </div>

        </div>

        <script>
        fetch("/api/{module_slug}")
          .then(res => res.json())
          .then(data => {{
              const insights = (data && data.insights) ? data.insights : {{}};

              let html = `
                  <div class="mt-2 space-y-2 text-sm">
                      <div><strong>🧠</strong> ${{insights.summary || ""}}</div>

                      ${{(insights.insights || []).map(i => `
                          <div>✔ ${{i}}</div>
                      `).join("")}}

                      ${{(insights.risks || []).map(r => `
                          <div style="color:red;">⚠ ${{r}}</div>
                      `).join("")}}

                      ${{(insights.recommendations || []).map(r => `
                          <div style="color:green;">💡 ${{r}}</div>
                      `).join("")}}
                  </div>
              `;

              document.getElementById("insights-{module_slug}").innerHTML = html;
          }})
          .catch(() => {{
              document.getElementById("insights-{module_slug}").innerHTML = "No insights";
          }});
        </script>
        """

    return f"""
<section class='py-20 px-6 max-w-6xl mx-auto bg-gradient-to-b from-gray-50 to-white rounded-3xl'>

    <h2 class='text-3xl font-bold text-center mb-12'>
        Product Capabilities
    </h2>

    <div class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8'>
        {sections}
    </div>

</section>
"""


def render_component(component_type, data=None):
    if component_type == "card":
        return f"""
      <div class='p-6 bg-white rounded-2xl shadow hover:shadow-xl transition'>
          {data}
      </div>
      """

    if component_type == "list":
        items = "".join(
            [f"<li class='p-3 bg-gray-50 rounded'>{i}</li>" for i in (data or [])]
        )
        return f"<ul class='space-y-2'>{items}</ul>"

    if component_type == "input":
        return """
      <input id="input-name" type="text"
          placeholder="Enter name"
          class='border p-2 rounded w-full' />
      """

    if component_type == "button":
        return """
      <button onclick="createItem()"
          class='bg-indigo-600 text-white px-4 py-2 rounded'>
          Add
      </button>
      """

    if component_type == "data_container":
        return "<div id='data-container'>Loading...</div>"

    return ""


def get_module_page_section(module):
    module_name = str(module.get("name") or "")

    module_slug = re.sub(r"[^a-z0-9]+", "_", module_name.lower()).strip("_")

    # 🔥 COMPONENTS
    input_field = render_component("input")
    button = render_component("button")
    data_container = render_component("data_container")

    form_section = f"""
  <div class='mb-4 flex gap-2'>
      {input_field}
      {button}
  </div>
  """

    # 🧠 UI DECISION ENGINE
    show_form = any(x in module_name.lower() for x in ["test", "management"])

    return f"""
    <section class='min-h-screen bg-gradient-to-br from-indigo-50 to-purple-100 px-6 py-16'>
    
    <div class='max-w-5xl mx-auto text-center mb-12'>
      <h1 class='text-4xl md:text-5xl font-extrabold text-indigo-700 mb-4'>
          {module_name}
      </h1>
    
      <p class='text-gray-600 text-lg'>
          {module.get("description")}
      </p>
    </div>
    
    <div class='max-w-5xl mx-auto'>
      <div class='bg-white rounded-2xl shadow p-6'>
    
          <h2 class='text-xl font-semibold mb-4 text-gray-800'>
              Live Data
          </h2>
    
          {form_section if show_form else ""}
    
          {data_container}
    
      </div>
    </div>
    
    <script>
    fetch("/api/{module_slug}")
      .then(res => res.json())
      .then(data => {{
      // 🔥 FETCH AI INSIGHTS FROM BACKEND
      const insights = data.insights || {{}};
          let items = [];
    
          if (data && data.data) {{
              let key = Object.keys(data.data || {{}})[0];
              items = key ? data.data[key] : [];
          }}
    
          let html = "";

          // 🔥 TEST LINE (ENGINE PROPAGATION CHECK)
          

          if (items.length === 0) {{
                html += "<p class='text-gray-500'>No data available</p>";
            }} else {{
                html = "<ul class='space-y-2'>";
            
                let active = 0;
                let inactive = 0;
                let totalAmount = 0;
                let hasAmount = false;
            
                items.forEach(item => {{
                    let status = (item.status || "").toLowerCase();
            
                    if (status === "active") active++;
                    if (status === "inactive") inactive++;
            
                    if (item.amount) {{
                        totalAmount += item.amount;
                        hasAmount = true;
                    }}
            
                    html += `<li class='p-3 bg-gray-50 rounded'>
                        ${{item.name || "N/A"}} - ${{item.status || "N/A"}} ${{item.amount ? "- ₹" + item.amount : ""}}
                    </li>`;
                }});
            
                html += "</ul>";
            
                // 🔥 AI INSIGHTS (FROM BACKEND)
                html += `
                <div class="mt-8 space-y-6">
                
                    <div class="p-5 rounded-2xl bg-gradient-to-r from-indigo-50 to-purple-50 border border-indigo-100 shadow-sm">
                        <h3 class="text-lg font-semibold text-indigo-700 mb-1">🧠 AI Summary</h3>
                        <p class="text-sm text-gray-700">
                            ${{insights.summary || "No summary available"}}
                        </p>
                    </div>
                
                    <div class="p-5 rounded-2xl bg-white border border-gray-200 shadow-sm">
                        <h3 class="text-md font-semibold text-gray-800 mb-3">✨ Key Insights</h3>
                        <div class="space-y-2">
                            ${{(insights.insights || []).map(i => `
                                <div class="flex items-start gap-2 text-sm text-gray-700">
                                    <span class="text-indigo-500">•</span>
                                    <span>${{i}}</span>
                                </div>
                            `).join("")}}
                        </div>
                    </div>
                
                    ${{(insights.risks && insights.risks.length) ? `
                    <div class="p-5 rounded-2xl bg-red-50 border border-red-200 shadow-sm">
                        <h3 class="text-md font-semibold text-red-700 mb-3">⚠️ Risks</h3>
                        <div class="space-y-2">
                            ${{insights.risks.map(r => `
                                <div class="flex items-start gap-2 text-sm text-red-600">
                                    <span>⚠️</span>
                                    <span>${{r}}</span>
                                </div>
                            `).join("")}}
                        </div>
                    </div>
                    ` : ""}}
                
                    ${{(insights.recommendations && insights.recommendations.length) ? `
                    <div class="p-5 rounded-2xl bg-green-50 border border-green-200 shadow-sm">
                        <h3 class="text-md font-semibold text-green-700 mb-3">✅ Recommendations</h3>
                        <div class="space-y-2">
                            ${{insights.recommendations.map(r => `
                                <div class="flex items-start gap-2 text-sm text-green-700">
                                    <span>✔</span>
                                    <span>${{r}}</span>
                                </div>
                            `).join("")}}
                        </div>
                    </div>
                    ` : ""}}
                
                </div>
                `;
          document.getElementById("data-container").innerHTML = html;
      }})
      .catch(() => {{
          document.getElementById("data-container").innerHTML = "Failed to load data";
      }});
    
    function createItem() {{
      const name = document.getElementById("input-name").value;
    
      fetch("/api/{module_slug}", {{
          method: "POST",
          headers: {{
              "Content-Type": "application/json"
          }},
          body: JSON.stringify({{ name: name }})
      }})
      .then(res => res.json())
      .then(() => {{
          location.reload();
      }});
    }}
    </script>
    
    <div class='text-center mt-12'>
      <a href="/" class='text-indigo-600 hover:underline'>
          ← Back to Home
      </a>
    </div>
    
    </section>
    """
