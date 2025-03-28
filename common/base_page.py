#defines the base class for the endpoints
class BasePage:
    def __init__(self, client):
        self.client = client

    def get(self, url, **kwargs):
        return self.client.get(url, **kwargs)

    def post(self, url, data=None, **kwargs):
        return self.client.post(url, data=data, **kwargs)