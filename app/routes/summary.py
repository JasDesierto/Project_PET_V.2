from flask import Blueprint, render_template, request
from app import db
from app.models.finance import Finance
from sqlalchemy import func

summary_bp = Blueprint("summary", __name__, url_prefix="/summary")


@summary_bp.route("/")
def show_summary():
    category_filter = request.args.get("category")

    if category_filter:
        # Show single category details
        transactions = (
            Finance.query.filter_by(category=category_filter)
            .order_by(Finance.date.desc())
            .all()
        )
        category_total = sum(t.expense for t in transactions)

        return render_template(
            "statistics.html",
            view_type="category",
            category_name=category_filter,
            transactions=transactions,
            category_total=category_total,
        )
    else:
        # Show full summary
        results = (
            db.session.query(Finance.category, func.sum(Finance.expense).label("total"))
            .group_by(Finance.category)
            .all()
        )

        categories = [{"name": r[0], "value": float(r[1])} for r in results]
        categories.sort(key=lambda x: x["value"], reverse=True)

        return render_template(
            "statistics.html",
            view_type="summary",
            categories=categories,
            total=sum(item["value"] for item in categories),
        )
