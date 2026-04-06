# [AUTO_WIRE IMPORTS]
from routes.api_gateway_routes import api_gateway_bp
from routes.test_executor_routes import test_executor_bp
from routes.test_repository_routes import test_repository_bp
from routes.analytics_dashboard_routes import analytics_dashboard_bp

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

        feature_1_title="Request Validation, Rate Limiting, Authentication, Test Execution, Test Result Reporting, Test Failure Analysis, Test Case Management, Test Data Management, Test Data Generation, Test Result Analysis, Performance Metrics, Alert System",
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
app.register_blueprint(api_gateway_bp)
app.register_blueprint(test_executor_bp)
app.register_blueprint(test_repository_bp)
app.register_blueprint(analytics_dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)