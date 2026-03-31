# [AUTO_WIRE IMPORTS]
from routes.auth_routes import auth_bp
from routes.core_logic_routes import core_logic_bp
from routes.payments_routes import payments_bp
from routes.event_planning_routes import event_planning_bp
from routes.event_hosting_routes import event_hosting_bp
from routes.dashboard_routes import dashboard_bp

from flask import Flask, render_template, redirect
from flask import url_for

PRODUCT_NAME = "EchoVerge"

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/")
def landing():
    return render_template(
        "index.html",
        product_name=PRODUCT_NAME,
        product_tagline="Build ATS-ready resumes instantly",
        product_headline="Create Perfect Resumes With AI",
        product_description="An AI-powered virtual event planning platform for creators and event organizers.",

        product_meta_description="AI powered resume builder",
        product_keywords="AI resume, ATS resume builder",

        product_about_title="Smart Resume Optimization",
        product_about_description="Our AI improves your resume for recruiters.",

        feature_1_title="AI-powered event planning, Virtual event hosting, Creator dashboard, Event organizer dashboard, Commission-based booking fees, User registration and login, Event planning and creation, Event attendance and participation, Payment processing and commission calculation, Event cancellations or rescheduling, Technical issues during events, User complaints or disputes, Payment disputes or refunds",
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
app.register_blueprint(core_logic_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(event_planning_bp)
app.register_blueprint(event_hosting_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)