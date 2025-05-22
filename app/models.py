from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    expense = db.Column(db.Float, nullable=False)


# need ibutang sa folder (model)
# instead na model, dapat name sa class
