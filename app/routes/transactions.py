from flask import Blueprint, render_template, request, jsonify
from app import db
from app.models.finance import Finance

transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")


@transactions_bp.route("/", methods=["POST"])
def get_expense():
    data = request.json
    date = data.get("date")
    expense_amount = data.get("expense")
    category = data.get("category")

    try:
        amount = float(expense_amount)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid expense input"}), 400

    if not date:
        return jsonify({"error": "Date is required"}), 400
    if not category:
        return jsonify({"error": "Category is required"}), 400

    new_entry = Finance(date=date, expense=amount, category=category)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Transaction recorded successfully."}), 201


@transactions_bp.route("/")
def transactions():
    return render_template("transactions.html")
