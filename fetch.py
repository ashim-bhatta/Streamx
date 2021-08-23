import requests

class Fetch:
    def __init__(self):
        self.base_url = 'https://yts.mx/api/v2/'

    def Fetch_data(self, end_url):
        return requests.get(url=f"{self.base_url}{end_url}").json()
