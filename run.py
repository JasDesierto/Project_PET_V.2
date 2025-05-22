# -- ! Ensure that your are specific when importing blueprints
from flask import Flask, jsonify, render_template
from app.routes.home import home_bp
from app.routes.summary import summary_bp
from app.routes.transactions import transactions_bp
from app.routes.user import user_bp
from app.models.finance import Finance


# Create the Flask app using the create_app function
def create_app():
    app = Flask(__name__)

    # Register the blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(summary_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(user_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
