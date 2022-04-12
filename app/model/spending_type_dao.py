from app import db
from datetime import datetime


class SpendingTypeDao(db.Model):
    __tablename__ = 'spending_type'

    # 1|Compra Mercadona|Compra|20.0|10|2021-10-13
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'SpendingTypeDao({self.id}, {self.name})'
