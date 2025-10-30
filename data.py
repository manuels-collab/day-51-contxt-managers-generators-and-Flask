
import requests

class Data():
    def __init__(self):
        URL = "https://api.npoint.io/2b95e28cc4bc7ccdcda1"
        response = requests.get(URL)
        self.data = response.json()