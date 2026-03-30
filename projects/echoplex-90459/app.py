# [AUTO_WIRE IMPORTS]
from routes.auth_routes import auth_bp
from routes.core_logic_routes import core_logic_bp
from routes.payments_routes import payments_bp
from routes.event_management_routes import event_management_bp
from routes.user_management_routes import user_management_bp
from routes.payment_gateway_routes import payment_gateway_bp
from routes.health_routes import health_bp
import os
from flask import Flask, render_template, redirect
from flask import url_for

PRODUCT_NAME = "EchoPlex"

app = Flask(__name__)
app.secret_key = "secret123"

from db import init_db

init_db()


@app.route("/")
def landing():
    return render_template(
        "index.html",
        product_name=PRODUCT_NAME,
        product_tagline="Build ATS-ready resumes instantly",
        product_headline="Create Perfect Resumes With AI",
        product_description="A virtual event planning and management platform that utilizes AI to create immersive and engaging experiences",
        product_meta_description="AI powered resume builder",
        product_keywords="AI resume, ATS resume builder",
        product_about_title="Smart Resume Optimization",
        product_about_description="Our AI improves your resume for recruiters.",
        feature_1_title="AI-powered event content curation, Virtual event space customization and management, Real-time engagement analytics and feedback, Integration with popular calendar and scheduling tools, Multi-language support for a global audience, User registration and profile creation, Event planning and proposal submission, Event creation and management, Virtual event attendance and participation, Post-event evaluation and feedback",
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
        contact_email="support@example.com",
    )


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", product_name=PRODUCT_NAME)


@app.route("/logout")
def logout():
    return redirect("/")


# [AUTO_WIRE REGISTRATION]
app.register_blueprint(auth_bp)
app.register_blueprint(core_logic_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(event_management_bp)
app.register_blueprint(user_management_bp)
app.register_blueprint(payment_gateway_bp)
app.register_blueprint(health_bp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
