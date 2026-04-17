def generate_full_ui(product):
    name = product.get("name", "AI Product")
    description = product.get("description", "AI powered platform")
    modules = product.get("modules", [])

    # 🎨 Dynamic gradient (domain-aware feel)
    gradients = [
        "from-indigo-500 to-purple-600",
        "from-blue-500 to-cyan-500",
        "from-pink-500 to-red-500",
        "from-green-500 to-emerald-600",
    ]

    import random

    gradient = random.choice(gradients)

    # 🔥 FEATURES GRID (RESTORE CARDS — BUT SMART)
    features_html = ""
    for m in modules:
        features_html += f"""
      <div class="group p-6 bg-white rounded-xl shadow hover:shadow-xl transition">
          <h3 class="text-xl font-semibold mb-2 group-hover:text-indigo-600">
              {m["name"]}
          </h3>
          <p class="text-gray-600 mb-3">{m["description"]}</p>
          <ul class="text-sm text-gray-500">
              {"".join([f"<li>• {f}</li>" for f in m.get("features", [])[:3]])}
          </ul>
      </div>
      """

    return f"""
<!doctype html>
<html>
<head>
<script src="https://cdn.tailwindcss.com"></script>
<title>{name}</title>
</head>

<body class="bg-gray-50">

<!-- 🔥 HERO -->
<section class="min-h-screen flex flex-col justify-center items-center text-center bg-gradient-to-r {gradient} text-white px-6">

<h1 class="text-5xl md:text-6xl font-bold mb-4">{name}</h1>
<p class="text-lg md:text-xl mb-6 opacity-90 max-w-xl">{description}</p>

<a href="/dashboard" class="bg-white text-indigo-600 px-6 py-3 rounded-lg shadow hover:scale-105 transition">
  Get Access
</a>

</section>

<!-- 🔥 FEATURES -->
<section class="py-20 px-6 max-w-6xl mx-auto">
<h2 class="text-3xl font-bold text-center mb-12">
  Product Capabilities
</h2>

<div class="grid md:grid-cols-3 gap-8">
  {features_html}
</div>
</section>

</body>
</html>
"""
