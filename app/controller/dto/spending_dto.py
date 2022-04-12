class SpendingDTO:
    def __init__(self, id, type, amount, supplier, description, purchase_date):
        self.id = id
        self.type = type
        self.amount = amount
        self.supplier = supplier
        self.description = description
        self.purchase_date = purchase_date

    def __json__(self):
        return {'id': self.id, 'type': self.type.__json__(), 'amount': self.amount,
                'supplier': self.supplier.__json__(), 'description': self.description,
                'purchase_date': self.purchase_date.strftime("%d/%m/%Y")}
