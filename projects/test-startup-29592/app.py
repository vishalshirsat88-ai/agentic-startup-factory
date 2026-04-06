# [AUTO_WIRE IMPORTS]
from routes.project_management_routes import project_management_bp
from routes.test_case_management_routes import test_case_management_bp
from routes.test_execution_routes import test_execution_bp
from routes.ci_cd_pipeline_management_routes import ci_cd_pipeline_management_bp
from routes.reporting_and_analytics_routes import reporting_and_analytics_bp

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
        feature_1_title="Create new project, Update project details, Delete project, Create new test case, Update test case details, Delete test case, Run test cases, View test case results, Retry failed test cases, Create new pipeline, Update pipeline details, Delete pipeline, Generate test case reports, View pipeline analytics, Configure reporting settings",
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
app.register_blueprint(project_management_bp)
app.register_blueprint(test_case_management_bp)
app.register_blueprint(test_execution_bp)
app.register_blueprint(ci_cd_pipeline_management_bp)
app.register_blueprint(reporting_and_analytics_bp)

if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000

    app.run(host="0.0.0.0", port=port, debug=True)
