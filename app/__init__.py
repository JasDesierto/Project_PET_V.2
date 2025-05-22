from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Moving here changes the code below to global in terms of scope
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("config.Config")
    # initializing db object
    db.init_app(app)

    # Registration of Blueprints
    from app.routes.home import home_bp
    from app.routes.transactions import transactions_bp
    from app.routes.summary import statistics_bp
    from app.routes.user import user_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(statistics_bp)
    app.register_blueprint(user_bp)

    return app
