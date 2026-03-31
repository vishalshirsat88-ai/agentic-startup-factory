# [AUTO_WIRE IMPORTS]
from routes.auth_routes import auth_bp
from routes.core_logic_routes import core_logic_bp
from routes.payments_routes import payments_bp
from routes.iot_device_registry_routes import iot_device_registry_bp
from routes.security_monitoring_routes import security_monitoring_bp
from routes.alert_system_routes import alert_system_bp
from routes.subscription_management_routes import subscription_management_bp

from flask import Flask, render_template, redirect
from flask import url_for

PRODUCT_NAME = "EchoGuard"

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/")
def landing():
    return render_template(
        "index.html",
        product_name=PRODUCT_NAME,
        product_tagline="Build ATS-ready resumes instantly",
        product_headline="Create Perfect Resumes With AI",
        product_description="AI-powered cybersecurity for IoT devices",

        product_meta_description="AI powered resume builder",
        product_keywords="AI resume, ATS resume builder",

        product_about_title="Smart Resume Optimization",
        product_about_description="Our AI improves your resume for recruiters.",

        feature_1_title="AI-powered threat detection, Real-time security monitoring, Device vulnerability assessment, Regular security updates, Intelligent alert system, IoT device registration and setup, Security monitoring and threat detection dashboard, Alert notification and incident response, Device security update and patch management, Subscription management and billing",
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
app.register_blueprint(iot_device_registry_bp)
app.register_blueprint(security_monitoring_bp)
app.register_blueprint(alert_system_bp)
app.register_blueprint(subscription_management_bp)

if __name__ == "__main__":
    app.run(debug=True)