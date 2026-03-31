# [AUTO_WIRE IMPORTS]
from routes.auth_routes import auth_bp
from routes.core_logic_routes import core_logic_bp
from routes.payments_routes import payments_bp
from routes.design_routes import design_bp
from routes.furniture_catalog_routes import furniture_catalog_bp
from routes.room_designer_routes import room_designer_bp

from flask import Flask, render_template, redirect
from flask import url_for

PRODUCT_NAME = "EchoVista"

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/")
def landing():
    return render_template(
        "index.html",
        product_name=PRODUCT_NAME,
        product_tagline="Build ATS-ready resumes instantly",
        product_headline="Create Perfect Resumes With AI",
        product_description="AI-powered virtual interior design tool for architects and home owners",

        product_meta_description="AI powered resume builder",
        product_keywords="AI resume, ATS resume builder",

        product_about_title="Smart Resume Optimization",
        product_about_description="Our AI improves your resume for recruiters.",

        feature_1_title="AI-powered room layout suggestions, Real-time furniture and decor placement, Virtual staging with real-world lighting effects, 3D interior design visualizations, Furniture and decor catalog with pricing and commission-based sales, User profiles for saving and sharing designs, Integration with popular CAD software, User authentication and authorization, Payment gateway integration, Design collaboration and sharing",
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
app.register_blueprint(design_bp)
app.register_blueprint(furniture_catalog_bp)
app.register_blueprint(room_designer_bp)

if __name__ == "__main__":
    app.run(debug=True)