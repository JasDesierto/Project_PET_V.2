from flask import Blueprint, render_template, request, jsonify
from app.models.finance import db, Finance  # importing database and model

transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")


@transactions_bp.route("/", methods=["POST"])
def get_expense():
    data = request.json
    date = data.get("date")
    expense_amount = data.get("expense")

    try:
        amount = float(expense_amount)
    except (ValueError, TypeError):
        return jsonify({"error: Invalid expense input"}), 400

    if not date:
        return jsonify({"error": "Month is Required"}), 400

    new_entry = Finance(date=date, expense=amount)
    db.session.add(new_entry)
    db.session.commit()


@transactions_bp.route("/")
def transactions():
    return render_template("transactions.html")
