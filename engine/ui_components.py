def get_header_section(product_name, description):
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
      Get Started
    </button>
  </div>

  </section>
  """


def get_features_section(modules):
    sections = ""

    for module in modules:
        feature_items = ""

        for f in module.get("features", [])[:3]:
            feature_items += f"""
          <li class='text-gray-600 text-sm leading-relaxed'>• {f}</li>
          """

        sections += f"""
      <div onclick="window.location='/module/{module.get("name").lower().replace(" ", "-")}'"
       class='cursor-pointer p-8 bg-white/80 backdrop-blur border border-gray-200 shadow-lg rounded-2xl hover:shadow-2xl hover:-translate-y-2 hover:scale-[1.02] transition duration-300 ease-out'>

          <div class='w-10 h-10 mb-4 rounded-lg bg-indigo-100 flex items-center justify-center'>
    <span class='text-indigo-600 font-bold'>★</span>
</div>

<h3 class='text-xl font-bold mb-4 text-indigo-700'>
              {module.get("name")}
          </h3>

          <ul class='space-y-2'>
              {feature_items}
          </ul>

      </div>
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
