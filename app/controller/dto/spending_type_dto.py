class SpendingTypeDTO:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __json__(self):
        return {'id': self.id, 'name': self.name}
