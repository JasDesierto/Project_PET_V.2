from flask import Flask
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()


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

    from app.routes.home import home_bp
    from app.routes.transactions import transactions_bp
    from app.routes.summary import summary_bp
    from app.routes.user import user_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(summary_bp)
    app.register_blueprint(user_bp)

    return app
