class RequestInterface:

    def get_all(self, json):
        raise NotImplementedError

    def get_one(self, id, json):
        raise NotImplementedError

    def post(self, json):
        raise NotImplementedError

    def put(self, id, sjson):
        raise NotImplementedError

    def delete(self, id):
        raise NotImplementedError
