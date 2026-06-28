from flask import Flask, render_template , session
from config.config import Config
from database.db import db
from app.models.user import User
from app.auth.routes import auth
from app.decorators.auth import login_required


def create_app():

    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Initialize Database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth)

    # ----------------------------
    # Home Page
    # ----------------------------
    @app.route("/")
    def home():
        return "🚀 CloudOps Portal is Running Successfully!"

    # ----------------------------
    # Protected Dashboard
    # ----------------------------
    @app.route("/dashboard")
    @login_required
    def dashboard():

     username = session.get("username")

     return render_template(
        "dashboard.html",
        username=username
    )

    # ----------------------------
    # Create Database Tables
    # ----------------------------
    with app.app_context():
        db.create_all()

    return app