# engine/ui_components.py

COMPONENTS = {
    "navbar": """
    <nav class="fixed w-full z-50 bg-white bg-opacity-90 backdrop-blur-md border-b border-gray-100">
      <div class="container mx-auto px-6 py-4 flex justify-between items-center">
        <div class="text-2xl font-bold text-primary">{product_name}</div>
        <div class="hidden md:flex space-x-8 text-gray-600 font-medium">
          <a href="#features" class="hover:text-primary transition">Features</a>
          <a href="#how-it-works" class="hover:text-primary transition">Solutions</a>
          <a href="/login" class="hover:text-primary transition">Sign In</a>
        </div>
        <a href="/signup" class="bg-primary text-white px-6 py-2 rounded-custom font-bold hover:opacity-90 transition">Get Started</a>
      </div>
    </nav>
    """,
    "hero": """
    <section class="relative pt-32 pb-20 overflow-hidden bg-app">
      <div class="container mx-auto px-6 relative z-10">
        <div class="flex flex-wrap items-center">
          <div class="w-full lg:w-1/2 mb-12 lg:mb-0">
            <span class="inline-block py-1 px-3 mb-4 text-xs font-semibold text-primary bg-blue-50 rounded-full uppercase tracking-widest">v1.0 Launch</span>
            <h1 class="text-5xl lg:text-6xl font-bold mb-6 text-gray-900 leading-tight">{product_name}</h1>
            <p class="text-xl text-gray-600 mb-8 leading-relaxed">{product_description}</p>
            <div class="flex flex-wrap gap-4">
              <a href="/signup" class="bg-primary text-white px-8 py-4 rounded-custom font-bold hover:opacity-90 transition shadow-lg shadow-blue-200">Start Building Now</a>
            </div>
          </div>
          <div class="w-full lg:w-1/2 px-4">
             <div class="rounded-3xl overflow-hidden shadow-2xl border-8 border-white transform lg:rotate-3">
                <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80" alt="Dashboard Preview">
             </div>
          </div>
        </div>
      </div>
    </section>
    """,
    "features": """
    <section id="features" class="py-24 bg-white">
      <div class="container mx-auto px-6">
        <div class="text-center max-w-2xl mx-auto mb-16">
          <h2 class="text-3xl font-bold mb-4 text-gray-900">Everything you need</h2>
          <p class="text-gray-600">Built for scale, designed for speed.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
          {feature_items}
        </div>
      </div>
    </section>
    """,
    "feature_item": """
    <div class="p-8 border border-gray-100 rounded-2xl hover:border-primary transition group">
      <div class="w-12 h-12 bg-primary bg-opacity-10 rounded-lg flex items-center justify-center mb-6 text-primary">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
      </div>
      <h3 class="text-xl font-bold mb-3">{title}</h3>
      <p class="text-gray-600">{description}</p>
    </div>
    """,
    "cta_section": """
  <section class="py-20 bg-primary">
    <div class="container mx-auto px-6 text-center">
      <h2 class="text-4xl font-bold mb-8 text-white">Ready to transform your workflow?</h2>
      <p class="text-blue-100 mb-10 text-xl max-w-2xl mx-auto">Join hundreds of teams using {product_name} to scale their operations.</p>
      <a href="/signup" class="bg-white text-primary px-10 py-4 rounded-custom font-bold hover:bg-gray-100 transition shadow-xl">Get Started for Free</a>
    </div>
  </section>
  """,
    "dashboard_shell": """
    <div class="flex h-screen bg-gray-50">
      <div class="w-64 bg-white border-r border-gray-200 hidden md:block">
        <div class="p-6 text-2xl font-bold text-primary">{product_name}</div>
        <nav class="mt-6 px-4 space-y-2">
          <a href="/dashboard" class="flex items-center p-3 text-gray-700 bg-gray-100 rounded-lg">Dashboard</a>
          {sidebar_links}
        </nav>
      </div>
      <div class="flex-1 flex flex-col overflow-hidden">
        <header class="bg-white border-b border-gray-200 p-4 flex justify-between items-center">
          <h2 class="text-xl font-semibold text-gray-800">{page_title}</h2>
          <div class="flex items-center space-x-4">
            <span class="text-sm text-gray-500">Welcome, User</span>
            <div class="w-10 h-10 bg-primary rounded-full"></div>
          </div>
        </header>
        <main class="flex-1 overflow-y-auto p-8">
          {main_content}
        </main>
      </div>
    </div>
    """,
    "sidebar_link": """
    <a href="/{route}" class="flex items-center p-3 text-gray-600 hover:bg-gray-50 rounded-lg transition">{name}</a>
    """,
    "pricing_card": """
  <div class="p-8 bg-white border border-gray-200 rounded-3xl shadow-sm hover:shadow-2xl transition-all transform hover:-translate-y-2">
    <h3 class="text-lg font-bold mb-2">{plan_name}</h3>
    <div class="text-4xl font-black mb-6">{price}<span class="text-sm font-normal text-gray-500">/mo</span></div>
    <ul class="space-y-4 mb-8 text-gray-600">
      {plan_features}
    </ul>
    <a href="/signup" class="block text-center py-3 px-6 rounded-custom border border-primary text-primary font-bold hover:bg-primary hover:text-white transition">Choose Plan</a>
  </div>
  """,
    "stats_grid": """
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      {stats_cards}
    </div>
    """,
    "stat_card": """
    <div class="p-6 bg-white rounded-xl shadow-sm border border-gray-100">
      <p class="text-sm font-medium text-gray-500 uppercase">{label}</p>
      <p class="text-2xl font-bold text-gray-900">{value}</p>
    </div>
    """,
    "data_table": """
    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <table class="w-full text-left">
        <thead class="bg-gray-50 border-b border-gray-100">
          <tr>{table_headers}</tr>
        </thead>
        <tbody class="divide-y divide-gray-100">
          {table_rows}
        </tbody>
      </table>
    </div>
    """,
    "footer": """
      <footer class="py-12 bg-gray-50 border-t border-gray-100">
        <div class="container mx-auto px-6 text-center">
          <div class="text-xl font-bold text-primary mb-4">{product_name}</div>
          <p class="text-gray-500 text-sm">© 2026 {product_name}. Built by Agentic Startup Factory.</p>
        </div>
      </footer>
      """,
}
