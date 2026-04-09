# engine/ui_components.py

COMPONENTS = {
    # --- [REPLACE NAVBAR] ---
    "navbar": """
    <nav class="fixed w-full z-50 border-b border-white/5 bg-[#030014]/50 backdrop-blur-xl">
      <div class="container mx-auto px-8 py-5 flex justify-between items-center">
        <div class="text-2xl font-black tracking-tighter text-white uppercase italic">{product_name}</div>
        <div class="hidden md:flex space-x-10 text-sm font-medium text-gray-400">
          <a href="#" class="hover:text-white transition">Platform</a>
          <a href="#" class="hover:text-white transition">Solutions</a>
          <a href="/login" class="hover:text-white transition">Sign In</a>
        </div>
        <a href="/signup" class="bg-white text-black px-6 py-2.5 rounded-full font-bold text-sm hover:bg-gray-200 transition shadow-xl shadow-blue-500/10">Start Building</a>
      </div>
    </nav>
    """,
    # --- [REPLACE Line 34 approx] ---
    "hero": """
    <section class="relative pt-48 pb-32 text-center" data-aos="zoom-out-up">
      <div class="container mx-auto px-6">
        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-bold mb-10 tracking-widest uppercase animate-pulse">
            <span>Live System Active</span>
        </div>
        <h1 class="text-7xl md:text-9xl font-black tracking-tighter mb-8 bg-clip-text text-transparent bg-gradient-to-b from-white to-white/40 leading-none hero-glow">
          {product_name}
        </h1>
        <p class="text-xl md:text-2xl text-gray-400 mb-12 max-w-3xl mx-auto font-light leading-relaxed">
          {hero_subtitle}
        </p>
        <a href="/signup" class="bg-blue-600 hover:bg-blue-500 text-white px-12 py-5 rounded-2xl font-bold text-lg transition-all shadow-[0_0_40px_rgba(37,99,235,0.3)] inline-block">
          {cta_text}
        </a>
      </div>
    </section>
    """,
    # --- [REPLACE features] ---
    "features": """
    <section id="features" class="py-24 bg-transparent">
      <div class="container mx-auto px-6">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">{feature_items}</div>
      </div>
    </section>
    """,
    # --- [REPLACE feature_item] ---
    "feature_item": """
    <div class="p-10 glass-card" data-aos="fade-up" data-aos-delay="200">
      <div class="w-14 h-14 bg-blue-500/10 rounded-2xl flex items-center justify-center mb-8 text-blue-400 border border-blue-500/20 group-hover:scale-110 transition-transform">
        <i data-lucide="shield-check"></i>
      </div>
      <h3 class="text-2xl font-bold mb-4 text-white tracking-tight">{title}</h3>
      <p class="text-gray-400 text-lg leading-relaxed font-light">{description}</p>
    </div>
    """,
    # --- [REPLACE cta_section] ---
    "cta_section": """
    <section class="py-20 bg-[#030712] relative">
      <div class="absolute inset-0 bg-primary/5 blur-[120px] rounded-full"></div>
      <div class="container mx-auto px-6 text-center relative z-10">
        <h2 class="text-4xl md:text-6xl font-black mb-8 text-white tracking-tighter italic">Ready to transform?</h2>
        <p class="text-gray-400 mb-10 text-xl max-w-2xl mx-auto italic">{product_name} is the last tool you'll ever need.</p>
        <a href="/signup" class="bg-white text-black px-12 py-5 rounded-full font-black hover:bg-indigo-50 transition-all hover:px-14 shadow-2xl inline-block uppercase tracking-widest text-sm">
            Launch Your Pipeline
        </a>
      </div>
    </section>
    """,
    "dashboard_shell": """
    <div class="flex h-screen bg-transparent text-white">
      <div class="w-64 border-r border-white/10 backdrop-blur-3xl p-8 bg-[#030014]/50">
        <div class="text-2xl font-black mb-10 tracking-tighter italic bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500">{product_name}</div>
        <nav class="space-y-2">{sidebar_links}</nav>
      </div>
      <main class="flex-1 p-10 overflow-y-auto">
        <div class="glass-card p-10">{main_content}</div>
      </main>
    </div>
    """,
    # --- [REPLACE sidebar_link] ---
    "sidebar_link": """
        <a href="/{route}" class="flex items-center px-4 py-3 text-gray-400 hover:text-white hover:bg-white/5 rounded-xl transition-all group">
          <span class="mr-3 opacity-20 group-hover:opacity-100 group-hover:text-primary transition-all">◇</span> {name}
        </a>
        """,
    "pricing_card": """
    <div class="p-8 bg-white/[0.02] border border-white/5 rounded-3xl backdrop-blur-md hover:border-primary/30 transition-all">
      <h3 class="text-lg font-bold mb-2 text-white">{plan_name}</h3>
      <div class="text-4xl font-black mb-6 text-white">{price}<span class="text-sm font-normal text-gray-400">/mo</span></div>
      <ul class="space-y-4 mb-8 text-gray-400">
        {plan_features}
      </ul>
      <a href="/signup" class="block text-center py-3 px-6 rounded-xl border border-primary text-primary font-bold hover:bg-primary hover:text-white transition">Choose Plan</a>
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
    <footer class="py-12 bg-[#030712] border-t border-white/5">
      <div class="container mx-auto px-6 text-center">
        <div class="text-xl font-bold text-white mb-4">{product_name}</div>
        <p class="text-gray-500 text-sm">© 2026 {product_name}. Built by Agentic Startup Factory.</p>
      </div>
    </footer>
    """,
}
