class UIRenderer:
    def render(self, sections):
        html = ""

        for section in sections:
            if section["type"] == "hero":
                html += self.render_hero(section)

            elif section["type"] == "features":
                html += self.render_features(section)

            elif section["type"] == "workflow":
                html += self.render_workflow(section)

            elif section["type"] == "cta":
                html += self.render_cta(section)

        return html

    def render_hero(self, data):
        return f"""
      <section class="hero">
          <h1>{data["headline"]}</h1>
          <p>{data["subheadline"]}</p>
          <button>{data["cta"]}</button>
      </section>
      """

    def render_features(self, data):
        items = "".join([f"<li>{item}</li>" for item in data["items"]])
        return f"""
      <section class="features">
          <ul>{items}</ul>
      </section>
      """

    def render_workflow(self, data):
        steps = "".join([f"<li>{step}</li>" for step in data["steps"]])
        return f"""
      <section class="workflow">
          <ol>{steps}</ol>
      </section>
      """

    def render_cta(self, data):
        return f"""
      <section class="cta">
          <h2>{data["headline"]}</h2>
          <button>{data["cta"]}</button>
      </section>
      """
