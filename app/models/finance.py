from flask_sqlalchemy import SQLAlchemy
from app import db  # you imported this db from init


class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    expense = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    category = db.relationship("Category", backref="finances")
