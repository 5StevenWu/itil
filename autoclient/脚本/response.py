class Response():

    def __init__(self):
        self.status = True
        self.error = ''
        self.data = None

    @property
    def dict(self):
        return self.__dict__


response = Response()
response.status = False
print(response.dict)
