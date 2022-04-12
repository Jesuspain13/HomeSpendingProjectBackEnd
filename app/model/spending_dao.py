from app import db
from datetime import datetime

from app.model.spending_type_dao import SpendingTypeDao


class SpendingDao(db.Model):
    __tablename__ = 'spendings'

    # 1|Compra Mercadona|Compra|20.0|10|2021-10-13
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('spending_type.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)
    description = db.Column(db.String, nullable=True)
    purchase_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    type = db.relationship("SpendingTypeDao", foreign_keys=[type_id])
    supplier = db.relationship("SupplierDao", foreign_keys=[supplier_id])

    def __init__(self, description, type_id, amount, supplier_id):
        self.description = description
        self.type_id = type_id
        self.amount = amount
        self.supplier_id = supplier_id

    def __repr__(self):
        return f'SpendingDao({self.id}, {self.description}, {self.type}, {self.amount},' \
               f' {self.supplier_id}, {self.purchase_date})'
