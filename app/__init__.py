from flask import Flask
from config.config import Config
from database.db import db

from app.models.user import User
from app.models.server import Server

from app.auth.routes import auth
from app.inventory.routes import inventory
from app.dashboard.routes import dashboard
from app.models.incident import Incident
from app.incidents.routes import incidents

from app.monitoring.routes import monitoring
from app.azure.routes import azure

from app.models.azure_config import AzureConfig
from app.azure_config.routes import azure_config

from app.models.audit_log import AuditLog
from app.audit.routes import audit

def create_app():

    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Initialize Database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(inventory)
    app.register_blueprint(dashboard)
    app.register_blueprint(incidents)
    app.register_blueprint(monitoring)
    app.register_blueprint(azure)
    app.register_blueprint(azure_config)
    app.register_blueprint(audit)

    # Home Page
    @app.route("/")
    def home():
        return "CloudOps Portal is Running Successfully!"

    # Create Database Tables
    with app.app_context():
        db.create_all()

    return app