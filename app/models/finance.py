from app.__init__ import db


class Finance(db.Model):
    __tablename__ = "finance"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    expense = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)  # Simple string field

    def __repr__(self):
        return f"<Finance {self.id}: {self.category} - {self.expense}>"
