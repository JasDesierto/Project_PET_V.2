from flask import Blueprint, render_template, request, jsonify
from app.models import db, Finance

summary_bp = Blueprint("summary", __name__, url_prefix="/summary")


@summary_bp.route("/summary", methods=["GET"])
def summary():
    all_data = Finance.query.all()
    summary_data = {}
    total = 0

    for item in all_data:
        if item.month in summary_data:
            summary_data[item.month] += item.expense
        else:
            summary_data[item.month] = item.expense
        total += item.expense

    return jsonify({"summary": summary_data, "total": total})


# - - ! This route renders the statistics html page
@summary_bp.route("/")
def statistics():
    return render_template("statistics.html")
