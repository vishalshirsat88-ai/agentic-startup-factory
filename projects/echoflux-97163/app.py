# [AUTO_WIRE IMPORTS]
from routes.auth_routes import auth_bp
from routes.music_composition_routes import music_composition_bp
from routes.collaboration_routes import collaboration_bp
from routes.premium_features_routes import premium_features_bp
from routes.royalties_routes import royalties_bp
from routes.payments_routes import payments_bp
from routes.networking_routes import networking_bp

from flask import Flask, render_template, redirect
from flask import url_for

PRODUCT_NAME = "EchoFlux"

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/")
def landing():
    return render_template(
        "index.html",
        product_name=PRODUCT_NAME,
        product_tagline="Build ATS-ready resumes instantly",
        product_headline="Create Perfect Resumes With AI",
        product_description="AI-powered music composition and collaboration platform for indie artists and producers",

        product_meta_description="AI powered resume builder",
        product_keywords="AI resume, ATS resume builder",

        product_about_title="Smart Resume Optimization",
        product_about_description="Our AI improves your resume for recruiters.",

        feature_1_title="AI-powered Music Composition Engine, Collaboration Tools with Real-time Feedback, Personalized Music Recommendation System, Premium Features for Subscription-based Model, Royalty-Sharing with Artists, Artist Onboarding and Profile Creation, Music Composition and Collaboration Workflow, Premium Feature Access and Subscription Management, Royalty-Sharing and Payment Tracking, Artist and Producer Networking and Discovery",
        feature_1_description="Upload resume and get instant feedback",

        feature_2_title="ATS Optimization",
        feature_2_description="Ensure recruiters see your resume",

        feature_3_title="One Click Export",
        feature_3_description="Download recruiter-ready resumes",

        plan_1_name="Free",
        plan_2_name="Starter",
        plan_2_price="9",
        plan_3_name="Pro",
        plan_3_price="29",
        plan_4_name="Business",
        plan_4_price="49",

        testimonial_1_name="Sarah",
        testimonial_1_text="This tool doubled my interview calls!",

        testimonial_2_name="David",
        testimonial_2_text="Best AI resume optimizer I’ve used.",

        contact_email="support@example.com"
    )



@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", product_name=PRODUCT_NAME)

@app.route("/logout")
def logout():
    return redirect("/")



# [AUTO_WIRE REGISTRATION]
app.register_blueprint(auth_bp)
app.register_blueprint(music_composition_bp)
app.register_blueprint(collaboration_bp)
app.register_blueprint(premium_features_bp)
app.register_blueprint(royalties_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(networking_bp)

if __name__ == "__main__":
    app.run(debug=True)