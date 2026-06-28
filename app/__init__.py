from flask import Flask
from config.config import Config
from database.db import db
from app.models.user import User


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    @app.route("/")
    def home():
        return "🚀 CloudOps Portal is Running Successfully!"

    with app.app_context():
        db.create_all()

    return app