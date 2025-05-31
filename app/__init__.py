from flask import Flask
from flask_cors import CORS
import os
import config
from app.routes import *  # this will import all the routes
from .db import db


def create_db(app):
    with app.app_context():
        from app.models.finance import Finance

        db.create_all()
        print("Tables created:", db.metadata.tables.keys())


def create_app():
    # Tell Flask to look for templates in app/templates
    template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "templates")
    app = Flask(__name__, template_folder=template_dir)

    app.config.from_object("config.Config")
    db.init_app(app)

    create_db(app)  # Create the database

    CORS(app)

    for bp in [home_bp, transactions_bp, summary_bp, user_bp]:
        app.register_blueprint(bp)  # Register the blueprint

    return app
