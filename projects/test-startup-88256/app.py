# [AUTO_WIRE IMPORTS]
from routes.test_configuration_routes import test_configuration_bp
from routes.test_execution_routes import test_execution_bp
from routes.test_analytics_routes import test_analytics_bp
from routes.integration_with_ci_cd_routes import integration_with_ci_cd_bp

from flask import Flask, render_template, redirect
from flask import url_for

PRODUCT_NAME = "AI Tool"

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/")
def landing():
    return render_template(
        "index.html",
        product_name=PRODUCT_NAME,
        product_tagline="Build ATS-ready resumes instantly",
        product_headline="Create Perfect Resumes With AI",
        product_description="AI powered solution",
        product_meta_description="AI powered resume builder",
        product_keywords="AI resume, ATS resume builder",
        product_about_title="Smart Resume Optimization",
        product_about_description="Our AI improves your resume for recruiters.",
        feature_1_title="Test Case Management, Configurable Test Settings, Automated Test Runner, Real-time Test Result Tracking, Test Result Analysis, Performance Metrics Tracking, CI/CD Integration, Automated Deployment",
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
app.register_blueprint(test_configuration_bp)
app.register_blueprint(test_execution_bp)
app.register_blueprint(test_analytics_bp)
app.register_blueprint(integration_with_ci_cd_bp)

if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000

    app.run(host="0.0.0.0", port=port, debug=True)
