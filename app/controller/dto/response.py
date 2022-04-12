

class Response():

    def __init__(self, message='', object=None):
        self.message = message
        self.object = object

    def __json__(self) -> dict:
        if self.object is None:
            return {'message': self.message}
        else:
            return {'message': self.message, 'object': self.object}
