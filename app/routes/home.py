from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)


# This route renders (displays) the index.html
@home_bp.route("/", methods=["GET"])
def home():
    return render_template("home.html")
